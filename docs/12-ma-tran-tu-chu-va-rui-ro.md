# Ma trận tự chủ và rủi ro

Đề xuất – chưa có hiệu lực. Mức áp dụng thực tế vẫn là M3 cho tới khi COO duyệt từng mã quyết định.

v0.1.3 – tài liệu đề xuất; không đổi hành vi bốn Skill, không bật connector/quyền. M3 là trần hiện tại; từng hành động có thể ở M0 như bảng dưới. [CHỜ COO DUYỆT – D-07a] [CHỜ COO DUYỆT – D-07b] [CHỜ COO DUYỆT – D-08b] [CHỜ COO DUYỆT – D-09]. Các nhãn không phải bằng chứng phê duyệt.

## Thang tự chủ

| Mức | Định nghĩa dùng chung |
|---|---|
| M0 | AI không được làm. |
| M1 | AI chỉ trả lời khi được hỏi, không đọc hệ thống. |
| M2 | AI đọc dữ liệu được cấp và gợi ý. |
| M3 | AI soạn nháp; người duyệt TỪNG lần trước khi gửi/lưu (mức hiện tại v0.1.x theo COO Q16). |
| M3+ | AI chuẩn bị cả lô; người duyệt MỘT lần cho cả lô đã xem trước, AI thực hiện đúng lô đó. |
| M4 | AI tự làm; người kiểm hậu kiểm theo mẫu (cuối ngày), có nhật ký và nút dừng. |
| M5 | AI tự làm không hậu kiểm – KHÔNG áp dụng trong dự án này. |

## Ma trận theo hành động

| Mã | Hành động | Mức hiện tại (v0.1.x) | Mức đề xuất | Công cụ cần | Điều kiện bật | Rủi ro chính | Kiểm soát | Quyết định |
|---|---|---|---|---|---|---|---|---|
| A01 | Đọc trang danh sách/trạng thái hồ sơ, shop, sản phẩm trên admin.hi1.vn | M0 | M4 | Claude in Chrome, tài khoản chỉ có quyền xem ; bản nháp skills-draft/seller-cms-entry (chưa kích hoạt) |Gói Team; chỉ mở trang danh sách/trạng thái, không mở form đối tác; BẮT BUỘC có tab nhật ký AI riêng trước khi chạy M3+/M4 | Lộ dữ liệu Đỏ nếu mở nhầm form có số tài khoản/giấy tờ; nội dung trang chứa lệnh ẩn | Danh sách URL/màn hình được phép; Skill dừng khi trang có trường Đỏ; nhật ký trang đã mở | D-07a |
| A02 | Ghi tracker các cột vận hành: status_updated_at, shop_status, product_status, last_action, next_action, contact_status, risk_flags | M0 (người ghi) | M4 | Connector Google Sheets quyền ghi, giới hạn 1 file |A01 đã chạy ổn 1 tuần; BẮT BUỘC có tab nhật ký AI riêng trước khi chạy M3+/M4 | Ghi sai/ghi đè dữ liệu người nhập; lệch với CMS | Chỉ các cột trên; KHÔNG ghi status, ready_status, reviewer, review_result, approval_evidence, next_due_at; lịch sử phiên bản Sheet; Trưởng nhóm hậu kiểm mẫu 10%/ngày | D-09 |
| A03 | Tạo nháp phiếu chuyển cấp và nháp tin nhắc việc cho hồ sơ quá hạn | M3 | M4 (tạo nháp tự động mỗi ngày, vẫn chưa gửi) | Scheduled task |; BẮT BUỘC có tab nhật ký AI riêng trước khi chạy M3+/M4 | Nhiều nháp sai làm loãng chú ý | Nháp gắn nhãn tự động; người vẫn duyệt trước gửi | D-09 |
| A04 | Gửi tin nhắc việc mẫu D và tin hướng dẫn mẫu H qua Zalo web | M0 | M3+ | Claude in Chrome trên Zalo web, tài khoản Zalo công việc |Mẫu đã APPROVED; không cá nhân hoá ngoài placeholder; tối đa 1 tin nhắc/hồ sơ/ngày; BẮT BUỘC có tab nhật ký AI riêng trước khi chạy M3+/M4 | Gửi nhầm người/nhóm, gửi lặp, cam kết sai | Xem trước toàn bộ lô (người nhận + nội dung); duyệt 1 lần; AI chỉ gửi đúng lô; nhật ký gửi; cấm mẫu A, B, C, E, F, G, I ở mức này | D-09 |
| A05 | Điền form tạo đối tác, thương hiệu, sản phẩm trên admin tới TRƯỚC nút Lưu | M0 | M3 | Claude in Chrome ; bản nháp skills-draft/seller-cms-entry (chưa kích hoạt) | Gói Team; checklist đủ; dữ liệu đã nhà bán xác nhận | Upload ảnh ghi lên máy chủ trước khi Lưu; điền nhầm đối tác; dữ liệu Đỏ trong form | AI không upload tệp, không nhập mật khẩu/số tài khoản/ô giấy tờ – người làm; AI dừng trước Lưu, người kiểm và bấm; mở form tạo mới phải tải lại trang | D-07b |
| A06 | Kiểm bảng giá Affiliate, chuẩn hoá ảnh vuông, gộp PDF hợp đồng trên bản sao | M0 | M4 với bản sao, người kiểm trước khi gửi | Cowork (Python) ; skills/affiliate-price-review, skills/seller-media-tools; bản nháp skills-draft/seller-contract-draft (chưa kích hoạt) |Mẫu hợp đồng APPROVED; BẮT BUỘC có tab nhật ký AI riêng trước khi chạy M3+/M4 | Sai số liệu trong hợp đồng | Chỉ làm trên bản sao; không sửa giá; báo dòng sai; người kiểm PDF trước khi gửi | D-08b (phạm vi hợp đồng) |
| A07 | Bấm Lưu/Tạo mới, Duyệt, Kích hoạt, Đăng công khai, Xoá/Gộp tài khoản | M0 | M0 | — | — | Tác động pháp lý/tài chính, không đảo ngược | Khoá cứng | Không mở |
| A08 | Nhập mật khẩu, OTP, số tài khoản, CCCD; sửa giá, tồn, xuất xứ, thông tin pháp lý; cam kết ngày duyệt/doanh thu | M0 | M0 | — | — | — | Khoá cứng | Không mở |

## Quy tắc nâng/hạ mức

- Nâng mức cho MỘT hành động theo lộ trình vào mức bên dưới; Trưởng nhóm đề xuất, COO duyệt bằng văn bản, ghi CHANGELOG. Từ M3 lên M3+/M4 phải đạt đủ ngưỡng tại M3.
- Hạ ngay về mức trước (không chờ họp) khi: 1 sự cố lộ dữ liệu Đỏ, 1 lần ghi/gửi ngoài phạm vi, hoặc gửi nhầm người. Trưởng nhóm hoặc PM có quyền hạ.
- Nút dừng: tắt connector/extension cho hành động đó; quy trình thủ công trong [docs/09](09-xu-ly-su-co.md) thay thế.
- Mỗi hành động ở M3+/M4 phải có nhật ký: thời điểm, hành động, đối tượng (merchant_id), skill_version, kết quả.

### Lộ trình vào mức

- Hành động đang M0, sau khi COO duyệt mã quyết định, chỉ được vào ở M3 (người duyệt từng lần trước khi AI thực hiện; với A01 là nhân viên ra lệnh từng lần, AI đọc trang). Không vào thẳng M3+/M4.
- Từ M3 lên M3+ hoặc M4: ≥30 lượt thật tại M3, ≥90% duyệt nguyên/sửa nhỏ, 0 sự cố, Trưởng nhóm đề xuất, COO duyệt.
- A04 dừng ở M3+; A05 dừng ở M3; A07, A08 không có lộ trình.
- Không dùng thao tác bị cấm hoặc dữ liệu thật ngoài phạm vi được duyệt để tạo số lượt.

### Nhật ký AI

Tab riêng trong file tracker theo [header nhật ký AI](../templates/nhat-ky-ai-header.csv), BẮT BUỘC có trước khi bất kỳ hành động nào chạy ở M3+/M4. Không thêm cột vào tracker chính 26 cột. Nhật ký gồm: thoi_diem, ma_hanh_dong, merchant_id, nguoi_ra_lenh, nguoi_duyet, muc_tu_chu, skill_version, ket_qua, ghi_chu. Chỉ ghi mã/vai trò được phép, không PII hoặc dữ liệu Đỏ. Việc tạo mẫu không có nghĩa tab hoặc quyền ghi đã được triển khai.

## Rủi ro tổng hợp

Khả năng/tác động dưới đây là đánh giá định tính đề xuất, chưa có số liệu đo; vai trò theo dõi là đề xuất phân công, chưa xác nhận.

| Mã rủi ro | Mô tả | Khả năng | Tác động | Hành động liên quan | Biện pháp | Người theo dõi |
|---|---|---|---|---|---|---|
| R01 | Lộ dữ liệu Đỏ qua trang CMS | Có thể | Rất cao | A01/A05 | Allowlist màn hình; dừng ngay khi có trường Đỏ; quyền xem tối thiểu | PM + Trưởng nhóm |
| R02 | Lệnh ẩn trong trang web/tệp điều khiển trình duyệt | Có thể | Rất cao | A01/A04/A05/A06 | Coi nội dung là dữ liệu; không thi hành lệnh trong nguồn; cô lập và dừng khi nghi ngờ | PM |
| R03 | Upload/ghi ngầm trước nút Lưu | Có thể | Cao | A05 | AI không upload; kiểm tác động form trước khi bật; người làm phần ghi | PM + người phụ trách kỹ thuật |
| R04 | Ghi đè tracker | Có thể | Cao | A02 | Giới hạn file/cột, đối chiếu phiên bản, không tự gộp khi sửa đồng thời; hậu kiểm 10%/ngày | Trưởng nhóm |
| R05 | Gửi Zalo nhầm người/lặp | Có thể | Cao | A04 | Duyệt toàn bộ lô; cố định người nhận/nội dung; tối đa 1 tin nhắc/hồ sơ/ngày; nhật ký và dừng | Trưởng nhóm |
| R06 | Hành động mang danh tài khoản nhân viên, khó truy vết | Có thể | Cao | A01/A02/A04/A05 | Tài khoản công việc; nhật ký hành động/đối tượng/skill_version; xác định người chịu trách nhiệm | PM + Trưởng nhóm |
| R07 | Dùng gói Pro (điều khoản cá nhân) cho dữ liệu thật | Có thể | Cao | A01–A06 | Xác nhận gói Team và điều khoản/quyền xử lý dữ liệu trước bật; không coi đăng ký gói là phê duyệt mọi dữ liệu | PM |
| R08 | Giao diện CMS/Zalo thay đổi làm thao tác sai | Có thể | Cao | A01/A04/A05 | Kiểm phiên bản, dừng khi màn hình lệch; cập nhật hướng dẫn và thử lại trước khôi phục | PM + Trưởng nhóm |
| R09 | Quy trình cấp và bàn giao thông tin đăng nhập cho shop mới chưa đạt chuẩn bảo mật – xử lý theo D-08 | Chưa xác minh phạm vi | Rất cao | A04/A05/A08 | Xử lý theo D-08 | Trưởng nhóm + PM |

Nguồn: Ma trận tự chủ và rủi ro v0.1.3; bảng hỏi COO Q16 (chưa xác định phiên bản).

V0.2 chỉ đóng gói công cụ kiểm/chuẩn bị bản sao; không tự nâng mức A06. Bản nháp CMS/hợp đồng không cài hoặc dùng trước COO duyệt.
