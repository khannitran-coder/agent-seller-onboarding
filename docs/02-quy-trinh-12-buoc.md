# Quy trình 12 bước

v0.2.0 – pilot, chưa COO duyệt

Cột “Pilot” theo [docs/13 mục 2](13-dieu-kien-chay-thu-ho-so-that.md): quyết định người thiết kế agent ngày 27/11/2026 thêm bước 1, 6, 9, 11 vào phạm vi AI hỗ trợ, vẫn mức tự chủ 3. Cách AI xử lý từng bước ở skill `seller-onboarding` (plugin/skills/seller-onboarding/SKILL.md).

| Bước | AI làm | Người làm | Skill dùng | Pilot |
|---|---|---|---|---|
| 1. Nhận lead | Kiểm tra trường thiếu, nháp chào | Tiếp nhận, phân công | seller-communication (A) | AI hỗ trợ (từ 27/11) |
| 2. Kiểm trùng | Gắn cờ nghi trùng | Xác minh, không giao AI gộp/xoá | Không dùng Skill riêng | Người làm |
| 3. Phân loại | Đề xuất loại hình/ngành hàng | Xác nhận phân loại | seller-document-checklist | AI hỗ trợ |
| 4. Đối chiếu checklist | Bảng đủ/thiếu/cần xác minh | Kiểm chứng nguồn và hồ sơ tại hệ thống chính thức | seller-document-checklist | AI hỗ trợ |
| 5. Yêu cầu bổ sung | Soạn nháp mục thiếu | Duyệt và gửi qua kênh chính thức | seller-communication (B) | AI hỗ trợ |
| 6. Hướng dẫn gian hàng (App Nhà Bán Hi1) | Tóm tắt hướng dẫn APPROVED đúng phiên bản | Hướng dẫn thao tác; nhà bán thực hiện | seller-onboarding (KU app, CMS); seller-communication (H; C chỉ sau bằng chứng duyệt) | AI hỗ trợ (từ 27/11) |
| 7. Chuẩn hoá sản phẩm đầu tiên | Nháp tiêu đề/mô tả, gắn cờ claim | Nhà bán xác nhận; người có quyền nhập/đăng | first-product-assistant; seller-media-tools (ảnh bản sao); affiliate-price-review (bảng giá) | AI hỗ trợ |
| 8. Chuyển duyệt | Nháp [phiếu bàn giao duyệt](../templates/phieu-ban-giao-duyet.md) | Người có quyền chuyển và duyệt trên CMS | seller-document-checklist; seller-media-tools (PDF không có dữ liệu Đỏ) | AI hỗ trợ |
| 9. Hướng dẫn vận hành đơn | Tóm tắt hướng dẫn APPROVED | Hướng dẫn và xác nhận nhà bán biết xử lý đơn | seller-onboarding (KU đơn hàng, đổi trả, đối soát); output-checker bắt buộc | AI hỗ trợ (từ 27/11) |
| 10. Kiểm tra sẵn sàng bán | Tổng hợp bằng chứng còn thiếu | Trưởng nhóm xác nhận đủ điều kiện | daily-operations-report | Người làm |
| 11. Bàn giao + hẹn chăm sóc | Nháp nhắc việc | Bàn giao, thống nhất mốc chăm sóc | seller-communication (D) | AI hỗ trợ (từ 27/11) |
| 12. Báo cáo cuối ngày | Đọc tracker, nháp báo cáo và chuyển cấp | Duyệt báo cáo, cập nhật tracker nếu cần | daily-operations-report | AI hỗ trợ |

Bước 2 và 10 người làm trong pilot: kiểm trùng cần tra CMS (hành động A01 ở docs/12, đang M0), còn điều kiện sẵn sàng bán và nhãn trạng thái CMS chưa có nguồn (docs/13 mục 5). AI không kết luận “không trùng” hay “sẵn sàng bán”.

Mọi đầu ra là nháp; thiếu hướng dẫn hiện hành thì dừng phần phụ thuộc nguồn, không tự dựng thao tác giao diện.

Công cụ mới chỉ kiểm/chuẩn bị nháp ở bước 7–8 theo lệnh và quyền được cấp; không thay quy trình người duyệt. seller-contract-draft và seller-cms-entry nằm trong skills/ và được đóng vào plugin từ 0.5.0 (quyết định người thiết kế agent, 27/11/2026) nhưng KHÔNG dùng trước quyết định tương ứng; khi bị gọi, skill tự dừng; không thuộc Skill dùng hằng ngày.

Nguồn: skill vận hành nội bộ của nhóm (bản 11/2026), đã lược thông tin nội bộ
