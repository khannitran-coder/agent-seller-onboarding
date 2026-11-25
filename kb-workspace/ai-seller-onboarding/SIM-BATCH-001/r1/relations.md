# Relations — SIM-BATCH-001 r1

Quan hệ do Claude đề xuất, người duyệt xác nhận. Định dạng `batch_id:client_record_id`.

| Từ | Loại | Đến | Căn cứ |
|---|---|---|---|
| c0002 | depends_on | c0017 | Điều 1 và Điều 11 Phụ lục cùng quy định hiệu lực khi thay đổi giá/tỷ lệ |
| c0003 | depends_on | c0007 | Nghĩa vụ đối soát, thanh toán, xuất hóa đơn |
| c0004 | depends_on | c0010 | Quyền chấm dứt hợp đồng và tạm ẩn/gỡ nội dung |
| c0005 | depends_on | c0009 | Quyền dùng dữ liệu khách hàng bị giới hạn bởi Điều 5 khoản 2 |
| c0006 | depends_on | c0007 | Chi phí cấu thành công thức thanh toán |
| c0007 | depends_on | c0006 | Công thức dùng "Chi phí theo Điều 4" (phụ thuộc hai chiều) |
| c0008 | depends_on | c0007 | Chênh lệch/chậm thanh toán theo Điều 6 khoản 1 |
| c0010 | depends_on | c0011 | Phụ lục và tất toán khi chấm dứt |
| c0011 | depends_on | c0018 | Suy luận: Phụ lục 03 hợp đồng = bảng giá Excel (từ tên file "PL GIÁ BÁN…") |
| c0012 | depends_on | c0006 | A là khoản khấu trừ ngoài các phí ở Điều 4 |
| c0012 | exception_of | c0007 | Phụ lục Affiliate ưu tiên hơn Hợp đồng chính về chiết khấu Affiliate, đối soát, chi hộ, VAT (Điều 12.2) |
| c0013 | depends_on | c0012 | Đối soát dựa trên A |
| c0014 | depends_on | c0013 | Hóa đơn VAT dựa trên bảng đối soát đã xác nhận |
| c0015 | exception_of | c0006 | Phụ lục riêng cho phép khấu trừ Affiliate ngoài các khoản ở Điều 4 |
| c0015 | depends_on | c0012 | Cùng cơ chế A |
| c0016 | depends_on | c0012 | Trường hợp loại trừ A |
| c0017 | exception_of | c0002 | Thay đổi tỷ lệ theo hệ thống có hiệu lực trong 24 giờ |
| c0018 | depends_on | c0012 | Quy tắc tính A áp dụng cho bảng nhập |
| c0019 | depends_on | c0001 | Đăng nhập App sau khi shop được tạo |

Không có `supersedes`: batch đầu, chưa có KU canonical cũ.
