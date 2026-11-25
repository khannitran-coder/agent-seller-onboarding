# Schema tracker

v0.1.1 – pilot, chưa COO duyệt

Schema dưới đây là đề xuất pilot [CHỜ COO DUYỆT – D-06]. Enum ngoài yêu cầu gốc cần PM/COO kiểm tra; chưa ánh xạ CMS thật [CHỜ XÁC MINH]. Không tự thêm cột để hợp thức hoá dữ liệu thiếu. Ô trống nghĩa chưa biết/chưa áp dụng, không đồng nghĩa đạt; giữ merchant_id và created_at bắt buộc.

| Cột (đúng thứ tự) | Kiểu | Giá trị cho phép / quy tắc |
|---|---|---|
| merchant_id | chuỗi | Mã hồ sơ không PII; ví dụ SIM-001; bắt buộc |
| source_channel | chuỗi | Tên kênh trong danh mục đã duyệt; chưa có danh mục thì để trống |
| created_at | thời gian | Thời điểm nhận lead, ISO 8601 có múi giờ; bắt buộc |
| first_contact_at | thời gian | Lần liên hệ đầu đã được duyệt gửi, ISO 8601 có múi giờ; trống nếu chưa liên hệ |
| seller_type | enum | doanh nghiệp / hộ kinh doanh / HTX; cá nhân tự do chờ QĐ-07, không tự nhận |
| product_category | chuỗi | Danh mục ngành hàng APPROVED; chưa có thì chờ xác minh |
| owner_role | chuỗi | Vai trò/mã nội bộ được phân công, không tên người/SĐT |
| status | enum | Đúng 8 nhãn trong 06-trang-thai.md |
| status_updated_at | thời gian | ISO 8601 có múi giờ; người ghi khi đổi trạng thái |
| shop_status | enum | chưa xác minh / đã gửi đăng ký / được kích hoạt / tạm dừng |
| product_status | enum | chưa xác minh / chưa có / chờ duyệt / hiển thị / không hiển thị |
| ready_status | enum | chưa xác minh / chưa sẵn sàng / chờ Trưởng nhóm xác nhận / sẵn sàng bán |
| missing_items | danh sách chuỗi | Tên mục thiếu, không nội dung giấy tờ; phân cách bằng dấu chấm phẩy |
| checklist_version | chuỗi | Phiên bản chính xác của checklist được dùng; không có thì để trống, chờ nguồn |
| contact_status | enum | chưa liên hệ / đã liên hệ / chờ phản hồi / cần nhắc |
| last_action | chuỗi | Hành động gần nhất + thời điểm có múi giờ; không PII |
| next_action | chuỗi | Hành động tiếp theo, không PII |
| next_due_at | thời gian | ISO 8601 có múi giờ; chỉ hạn đã xác nhận, thiếu thì để trống |
| approval_evidence | chuỗi | Tham chiếu CMS/bằng chứng từ người có quyền, thời điểm; không chép nội dung nhạy cảm |
| risk_flags | danh sách chuỗi | nghi trùng / mâu thuẫn / thiếu nguồn / lỗi hệ thống / chờ kiểm tra ngành hàng / sự cố dữ liệu / khác đã che |
| escalation_to | enum | cấp 1 / cấp 2-kiểm duyệt nhà bán / cấp 2-ngành hàng-pháp chế / cấp 2-kỹ thuật / cấp 2-CSKH-vận chuyển-thanh toán / cấp 3-COO |
| ai_used | boolean | true / false |
| skill_version | chuỗi | Skill sinh nháp dạng seller-communication@0.1.1; nhiều Skill phân cách ; (ví dụ phiên bản cũ seller-communication@0.1.0); trống khi không dùng AI |
| reviewer | chuỗi | Vai trò/mã người duyệt được phép, không PII |
| review_result | enum | duyệt nguyên / sửa nhỏ / sửa lớn / bỏ; trống nếu chưa duyệt |
| handling_minutes | số | Số phút xử lý thực tế ≥0; không cộng thời gian chờ; trống nếu chưa đo |

Mọi cột cấm dữ liệu Đỏ. Trường tự do phải che PII, không ghi tên người/SĐT hoặc URL có token. AI chỉ đọc; nhân viên chịu trách nhiệm ghi sau duyệt. Đồng bộ Sheet–CMS chưa được thiết lập trong repo.

Tuổi hồ sơ = thời điểm chốt − created_at, quy đổi cùng múi giờ; thiếu created_at ghi “Chưa có căn cứ xác nhận”, không lấy status_updated_at thay thế hoặc suy từ merchant_id. created_at sau thời điểm chốt là lỗi dữ liệu, không trả tuổi âm. Thời gian phản hồi đầu tiên = first_contact_at − created_at; first_contact_at trống thì chưa có phản hồi đầu, không coi là 0. Mốc liên hệ trước mốc nhận lead phải chuyển người xác minh.

Schema chưa có lịch sử phân công và lịch làm việc: chưa đủ để tính mọi SLA theo giờ làm việc. Không tự suy lịch làm việc. handling_minutes do người ghi nhận thời gian thao tác, không lấy chênh lệch thời điểm bao gồm chờ. Tổng cộng 26 cột; AI chỉ đọc, owner/người ghi và quyền review/nghiệm thu chờ xác nhận [CHỜ COO DUYỆT – D-06].

Nguồn bổ sung skill_version: HI1-P1A-SOL-001 v0.1 mục §4.1 (ai_prompt_version); BRD HI1-AI-BRD-SD-1.2 mục NFR-03; quy tắc truy vết: dùng skill_version, không tự thêm ai_run_id/source_evidence_ref/human_action_ref.

Tab nhật ký AI riêng trong file tracker theo [header nhật ký](../templates/nhat-ky-ai-header.csv) là BẮT BUỘC trước khi bất kỳ hành động nào chạy ở M3+/M4; không thêm cột vào tracker chính 26 cột và không coi mẫu này là cấp quyền ghi.
