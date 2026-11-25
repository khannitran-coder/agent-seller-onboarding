# Quy trình 12 bước

v0.1.0 – pilot, chưa COO duyệt

| Bước | AI làm | Người làm | Skill dùng |
|---|---|---|---|
| 1. Nhận lead | Kiểm tra trường thiếu, nháp chào | Tiếp nhận, phân công | seller-communication (A) |
| 2. Kiểm trùng | Gắn cờ nghi trùng | Xác minh, không giao AI gộp/xoá | Không dùng Skill riêng |
| 3. Phân loại | Đề xuất loại hình/ngành hàng | Xác nhận phân loại | seller-document-checklist |
| 4. Đối chiếu checklist | Bảng đủ/thiếu/cần xác minh | Kiểm chứng nguồn và hồ sơ tại hệ thống chính thức | seller-document-checklist |
| 5. Yêu cầu bổ sung | Soạn nháp mục thiếu | Duyệt và gửi qua kênh chính thức | seller-communication (B) |
| 6. Hướng dẫn gian hàng (App Nhà Bán Hi1) | Tóm tắt hướng dẫn APPROVED đúng phiên bản | Hướng dẫn thao tác; nhà bán thực hiện | seller-communication (C, chỉ sau bằng chứng duyệt) |
| 7. Chuẩn hoá sản phẩm đầu tiên | Nháp tiêu đề/mô tả, gắn cờ claim | Nhà bán xác nhận; người có quyền nhập/đăng | first-product-assistant; seller-media-tools (ảnh bản sao); affiliate-price-review (bảng giá) |
| 8. Chuyển duyệt | Nháp [phiếu bàn giao duyệt](../templates/phieu-ban-giao-duyet.md) | Người có quyền chuyển và duyệt trên CMS | seller-document-checklist; seller-media-tools (PDF không có dữ liệu Đỏ) |
| 9. Hướng dẫn vận hành đơn | Tóm tắt hướng dẫn APPROVED | Hướng dẫn và xác nhận nhà bán biết xử lý đơn | Không dùng Skill riêng |
| 10. Kiểm tra sẵn sàng bán | Tổng hợp bằng chứng còn thiếu | Trưởng nhóm xác nhận đủ điều kiện | daily-operations-report |
| 11. Bàn giao + hẹn chăm sóc | Nháp nhắc việc | Bàn giao, thống nhất mốc chăm sóc | seller-communication (D) |
| 12. Báo cáo cuối ngày | Đọc tracker, nháp báo cáo và chuyển cấp | Duyệt báo cáo, cập nhật tracker nếu cần | daily-operations-report |

Mọi đầu ra là nháp; thiếu hướng dẫn hiện hành thì dừng phần phụ thuộc nguồn, không tự dựng thao tác giao diện.

Công cụ mới chỉ kiểm/chuẩn bị nháp ở bước 7–8 theo lệnh và quyền được cấp; không thay quy trình người duyệt. seller-contract-draft và seller-cms-entry nằm trong skills-draft/, KHÔNG cài hoặc dùng trước quyết định tương ứng; không thuộc Skill dùng hằng ngày.

Nguồn: skill vận hành nội bộ của nhóm (bản 11/2026), đã lược thông tin nội bộ
