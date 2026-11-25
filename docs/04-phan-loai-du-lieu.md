# Phân loại dữ liệu

v0.1.2 – pilot, chưa COO duyệt

[CHỜ COO DUYỆT – D-02]

| Nhóm | Nội dung | Quy tắc |
|---|---|---|
| Xanh | Chính sách đã duyệt, checklist, mẫu tin, hướng dẫn giao diện | Chỉ bản APPROVED hiện hành; bản pilot không tự thành APPROVED |
| Vàng | Loại hình, ngành hàng, trạng thái, mục thiếu, tên shop, nội dung sản phẩm, tên người, SĐT, email, MST, địa chỉ | Chỉ dùng trên gói Claude doanh nghiệp được cấp. Giai đoạn 1 dùng giá trị thật trong workspace theo quyết định bên dưới; placeholder khi xuất báo cáo rộng hoặc ghi vào repo |
| Vàng nhạy cảm (giai đoạn 1) | Số CCCD của người đại diện, số tài khoản ngân hàng của công ty, ảnh giấy tờ trong hồ sơ nhà bán | Được xử lý trong workspace doanh nghiệp; không lặp lại đầy đủ trong đầu ra; không vào repo, kho tri thức dùng chung, tracker hoặc log rộng |
| Đỏ | OTP, mật khẩu, token, khóa API | Không bao giờ đưa vào AI hoặc repo |

[Quyết định giai đoạn 1 – người thiết kế agent, 2026-11-22; không cần COO ký] Trong workspace doanh nghiệp được cấp, được xử lý dữ liệu hồ sơ nhà bán gồm tên, SĐT, email, MST, địa chỉ, số CCCD của người đại diện và số tài khoản ngân hàng của công ty. Chỉ dùng trường cần thiết; không lặp lại đầy đủ số CCCD hoặc số tài khoản trong tin nhắn, báo cáo, log, tracker hoặc phiếu (ghi “đã nhận” hoặc 4 số cuối); không ghi vào repo. Nếu input chứa mật khẩu, OTP, token hoặc khóa API: dừng ngay, không lặp lại giá trị, không xử lý hay lưu; nhắc người dùng xoá khỏi hội thoại và ghi sự cố qua người phụ trách, chỉ ghi mã SIM-xxx/loại sự cố.

Dùng [Tên NB], [Tên nhân viên], [SĐT], [Mã hồ sơ], [kênh chính thức], [thời điểm]. Ví dụ chỉ SIM-xxx, không dùng số giả giống dữ liệu thật. Giai đoạn 1: không bắt buộc che dữ liệu hồ sơ nhà bán trước khi đưa vào workspace doanh nghiệp; tài liệu nạp kho tri thức dùng chung vẫn che. Không dùng AI để che ảnh giấy tờ (dùng công cụ PDF). Mã merchant_id vận hành chỉ được dùng theo phân quyền; repo chỉ có SIM-xxx. [CHỜ COO DUYỆT – D-02] Theo kiến trúc Data Pipeline v1.0, merchant_id thuộc nhóm Vàng vì truy ngược được nhà bán: mặc định thay [Mã hồ sơ], chỉ dùng mã thật khi COO quyết định. Không lưu bản nguồn/ảnh/link chứa bí mật. Sự cố được người ghi tại nơi được phép, không lặp lại giá trị bị lộ.

## Gate 0 trước mọi xử lý AI

[CHỜ COO DUYỆT – D-02] Đề xuất theo kiến trúc Data Pipeline v1.0, chưa có hiệu lực: người nạp tài liệu (owner) đánh dấu từng file khi tải lên là có hay không chứa dữ liệu Đỏ (số tài khoản, CCCD, hợp đồng có chữ ký). Có: bản gốc vào thư mục hạn chế quyền “T0-restricted” (chỉ owner và COO), tạo bản che có người thứ hai kiểm; chỉ bản che đi tiếp vào trích xuất và biên tập. Mỗi file một dòng trong sổ Gate 0 (mã Gate 0, nhãn Đỏ/Vàng/Xanh, người kiểm) do PM giữ nội bộ, không lưu trong repo. Công cụ biên tập tri thức không tự xác nhận Gate 0 và dừng file khi còn thấy dấu hiệu Đỏ. Tài liệu có khối thông tin các bên trong hợp đồng (số tài khoản, chữ ký) phải che trước khi xử lý. Giai đoạn 1: Gate 0 chỉ bắt buộc cho tài liệu đưa vào kho tri thức dùng chung; hồ sơ nhà bán xử lý từng ca theo quyết định ở trên. Công cụ biên tập tri thức giữ nguyên quy tắc dừng với dữ liệu Đỏ của tài liệu nguồn.

Ghi chú nguồn L2: HI1-P1A-SOL-001 v0.1 §4 xếp SĐT/liên hệ vào RED; Architecture Review v1.3 đã chốt thay bằng placeholder. Theo kết quả kiểm định, giữ phân loại repo/v1.3, không đổi SĐT thành dữ liệu Đỏ. Token vẫn bị chặn theo guardrails đã audit.
