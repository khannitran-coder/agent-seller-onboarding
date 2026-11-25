"""Tác giả: PM - TKC. Chỉ ảnh đã được người xác nhận không chứa dữ liệu Đỏ."""
import argparse
from pathlib import Path
from PIL import Image, ImageFilter, ImageOps

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input',type=Path);p.add_argument('output_dir',type=Path);p.add_argument('--nen-trang',action='store_true')
    a=p.parse_args();created=[]
    try:
        src,out=a.input.resolve(),a.output_dir.resolve()
        if not src.exists():raise ValueError('Thiếu đầu vào')
        exts={'.jpg','.jpeg','.png','.webp','.bmp'}
        files=[src] if src.is_file() else sorted(f for f in src.iterdir() if f.is_file() and f.suffix.lower() in exts)
        if not files or any(f.suffix.lower() not in exts for f in files):raise ValueError('Không có ảnh hợp lệ')
        targets=[out/(f.stem+'-vuong.jpg') for f in files]
        if len(set(targets))!=len(targets):raise ValueError('Trùng tên')
        for f,dst in zip(files,targets):
            if f.parent==out or dst.exists() or f==dst.resolve():raise ValueError('Không ghi đè hoặc dùng thư mục nguồn')
            with Image.open(f) as im:im.verify()
        out.mkdir(parents=True,exist_ok=True)
        for f,dst in zip(files,targets):
            with Image.open(f) as raw:
                im=ImageOps.exif_transpose(raw).convert('RGB');side=min(max(im.size),1400)
                bg=Image.new('RGB',(side,side),'white') if a.nen_trang else ImageOps.fit(im,(side,side)).filter(ImageFilter.GaussianBlur(40))
                im.thumbnail((side,side));bg.paste(im,((side-im.width)//2,(side-im.height)//2))
                with dst.open('xb') as stream:
                    created.append(dst);bg.save(stream,'JPEG',quality=88)
                print(f'{dst.name}: {side}x{side}')
    except Exception as exc:
        for dst in created:dst.unlink(missing_ok=True)
        p.exit(1,f'Lỗi chuẩn bị ảnh: {type(exc).__name__}; kiểm tra đầu vào/đầu ra.\n')
if __name__=='__main__':main()
