"""Tác giả: PM - TKC. Tạo tài sản mô phỏng, không có giá trị pháp lý."""
from __future__ import annotations

import argparse
import csv
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
FONT = Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
BOLD = Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
WATERMARK = 'MẪU GIẢ LẬP – KHÔNG CÓ GIÁ TRỊ PHÁP LÝ'


def font(size: int, bold: bool = False):
    return ImageFont.truetype(str(BOLD if bold else FONT), size)


def write_image(name: str, image: Image.Image, force: bool):
    path = ROOT / name
    if path.exists() and not force:
        print(f'Bỏ qua: {name} (đã có)')
        return
    image.save(path, quality=92, optimize=False)
    print(f'Tạo: {name}')


def certificate(name: str, title: str, lines: list[str], force: bool):
    image = Image.new('RGB', (1240, 1754), '#fffefb')
    draw = ImageDraw.Draw(image)
    draw.rectangle((65, 65, 1175, 1689), outline='#222222', width=4)
    draw.text((620, 125), 'TÀI LIỆU MÔ PHỎNG', anchor='mt', font=font(28, True), fill='#222222')
    for index, title_line in enumerate(title.splitlines()):
        draw.text((620, 255 + index * 44), title_line, anchor='mt', font=font(29, True), fill='#111111')
    y = 465
    for line in lines:
        draw.text((145, y), line, font=font(25), fill='#111111')
        y += 92
    # Lớp chữ bán trong suốt đủ lớn để không thể nhầm với giấy thật.
    overlay = Image.new('RGBA', image.size, (0, 0, 0, 0))
    wd = ImageDraw.Draw(overlay)
    wd.text((620, 850), WATERMARK, anchor='mm', font=font(38, True), fill=(80, 80, 80, 95))
    overlay = overlay.rotate(24, resample=Image.Resampling.BICUBIC)
    image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(image)
    draw.text((620, 1590), 'Hi1 test – SIM', anchor='mm', font=font(28, True), fill='#222222')
    write_image(name, image, force)


def logo(force: bool):
    im = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse((235, 160, 765, 690), fill='#268b45')
    d.ellipse((380, 245, 610, 570), fill='#6cbd68')
    d.line((315, 650, 690, 250), fill='#0b5630', width=28)
    d.text((500, 790), 'BM', anchor='mm', font=font(170, True), fill='#176332')
    write_image('logo-thach-den-sim.png', im, force)


def product(force: bool):
    im = Image.new('RGB', (1600, 900), '#b78d65')
    d = ImageDraw.Draw(im)
    for y in range(0, 900, 155):
        d.line((0, y, 1600, y), fill='#8b694b', width=6)
    d.rectangle((565, 220, 1035, 720), fill='#353538', outline='#1a1a1d', width=8)
    d.rectangle((620, 280, 980, 570), fill='#eee9da')
    d.text((800, 385), 'THẠCH ĐEN', anchor='mm', font=font(48, True), fill='#242424')
    d.text((800, 455), 'BẢN MÂY', anchor='mm', font=font(40, True), fill='#242424')
    d.text((800, 95), 'ẢNH SẢN PHẨM GIẢ LẬP', anchor='mm', font=font(56, True), fill='#ffffff')
    write_image('san-pham-ngang-sim.jpg', im, force)


def tracker(force: bool):
    target = ROOT / 'tracker-sim-110.csv'
    if target.exists() and not force:
        print(f'Bỏ qua: {target.name} (đã có)')
        return
    header = (REPO / 'templates/tracker-header.csv').read_text(encoding='utf-8').strip().split(',')
    assert len(header) == 26
    common = dict(source_channel='Zalo', seller_type='hộ kinh doanh', product_category='thực phẩm giả lập', owner_role='NV-SIM', status='CHỜ BỔ SUNG', status_updated_at='2026-11-16T15:00:00+07:00', shop_status='đã gửi đăng ký', product_status='chưa có', ready_status='chưa sẵn sàng', checklist_version='DRAFT-0.1', contact_status='đã liên hệ', last_action='Đã hỏi tài liệu', next_action='Nhắc bổ sung', next_due_at='2026-11-16T16:00:00+07:00', ai_used='false', handling_minutes='20')
    rows = []
    for mid, created, first in [
        ('SIM-110', '2026-11-14T09:00:00+07:00', '2026-11-14T12:00:00+07:00'),
        ('SIM-110A', '', '2026-11-14T12:00:00+07:00'),
        ('SIM-110B', '2026-11-14T09:00:00+07:00', ''),
    ]:
        row = dict.fromkeys(header, '')
        row.update(common)
        row.update(merchant_id=mid, created_at=created, first_contact_at=first)
        rows.append(row)
    with target.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    print(f'Tạo: {target.name}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--force', action='store_true', help='Ghi đè đúng các tài sản do script tạo')
    args = parser.parse_args()
    logo(args.force)
    certificate('ocop-3sao-sim.jpg', 'GIẤY CHỨNG NHẬN OCOP 3 SAO\n(giả lập)', [
        'Sản phẩm: Thạch đen Bản Mây',
        'Đơn vị: Hộ kinh doanh [Tên chủ hộ]',
        'Địa chỉ: Xóm 2, xã Đông Lam (giả lập),',
        'tỉnh Sơn Lam (giả lập)',
        'Ngày cấp: 12/03/2026',
        'Giá trị: 36 tháng',
    ], args.force)
    certificate('nhan-hieu-chung-nhan-sim.jpg', 'GIẤY CHỨNG NHẬN QUYỀN SỬ DỤNG\nNHÃN HIỆU CHỨNG NHẬN\n“THẠCH ĐEN SƠN LAM” (giả lập)', [
        'Cá nhân: [Tên chủ hộ]',
        'Địa chỉ: Tổ dân phố 1, TT Đông Lam (giả lập),',
        'huyện Lam Sơn (giả lập), tỉnh Sơn Lam (giả lập)',
        'Ngày cấp: 10/11/2021',
        'Có giá trị: 05 năm kể từ ngày cấp',
    ], args.force)
    certificate('attp-sim.jpg', 'GIẤY CHỨNG NHẬN CƠ SỞ ĐỦ ĐIỀU KIỆN\nAN TOÀN THỰC PHẨM (giả lập)', [
        'Cơ sở: Hộ kinh doanh Thạch đen Bản Mây',
        'Địa chỉ: Tổ dân phố 2, TT Đông Lam (giả lập),',
        'huyện Lam Sơn (giả lập), tỉnh Sơn Lam (giả lập)',
        'Điện thoại: [SĐT-NB]',
        'Sản phẩm: Thạch đen thương phẩm',
        'Ngày cấp: 27/05/2024',
        'Hiệu lực: 03 năm',
    ], args.force)
    certificate('dkkd-cong-ty-sim.jpg', 'GIẤY CHỨNG NHẬN ĐĂNG KÝ DOANH NGHIỆP\n(giả lập)', [
        'Tên: Công ty TNHH Gốm Hạ Lam (giả lập)',
        'Mã số: [MST-SIM]',
        'Trụ sở: số 4, xã Hạ Lam (giả lập),',
        'tỉnh Sơn Lam (giả lập)',
        'Loại tài liệu: mô phỏng để kiểm thử',
    ], args.force)
    product(args.force)
    tracker(args.force)

if __name__ == '__main__':
    main()
