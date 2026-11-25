# Ba form dự kiến

Tác giả: PM - TKC

BẢN NHÁP – không cài đặt, không dùng cho tới khi COO duyệt D-07a/D-07b.

Tên menu cần kiểm lại theo giao diện được phê duyệt. Chỉ người có quyền thực hiện các ô nhạy cảm/ghi; dữ liệu Đỏ không đưa vào AI. Nếu trang có trường Đỏ, AI dừng, không đọc giá trị. Không được hiểu bảng này là quyền sửa trường đang bị guardrails cấm.

## Quản trị → Đối tác

| Trường | Nguồn dữ liệu | Ai điền |
|---|---|---|
| Tên shop | Tên nhà bán xác nhận | AI đề xuất sau D-07b, người duyệt từng lần |
| Logo/chọn tệp | File đã người kiểm | Người |
| SĐT quản trị, email | Dữ kiện xác nhận tại hệ thống chính thức | Người; không đưa PII vào AI |
| Địa chỉ kho, tỉnh/thành, quận/huyện, phường/xã | Địa chỉ nhà bán xác nhận; danh mục hiện hành | Người; AI chỉ đề xuất từ bản đã che nếu được duyệt |
| Loại hình DN, phân phối, kênh, mô hình, mảng phụ trách | Danh mục/chính sách APPROVED, người xác nhận | Người quyết; không suy loại hình từ vốn hoặc giấy chứng nhận |
| Tên pháp lý, MST, người đại diện | Hồ sơ tại hệ thống chính thức | Người |
| Ô mật khẩu, số tài khoản ngân hàng | Quy trình bảo mật chính thức | Người; AI không nhận/nhập/đọc |
| Giấy tờ công ty/sản phẩm, CCCD, chọn tệp | Hồ sơ chính thức | Người; AI không upload |
| GPS | Vị trí kho đã người xác nhận | Người, không tự đoán vị trí |
| Affiliate | Quyết định/chính sách đã duyệt | Người |
| Lưu/Tạo mới | Người kiểm toàn bộ form | Người |

## Quản trị → Thương hiệu

| Trường | Nguồn dữ liệu | Ai điền |
|---|---|---|
| Tên thương hiệu | Tên xác nhận; tìm trùng trước tạo | AI đề xuất sau D-07b, người duyệt từng lần |
| Ảnh/chọn tệp | Logo đã kiểm | Người |
| Độ hot, Trạng thái | Chính sách APPROVED | Người xác nhận, không tự bật |
| Lưu/Tạo mới | Người kiểm | Người |

## Quản trị → Quản lý sản phẩm

| Trường | Nguồn dữ liệu | Ai điền |
|---|---|---|
| Đối tác | Hồ sơ đúng merchant_id, chọn trước Danh mục/Thương hiệu | AI đề xuất sau D-07b, người duyệt từng lần |
| Danh mục, Thương hiệu | Danh mục đã có, đúng dữ kiện | AI đề xuất, không tự tạo mới; không thấy đúng thì dừng |
| Tên, mô tả ngắn, mô tả, HDSD, hashtag | Nháp đã người duyệt, hồ sơ công bố hiện hành | AI đề xuất sau D-07b, người duyệt từng lần |
| Ảnh chính/slide, chọn tệp | File đã kiểm | Người; AI không upload |
| Giá gốc, giá hội viên, giá liên hệ, tồn | Bảng giá/dữ kiện được nhà bán xác nhận | Người; AI không sửa |
| Xuất xứ, chứng nhận, thời hạn | Hồ sơ chính thức được xác nhận | Người |
| Khối lượng gam, quy cách, biến thể, chủng loại | Dữ kiện xác nhận, thuộc tính đã có | Người; AI chỉ chuẩn bị nháp, không tạo thuộc tính mới |
| Trạng thái, vận chuyển, hot, miễn phí vận chuyển, giới hạn tỉnh, affiliate/tỷ lệ | Chính sách và phụ lục đã duyệt | Người; không mặc định bật/tắt |
| Hỗ trợ/CSKH | Kênh được xác nhận | Người, không đưa PII vào AI |
| Lưu/Tạo mới | Người kiểm bảng tóm tắt trước lưu | Người |

Tìm trùng trước tạo; tải lại khi mở form tạo mới; không mở chế độ sửa rồi lưu. AI dừng trước Lưu và báo trường, nguồn, điểm chưa xác nhận, người thực hiện. A01 vào M3 trước theo lệnh từng lần; A05 tối đa M3. Không tự nâng mức.

Nguồn: skill vận hành nội bộ của nhóm (bản 11/2026), đã lược thông tin nội bộ
