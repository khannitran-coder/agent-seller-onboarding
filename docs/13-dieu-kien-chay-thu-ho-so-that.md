# Điều kiện chạy thử với hồ sơ thật

v0.4.0 – pilot, chưa COO duyệt

Danh sách kiểm Chạy/Không chạy cho người thiết kế agent. Quyết định giai đoạn 1 của người thiết kế agent (2026-11-22): không cần COO ký; các nhãn [CHỜ COO DUYỆT] trong repo giữ nguyên làm lịch sử và không chặn pilot. Tài liệu này không coi bản pilot là chính sách đã duyệt.

## 1. Mục tiêu và mức độ của lần chạy thử

Theo bảng trả lời đào tạo của COO và [tổng quan](01-tong-quan.md): AI hỗ trợ quy trình 12 bước từ tiếp nhận nhà bán đến bàn giao sẵn sàng bán, ở mức tự chủ 3. AI đọc dữ liệu được cấp, đối chiếu, soạn nháp; người kiểm tra, gửi tin, thao tác CMS và quyết định. AI không duyệt, kích hoạt, đăng công khai hay gửi tin ra ngoài.

Đầu vào của AI là bộ hồ sơ nhà bán; kho tri thức là các tài liệu nghiệp vụ trên Drive (xử lý qua kb-workspace). Theo [phân loại dữ liệu](04-phan-loai-du-lieu.md), giai đoạn 1 cho phép xử lý tên, SĐT, email, MST, địa chỉ, số CCCD của người đại diện và số tài khoản công ty trong workspace doanh nghiệp. Khi xử lý, AI không lặp lại đầy đủ số CCCD hoặc số tài khoản trong tin nhắn, báo cáo, log, tracker. Mật khẩu, OTP, token, khóa API vẫn bị chặn. Tài liệu nguồn nghiệp vụ đã được người thiết kế agent xác nhận duyệt ngày 25/11/2026 ([sổ nguồn](../kb-workspace/ai-seller-onboarding/so-nguon.csv)); AI chỉ trả lời theo KU đã APPROVED. Khi chưa có KU APPROVED đúng nhóm, AI trả “Chưa có căn cứ xác nhận”; nhân viên không chuyển tiếp lời AI cho nhà bán như căn cứ.

## 2. Phạm vi pilot (đã chốt 2026-11-23 bởi người thiết kế agent)

| Hạng mục | Phạm vi |
|---|---|
| Nhà bán | Doanh nghiệp, HTX, hộ kinh doanh có MST và hóa đơn (theo tờ rơi mở shop). Không nhận cá nhân tự do; gặp thì chuyển Trưởng nhóm |
| Ngành hàng | Hàng thông thường. Thực phẩm, TPCN, mỹ phẩm, hàng nhập khẩu, OCOP: chỉ đối chiếu giấy tờ theo danh sách trong KU 002:c0002 (KU duyệt cho pilot), chuyển kiểm duyệt ngành hàng vì chưa có KU duyệt về điều kiện ngành hàng |
| Bước AI hỗ trợ | Bước 1 (kiểm trường thiếu của lead, nháp chào), 3, 4, 5 (phân loại, đối chiếu checklist, nháp yêu cầu bổ sung), 6 (tóm tắt hướng dẫn App/CMS theo KU), 7 (nháp sản phẩm), 8 (phiếu bàn giao duyệt), 9 (tóm tắt vận hành đơn theo KU), 11 (nháp nhắc việc khi bàn giao), 12 (báo cáo). Bước 2 và 10 do người làm. Bước 1, 6, 9, 11 thêm ngày 27/11/2026 theo quyết định người thiết kế agent, chạy trên bản test với dữ liệu mô phỏng trước (ca BX-01…BX-06). Xem [quy trình](02-quy-trinh-12-buoc.md) |
| Quy mô | 10–15 hồ sơ, 2–4 tuần, 2–3 nhân viên |
| Cách chạy | Song song: nhân viên làm như cũ, AI soạn nháp để so sánh; không gửi nhà bán lời AI chưa có KU APPROVED |
| Ngoài phạm vi | AI gửi tin, sửa CMS hoặc tracker, duyệt, kích hoạt, đăng sản phẩm; hứa ngày duyệt, doanh thu, ưu đãi; trả lời về phí thanh toán, cước vận chuyển, ngành hàng cấm khi chưa có KU APPROVED |
| Đo | Thời gian phản hồi đầu, tỷ lệ hồ sơ đủ sau lượt đầu, phút xử lý mỗi hồ sơ, tỷ lệ nháp được duyệt không cần sửa, số sự cố bằng 0 |
| Ngày bắt đầu | 24/11/2026 (chốt 2026-11-23). Kết thúc dự kiến từ 08/12/2026 đến 22/12/2026 (2–4 tuần). Chỉ nhận hồ sơ thật khi các điều kiện bắt buộc ở mục 3 đạt; ngày 24/11 chưa đạt thì chạy 14 ca trên dữ liệu mô phỏng trước và ghi ngày nhận hồ sơ thật đầu tiên vào CHANGELOG |
| Người tham gia | Người dùng xác nhận 25/11/2026 đã có người tham gia và người ghi sự cố; vai trò cụ thể chưa ghi vào repo |
| Nền tảng | Plugin Cowork (quyết định 25/11/2026), triển khai theo [docs/14](14-trien-khai-cowork.md) |

## 3. Kiểm trước khi chạy

Trạng thái ghi theo bằng chứng trong repo; việc chưa có bằng chứng ghi “Chưa xác nhận”, không suy là đạt.

| # | Điều kiện | Người xác nhận | Trạng thái |
|---|---|---|---|
| 1 | Phạm vi pilot, dữ liệu vào AI, gói Claude | Người thiết kế agent | Đã quyết: dữ liệu, gói (gói doanh nghiệp đã mua, chờ cài đặt) và phạm vi ở mục 2 |
| 2 | Plugin bản test và bản vận hành đóng gói từ repo, cài cho đúng người pilot, qua kiểm khói [docs/14 mục 5](14-trien-khai-cowork.md); hai skill bản nháp seller-cms-entry, seller-contract-draft có trong gói từ 0.5.0 nhưng không dùng trước D-07a/b, D-08b | Người cấu hình | Đóng gói và kiểm script đạt; chưa tải lên, chưa kiểm khói |
| 3 | KU APPROVED cho các nhóm trong [danh mục](../project/knowledge-base-index.md); Huyền ghi phê duyệt vào bản sao của [mẫu](../templates/phe-duyet-ku.csv) rồi chạy `tools/export_kb.py --approvals` để tạo gói vận hành | Bắc (owner), Huyền (duyệt) | Đạt theo quyết định 25/11/2026: người thiết kế agent duyệt 33 KU cho pilot (thay người duyệt; chưa đối chiếu từng KU với nguồn), đã sinh gói `project/kb/`. KU có cho: thông tin và giấy tờ mở shop, hợp đồng, Affiliate, CMS và app, đơn hàng, thanh toán, đổi trả. Chưa có nguồn cho: điều kiện duyệt/từ chối nhà bán, ngành hàng cấm, trạng thái hồ sơ trên CMS, SLA |
| 4 | Owner và người duyệt từng nhóm | Người thiết kế agent | Đã xác định: Bắc là owner, Huyền duyệt |
| 5 | Gate 0 cho tài liệu đưa vào kho dùng chung | Owner tài liệu | Đã áp dụng cho nguồn đã xử lý: khối có số tài khoản và chữ ký bị loại khỏi KU. Hồ sơ nhà bán xử lý từng ca không cần che theo quyết định giai đoạn 1 |
| 6 | Không kết luận phần đang mâu thuẫn (CF-01); dùng đúng quyết định CF-02…CF-06 | Owner | Quyết định 25/11/2026: CF-02…CF-06 đã quyết, chín KU revision mới đã duyệt; CF-01 mở, 2 KU gắn nhãn. Hành vi chưa kiểm trên Cowork. Văn bản gốc (Phụ lục Affiliate, Sổ tay, tờ rơi) chưa sửa |
| 7 | 14 ca pilot và 6 ca bước mở rộng BX-01…BX-06 chạy trên plugin bản test, ghi kết quả thực tế ([test-cases](../tests/test-cases.md)); SAFE-02 đã đổi theo quyết định giai đoạn 1 | Người kiểm định | Chưa chạy |
| 8 | Bộ đánh giá 50–80 ca phân tầng, có phần ca giữ riêng; cổng cứng bằng 0, ba chỉ số mềm đạt ngưỡng (đúng-có-căn-cứ ≥95%, từ chối đúng ≥95%, độ phủ ≥85%) | Người kiểm định | Chưa có bộ ca |
| 9 | Tracker 26 cột và tab nhật ký AI 9 cột đã tạo theo [template](../templates/nhat-ky-ai-header.csv) | Người giữ tracker | Chưa. Chỉ có mẫu |
| 10 | Người phụ trách ghi sự cố (mật khẩu/OTP/token lộ, AI vượt quyền) đã đặt tên, kênh chuyển cấp ([xử lý sự cố](09-xu-ly-su-co.md)) | Người thiết kế agent | Đã có người (người dùng xác nhận 25/11/2026); kênh chuyển cấp chưa ghi |
| 11 | Đã chọn 2–3 nhân viên tham gia và họ đã đọc [SOP](07-sop-nhan-vien.md) | Trưởng nhóm | Đã chọn người (người dùng xác nhận 25/11/2026); chưa xác nhận đã đọc SOP |
| 12 | Đường cơ sở 2–4 tuần cho thời gian phản hồi đầu, tỷ lệ hồ sơ đủ sau lượt đầu, phút xử lý mỗi hồ sơ | Trưởng nhóm | Chưa |

Chỉ chạy với hồ sơ thật khi các mục 1 đến 5, 7 và 9 đến 11 đều Có. Mục 3 tối thiểu phải duyệt nhóm Checklist hồ sơ và Hướng dẫn App; các nhóm chưa có nguồn thì agent trả “Chưa có căn cứ xác nhận”. Mục 6 bắt buộc với nhóm được nạp. Mục 8 và 12 bắt buộc trước khi đánh giá kết quả pilot hay mở rộng.

## 4. Điều kiện dừng ngay

Dừng pilot, báo Trưởng nhóm và ghi sự cố đã che khi có một trong các việc: mật khẩu, OTP, token hoặc khóa API vào AI hay log; số CCCD hoặc số tài khoản đầy đủ xuất hiện trong tin nhắn gửi nhà bán, báo cáo, tracker hoặc repo; nhân viên dùng lời AI chưa có KU APPROVED làm căn cứ gửi nhà bán; AI trích bản DRAFT hoặc case như quy định; AI kết luận phần đang mâu thuẫn; hứa ngày duyệt, doanh thu hay ưu đãi chưa duyệt; AI thực hiện thao tác ghi (gửi tin, sửa CMS, cập nhật tracker); lỗi quyền truy cập. Rollback về bản an toàn trước đó theo [quy tắc thay đổi](08-quy-tac-thay-doi.md) và kiểm thử lại.

## 5. Thông tin cần bổ sung từ nghiệp vụ

Các điểm sau chưa có tài liệu trong Drive hoặc trên trang Nhà bán; Bắc cung cấp hoặc quyết định, Huyền duyệt:

1. Hồ sơ bắt buộc theo loại hình (DN/HKD/HTX) và theo ngành, gồm OCOP.
2. Điều kiện nhận, duyệt, từ chối nhà bán; tiêu chí và ai quyết định.
3. Danh mục ngành hàng cấm hoặc có điều kiện.
4. Tên nhãn trạng thái hồ sơ trên CMS và ai được bấm Duyệt, Kích hoạt (kèm ảnh chụp màn hình có ngày).
5. SLA và các cấp chuyển cấp chính thức.
6. Phí, ưu đãi, vận chuyển, thanh toán và lời hứa được phép dùng khi tư vấn (biểu phí thanh toán và biểu cước vận chuyển còn trống).
7. Bản chép lời hoặc ảnh chụp của các video hướng dẫn CMS, vận hành đơn hàng và cài phí Affiliate.
8. 5–10 ca thực tế đã ẩn danh để hiệu chỉnh câu trả lời.

Các thời hạn SLA, vai trò và tên menu trong bảng trả lời của COO là phương án đề xuất, chưa phải quy định hiện hành của Hi1.

## 6. Việc làm ngay được

- Đối chiếu lại 33 KU với tài liệu gốc theo [trang chuẩn hóa](../kb-workspace/ai-seller-onboarding/chuan-hoa-mau-thuan.md); sửa Phụ lục Affiliate, Sổ tay, tờ rơi theo CF-02…CF-06; quyết CF-01.
- Chạy kiểm khói và 14 ca trên dữ liệu mô phỏng bằng plugin bản test.
- Gửi tài liệu còn thiếu ở mục 5.

Nguồn: bảng trả lời đào tạo AI Agent của COO (phương án đề xuất); kiến trúc Data Pipeline Tri thức v1.0; Sổ tay nhà bán.
