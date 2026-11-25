# Batch manifest — SIM-BATCH-001 r5

| Tham số | Giá trị |
|---|---|
| contract_version | hi1-ku-contract/1.1 |
| profile / mode / revision | nocode / A / 5 |
| Records | c0001: bỏ một câu ở mục Chứng từ và thêm ghi chú cho người duyệt; điều kiện, nội dung, ngoại lệ, danh sách chứng từ không đổi |

Lý do: câu “Giá trị số tài khoản là dữ liệu Đỏ… không đưa vào AI” trái quyết định giai đoạn 1 ngày 22/11/2026 ([phân loại dữ liệu](../../../../docs/04-phan-loai-du-lieu.md)). Quy tắc xử lý dữ liệu nằm ở Project instructions, không đặt trong KU.

Revision này sửa từ candidate r2, không đọc lại file nguồn. Gate 0 chưa xác nhận, giữ cờ `gate0_unverified`. Cập nhật 25/11/2026: người thiết kế agent duyệt c0001 r5 cho pilot, chưa đối chiếu lại với nguồn; gói vận hành đã sinh lại với r5.

```yaml
pending_human:
  - {owner: "Huyền (người duyệt)", records: "đối chiếu c0001 với tài liệu gốc cùng đợt 33 KU"}
```
