# Danh mục kho tri thức

v0.7.0 – pilot, chưa COO duyệt

**Hiện trạng 25/11/2026: 33 KU APPROVED cho pilot, trong đó 2 KU còn mâu thuẫn chưa quyết (CF-01).** CF-02…CF-06 đã quyết cùng ngày; chín KU có revision mới, chi tiết ở [trang chuẩn hóa](../kb-workspace/ai-seller-onboarding/chuan-hoa-mau-thuan.md). Người thiết kế agent duyệt ngày 25/11/2026, thay cho người duyệt được chỉ định; chưa ai đối chiếu từng KU với nguồn. Danh mục này chỉ để TÌM đúng nhóm tài liệu; không phải căn cứ trả lời. Căn cứ là KU đầy đủ trong gói vận hành `kb/`. Khi không có KU APPROVED đúng nội dung, hoặc nội dung đang mâu thuẫn, agent trả đúng câu “Chưa có căn cứ xác nhận”. Không upload bản pilot để thay nguồn duyệt. Riêng Project thử nghiệm (dữ liệu mô phỏng) được nạp gói DRAFT ở mục E để kiểm hành vi; câu trả lời ở đó vẫn phải ghi rõ KU đang ở DRAFT.

Owner và người duyệt: theo quyết định của người thiết kế agent (2026-11-22), owner là Bắc (Phát triển nhà bán), người duyệt là Huyền. Người duyệt không tự duyệt KU do chính mình soạn; mỗi KU có hai người khác nhau soạn và duyệt. Ngoại lệ pilot: đợt duyệt 25/11/2026 do người thiết kế agent quyết; Huyền đối chiếu lại sau.

Duyệt tài liệu nguồn: người thiết kế agent xác nhận ngày 25/11/2026 mọi tài liệu nguồn nghiệp vụ đang dùng (thư mục Drive, Sổ tay nhà bán, thư thông báo Affiliate) đã được duyệt; danh sách từng tài liệu ở [sổ nguồn](../kb-workspace/ai-seller-onboarding/so-nguon.csv). Duyệt tài liệu nguồn khác duyệt KU (ghi trong phiếu duyệt); các mâu thuẫn giữa tài liệu vẫn phải được owner quyết. “Nguồn APPROVED” trong giao thức dưới đây và trong các Skill là KU có trạng thái APPROVED trong gói vận hành; tài liệu nguồn đã duyệt chưa đủ để trả lời.

KU 001:c0001 dùng revision r5, người thiết kế agent duyệt cho pilot ngày 25/11/2026: bỏ câu “số tài khoản là dữ liệu Đỏ… không đưa vào AI” vì trái quyết định giai đoạn 1 ngày 22/11/2026; nội dung nghiệp vụ không đổi.

## A. Giao thức truy xuất (bắt buộc)

1. Bảng B và C chỉ dùng để tìm. Tên nhóm, ý định hay tóm tắt không phải căn cứ trả lời.
2. Trước khi trả lời nghiệp vụ, mở tài liệu hoặc KU đầy đủ và các KU liên quan (ngoại lệ, phụ thuộc, bản thay thế). Thiếu một phần thì không kết luận.
3. Chỉ dùng dòng có Trạng thái KU là APPROVED, còn hiệu lực và đúng phạm vi (loại nhà bán, ngành hàng, kênh). DRAFT và VERIFIED không dùng.
4. Case (L2) và bài học (L3) chỉ để tham khảo nội bộ, không nói với nhà bán như quy định.
5. Hai nguồn mâu thuẫn: không chọn hộ, ghi cả hai và chuyển owner. KU có nhãn MÂU THUẪN CHƯA QUYẾT: phần được nêu trong nhãn không dùng để kết luận hay gửi nhà bán.
6. Không có căn cứ: ghi “Chưa có căn cứ xác nhận” và chuyển owner của nhóm đó. Không hứa ngày duyệt, doanh thu, ưu đãi hay SLA chưa duyệt.
7. Mỗi câu trả lời nghiệp vụ ghi tên tài liệu hoặc mã KU và phiên bản (mục Nguồn trong output contract).

## B. Nhóm tài liệu, nguồn hiện có và trạng thái

Cột Version ghi theo tên file hoặc ngày sửa trên Drive, không phải số phiên bản đã duyệt. KU tạm là mã `batch:cXXXX` trong kb-workspace, với 001 là SIM-BATCH-001 và 002 là SIM-BATCH-002; chỉ để người duyệt đối chiếu. Ngày hiệu lực chưa ghi: KU được dùng từ ngày duyệt trong pilot.

| Nhóm tài liệu cần tìm | Tài liệu hiện có | Duyệt tài liệu nguồn | Owner → duyệt | Version | Ngày hiệu lực | Trạng thái KU | Người duyệt | Ngày rà soát tiếp | KU tạm | Nạp Project |
|---|---|---|---|---|---|---|---|---|---|---|
| Checklist hồ sơ theo loại hình/ngành hàng | Thông tin và giấy tờ mở shop (văn bản mở shop, tờ rơi, Sổ tay nhà bán); giấy tờ riêng cho thực phẩm, TPCN, mỹ phẩm, hàng nhập khẩu. Chưa có checklist theo loại hình DN/HKD/HTX và chưa có OCOP | Đã duyệt 25/11/2026 | Bắc → Huyền | Sổ tay không rõ ngày; văn bản mở shop sửa 21/11/2026 | | APPROVED (pilot) | Người thiết kế agent, 25/11/2026 | | 001:c0001; 002:c0002, c0004 | Vận hành: kb/checklist-mo-shop.md; thử nghiệm: kb-draft/checklist-mo-shop.md |
| Chính sách nhà bán và điều kiện phê duyệt | Mô hình F2C và đối tượng hợp tác (nhà sản xuất, nhập khẩu, đại lý ủy quyền); quy định cơ bản (giá niêm yết, phí ship, nguồn gốc hàng). Chưa có điều kiện duyệt, từ chối, tiêu chí | Đã duyệt 25/11/2026 | Bắc → Huyền | Sổ tay không rõ ngày | | APPROVED (pilot) | Người thiết kế agent, 25/11/2026 | | 001:c0021; 002:c0001, c0010 | Vận hành: kb/chinh-sach-nha-ban.md; thử nghiệm: kb-draft/chinh-sach-nha-ban.md |
| Chính sách nội dung, ngành hàng cấm/có điều kiện | Chỉ có quy định chung “không bán hàng giả, nhái, cấm”. Chưa có danh mục cấm hoặc có điều kiện | Đã duyệt 25/11/2026 (chỉ có quy định chung) | Bắc → Huyền | | | APPROVED (pilot, một phần) | Người thiết kế agent, 25/11/2026 | | 002:c0010 | Vận hành: kb/chinh-sach-nha-ban.md; thử nghiệm: kb-draft/chinh-sach-nha-ban.md |
| Hướng dẫn App Nhà Bán Hi1 hiện hành | Hướng dẫn tải và dùng app; CMS (đăng nhập, thông tin shop, thương hiệu, sản phẩm, đơn hàng); app Hi1 Seller. Menu chưa được xác minh bằng ảnh chụp hiện hành | Đã duyệt 25/11/2026 | Bắc → Huyền | Sổ tay không rõ ngày; ảnh hướng dẫn sửa 02/10/2026 (đã đối chiếu trực quan; không nạp ảnh gốc vì lộ thông tin đăng nhập) | | APPROVED (pilot) | Người thiết kế agent, 25/11/2026 | | 001:c0019; 002:c0005–c0008 | Vận hành: kb/app-cms.md; thử nghiệm: kb-draft/app-cms.md |
| Hướng dẫn vận chuyển/thanh toán/xử lý đơn | Trạng thái đơn hàng, quy trình đơn, thanh toán COD/online, đối soát, đổi trả; hợp đồng mẫu Điều 4 và 6. Biểu phí thanh toán và biểu cước vận chuyển chưa có nội dung | Đã duyệt 25/11/2026 | Bắc → Huyền | 11.11.2026; Sổ tay | | APPROVED (pilot) | Người thiết kế agent, 25/11/2026 | | 001:c0006–c0008; 002:c0007, c0009, c0011, c0012 | Vận hành: kb/don-hang-thanh-toan.md; thử nghiệm: kb-draft/don-hang-thanh-toan.md |
| Mẫu tin và kênh liên hệ chính thức | Mẫu tin A–I trong skills/seller-communication/templates; mẫu A–D đề xuất trong bảng trả lời của COO. Cấu hình Skill, không tạo KU | Chưa ghi nhận (mẫu trong repo) | Bắc → Huyền | v0.1.2 | | DRAFT | | | | Không |
| SLA, lịch làm việc và chuyển cấp | SLA đề xuất thí điểm và ba cấp chuyển cấp trong bảng trả lời của COO (tài liệu nêu rõ chưa phải quy định hiện hành) | Chưa: tài liệu nêu là đề xuất | Bắc → Huyền | | | DRAFT | | | | Không |
| Ánh xạ trạng thái CMS và bằng chứng sẵn sàng bán | Tám nhãn hồ sơ trong docs/06 (khớp bảng trả lời COO), mã CMS thật [CHỜ XÁC MINH]. Sổ tay chỉ có trạng thái đơn hàng và sản phẩm | Một phần: Sổ tay đã duyệt; nhãn docs/06 chưa ghi nhận | Bắc → Huyền | v0.1.0 | | DRAFT | | | 002:c0009 (đơn hàng) | Thử nghiệm: kb-draft/don-hang-thanh-toan.md; vận hành: chưa |
| Hợp đồng hợp tác và phụ lục (phí, đối soát, chấm dứt) | Hợp đồng hợp tác mẫu; quy trình ký hợp đồng và phụ lục. Khối thông tin các bên cần bản che | Đã duyệt 25/11/2026 | Bắc → Huyền | 11.11.2026 | | APPROVED (pilot); CF-01 mở | Người thiết kế agent, 25/11/2026 | | 001:c0002–c0011; 002:c0003 | Vận hành: kb/hop-dong.md; thử nghiệm: kb-draft/hop-dong.md |
| Chiết khấu Affiliate (phụ lục, cơ sở tính, đối soát, chi hộ) | Phụ lục Affiliate; bảng nhập giá; thư thông báo triển khai (dự kiến 1/7/2026). CF-01 chưa quyết | Đã duyệt 25/11/2026 | Bắc → Huyền | 11.11.2026; thư sửa 25/06/2026 | | APPROVED (pilot); CF-01 mở | Người thiết kế agent, 25/11/2026 | | 001:c0012–c0018; 002:c0013 | Vận hành: kb/affiliate.md; thử nghiệm: kb-draft/affiliate.md |
| SOP 12 bước, bàn giao, xử lý sự cố | docs/02, docs/07, docs/09 của repo | Chưa ghi nhận (tài liệu repo) | Bắc → Huyền | v0.1.0 | | DRAFT | | | | Không |

Ngoài phạm vi nhà bán (không đưa vào agent này): ưu đãi “Chủ tịch tặng” dành cho khách hàng (001:c0020), thuộc Marketing.

Mâu thuẫn đang chờ owner: CF-01 (hiệu lực đổi giá/tỷ lệ). Đã quyết 25/11/2026: CF-02 (chi hoa hồng ngày 05 tháng N+2), CF-03 (giá hội viên trừ voucher nhà bán tài trợ), CF-04 (theo hợp đồng), CF-05 (05 ngày lịch), CF-06 (tư vấn theo hợp đồng). Chi tiết trong kb-workspace.

## C. Ý định thường gặp → nhóm cần mở

Ý định lấy từ bảng trả lời đào tạo của COO. Cột KU tạm cho biết KU cần mở; căn cứ là nội dung KU, không phải bảng này.

| Ý định | Nhóm cần mở | KU tạm | Giới hạn khi trả lời |
|---|---|---|---|
| “Anh/chị muốn mở shop trên Hi1” | Checklist; Mẫu tin | 001:c0001; 002:c0004 | Soạn nháp, ghi “Chưa có căn cứ xác nhận” cho mục không có trong KU |
| “Thiếu giấy tờ gì?”, “Kiểm tra hồ sơ doanh nghiệp/HTX” | Checklist | 001:c0001; 002:c0002 | Liệt kê theo KU, dẫn mã; hồ sơ riêng theo loại hình DN/HKD/HTX chưa có nguồn thì không kết luận |
| “Hướng dẫn đưa sản phẩm OCOP lên sàn” | Checklist theo ngành; Ngành hàng cấm/có điều kiện; App | 002:c0002, c0006 | Chưa có nguồn OCOP; chuyển kiểm duyệt ngành hàng |
| Hàng thực phẩm, TPCN, mỹ phẩm, hàng nhập khẩu cần giấy tờ gì | Checklist | 002:c0002 | Nêu danh sách trong KU; chuyển kiểm duyệt ngành hàng |
| Hi1 hợp tác với đối tượng nào (nhà sản xuất, đại lý…) | Chính sách nhà bán | 002:c0001 | Chuyển Trưởng nhóm; không kết luận từ chối nhà bán |
| “Em đăng ký rồi nhưng chưa được duyệt” | Trạng thái CMS; SLA | | Không hứa ngày duyệt; chuyển Trưởng nhóm |
| “Shop đã mở mà không thấy sản phẩm” | Trạng thái CMS; App | 001:c0019; 002:c0006, c0008 | Không đánh dấu sẵn sàng bán; tạo phiếu cho nhân viên đối chiếu |
| “Hỗ trợ đăng 10 sản phẩm đầu tiên” | App; Chính sách nội dung | 002:c0006, c0010 | Hướng dẫn theo bản đã xác minh; claim chỉ khi có chứng cứ |
| Xử lý đơn hàng, trạng thái đơn, đổi trả | Hướng dẫn xử lý đơn | 002:c0007, c0009, c0012 | Hướng dẫn theo nguồn đã duyệt; không hứa hoàn tiền |
| Hỏi về phí, doanh thu, bảo đảm có đơn | Hợp đồng; Affiliate | 001:c0006, c0007, c0021; 002:c0001 | Không cam kết doanh thu hay ưu đãi chưa duyệt; không khẳng định “không có phí”; không dùng “0 phí trung gian” |
| Cách tính chiết khấu Affiliate | Affiliate | 001:c0012, c0018 | Giá hội viên trừ voucher nhà bán tài trợ; văn bản phụ lục chưa sửa thì chuyển Bắc khi nhà bán viện dẫn |
| Lịch đối soát, thời gian nhận tiền hàng | Hợp đồng; Hướng dẫn thanh toán | 001:c0007, c0013; 002:c0011 | Tiền hàng: 05 ngày lịch rồi trả kỳ gần nhất; hoa hồng: xem 001:c0013; thời điểm tiền vào ví chưa có căn cứ |
| Đổi giá hoặc tỷ lệ Affiliate có hiệu lực khi nào | Hợp đồng; Affiliate | 001:c0002, c0017 | Không kết luận: CF-01 chưa quyết |
| Bị gỡ sản phẩm hoặc khóa shop | Chính sách nhà bán; Hợp đồng | 002:c0010; 001:c0004 | Thông báo và 03 ngày làm việc theo hợp đồng; người có quyền quyết định, chuyển Trưởng nhóm |
| Chấm dứt hợp tác, tranh chấp | Hợp đồng | 001:c0010, c0011 | Chuyển pháp chế |

## D. Điều kiện để một dòng được nạp Project

Quy trình chuẩn (đợt pilot 25/11/2026 là ngoại lệ, xem đầu tệp): một dòng chuyển sang APPROVED và được nạp khi đủ: Bắc xác nhận nội dung (owner); Huyền duyệt và ghi phiên bản, ngày hiệu lực; mâu thuẫn liên quan đã được owner quyết; chạy lại các ca đánh giá gắn nhóm đó và đạt cổng cứng. Tài liệu nạp kho dùng chung phải che số CCCD, số tài khoản và chữ ký (Gate 0, xem [phân loại dữ liệu](../docs/04-phan-loai-du-lieu.md)). Điều kiện chạy thử hồ sơ thật: [docs/13](../docs/13-dieu-kien-chay-thu-ho-so-that.md). Vòng đời và trường metadata: [quản trị kho tri thức](../docs/10-quan-tri-kho-tri-thuc.md).

Khi đổi phiên bản nguồn: dừng hướng dẫn cũ, owner kiểm tra hiệu lực trước khi thay. Không nạp mật khẩu, OTP, token hay dữ liệu cá nhân của nhà bán vào kho tri thức dùng chung.

## E. Gói nạp theo Project

Hai Project dùng hai gói khác nhau. Các tệp trong `kb-draft/` và `kb/` do công cụ sinh tự động từ candidate KU, không sửa tay.

| Project | Nạp những gì | Trạng thái hiện tại |
|---|---|---|
| Thử nghiệm (dữ liệu mô phỏng, chạy 14 ca và TC-11…TC-18) | Tệp này; `kb-draft/catalog.md` và 6 tệp nhóm trong `kb-draft/` (33 KU, khoảng 20.000 token kể cả catalog) | Có sẵn. Gói cố ý ghi DRAFT để kiểm hành vi |
| Vận hành (hồ sơ thật) | Tệp này; `kb/catalog.md` và 6 tệp nhóm trong `kb/` | Có sẵn: 33 KU APPROVED cho pilot, 2 KU gắn nhãn mâu thuẫn |

Cách tạo:

1. Gói thử nghiệm: chạy `python tools/export_kb.py`. Công cụ đọc candidate trong kb-workspace và ghi `project/kb-draft/`; bỏ KU ngoài phạm vi nhà bán (001:c0020).
2. Gói vận hành: Huyền (người duyệt) ghi mỗi KU đã duyệt một dòng vào bản sao của [mẫu phê duyệt](../templates/phe-duyet-ku.csv): batch_id, client_record_id, revision, decision, approver, approved_at, effective_from, conflict_resolved. Rồi chạy `python tools/export_kb.py --approvals <đường dẫn tệp>`. Công cụ chỉ lấy dòng decision=APPROVED có đủ approver, approved_at và đúng revision mới nhất (xem “Phiên bản candidate” trong gói); KU có cờ conflict chỉ vào gói khi conflict_resolved=yes, hoặc =hoan kèm mã ở cột mau_thuan_chua_quyet (nạp kèm nhãn mâu thuẫn).
3. Tệp phê duyệt chứa tên người duyệt và ngày duyệt: lưu nội bộ, không commit vào repo. Sau mỗi lần Bắc sửa hoặc thêm candidate, chạy lại cả hai lệnh rồi nạp lại Project.

## F. Tài liệu đặt ở đâu và agent tìm ở đâu

Bản plugin Cowork đóng gói sẵn hai gói trên vào plugin ([docs/14](../docs/14-trien-khai-cowork.md)); đổi KU thì đóng gói và tải plugin lại.

Khi chạy, agent chỉ tìm trong các tệp đã nạp vào Project knowledge. Repo không có kết nối để agent tự đọc thư mục Drive hay kb-workspace.

| Loại | Nơi đặt | Agent vận hành có đọc không |
|---|---|---|
| Bản gốc (Word, PDF, Excel, ảnh) | Thư mục Drive nghiệp vụ, phân quyền theo vai trò | Không |
| Candidate đã chuyển sang .md, kèm metadata | `kb-workspace/ai-seller-onboarding/<batch>/<revision>/candidates/` | Không |
| Tệp phê duyệt của người duyệt | Thư mục nội bộ hạn chế quyền, ngoài repo | Không |
| KU đã duyệt, dạng .md | `project/kb/` do công cụ sinh, rồi tải lên Project knowledge | Có |
| Gói nháp để thử | `project/kb-draft/` | Chỉ Project thử nghiệm |

Không phải mọi tài liệu đã được chuyển sang .md. Chỉ nội dung đã tách thành candidate mới nằm trong gói. Chưa chuyển: biểu phí thanh toán và cước vận chuyển (Phụ lục trống), VTP.pdf và Ủy quyền KTA scan.pdf (đã loại), video hướng dẫn, dòng dữ liệu mẫu trong bảng Excel, nội dung quảng bá.

Thêm hoặc sửa tài liệu: đặt bản gốc lên Drive → xử lý thành candidate (revision mới) → Bắc xác nhận, Huyền duyệt → chạy `tools/export_kb.py --approvals` → thay tệp cũ trong Project knowledge. Bản gốc đặt thêm vào Drive không tự xuất hiện trong Project.

