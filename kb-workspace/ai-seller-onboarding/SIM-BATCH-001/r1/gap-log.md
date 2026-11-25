# Gap log — SIM-BATCH-001 r1

| Mã | Khoảng trống | Ảnh hưởng | Cần ai |
|---|---|---|---|
| G-01 | Hợp đồng: Phụ lục I (biểu phí thanh toán), Phụ lục II (phí vận chuyển), Phụ lục 03 (bảng giá) trống hoặc không trích được (nhiều khả năng là ảnh/bảng nhúng; file 2,4 MB). | Agent không trả lời được câu hỏi về mức phí; c0006, c0011 phụ thuộc | Người nạp: trích lại ở T1 (bản che) hoặc cung cấp bảng phí |
| G-02 | ĐÓNG (ngoài phạm vi theo người dùng). VTP.pdf không dùng. Hệ quả còn lại: chưa có nguồn về cước vận chuyển, Phụ lục II của hợp đồng vẫn trống (xem G-01). | Chưa có KU về cước vận chuyển | Người nạp, nếu sau này cần |
| G-03 | ĐÓNG (ngoài phạm vi theo người dùng). Ủy quyền KTA scan.pdf không mở, không dùng. | — | — |
| G-04 | ĐÓNG (ngoài phạm vi theo người dùng). GIAO DIỆN APP.jpg không dùng. | Không có KU về giao diện App | — |
| G-05 | Khối thông tin các bên trong hợp đồng và phụ lục có số tài khoản (Đỏ) cùng địa chỉ, điện thoại, MST, người đại diện (Vàng); khối chữ ký. Đã loại khỏi KU. | Không có KU về thông tin pháp nhân Hi1 | Gate 0 owner: bản che |
| G-06 | VĂN MỞ SHOP.docx là mẫu tin gửi nhà bán (cấu hình skill, không phải KU). Nơi nên đặt: `skills/seller-communication/templates/mau-F-xin-giay-to.md` (đã có, xem repo-label-audit). | Tránh trùng lặp nội dung mẫu tin vào kho | PM |
| G-07 | Bảng Excel: cấu trúc cột, công thức, quy ước chữ đỏ/nền vàng, dòng mẫu là cấu hình công cụ. Nơi nên đặt: `skills/affiliate-price-review/references/` (đã có). Dòng mẫu A/B/C và ô "Ghi chú" lệch số (xem conflict-log) không thành KU. | Tránh trộn cấu hình công cụ vào kho tri thức | PM |
| G-08 | Tờ rơi chứa nội dung quảng bá (báo chí, Quốc hội, "đồng hành cùng doanh nghiệp Việt") và khuyến khích niêm yết giá tốt nhất, miễn phí ship. Không phải quy tắc bắt buộc. | Không đưa vào KU; owner quyết định có dùng làm tư vấn hay không | Owner Marketing/Hỗ trợ nhà bán |
| G-09 | Phụ lục Affiliate Điều 4: tỷ lệ phân bổ A cho Agency/cộng tác viên "có danh sách đính kèm theo từng sản phẩm", nguồn không có danh sách. | c0012 thiếu phần phân bổ | Owner Affiliate |
| G-10 | Không có nguồn nào nêu owner, ngày hiệu lực, người duyệt hay sổ phê duyệt. | 20 record giữ `missing_owner`, `missing_effective_date`, approval_state UNKNOWN | PM, COO |
| G-11 | App guide nêu "mật khẩu được cấp" nhưng nguồn không có quy trình cấp tài khoản cho shop mới (repo đang chờ D-08). | c0019 không thể hướng dẫn cách nhận tài khoản | COO (D-08) |
| G-12 | Phạm vi áp dụng (loại hình DN/HKD/HTX, ngành hàng, kênh) chỉ rõ ở c0001 (từ tờ rơi). Các KU còn lại nguồn im lặng → `null` + `scope_unconfirmed`. | Agent không biết quy tắc áp dụng cho ai | Owner theo mảng |
| G-13 | Voucher "Chủ tịch tặng" (c0020): không có thời hạn, đối tượng, số lượng; là ưu đãi cho khách hàng, ngoài phạm vi seller. Trước khi dùng cần owner Marketing xác nhận còn hiệu lực. | Không được trả lời như ưu đãi đang hiệu lực | Owner Marketing |
| G-14 | Hợp đồng Điều 6 khoản 1: nguồn không nêu cách xử lý đơn có khiếu nại/hoàn trả trong 05 ngày. | c0007 thiếu nhánh xử lý | Owner Tài chính |
| G-15 | Phủ nguồn so với 9 nhóm ưu tiên của kiến trúc: có phần cho nhóm 1 (thông tin mở shop, chưa phải checklist theo loại hình và ngành), 5 (App), 9 (vận chuyển: chưa có nguồn, chỉ có phần thanh toán ở c0006–c0008). Chưa có nhóm 2, 3, 4, 6, 7, 8. | Chưa đủ nguồn để mở kênh trả lời nhà bán | PM thu thập nguồn |
