# Chính sách nhà bán: mô hình F2C, quy định cơ bản, thông điệp phí

> **DRAFT – CHỈ NẠP PROJECT THỬ NGHIỆM (dữ liệu mô phỏng).** Gói này cố ý ghi mọi KU là DRAFT để kiểm hành vi; trạng thái duyệt thật xem gói vận hành. Không dùng để trả lời nhà bán thật; không nạp vào Project vận hành.

### 001:c0021 — Cách tư vấn phí cho nhà bán
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r6
- Loại: L1/RULE; đối tượng: staff; phạm vi: {"seller_type": ["DN", "HKD", "HTX"]}
- Nguồn: SIM-SRC-002 (61e9c3c2dec45e9a07d5.jpg, Dải chữ đỏ dưới tiêu đề)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0006

**Điều kiện**
Nhân viên tư vấn nhà bán về phí khi mở shop.

**Nội dung**
- Câu được dùng: nhà bán được sử dụng sàn Hi1.vn miễn phí; nhà bán chịu phí cổng thanh toán (chỉ tính trên đơn giao thành công thanh toán trực tuyến qua cổng do Hi1 tích hợp), phí vận chuyển nếu có (trường hợp nhà bán miễn phí cho khách) và khoản phí khác chỉ khi có thỏa thuận, xác nhận bằng văn bản hoặc phụ lục riêng (xem 001:c0006).
- Không dùng câu “0 phí trung gian” hoặc nói rằng không có phí nào.

**Ngoại lệ**
Tờ rơi mở shop đang ghi “0 phí trung gian” và chưa được sửa. Khi nhà bán viện dẫn tờ rơi, giải thích theo hợp đồng và chuyển Bắc. Mức phí cổng thanh toán (Phụ lục 01) chưa có nguồn.

**Chứng từ**
Không nêu.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Bản r6: CF-06 đã quyết nói theo hợp đồng, bỏ câu “0 phí trung gian” (quyết định của người thiết kế agent (nhận thẩm quyền owner) ngày 25/11/2026). Cần sửa tờ rơi.


### 002:c0001 — Mô hình F2C của Hi1 và đối tượng nhà bán được hợp tác
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-011 (SỔ TAY NHÀ BÁN.pdf (liên kết từ trang Nhà bán của website Hi1), Mục 01 Giới thiệu mô hình sàn F2C; mục 02 Ghi chú dưới phần Cung cấp thông tin)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0006

**Điều kiện**
Nhà bán muốn hợp tác với sàn Hi1 theo mô hình F2C (Factory to Consumer: bán từ nhà máy đến người tiêu dùng, bỏ qua trung gian).

**Nội dung**
Sàn TMĐT F2C Hi1 chỉ hợp tác với nhà sản xuất, nhà nhập khẩu hoặc đại lý ủy quyền; không hợp tác với trung gian kinh doanh.
Theo mô hình F2C trên Hi1: nhà sản xuất/nhà bán chủ động đăng sản phẩm và tự vận hành gian hàng; sàn kết nối công nghệ, không thu phí sàn, hỗ trợ marketing, CSKH, vận hành, livestream trên app và tích hợp AI; người tiêu dùng mua hàng chính hãng trực tiếp từ nhà sản xuất.

**Ngoại lệ**
Nguồn không nêu ngoại lệ. “Không thu phí sàn” không đồng nghĩa không có phí nào: phí cổng thanh toán và phí vận chuyển (nếu có) vẫn do nhà bán chịu theo hợp đồng.

**Chứng từ**
Không nêu ở mục này.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Phạm vi 'nhà sản xuất, nhà nhập khẩu, đại lý ủy quyền' là trục khác với loại hình DN/HKD/HTX nên facet seller_type để null. Không dùng 'chính hãng' để hứa với khách hay nhà bán khi chưa có chứng cứ.


### 002:c0010 — Quy định cơ bản cho nhà bán: giá niêm yết, phí ship, nguồn gốc hàng hóa
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r2
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-011 (SỔ TAY NHÀ BÁN.pdf (liên kết từ trang Nhà bán của website Hi1), Mục 05 — khung 'Quy định cơ bản cho nhà bán' A–C)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0004

**Điều kiện**
Nhà bán đăng bán sản phẩm trên Hi1.

**Nội dung**
A. Giá niêm yết công khai: mỗi sản phẩm phải có giá rõ ràng, gồm giá thị trường và giá cho hội viên Hi1. Không ghi “inbox giá”, không đăng giá ảo. Thay đổi giá thì cập nhật trực tiếp trên CMS.
B. Phí ship: trường hợp 1, người bán chịu toàn bộ phí; trường hợp 2, khách tự trả 100%. Tùy chỉnh tại mục “Cài đặt miễn phí vận chuyển” trên app Hi1.
C. Hàng hóa phải có nguồn gốc rõ ràng: không bán hàng giả, hàng nhái, hàng cấm. Sản phẩm cần có nhãn mác, mô tả đúng, thông tin xuất xứ rõ ràng. Vi phạm thì có thể bị gỡ sản phẩm, cảnh báo hoặc khóa gian hàng, sau quy trình theo hợp đồng: Hi1 thông báo bằng văn bản/email nêu lý do và yêu cầu khắc phục trong 03 (ba) ngày làm việc (xem 001:c0004).

**Ngoại lệ**
Được tạm ẩn/gỡ ngay nếu có yêu cầu bằng văn bản từ cơ quan nhà nước có thẩm quyền. Chưa có danh mục hàng cấm cụ thể.

**Chứng từ**
Nhãn mác, mô tả, thông tin xuất xứ của sản phẩm.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Bản r2: CF-04 đã quyết theo hợp đồng (quyết định của người thiết kế agent (nhận thẩm quyền owner) ngày 25/11/2026). Sổ tay mục 05 nên bổ sung bước thông báo.

