"""Tác giả: PM - TKC. Fixture SIM, sáu lỗi quy tắc, không ghi đè."""
from pathlib import Path
from openpyxl import Workbook

def make(path):
    path=Path(path)
    if path.exists():raise FileExistsError('Fixture đã tồn tại')
    w=Workbook();w.properties.creator='PM - TKC';w.properties.lastModifiedBy='PM - TKC';s=w.active;s.title='Bang_Gia'
    s.append(['STT','Sản phẩm','Giá thị trường','Giá hội viên','% nhà bán','% Affiliate','Cơ sở tính','Trạng thái','Ghi chú'])
    for i in range(1,7):
        row=[i,f'SIM-{300+i}',100,80,.8,.2,'GIÁ HỘI VIÊN','ĐÚNG','']
        if i==1:row[7]='LỆCH'
        if i==3:row[6]='GIÁ THỊ TRƯỜNG'
        if i==4:row[3]=100
        if i==5:row[8]='DÒNG VÍ DỤ SIM'
        if i==6:row[3]='KHÔNG PHẢI SỐ'
        s.append(row)
        if i==2:s.append(['KIỂM TRA','SIM-302',None,None,.7,.2])
    for row in s.iter_rows(min_row=2):
        for cell in row[4:6]:cell.number_format='0%'
    w.save(path);print(path.name)

def make_real(path):
    path=Path(path)
    if path.exists():raise FileExistsError('Fixture đã tồn tại')
    w=Workbook();w.properties.creator='PM - TKC';w.properties.lastModifiedBy='PM - TKC'
    s=w.active;s.title='Bang_Nhap_Affiliate'
    s.append(['STT','tên sản phẩm','thương hiệu','giá thị trường','giá bán hội viên','% chiết khấu Affiliate','Trạng thái','Ghi chú'])
    for i in range(1,7):
        row=[i,f'SIM-{400+i}','SIM-BRAND',100,80,.2,'ĐÚNG','']
        if i==1:row[6]='CHỜ KIỂM'
        if i==3:row[6]='Lệch so với giá hội viên'
        if i==4:row[4]=100
        if i==5:row[7]='DÒNG VÍ DỤ SIM'
        if i==6:row[4]='KHÔNG PHẢI SỐ'
        s.append(row)
        if i==2:s.append(['KIỂM TRA','SIM-402',None,None,None,None,'KHÔNG ĐỦ 100%'])
    for row in s.iter_rows(min_row=2):row[5].number_format='0%'
    w.save(path);print(path.name)

def make_all(directory):
    directory=Path(directory);directory.mkdir(parents=True,exist_ok=True)
    for name,fn in [('bang-gia-sim.xlsx',make),('bang-gia-mau-that-sim.xlsx',make_real)]:
        target=directory/name
        if target.exists():print(f'{name}: giữ file đã có, không ghi đè')
        else:fn(target)

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,default=Path(__file__).parent)
    make_all(parser.parse_args().output_dir)
