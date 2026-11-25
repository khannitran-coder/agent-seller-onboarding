# Chiết khấu Affiliate

> **DRAFT – CHỈ NẠP PROJECT THỬ NGHIỆM (dữ liệu mô phỏng).** Gói này cố ý ghi mọi KU là DRAFT để kiểm hành vi; trạng thái duyệt thật xem gói vận hành. Không dùng để trả lời nhà bán thật; không nạp vào Project vận hành.

### 001:c0012 — Phụ lục Affiliate: định nghĩa, căn cứ tính và phân bổ chiết khấu Affiliate Tổng (A)
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r6
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-004 (Phụ lục Affiliate Hi1 11.11.2026.docx, Điều 2; Điều 3; Điều 4)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0006; exception_of 001:c0007

**Điều kiện**
Nhà bán ký Phụ lục Affiliate với Hi1. Khoản chiết khấu chỉ được ghi nhận khi đơn hàng hợp lệ, giao thành công, được hệ thống xác nhận đủ điều kiện đối soát và không thuộc trường hợp hủy, hoàn, đổi trả hoặc tranh chấp chưa xử lý xong.

**Nội dung**
Chiết khấu Affiliate Tổng (A): mức chiết khấu/hoa hồng do Nhà bán tự cấu hình, cam kết hoặc xác nhận trên hệ thống Hi1 cho từng sản phẩm, nhóm sản phẩm, đơn hàng hoặc chương trình bán hàng, dựa trên giá bán cho hội viên sàn Hi1.
Căn cứ tính A: doanh thu hàng hóa thực tế thu được của các đơn đủ điều kiện, tính theo giá bán cho hội viên sàn Hi1 sau khi trừ giảm giá, mã khuyến mại, voucher do Nhà bán tài trợ; không có khoản giảm nào thì bằng giá bán hội viên. Không tính trên giá thị trường. Căn cứ tính A không bao gồm VAT nếu hai bên có thỏa thuận tính trên giá trước thuế; không bao gồm phí vận chuyển, phí cổng thanh toán, phụ phí phát sinh, khoản hoàn tiền hoặc giảm trừ khác.
Hình thức xác định A: (a) tỷ lệ phần trăm trên giá bán sản phẩm; (b) số tiền cố định trên mỗi sản phẩm/đơn hàng; (c) theo từng chương trình bán hàng, chiến dịch khuyến mại hoặc thỏa thuận riêng giữa Hi1 và Nhà bán.
Công thức: với hình thức %, A = doanh thu hàng hóa làm căn cứ × tỷ lệ chiết khấu Affiliate (%) do Nhà bán thiết lập; với số tiền cố định, A theo mức đã xác nhận trên hệ thống. Tổng tỷ lệ phân bổ là 100% A; có danh sách đính kèm theo từng sản phẩm.
Nhà bán chịu trách nhiệm thiết lập % hoa hồng, xác nhận và đảm bảo nguồn chi trả cho khoản chiết khấu đã cam kết trên hệ thống Hi1.

**Ngoại lệ**
Văn bản Phụ lục Affiliate 11.11.2026 Điều 3 đang ghi “giá bán niêm yết”, chưa sửa theo quyết định ngày 25/11/2026. Khi nhà bán viện dẫn văn bản phụ lục, không tự giải thích, chuyển Bắc.
Khoản chiết khấu không được ghi nhận/bị thu hồi trong các trường hợp ở Điều 10 (xem c0016). Tỷ lệ phân bổ chi tiết cho Agency/cộng tác viên không có trong nguồn (xem Gap Log G-09).

**Chứng từ**
Danh sách đính kèm theo từng sản phẩm (chưa có trong nguồn).

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Bản r6: CF-03 đã quyết giá hội viên trừ voucher do nhà bán tài trợ (quyết định của người thiết kế agent (nhận thẩm quyền owner) ngày 25/11/2026). Cần sửa Phụ lục Affiliate Điều 3.


### 001:c0013 — Phụ lục Affiliate: đối soát và chi hộ hoa hồng cho Agency, cộng tác viên
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r6
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-004 (Phụ lục Affiliate Hi1 11.11.2026.docx, Điều 5 khoản 1–5)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0012

**Điều kiện**
Có đơn hàng Affiliate đủ điều kiện ghi nhận.

**Nội dung**
- Nhà bán ủy quyền Hi1 quản lý toàn bộ dữ liệu Affiliate phát sinh; Hi1 ghi nhận thông tin đơn hàng, mã giới thiệu, tuyến Affiliate, doanh số đủ điều kiện và chiết khấu phát sinh.
- Định kỳ ngày 5 hằng tháng N+1 hoặc theo kỳ đối soát Hi1 công bố, Hi1 lập bảng đối soát gửi Nhà bán, tối thiểu gồm: mã đơn hàng; tên sản phẩm; giá trị đơn hàng đủ điều kiện; mức chiết khấu Affiliate; trạng thái đơn hàng và trạng thái thanh toán.
- Trong 03 (ba) ngày làm việc kể từ ngày Hi1 gửi bảng đối soát, Nhà bán có quyền phản hồi, xác nhận hoặc gửi văn bản/email nêu nội dung chưa thống nhất. Phần có ý kiến chưa được coi là chấp thuận; phần không tranh chấp vẫn đối soát, thanh toán bình thường. Hết hạn mà Nhà bán không phản hồi: bảng đối soát mặc nhiên được xem là đã chấp thuận; Hi1 chuyển tiền hàng đến hạn vào tài khoản Nhà bán sau khi khấu trừ các khoản hợp lệ (nếu có) theo Hợp đồng chính.
- Sau khi bảng đối soát được xác nhận hoặc mặc nhiên chấp thuận, Hi1 chi hộ hoa hồng cho Agency, cộng tác viên. Kỳ chi trả là ngày 05 của tháng N+2 (N là tháng phát sinh) đối với khoản đủ điều kiện và hoàn tất đối soát trước ngày chi trả.

**Ngoại lệ**
Văn bản Phụ lục Affiliate 11.11.2026 Điều 5 khoản 4 đang ghi ngày 05 tháng N+1, chưa sửa theo quyết định ngày 25/11/2026. Khi nhà bán viện dẫn văn bản phụ lục, không tự giải thích, chuyển Bắc.
Khoản chưa đủ điều kiện, đang khiếu nại hoặc đang chờ xác minh được tạm giữ và xử lý vào kỳ chi trả tiếp theo sau khi hoàn tất đối soát. Hai Bên có thể thỏa thuận khác bằng văn bản.

**Chứng từ**
Bảng đối soát do Hi1 lập.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Bản r6: CF-02 đã quyết chi trả ngày 05 tháng N+2 (quyết định của người thiết kế agent (nhận thẩm quyền owner) ngày 25/11/2026). Nội dung khác với văn bản phụ lục hiện hành; cần sửa Phụ lục Affiliate Điều 5.4.


### 001:c0014 — Phụ lục Affiliate: hóa đơn VAT, chứng từ và hoàn trả khi đơn không còn đủ điều kiện
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-004 (Phụ lục Affiliate Hi1 11.11.2026.docx, Điều 6 khoản 1–6)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0013

**Điều kiện**
Hi1 quản lý, vận hành, đối soát và chi hộ cho hệ thống Agency, cộng tác viên; có bảng đối soát được xác nhận.

**Nội dung**
- Căn cứ bảng đối soát được xác nhận, Hi1 xuất hóa đơn VAT cho Nhà bán đối với khoản phí chiết khấu Affiliate/chi phí dịch vụ Affiliate phát sinh theo từng kỳ. Nội dung hóa đơn có thể ghi “Phí dịch vụ quản lý, vận hành và phân phối Affiliate theo bảng đối soát kỳ …” hoặc nội dung tương đương. Thuế suất VAT theo quy định pháp luật tại thời điểm xuất hóa đơn.
- Nhà bán thanh toán đầy đủ giá trị hóa đơn cho Hi1 hoặc đồng ý để Hi1 khấu trừ vào số tiền phải thanh toán cho Nhà bán trong kỳ đối soát.
- Nếu đơn đã đối soát và xuất hóa đơn nhưng sau đó có hoàn trả hàng, khiếu nại được chấp nhận hoặc xác định gian lận làm đơn không đủ điều kiện ghi nhận: Hi1 hoàn trả cho Nhà bán toàn bộ khoản chiết khấu đã thu/khấu trừ cho đơn đó, gồm cả VAT tương ứng nếu đã thu, bằng cấn trừ vào kỳ đối soát liền kề tiếp theo hoặc hoàn tiền theo thỏa thuận; hóa đơn được điều chỉnh hoặc xử lý theo pháp luật về thuế. Hoa hồng chưa chi cho Agency/cộng tác viên: Hi1 dừng chi và hoàn trả hoặc bù trừ cho Nhà bán; khoản đã chi: Hi1 xử lý thu hồi và hoàn trả hoặc bù trừ theo kỳ đối soát tiếp theo.

**Ngoại lệ**
Không nêu ngoại lệ riêng.

**Chứng từ**
Hóa đơn VAT; bảng đối soát.


### 001:c0015 — Phụ lục Affiliate: phương thức thanh toán và trách nhiệm của Nhà bán và Hi1
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-004 (Phụ lục Affiliate Hi1 11.11.2026.docx, Điều 7; Điều 8; Điều 9)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: exception_of 001:c0006; depends_on 001:c0012

**Điều kiện**
Nhà bán và Hi1 đã ký Phụ lục Affiliate.

**Nội dung**
Phương thức thanh toán: (a) Hi1 khấu trừ trực tiếp khoản chiết khấu Affiliate vào số tiền hàng phải thanh toán cho Nhà bán; (b) phương thức khác do hai bên thống nhất bằng văn bản hoặc xác nhận trên hệ thống Hi1. Thời hạn thanh toán: trong kỳ đối soát đơn hàng giữa Sàn Hi1 và nhà bán.
Trách nhiệm Nhà bán: cấu hình đúng mức A trên hệ thống hoặc xác nhận bằng văn bản/thỏa thuận điện tử; đảm bảo giá bán, khuyến mại, chiết khấu và hoa hồng không vi phạm pháp luật và không gây hiểu nhầm cho khách; cung cấp sản phẩm đúng chất lượng, nguồn gốc, cam kết; thanh toán đầy đủ chiết khấu và VAT theo hóa đơn Hi1; phối hợp xử lý khiếu nại, hủy, hoàn, đổi trả, đối soát.
Trách nhiệm Hi1: quản lý hệ thống ghi nhận Affiliate minh bạch, có dữ liệu đối soát; phân bổ chiết khấu đúng cơ chế; chi hộ cho Agency theo dữ liệu hợp lệ; xuất hóa đơn VAT; cung cấp bảng đối soát định kỳ. Hi1 có quyền điều chỉnh, tạm giữ hoặc thu hồi khoản chiết khấu khi phát hiện gian lận, đơn không hợp lệ, khách hoàn trả hàng hoặc tranh chấp chưa xử lý xong.

**Ngoại lệ**
Không nêu.

**Chứng từ**
Không nêu.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Phụ lục này là 'phụ lục riêng' cho phép khấu trừ khoản Affiliate ngoài các khoản ở Điều 4 hợp đồng chính (quan hệ suy luận).


### 001:c0016 — Phụ lục Affiliate: các trường hợp không ghi nhận hoặc bị thu hồi chiết khấu
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-004 (Phụ lục Affiliate Hi1 11.11.2026.docx, Điều 10 khoản 1–5)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0012

**Điều kiện**
Đơn hàng Affiliate thuộc một trong các trường hợp sau.

**Nội dung**
Khoản chiết khấu Affiliate không được ghi nhận hoặc bị thu hồi nếu: (1) đơn bị hủy trước khi giao thành công; (2) khách hoàn trả hàng hoặc từ chối nhận hàng; (3) đơn phát sinh do gian lận, tự mua, tạo đơn ảo, lợi dụng mã giới thiệu hoặc dùng thông tin khách hàng không hợp lệ; (4) sản phẩm bị khiếu nại về chất lượng, nguồn gốc, pháp lý hoặc không được phép lưu thông; (5) Nhà bán và Hi1 có thỏa thuận loại trừ đối với một số sản phẩm, nhóm sản phẩm hoặc chương trình cụ thể.

**Ngoại lệ**
Không nêu.

**Chứng từ**
Không nêu.


### 001:c0017 — Phụ lục Affiliate: điều chỉnh tỷ lệ chiết khấu và hiệu lực của Phụ lục
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-004 (Phụ lục Affiliate Hi1 11.11.2026.docx, Điều 11; Điều 12)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: conflict, gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: exception_of 001:c0002

**Điều kiện**
Nhà bán muốn áp dụng mức chiết khấu Affiliate khác cho từng sản phẩm, nhóm sản phẩm hoặc chiến dịch.

**Nội dung**
- Tỷ lệ phân bổ trong Phụ lục là tỷ lệ Nhà bán tự nguyện áp dụng dựa trên ngân sách Marketing cho sản phẩm.
- Mức khác có thể được xác nhận bằng phụ lục riêng, email, văn bản điện tử hoặc thao tác xác nhận trên hệ thống Hi1.
- Thay đổi tỷ lệ do Nhà bán thiết lập trên hệ thống hoặc thông báo qua email/văn bản điện tử có hiệu lực ngay khi hệ thống Hi1 ghi nhận thành công, nhưng không muộn hơn 24 giờ kể từ thời điểm Nhà bán gửi yêu cầu hoặc thực hiện thao tác; Hi1 cập nhật và ghi nhận trong thời hạn này.
- Đơn phát sinh trước thời điểm thay đổi vẫn áp dụng chính sách có hiệu lực tại thời điểm khách đặt hàng.
- Phụ lục có hiệu lực từ ngày ký, là bộ phận không tách rời của Hợp đồng/Thỏa thuận hợp tác. Nếu nội dung khác Hợp đồng chính, Phụ lục được ưu tiên áp dụng đối với chiết khấu Affiliate, đối soát, chi hộ và xuất hóa đơn VAT. Nội dung không quy định tại Phụ lục thực hiện theo Hợp đồng chính, Quy chế hoạt động Sàn và pháp luật hiện hành.
- Phụ lục lập 02 bản, mỗi bên giữ 01 bản.

**Ngoại lệ**
Ngoại lệ về thứ tự ưu tiên: Phụ lục ưu tiên hơn Hợp đồng chính chỉ đối với các vấn đề nêu trên.

**Chứng từ**
Không nêu.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Mâu thuẫn nghi ngờ CF-01 với c0002 (thông báo trước 24 giờ vs hiệu lực trong 24 giờ sau yêu cầu).


### 001:c0018 — Bảng nhập giá và chiết khấu Affiliate: chiết khấu tính trên giá bán hội viên Hi1
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r6
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-005 (PL GIÁ BÁN CÓ AFFILIATE.xlsx, Sheet Bang_Nhap_Affiliate: ô LƯU Ý, VÍ DỤ, hàng tiêu đề cột; Sheet Huong_Dan: bước 1–4)
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_effective_date, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0012

**Điều kiện**
Nhà bán nhập bảng giá và chiết khấu Affiliate cho sản phẩm tham gia.

**Nội dung**
- Chiết khấu phí Affiliate được tính trên GIÁ BÁN HỘI VIÊN HI1, không tính trên giá thị trường. Khi có giảm giá, mã khuyến mại, voucher do nhà bán tài trợ thì trừ các khoản này khỏi giá hội viên trước khi tính (xem 001:c0012).
- Ví dụ trong nguồn: 100.000 giá thị trường → 80.000 giá hội viên → nhà bán thu về 50.000 → Affiliate 30.000 = 37,5% × 80.000.
- Nhà bán nhập: tên sản phẩm, thương hiệu, ngành hàng; giá thị trường niêm yết trên Hi1 và giá bán hội viên Hi1; % nhà bán thu về và % chiết khấu phí Affiliate. Các cột còn lại (số tiền hội viên tiết kiệm, giá nhà bán thu về, tổng phân bổ, lệch so với giá hội viên, trạng thái) do công thức tự tính.
- Cột 'Trạng thái' nhận giá trị ĐÚNG khi tổng phân bổ bằng giá bán hội viên (lệch = 0).

**Ngoại lệ**
Dòng ví dụ/dòng mẫu (Sản phẩm A, B, C) là dữ liệu minh họa, không phải quy tắc hay dữ liệu thật.

**Chứng từ**
Bảng giá do nhà bán nhập (file Excel).

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Bản r6: CF-03 đã quyết (quyết định của người thiết kế agent (nhận thẩm quyền owner) ngày 25/11/2026). Cấu trúc cột/công thức thuộc cấu hình skill affiliate-price-review (Gap G-07).


### 002:c0013 — Thông báo triển khai mô hình Affiliate cho nhà bán (dự kiến 1/7/2026)
- Trạng thái: DRAFT (chưa duyệt)
- Phiên bản candidate: r1
- Loại: L1/RULE; đối tượng: staff, seller; phạm vi: chưa xác nhận
- Nguồn: SIM-SRC-012 (Kính gửi Quý Nhà bán.docx, Toàn văn thư 'Kính gửi Quý Nhà bán')
- Tài liệu nguồn: đã duyệt (xác nhận 2026-11-25); trạng thái KU ghi ở dòng Trạng thái
- Cờ: gate0_unverified, inferred, missing_owner, scope_unconfirmed
- Quan hệ: depends_on 001:c0012

**Điều kiện**
Nhà bán nhận thông báo từ Hi1 và Phụ lục hợp đồng về cơ chế chiết khấu Affiliate.

**Nội dung**
Hi1 triển khai mô hình tiếp thị liên kết Affiliate cho nhà bán: sản phẩm của nhà bán có thêm Agency và cộng tác viên giới thiệu, chia sẻ link đến khách hàng. Nhà bán không bị thu phí sàn; chỉ chi trả chiết khấu Affiliate khi phát sinh đơn hàng đủ điều kiện.
Tỷ lệ chiết khấu do nhà bán chủ động cài đặt theo từng sản phẩm, nhóm sản phẩm hoặc chương trình bán hàng, phù hợp ngân sách marketing. Hi1 quản lý hệ thống, ghi nhận dữ liệu, đối soát đơn hàng, chi hộ hoa hồng cho Agency/cộng tác viên và xuất hóa đơn VAT theo quy định.
Thời gian dự kiến triển khai: 1/7/2026. Nhà bán được mời tham gia nhóm Zalo để nắm thêm thông tin triển khai.

**Ngoại lệ**
Không nêu.

**Chứng từ**
Phụ lục hợp đồng về cơ chế chiết khấu Affiliate.

> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): Đây là thư thông báo, không phải văn bản chính sách: chỉ bổ trợ SIM-BATCH-001:c0012; ngày 1/7/2026 là 'dự kiến', cần owner xác nhận ngày hiệu lực thực tế. Link nhóm Zalo không đưa vào KU.

