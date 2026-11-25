# Batch manifest — SIM-BATCH-001 r1

Dữ liệu giả lập theo xác nhận của người dùng. Mọi định danh bên dưới là giá trị mô phỏng để chạy thử quy trình, không lấy từ sổ PM/backend. Khi chạy dữ liệu thật phải thay bằng `batch_id`, `source_id`, `gate0_id` do sổ cấp.

| Tham số | Giá trị |
|---|---|
| contract_version | hi1-ku-contract/1.1 |
| profile | nocode |
| mode | A (Curate batch) |
| batch_id | SIM-BATCH-001 (mô phỏng, không phải sổ PM) |
| revision | 1 |
| agent | AI Seller Onboarding |
| domain | SEL (19 record), MKT (1 record) |
| Gate 0 | Người dùng xác nhận "giả lập, cứ chạy"; chưa đối chiếu sổ → mọi record có flag `gate0_unverified` |
| approval_state | UNKNOWN cho mọi nguồn: người dùng nói "đã approved" nhưng chưa có sổ hoặc nhãn trong tài liệu |

## Inputs

| source_id | File | version (mô phỏng) | gate0_id (mô phỏng) | Tình trạng | Ghi chú |
|---|---|---|---|---|---|
| SIM-SRC-001 | VĂN MỞ SHOP.docx | drive-mod-2026-11-21 | SIM-G0-001 | Đã xử lý | Là mẫu tin; chỉ lấy phần quy tắc (c0001) |
| SIM-SRC-002 | 61e9c3c2dec45e9a07d5.jpg | drive-mod-2026-10-09 | SIM-G0-002 | Đã xử lý | Tờ rơi mở shop; OCR có đoạn vỡ chữ |
| SIM-SRC-003 | MC. Mẫu Hợp đồng hợp tác 11.11.2026.docx | drive-mod-2026-11-14 | SIM-G0-003 | Xử lý một phần | Chặn khối thông tin các bên (có dấu hiệu Đỏ); Phụ lục I–II không trích xuất được |
| SIM-SRC-004 | Phụ lục Affiliate Hi1 11.11.2026.docx | drive-mod-2026-11-14 | SIM-G0-004 | Xử lý một phần | Chặn khối thông tin các bên và khối chữ ký |
| SIM-SRC-005 | PL GIÁ BÁN CÓ AFFILIATE.xlsx | drive-mod-2026-11-14 | SIM-G0-005 | Đã xử lý | Dòng mẫu A/B/C chỉ là minh họa |
| SIM-SRC-006 | VTP.pdf | drive-mod-2026-10-14 | — | Ngoài phạm vi | Người dùng xác nhận không cần. Trước đó bị chặn: bản quét hợp đồng có chữ ký/con dấu và liên hệ cá nhân bên thứ ba. Không có candidate nào dùng file này |
| SIM-SRC-007 | Ủy quyền KTA scan.pdf | drive-mod-2026-10-14 | — | Ngoài phạm vi | Người dùng xác nhận không cần. Không mở (bản quét văn bản ủy quyền, suy từ tên file) |
| SIM-SRC-008 | GIAO DIỆN APP.jpg | drive-mod-2026-10-02 | — | Ngoài phạm vi | Người dùng xác nhận không cần. Ảnh không có chữ, không trích được |
| SIM-SRC-009 | Hướng Dẫn Tải APP.jpg | drive-mod-2026-10-02 | SIM-G0-009 | Đã xử lý | ocr_low |
| SIM-SRC-010 | Voucher.jfif | drive-mod-2026-10-29 | SIM-G0-010 | Đã xử lý | Ưu đãi cho khách hàng, ngoài phạm vi seller |

## Checkpoint

```yaml
phase_done: [inventory, extract(T1), split(T2), normalize]
phase_pending: [QA-human, owner-assignment, gate0-ledger, approval-ledger]
processed: [SIM-SRC-001, SIM-SRC-002, SIM-SRC-003(partial), SIM-SRC-004(partial), SIM-SRC-005, SIM-SRC-009, SIM-SRC-010]
blocked:
  - {source_id: SIM-SRC-003, reason: "Dấu hiệu Đỏ: số tài khoản ngân hàng trong khối thông tin Bên A", locator: "Khối bảng thông tin Bên A, dòng 'Tài khoản số'"}
  - {source_id: SIM-SRC-004, reason: "Dấu hiệu Đỏ: số tài khoản ngân hàng trong khối thông tin Bên A; khối chữ ký", locator: "Khối bảng thông tin Bên A; bảng ĐẠI DIỆN BÊN A/BÊN B cuối văn bản"}
out_of_scope:
  - {source_id: SIM-SRC-006, reason: "Người dùng xác nhận không cần"}
  - {source_id: SIM-SRC-007, reason: "Người dùng xác nhận không cần"}
  - {source_id: SIM-SRC-008, reason: "Người dùng xác nhận không cần"}
pending_human:
  - {owner: "Gate 0 owner", records: "SIM-SRC-003, 004: tạo bản che khối thông tin các bên và khối chữ ký, kiểm hai người"}
  - {owner: "PM", records: "20 record: cấp batch_id/source_id/gate0_id thật; xác nhận owner theo mảng"}
  - {owner: "Người duyệt nội dung", records: "20 record: quyết định ở review-index; 5 record có flag conflict"}
```

## Quy tắc xử lý Vàng đã áp dụng

- Tên các tổ chức đối tác thanh toán thay bằng `[ORG_1]`, `[ORG_2]` (c0006). Owner có thể quyết định giữ tên thật.
- Giữ nguyên tên văn bản luật và VIAC (cơ quan trọng tài được chỉ định trong điều khoản).
- Không đưa vào KU: địa chỉ, điện thoại, email, mã số thuế, tên người đại diện, số tài khoản của các bên.
