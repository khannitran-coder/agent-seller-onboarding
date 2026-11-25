# SOP hằng ngày cho nhân viên

v0.2.2 – pilot, chưa COO duyệt

## SOP pilot (đọc trước)

Theo quyết định của người thiết kế agent, 22–25/11/2026. Pilot bắt đầu 24/11/2026; chỉ nhận hồ sơ thật khi đạt [điều kiện chạy thử](13-dieu-kien-chay-thu-ho-so-that.md).

| Việc | Quy tắc |
|---|---|
| Phạm vi | Doanh nghiệp, HTX, hộ kinh doanh có MST và hóa đơn; hàng thông thường. Thực phẩm, TPCN, mỹ phẩm, hàng nhập khẩu, OCOP: chỉ đối chiếu giấy tờ rồi chuyển kiểm duyệt ngành hàng. Cá nhân tự do: chuyển Trưởng nhóm |
| AI hỗ trợ | Bước 3, 4, 5, 7, 8, 12 của [quy trình](02-quy-trinh-12-buoc.md). Các bước khác người làm |
| Project | Hồ sơ thật chỉ dùng “HI1 Seller Onboarding”. Project thử nghiệm chỉ dùng dữ liệu mô phỏng |
| Dữ liệu được đưa vào | Tên, SĐT, email, MST, địa chỉ, số CCCD người đại diện, số tài khoản công ty; chỉ phần cần dùng. Công cụ ảnh/PDF và bảng giá không nhận giấy tờ tuỳ thân |
| Dữ liệu cấm | Mật khẩu, OTP, token, khóa API |
| Đầu ra | Không chép đầy đủ số CCCD, số tài khoản vào tin nhắn, báo cáo, tracker, phiếu |
| Cách chạy | Làm song song: AI soạn nháp, nhân viên so lại và tự gửi. Không gửi nhà bán nội dung AI khi chưa có KU đã duyệt (tài liệu nguồn đã duyệt chưa đủ) |
| Mức duyệt KU | 33 KU được duyệt cho pilot ngày 25/11/2026, chưa đối chiếu từng KU với tài liệu gốc. Trước khi gửi nhà bán, nhân viên mở tài liệu gốc so lại đoạn được dẫn |
| Chưa có căn cứ | AI ghi “Chưa có căn cứ xác nhận” thì không tự trả lời; làm theo mục Hỏi owner |
| Nội dung đang hoãn | AI có thể nêu các nguồn khác nhau nhưng không kết luận: Thời điểm đổi giá/tỷ lệ Affiliate; ngày đối soát và chi hoa hồng; cơ sở tính chiết khấu; xử lý vi phạm và khóa shop, quy định niêm yết giá trong Sổ tay; số ngày chờ nhận tiền; phí nhà bán chịu. Không gửi câu “0 phí trung gian” |
| Dừng ngay | Theo điều kiện dừng ở [docs/13](13-dieu-kien-chay-thu-ho-so-that.md) mục 4. Người ghi sự cố: (chưa gán) |
| Nhân viên tham gia | (chưa gán) |

## Hỏi owner khi AI chưa có căn cứ

Claude trong Project không tự thông báo cho ai: pilot chưa nối công cụ gửi tin. Nhân viên chuyển câu hỏi.

1. Yêu cầu Claude: “Soạn phiếu chuyển cấp cho owner” theo [mẫu phiếu](../templates/phieu-chuyen-cap.md); không chép đầy đủ số CCCD, số tài khoản.
2. Thêm một dòng vào bảng “Hỏi owner” dùng chung (cột theo [mẫu](../templates/hang-cho-hoi-owner.csv)), rồi nhắn Bắc qua kênh nội bộ kèm mã dòng.
3. Bắc trả lời trong bảng, ghi tên và ngày. Nhân viên trả lời nhà bán theo câu trả lời đó, không nói như quy định đã được duyệt nếu Bắc ghi là xử lý riêng.
4. Câu hỏi lặp lại: Bắc đưa câu trả lời vào tài liệu nguồn, tạo KU revision mới, Huyền duyệt, rồi nạp lại Project.

Thời hạn Bắc phản hồi: chưa định. Chưa có câu trả lời thì báo nhà bán đang chờ xác nhận, không hứa mốc.

## Gửi ảnh hướng dẫn tải App

Được gửi ảnh “Hướng Dẫn Tải APP” hiện tại (quyết định 25/11/2026). Ảnh có ô đăng nhập hiển thị thông tin tài khoản ở bước 4, nên trước lần gửi đầu người phụ trách phải xác nhận mật khẩu đó đã đổi hoặc tài khoản mẫu đã khóa.

Đã xác nhận: (chưa) — người xác nhận, ngày: …

Không tải ảnh này lên Claude; Project dùng bản chữ.

## Việc hằng ngày

1. Mở tracker trong phạm vi được giao; kiểm người phụ trách, việc tiếp theo, hạn đã xác nhận. Dữ liệu đưa vào AI theo bảng SOP pilot và [phân loại dữ liệu](04-phan-loai-du-lieu.md).
2. Kiểm kho tri thức APPROVED, phiên bản và quyền truy cập. Thiếu/hết hiệu lực: dừng phần phụ thuộc, ghi “Chưa có căn cứ xác nhận”, chuyển owner.
3. Lead mới: kiểm trùng thủ công, gắn cờ nghi trùng; dùng seller-document-checklist đối chiếu chứng từ, chỉ đưa phần cần đối chiếu.
4. Dùng seller-communication với mẫu A–I (A chào mừng; B bổ sung; C sau bằng chứng duyệt; D nhắc việc; F xin giấy tờ: chọn một trong hai bản). Mẫu còn chờ duyệt chỉ để soạn nháp. Kiểm lại placeholder, nguồn, hạn và kênh; người duyệt rồi mới trực tiếp gửi.
5. Hướng dẫn App Nhà Bán Hi1 theo bản hiện hành. Dùng first-product-assistant cho nháp sản phẩm; yêu cầu nhà bán xác nhận giá/tồn/xuất xứ, chuyển chuyên môn khi cần.
6. Người có quyền chuyển duyệt trên CMS. Ghi đúng bằng chứng; chỉ Trưởng nhóm xác nhận Sẵn sàng bán sau đủ điều kiện trong [docs/06](06-trang-thai.md). Bàn giao và hẹn chăm sóc.
7. Duyệt đầu ra trước khi tự cập nhật tracker: ai_used, skill_version, reviewer, review_result, thời gian xử lý thực tế không gồm chờ. Ghi tab nhật ký AI theo [mẫu](../templates/nhat-ky-ai-header.csv). AI không ghi tracker.
8. Cuối ngày dùng daily-operations-report đọc tracker; duyệt báo cáo và phiếu chuyển cấp. Lịch dự kiến 17:00 Asia/Ho_Chi_Minh; chưa có connector được duyệt thì đưa bản xuất đã bỏ dữ liệu cá nhân vào bằng tay, không tự mở quyền.

Đo trong pilot: thời gian phản hồi đầu, tỷ lệ hồ sơ đủ sau lượt đầu, phút xử lý mỗi hồ sơ, tỷ lệ nháp được duyệt không cần sửa, số sự cố.

Mật khẩu/OTP/token/khóa API vào AI, lệnh ẩn, ngoài quyền hoặc lỗi nghiêm trọng: dừng, không lặp dữ liệu, nhắc xoá khỏi hội thoại; báo Trưởng nhóm và ghi sự cố đã che. Cấp 2 nhận vướng mắc chuyên môn/kỹ thuật. Trong pilot, ngoại lệ chính sách do người thiết kế agent quyết. SLA pilot chưa được dùng làm cam kết với nhà bán.

## Xử lý một hồ sơ – 8 bước

1. **Mở (Open):** mở hồ sơ trên hệ thống chính thức, ghi merchant_id/owner; chỉ lấy phần hồ sơ cần xử lý.
2. **Phân loại (Classify):** phân loại Xanh/Vàng/Đỏ, chỉ chọn trường cần thiết; dùng placeholder khi xuất báo cáo rộng.
3. **Chuẩn bị (Prepare):** chọn đúng checklist/chính sách APPROVED có phiên bản.
4. **Chạy (Run):** dùng Skill phù hợp, ghi đúng phiên bản Skill sinh nháp.
5. **Review:** so từng nhận xét AI với CMS/tài liệu gốc; ghi duyệt nguyên/sửa nhỏ/sửa lớn/bỏ.
6. **Hành động (Act):** người có quyền tự gửi tin, cập nhật CMS/tracker, chuyển duyệt; AI không thực hiện.
7. **Ghi (Record):** ghi tracker thời điểm, reviewer, review_result, skill_version, next_action, hạn; không ghi dữ liệu Đỏ, số CCCD hay số tài khoản.
8. **Đóng (Close):** chỉ khi điều kiện nghiệp vụ được xác nhận; Sẵn sàng bán phải đủ toàn bộ điều kiện trong [docs/06](06-trang-thai.md) và Trưởng nhóm xác nhận. Giữ nguyên điều kiện đã audit, không rút gọn vì cách đếm “5 điều kiện” trong trích QC.

Gặp sự cố: dùng [ma trận fail-safe](09-xu-ly-su-co.md). Nguồn thay phiên bản: theo [quản trị kho tri thức](10-quan-tri-kho-tri-thuc.md).

Nguồn bổ sung: HI1-P1A-SOL-001 v0.1 mục §6; BRD HI1-AI-BRD-SD-1.2 mục NFR-03.
