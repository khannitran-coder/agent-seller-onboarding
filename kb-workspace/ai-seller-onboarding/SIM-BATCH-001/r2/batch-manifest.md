# Batch manifest — SIM-BATCH-001 r2

Revision chỉ gồm record sửa hoặc thêm; record khác giữ ở r1. Định danh mô phỏng như r1.

| Tham số | Giá trị |
|---|---|
| contract_version | hi1-ku-contract/1.1 |
| profile / mode / revision | nocode / A / 2 |
| Lý do | Người dùng yêu cầu đọc phần bổ sung trong thư mục Drive (hướng dẫn app, thoại mở shop) |
| approval_state | UNKNOWN |

## Đối chiếu thư mục Drive

Ngày đối chiếu 25/11/2026: thư mục có 3 thư mục con và 10 file, trùng danh sách và ngày sửa của r1 (mới nhất 21/11/2026). Connector không thấy file nào thêm sau lần xử lý trước.

| source_id | File | Cách đọc ở r2 | Kết quả |
|---|---|---|---|
| SIM-SRC-001 | VĂN MỞ SHOP.docx | Đọc lại | Không đổi. Phần thoại đưa vào Mẫu F (bản ngắn), không tạo KU |
| SIM-SRC-002 | Tờ rơi mở shop | Xem trực tiếp ảnh | Sửa c0001; thêm c0021 (thông điệp phí) |
| SIM-SRC-008 | GIAO DIỆN APP.jpg | Xem trực tiếp ảnh (trước đây ngoài phạm vi) | Dùng cho phần nhận diện ứng dụng của c0019 |
| SIM-SRC-009 | Hướng Dẫn Tải APP.jpg | Xem trực tiếp ảnh | 8 bước khớp; **chặn ảnh gốc** vì có thông tin đăng nhập |

## Records

c0001 (sửa), c0006 (thêm cờ conflict), c0019 (sửa), c0021 (mới). Quan hệ: c0021 depends_on c0006.

## Checkpoint

```yaml
phase_done: [inventory, extract(T1), split(T2), normalize]
blocked:
  - {source_id: SIM-SRC-009, reason: "Dấu hiệu Đỏ: mật khẩu đăng nhập kèm số điện thoại trong ảnh chụp màn hình", locator: "Bước 4, hai ô nhập trên màn hình đăng nhập"}
pending_human:
  - {owner: "Bắc (owner)", records: "đổi mật khẩu tài khoản trong ảnh, thay ảnh đã che trên Drive; quyết CF-06"}
  - {owner: "Huyền (người duyệt)", records: "c0001, c0006, c0019, c0021 r2"}
```
