"""Tác giả: PM - TKC. Chỉ đọc; công thức là dữ liệu cho người đối chiếu, không phải lệnh."""
import argparse
import json
import math
import unicodedata
from numbers import Real
from pathlib import Path
from openpyxl import load_workbook

def norm(value):
    text=unicodedata.normalize('NFD',str(value or '').casefold().replace('đ','d'))
    return ''.join(c for c in text if not unicodedata.combining(c) and not c.isspace())

def number(v):
    return isinstance(v,Real) and not isinstance(v,bool) and math.isfinite(v)

def review(path,map_path=None,sheet=None):
    config=json.loads(Path(map_path or Path(__file__).parent.parent/'references/column-map.json').read_text())
    w=load_workbook(path,data_only=True,read_only=True)
    f=None;errors=[];unknown=[];evidence=[]
    def result():
        return {'tổng kết':'Không đạt' if errors else ('Chưa xác minh' if unknown else 'Đạt kiểm tra kỹ thuật'),
                'lỗi':errors,'chưa xác minh':unknown,'đối chiếu công thức':evidence,
                'lưu ý':'[CHỜ COO DUYỆT – D-04]; xác nhận mẫu/cache/quy tắc, không phải phê duyệt nghiệp vụ'}
    def add(row,code,value):
        errors.append({'STT':row,'sản phẩm':f'dòng {row}','quy tắc vi phạm':code,'giá trị':value,'đề xuất người kiểm':'Đối chiếu nguồn, không tự sửa'})
    try:
        f=load_workbook(path,data_only=False,read_only=True)
        name=sheet or config['sheet']
        if name not in w.sheetnames:
            unknown.append({'sheet thiếu':name});return result()
        data=list(w[name].values);forms=list(f[name].values)
        cols={};header_row=None
        # Find a complete header if present, including templates with a title above it.
        candidates=[]
        for idx,row in enumerate(forms):
            found={}
            for key,aliases in config['columns'].items():
                hits=[i for i,v in enumerate(row) if norm(v) in {norm(a) for a in aliases}]
                if len(hits)==1:found[key]=hits[0]
            candidates.append((len(set(found)&set(config['required'])),idx,found))
        if candidates:
            _,header_row,cols=max(candidates,key=lambda item:(item[0],-item[1]))
        missing=[key for key in config['required'] if key not in cols]
        if missing:
            unknown.append({'cột thiếu':[config['columns'].get(k,[k])[0] for k in missing]});return result()
        def cell(row,key):
            idx=cols.get(key)
            return row[idx] if idx is not None and idx<len(row) else None
        product_count=0;checks=0
        last=max((i for i,row in enumerate(forms) if any(v is not None for v in row)),default=header_row)
        for index in range(header_row+1,last+1):
            row=data[index];form=forms[index];excel_row=index+1
            if not any(v is not None for v in form):add(excel_row,'PR-06','Dòng trống giữa bảng');continue
            missing_cache=set()
            for key,col in cols.items():
                expr=cell(form,key)
                if isinstance(expr,str) and expr.startswith('=') and cell(row,key) is None:
                    missing_cache.add(key);unknown.append({'dòng':excel_row,'cột':config['columns'][key][0],'lý do':'Thiếu cache công thức'})
            if any(norm(v)=='kiemtra' for v in row):
                checks+=1
                if 'seller' in cols:
                    a,b=cell(row,'seller'),cell(row,'affiliate')
                    if not missing_cache.intersection({'seller','affiliate'}):
                        if not number(a) or not number(b) or not math.isclose(a+b,1,abs_tol=1e-9):add(excel_row,'PR-02','Tổng tỷ lệ không đủ 100% hoặc không phải số')
                else:
                    signals={norm(cell(row,k)) for k in ['status','notes'] if k not in missing_cache}
                    if signals & {norm(v) for v in config['check_bad']}:add(excel_row,'PR-02','Dòng KIỂM TRA báo tổng tỷ lệ không đủ 100%')
                    elif not signals & {norm(v) for v in config['check_ok']}:unknown.append({'dòng':excel_row,'lý do':'Cần người đối chiếu dòng KIỂM TRA; không suy tổng khi thiếu % nhà bán'})
                continue
            stt=cell(row,'stt')
            if not number(stt) or int(stt)!=stt:
                unknown.append({'dòng':excel_row,'lý do':'Không xác định dòng sản phẩm'});continue
            product_count+=1
            status=norm(cell(row,'status'))
            if 'status' not in missing_cache and status!=norm('ĐÚNG'):add(excel_row,'PR-01','Trạng thái khác ĐÚNG')
            if status==norm('Lệch so với giá hội viên'):
                add(excel_row,'PR-03','Trạng thái báo lệch so với giá hội viên')
            elif 'basis' in cols and 'basis' not in missing_cache and norm(cell(row,'basis'))!=norm('GIÁ HỘI VIÊN'):
                add(excel_row,'PR-03','Cơ sở tính không phải GIÁ HỘI VIÊN')
            expressions={key:cell(form,key) for key in ['status','affiliate','seller'] if isinstance(cell(form,key),str) and cell(form,key).startswith('=')}
            evidence.append({'dòng':excel_row,'công thức (dữ liệu, không thực thi)':expressions or 'cần người đối chiếu công thức'})
            if not missing_cache.intersection({'market','member'}):
                a,b=cell(row,'market'),cell(row,'member')
                if not number(a) or not number(b):add(excel_row,'PR-06','Ô giá không phải số')
                elif b>=a:add(excel_row,'PR-04','Giá hội viên không thấp hơn giá thị trường')
            if any(norm(marker) in norm(cell(row,'notes')) for marker in config['sample_markers']):add(excel_row,'PR-05','Còn câu/dòng ví dụ của mẫu')
        if not product_count:unknown.append({'lý do':'Không có dòng sản phẩm đã xác định'})
        if not checks:unknown.append({'lý do':'Không có dòng KIỂM TRA; cần người đối chiếu tổng tỷ lệ'})
        return result()
    finally:
        w.close()
        if f:f.close()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('file');p.add_argument('--map',type=Path);p.add_argument('--sheet')
    a=p.parse_args()
    try:
        result=review(a.file,a.map,a.sheet);print(json.dumps(result,ensure_ascii=False,indent=2))
        return 2 if result['lỗi'] else (3 if result['chưa xác minh'] else 0)
    except Exception as exc:p.exit(1,f'Chưa xác minh: {type(exc).__name__}; kiểm file/map/quyền.\n')
if __name__=='__main__':raise SystemExit(main())
