# Hướng dẫn App Nhà Bán và CMS

> **DRAFT – CHỈ NẠP PROJECT THỬ NGHIỆM (dữ liệu mô phỏng).** Gói này cố ý ghi mọi KU là DRAFT để kiểm hành vi; trạng thái duyệt thật xem gói vận hành. Không dùng để trả lời nhà bán thật; không nạp vào Project vận hành.

### 001:c0019 — Hướng dẫn tải và sử dụng App Hi1 – Nhà bán (8 bước)
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r4
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-009 (Hướng Dẫn Tải APP.jpg, Ảnh 'HƯỚNG DẪN TẢI APP Hi1 – NHÀ BÁN': bước 1–4 (khung 1), bước 5–8 (khung 2)); SIM-SRC-008 (GIAO DIỆN APP.jpg, Hai biểu tượng ứng dụng và tên hiển thị dưới biểu tượng)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0001

**Điều kiện**
Nhà bán đã được cấp số điện thoại và mật khẩu đăng nhập (nguồn nêu 'được cấp'; quy trình cấp chưa có trong nguồn).

**Nội dung**
Nhận diện ứng dụng: ứng dụng cho nhà bán có biểu tượng “Hi 1 – NHÀ BÁN” và tên hiển thị “Hi1 - Nhà Bán”. Biểu tượng ghi “SÀN TMĐT VIỆT NAM” (tên hiển thị bắt đầu “Hi1-SànTMĐTV…”) là ứng dụng khác, không dùng cho các bước dưới đây.
Bước 1: trên màn hình nhấp một trong hai biểu tượng CH Play hoặc App Store.
Bước 2: gõ “Hi1 Nhà bán” trên thanh tìm kiếm và nhấn “Cài đặt” để tải ứng dụng.
Bước 3: chọn “ĐĂNG NHẬP” để vào ứng dụng Hi1 – Merchant.
Bước 4: nhập số điện thoại và mật khẩu được cấp và chọn “ĐĂNG NHẬP”.
Bước 5: vào mục “Tình trạng đơn hàng” để kiểm tra các trạng thái của đơn hàng.
Bước 6: bấm vào mục “Sản phẩm của tôi” để bật hoặc tắt sản phẩm hiển thị trên app khách hàng.
Bước 7: chọn mục “Báo cáo” để xem doanh thu ngày, tuần, tháng, năm.
Bước 8: chọn mục “Start Live” để livestream và mục “Phát lại video” để phát lại video đã live.

**Ngoại lệ**
Không nêu.

**Chứng từ**
Không nêu.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Bản r4: nội dung KU không đổi so với r2 (8 bước đã đối chiếu ảnh). Theo quyết định 25/11/2026, nhân viên được gửi ảnh “Hướng Dẫn Tải APP” hiện tại, sau khi người phụ trách xác nhận mật khẩu hiển thị ở bước 4 đã đổi hoặc tài khoản mẫu đã khóa (docs/07). Không nạp ảnh gốc vào Claude (Gap G-29).


### 002:c0005 — CMS (admin.hi1.vn): đăng nhập, cập nhật thông tin shop và quản lý thương hiệu
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-011 (SỔ TAY NHÀ BÁN.pdf (liên kết từ trang Nhà bán của website Hi1), Mục 03 Quản lý phần mềm CMS — khung 'Quản trị shop', 'Quản lý thương hiệu')
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, ocr_low, scope_unconfirmed

**Điều kiện**
Nhà bán có tài khoản được cấp gồm số điện thoại, mật khẩu và mã Captcha.

**Nội dung**
Quản trị shop: truy cập địa chỉ CMS admin.hi1.vn và đăng nhập tài khoản được cấp. Vào dấu V cạnh tên shop → mục “thông tin” → thay banner, logo và các thông tin khác → bấm “cập nhật”.
Quản lý thương hiệu: bấm dấu “+” (Quản lý thương hiệu) → điền tên thương hiệu và logo thương hiệu → “Tạo mới”. Nên tra cứu trước khi tạo mới; chưa có thì mới tạo.

**Ngoại lệ**
Không nêu.

**Chứng từ**
Không nêu.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Đường đi menu theo ảnh hướng dẫn trong sổ tay; chưa được đội quản trị xác minh bằng ảnh chụp có ngày hiệu lực (COO yêu cầu xác minh trước khi lập chỉ dẫn thao tác).


### 002:c0006 — CMS: tạo và đăng sản phẩm, giá, tồn kho, sản phẩm chờ duyệt
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-011 (SỔ TAY NHÀ BÁN.pdf (liên kết từ trang Nhà bán của website Hi1), Mục 03 — khung 'Quản lý sản phẩm')
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, ocr_low, scope_unconfirmed
- Quan hệ: depends_on 001:c0018

**Điều kiện**
Nhà bán đã có shop và tài khoản CMS.

**Nội dung**
Tạo sản phẩm mới: bấm dấu “+” → điền ảnh sản phẩm, slide ảnh → Đối tác (chính là tên cửa hàng) → danh mục sản phẩm → thương hiệu → giá gốc (giá thị trường) → giá bán (giá dành cho hội viên Hi1) → tên loại sản phẩm (tiêu đề chuẩn SEO) → nội dung sản phẩm.
Đăng sản phẩm: tên, mô tả chi tiết, hình ảnh đúng chuẩn, mã SKU. Thiết lập giá bán gồm giá thị trường và giá bán cho sàn Hi1 theo phụ lục ký kết. Quản lý tồn kho: ghi đúng số lượng kho còn hàng. Có thể tạo combo, khuyến mãi, phân loại biến thể (màu sắc, dung tích…).
Sản phẩm chờ duyệt: đang ở trạng thái chờ Admin sàn Hi1 duyệt. Quản lý đánh giá: các đánh giá của khách sau khi mua.

**Ngoại lệ**
Nguồn không nêu thời hạn duyệt sản phẩm.

**Chứng từ**
Không nêu.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Giá bán cho hội viên Hi1 là cơ sở tính chiết khấu Affiliate theo SIM-BATCH-001:c0018 (CF-03 chưa quyết).


### 002:c0007 — CMS: tiếp nhận, xác nhận và in đơn hàng
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-011 (SỔ TAY NHÀ BÁN.pdf (liên kết từ trang Nhà bán của website Hi1), Mục 03 — khung 'Tiếp nhận và xác nhận đơn hàng')
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 002:c0009

**Điều kiện**
Có đơn hàng ở trạng thái chờ xử lý.

**Nội dung**
Bước 1: vào mục “Đơn hàng” → “Chờ xử lý”, bấm “Chi tiết” để xem thông tin đơn.
Bước 2: bấm “Xác nhận” để xác nhận xử lý đơn (có thể xác nhận nhanh trên app nhà bán nếu không dùng máy tính).
Bước 3: bấm biểu tượng máy in để in vận đơn (bill) dán lên gói hàng; chọn đúng khổ giấy (A5/A6/A7).

**Ngoại lệ**
Không nêu.

**Chứng từ**
Không nêu.


### 002:c0008 — App Hi1 Seller: đăng nhập, quản lý sản phẩm, báo cáo, livestream, tài khoản và cài đặt shop
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-011 (SỔ TAY NHÀ BÁN.pdf (liên kết từ trang Nhà bán của website Hi1), Mục 04 Vận hành app nhà bán — các khung 'Các bước sử dụng', 'Quản lý sản phẩm', 'Báo cáo', 'Start Live', 'Quản lý tài khoản', 'Cài đặt thông tin shop', 'Quản lý voucher', 'Quản lý hồ sơ shop')
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, ocr_low, scope_unconfirmed
- Quan hệ: depends_on 001:c0019; depends_on 002:c0009

**Điều kiện**
Nhà bán dùng app Hi1 Seller. Tài khoản đăng nhập dùng chung với tài khoản CMS quản trị sản phẩm: số điện thoại shop đăng ký và mật khẩu do Hi1 cung cấp khi đăng ký tài khoản.

**Nội dung**
- Tra cứu tình trạng đơn hàng: mục “Tình trạng đơn hàng” (quản lý vận đơn). Xử lý đơn theo từng tab trạng thái trong mục “Đơn hàng”.
- Sản phẩm: mục “Sản phẩm của tôi”. “Còn hàng” là tồn kho lớn hơn 0 (tối thiểu bằng 1); nhà bán có thể “Ẩn sản phẩm”. “Hết hàng” là tồn kho bằng 0. “Chờ duyệt” là chờ Admin duyệt để hiện lên app của Hi1.
- Báo cáo: xem doanh thu bán hàng theo ngày, tuần, tháng…
- Start Live: bấm “Start Live” → “Start” để bắt đầu. Ghim sản phẩm: bấm giỏ hàng góc dưới trái → “Ghim” → chọn chỉnh giá nếu muốn giảm giá → “Xác nhận”; “Bỏ ghim” để bỏ.
- Tài khoản: chat với khách; quả chuông thông báo (mục “Hệ thống”, “Cá nhân”); lịch sử đối soát voucher; chỉnh hồ sơ shop (banner, logo — làm trong CMS).
- Cài đặt shop: “Miễn phí vận chuyển” — khi bật, đơn hàng miễn phí cho khách và phí vận chuyển tính cho nhà bán. Thêm thông tin ngân hàng: điền tài khoản doanh nghiệp để nhận tiền hàng thu hộ từ sàn Hi1.

**Ngoại lệ**
Không nêu.

**Chứng từ**
Không nêu.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Bổ sung chi tiết cho SIM-BATCH-001:c0019 (8 bước hướng dẫn tải). Cần ảnh giao diện có phiên bản để xác minh; mật khẩu 'do Hi1 cung cấp' nhưng quy trình cấp chưa có nguồn (Gap G-11 batch 1).

