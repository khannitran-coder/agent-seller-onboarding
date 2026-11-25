"""Tác giả: PM - TKC. Chỉ PDF đã được người kiểm dữ liệu."""
import argparse
from pathlib import Path
from pypdf import PdfReader,PdfWriter

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('output_dir',type=Path);p.add_argument('output_name');p.add_argument('parts',nargs='+',type=Path)
    a=p.parse_args();created=False;target=None
    try:
        out=a.output_dir.resolve();target=out/a.output_name
        if Path(a.output_name).name!=a.output_name or not a.output_name.lower().endswith('.pdf'):raise ValueError('Chỉ tên PDF mới')
        parts=[v.resolve() for v in a.parts]
        if target.exists() or any(v==target.resolve() or v.parent==out for v in parts):raise ValueError('Không ghi đè hoặc dùng thư mục nguồn')
        writer=PdfWriter()
        for i,part in enumerate(parts,1):
            if not part.is_file() or part.suffix.lower()!='.pdf':raise ValueError('Đầu vào không phải PDF')
            reader=PdfReader(part)
            if reader.is_encrypted or not reader.pages:raise ValueError('PDF khoá/rỗng')
            print(f'Phần {i}: {len(reader.pages)} trang')
            for page in reader.pages:writer.add_page(page)
        out.mkdir(parents=True,exist_ok=True)
        with target.open('xb') as stream:
            created=True;writer.write(stream)
        print(f'Tổng: {len(writer.pages)} trang; file: {target.name}');writer.close()
    except Exception as exc:
        if created and target:target.unlink(missing_ok=True)
        p.exit(1,f'Lỗi gộp PDF: {type(exc).__name__}; không có bản gộp hoàn tất.\n')
if __name__=='__main__':main()
