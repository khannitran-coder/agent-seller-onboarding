# Checklist hồ sơ và giấy tờ mở shop

> **DRAFT – CHỈ NẠP PROJECT THỬ NGHIỆM (dữ liệu mô phỏng).** Gói này cố ý ghi mọi KU là DRAFT để kiểm hành vi; trạng thái duyệt thật xem gói vận hành. Không dùng để trả lời nhà bán thật; không nạp vào Project vận hành.

### 001:c0001 — Thông tin và giấy tờ nhà bán cung cấp để mở shop
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r5
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: {"seller_type": ["DN", "HKD", "HTX"]}
- Nguồn: SIM-SRC-001 (VĂN MỞ SHOP.docx, Đoạn mở đầu + mục 1–8); SIM-SRC-002 (61e9c3c2dec45e9a07d5.jpg, Khung 'ĐIỀU KIỆN MỞ SHOP' mục 1–7; khung 'Điều kiện bắt buộc'; dòng 'cho doanh nghiệp, HTX, hộ kinh doanh')
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed

**Điều kiện**
Nhà bán muốn mở shop trên Hi1. Tờ rơi mở shop (SIM-SRC-002) ghi áp dụng cho doanh nghiệp, HTX, hộ kinh doanh có mã số thuế và hóa đơn hàng hóa.

**Nội dung**
Nhà bán cung cấp các mục sau để Hi1 hỗ trợ mở shop:
1. Đăng ký kinh doanh (file PDF).
2. Tên shop (shop tự đặt tên).
3. Số điện thoại quản trị (không thay được sau khi tạo shop).
4. Địa chỉ kho hàng (địa chỉ để ship đến lấy hàng).
5. Logo công ty (hình ảnh).
6. Email.
7. Số tài khoản ngân hàng của công ty (không dùng số cá nhân).
8. Các bộ giấy tờ về sản phẩm (giấy công bố, giấy chứng nhận…).
Điều kiện bắt buộc (tờ rơi): nhà bán cần đảm bảo đầy đủ hóa đơn đầu vào – đầu ra và các giấy tờ công bố sản phẩm theo quy định.

**Ngoại lệ**
Số điện thoại quản trị không thay được sau khi tạo shop. Tài khoản ngân hàng phải của công ty, không dùng số cá nhân. Nguồn không nêu mục nào được miễn. Tờ rơi chỉ liệt kê 7 mục thông tin (không có mục 8) nhưng nêu giấy tờ công bố sản phẩm là điều kiện bắt buộc.

**Chứng từ**
Đăng ký kinh doanh (PDF); logo công ty; bộ giấy tờ sản phẩm (giấy công bố, giấy chứng nhận…); hóa đơn đầu vào – đầu ra.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): VĂN MỞ SHOP.docx thực chất là mẫu tin gửi nhà bán (cấu hình skill) — phần văn bản mẫu ghi ở Gap Log G-06; KU này chỉ giữ nội dung quy tắc. Bản r2: đã đối chiếu trực quan ảnh tờ rơi, 7 mục và điều kiện bắt buộc khớp; bỏ cờ ocr_low. Bản r5: bỏ câu quy tắc xử lý số tài khoản ở mục Chứng từ vì là cấu hình hành vi AI, không phải chứng từ nhà bán nộp, và đã trái quyết định phân loại dữ liệu giai đoạn 1 ngày 22/11/2026; nội dung nghiệp vụ không đổi.


### 002:c0002 — Giấy tờ cung cấp khi đăng ký shop, kể cả thực phẩm, TPCN, mỹ phẩm và hàng nhập khẩu
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: {"category": ["thực phẩm", "TPCN", "mỹ phẩm"]}
- Nguồn: SIM-SRC-011 (SỔ TAY NHÀ BÁN.pdf (liên kết từ trang Nhà bán của website Hi1), Mục 02 Đăng ký tài khoản người bán — khung 'Cung cấp thông tin')
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0001

**Điều kiện**
Nhà bán cung cấp thông tin cho người phụ trách sàn Hi1 để hỗ trợ tạo tài khoản shop. Các giấy tờ về an toàn thực phẩm, quảng cáo và nhập khẩu áp dụng theo loại sản phẩm nêu dưới đây.

**Nội dung**
- Giấy đăng ký kinh doanh.
- Giấy xác nhận công bố an toàn thực phẩm (từng sản phẩm).
- Giấy xác nhận quảng cáo (đối với TPCN, mỹ phẩm).
- TPCN/mỹ phẩm nhập khẩu: giấy chứng nhận đại lý, hoặc hợp đồng mua bán, hoặc hóa đơn mua hàng.

**Ngoại lệ**
Nguồn không nêu ngoại lệ hay miễn giấy tờ. Nguồn không có danh mục ngành hàng cấm hoặc có điều kiện khác ngoài các nhóm trên.

**Chứng từ**
Giấy đăng ký kinh doanh; giấy xác nhận công bố an toàn thực phẩm (từng sản phẩm); giấy xác nhận quảng cáo (TPCN, mỹ phẩm); giấy chứng nhận đại lý/hợp đồng mua bán/hóa đơn mua hàng (TPCN, mỹ phẩm nhập khẩu).

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Giá trị facet category lấy nguyên văn nguồn, chưa chuẩn hóa theo enum của domain. Bổ sung cho checklist 8 mục ở SIM-BATCH-001:c0001; chưa phải checklist theo loại hình DN/HKD/HTX. Chưa có chứng cứ về OCOP.


### 002:c0004 — Thông tin nhà bán cung cấp để tạo và thiết lập gian hàng
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-011 (SỔ TAY NHÀ BÁN.pdf (liên kết từ trang Nhà bán của website Hi1), Mục 02 — khung 'Tạo và thiết lập gian hàng')
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0001

**Điều kiện**
Nhà bán cung cấp cho người phụ trách của sàn Hi1 để tạo shop.

**Nội dung**
1. Tên shop, tên gian hàng (nên gắn với thương hiệu và sản phẩm).
2. Số điện thoại di động: không đổi được sau khi tạo; dùng làm tài khoản đăng nhập và gắn với ID Livestream.
3. Email của shop: nhận thông tin đơn hàng từ khách và email về đối soát thanh toán.
4. Địa chỉ kho hàng: để ship đến lấy hàng; có thể tạo nhiều địa chỉ kho khác nhau sau khi tạo shop.
5. Logo.
6. Mô tả hoạt động, mô tả shop.
7. Số tài khoản ngân hàng để đối soát tiền hàng.

**Ngoại lệ**
Số điện thoại di động không đổi được sau khi tạo shop.

**Chứng từ**
Logo; thông tin trên. Giá trị số tài khoản ngân hàng nhập tại kênh chính thức, không lặp lại trong tin nhắn hay báo cáo.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Khớp danh sách mở shop ở SIM-BATCH-001:c0001; Sổ tay thêm lý do dùng số điện thoại (tài khoản đăng nhập, ID Livestream), email nhận đơn/đối soát, nhiều kho và mô tả shop.

