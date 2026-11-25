# Đối soát repo: bước nào cần label — SIM-BATCH-001 r1

Cơ sở: tài liệu "Kiến trúc Data Pipeline Tri thức cho AI Agent – Hi1 v1.0" (Gate 0 → T0 → T1 → T2 → T3 → T4) và 20 candidate của batch này. Cập nhật 2026-11-22: đã áp dụng vào repo cho R1, R2, R3, R4, R7 (chỉ gắn nhãn và thêm khung trống, xem CHANGELOG). R5, R6 là nguyên tắc sử dụng, không sửa file. Mục 1, 2 và 4 là đề xuất cho người kiểm.

## 1. Label theo từng bước của pipeline

| Bước | Label cần gắn | Repo hiện có | Việc cần làm |
|---|---|---|---|
| Gate 0 | Đỏ / Vàng / Xanh theo từng file; `gate0_id`; người kiểm thứ hai | [docs/04](../../../../docs/04-phan-loai-du-lieu.md) có ba nhóm và quy tắc dừng, chưa có sổ theo file, chưa có thư mục `T0-restricted` | Thêm sổ Gate 0 (một dòng một file) và mô tả `T0-restricted` |
| T0 | `source_id`, `version`, hash, `approval_state` (APPROVED / PENDING / UNKNOWN) | [knowledge-base-index](../../../../project/knowledge-base-index.md) chỉ có tên/owner/version/hiệu lực/trạng thái, không có `source_id`, hash, `approval_state` | Thêm sổ nguồn; ánh xạ nhãn `[CHỜ COO DUYỆT – D-xx]` → `approval_state = PENDING` |
| T1 | Cờ `ocr_low`, `image_described`; locator (sheet!ô, mục, trang) | Không có | Quy ước cờ ở tầng trích xuất; áp dụng cho SIM-SRC-002, 008, 009 |
| T2 | `layer`, `authority_type`, `scope`, `sensitivity`, `flags`, `status = DRAFT` | [docs/10](../../../../docs/10-quan-tri-kho-tri-thuc.md): có `status` DRAFT/VERIFIED/APPROVED; hồ sơ 9 trường thiếu `layer`, `authority_type`, `scope`, `sensitivity` | Bổ sung 4 trường để khớp 12 trường của kiến trúc |
| T3 | `status = APPROVED`, `ku_id`, owner, hiệu lực, người duyệt | knowledge-base-index trống, "chưa có tài liệu APPROVED nào" | Chỉ điền sau khi có sổ duyệt; sinh index từ danh sách KU APPROVED |
| T4 | `ku_id` + version trong bản xuất (Project, skills/references, tests) | references trong skill ghi nguồn bằng câu chung "skill vận hành nội bộ của nhóm (bản 11/2026)" | Sau phát hành, thay bằng `ku_id` + version + manifest; hiện chưa có manifest và quy trình thu hồi trong repo |

## 2. Label đề xuất cho 10 file nguồn (Gate 0, để người kiểm xác nhận)

| source_id | File | Label đề xuất | Lý do |
|---|---|---|---|
| SIM-SRC-001 | VĂN MỞ SHOP.docx | Xanh | Chỉ tên mục, không có giá trị |
| SIM-SRC-002 | Tờ rơi mở shop (.jpg) | Xanh | Quảng bá; có hotline công ty |
| SIM-SRC-003 | Hợp đồng hợp tác mẫu | **Đỏ** cho khối thông tin các bên (số tài khoản); các điều khoản còn lại Xanh | Cần bản che khối này |
| SIM-SRC-004 | Phụ lục Affiliate | **Đỏ** cho khối thông tin các bên (số tài khoản) và khối chữ ký | Như trên |
| SIM-SRC-005 | Bảng giá Affiliate (.xlsx) | Xanh | Dòng mẫu giả lập |
| SIM-SRC-006 | VTP.pdf | **Đỏ** | Bản quét hợp đồng có chữ ký/con dấu; tên, SĐT, MST bên thứ ba |
| SIM-SRC-007 | Ủy quyền KTA scan.pdf | **Đỏ** (chưa mở, suy từ tên và loại file) | Bản quét văn bản ủy quyền |
| SIM-SRC-008 | GIAO DIỆN APP.jpg | Chưa biết | Ảnh, chưa trích được |
| SIM-SRC-009 | Hướng dẫn tải App (.jpg) | Xanh | Hướng dẫn giao diện |
| SIM-SRC-010 | Voucher.jfif | Xanh | Ưu đãi cho khách hàng |

## 3. Chỗ lệch giữa repo và nguồn Drive

| # | Repo | Nguồn Drive | Việc cần label / xử lý |
|---|---|---|---|
| R1 | [seller-communication/templates/mau-F-xin-giay-to.md](../../../../skills/seller-communication/templates/mau-F-xin-giay-to.md): 9 mục, câu mở "Sàn TIỀN KIỂM ĐẦU VÀO", dòng đồng bộ lên App của đối tác | VĂN MỞ SHOP.docx chỉ có 8 mục, không có câu mở. Mục 9 (bộ hợp đồng + phụ lục) chỉ gián tiếp từ hợp đồng Điều 10 (đi kèm 03 phụ lục). Dòng đối tác không có trong nguồn nào của batch | Gắn nhãn "chưa có nguồn trong batch" cho mục 9 và dòng đối tác; repo đã tự nhắc xác nhận hiệu lực dòng này |
| R2 | [seller-document-checklist/SKILL.md:34-46](../../../../skills/seller-document-checklist/SKILL.md): checklist 9 mục, điều kiện chủ thể DN/HTX/HKD có MST và hóa đơn | Tờ rơi (SIM-SRC-002) xác nhận điều kiện chủ thể và mục 1–7; văn bản mở shop xác nhận mục 8. Mục 9 như R1. Không có nguồn cho ATVSTP/OCOP | Checklist gắn D-04 PENDING: nên nhận label theo `source_id` cho từng mục; ATVSTP/OCOP gắn "chưa có nguồn" |
| R3 | [knowledge-base-index.md](../../../../project/knowledge-base-index.md): 8 nhóm | Affiliate (c0012–c0018) và hợp đồng/phụ lục (c0002–c0011) không có nhóm; nhóm "SOP 12 bước, bàn giao, xử lý sự cố" của kiến trúc §7 chưa có dòng | Thêm nhóm "Hợp đồng và phụ lục", "Chiết khấu Affiliate", "SOP 12 bước/bàn giao/sự cố" |
| R4 | [affiliate-price-review/references/bang-gia-schema.md:11](../../../../skills/affiliate-price-review/references/bang-gia-schema.md): cột "Cơ sở tính" tuỳ chọn | CF-03: căn cứ tính A chưa thống nhất giữa Phụ lục (sau giảm giá/voucher) và Excel (giá hội viên) | Gắn nhãn "chờ owner Affiliate xác nhận cơ sở tính" cho PR-03 và các ca liên quan |
| R5 | [claude-project-instructions.md:11](../../../../project/claude-project-instructions.md): "chỉ dùng kho APPROVED, có tên tài liệu + phiên bản" | Hợp đồng, phụ lục, bảng giá chỉ là DRAFT, approval_state UNKNOWN | Không dùng 20 candidate làm căn cứ trả lời cho tới khi VERIFIED/APPROVED |
| R6 | README: mẫu C "chỉ sau bằng chứng duyệt" dùng hướng dẫn App | c0019 là DRAFT, ocr_low | Mẫu C chưa có nguồn APPROVED |
| R7 | [docs/04](../../../../docs/04-phan-loai-du-lieu.md): `merchant_id` dùng theo phân quyền | Kiến trúc xếp `merchant_id` là Vàng | Thống nhất nhãn: Vàng (placeholder) |

## 4. Ánh xạ candidate → nhóm tài liệu trong knowledge-base-index

| Nhóm trong index | Candidate | Ghi chú |
|---|---|---|
| Checklist hồ sơ theo loại hình/ngành hàng | c0001 | Chỉ phần thông tin mở shop; thiếu theo ngành |
| Chính sách nhà bán và điều kiện phê duyệt | c0002–c0005, c0009–c0011 | Là hợp đồng mẫu, không phải chính sách duyệt hồ sơ |
| Chính sách nội dung, ngành hàng cấm/có điều kiện | — | Chỉ c0004 (kiểm duyệt nội dung) nêu cơ chế, không có danh mục cấm |
| Hướng dẫn App Nhà Bán Hi1 | c0019 | ocr_low |
| Hướng dẫn vận chuyển/thanh toán/xử lý đơn | c0006–c0008 | Phần vận chuyển nằm trong nguồn bị chặn (VTP.pdf) |
| Mẫu tin và kênh liên hệ chính thức | — | VĂN MỞ SHOP.docx là mẫu tin: đã có Mẫu F |
| SLA, lịch làm việc và chuyển cấp | — | Chỉ rải rác (03 ngày làm việc ở c0004, c0008, c0013) |
| Ánh xạ trạng thái CMS và bằng chứng sẵn sàng bán | — | Không có nguồn |
| (chưa có nhóm) Chiết khấu Affiliate | c0012–c0018 | Thêm nhóm |
| (ngoài phạm vi seller) Ưu đãi khách hàng | c0020 | Marketing |
