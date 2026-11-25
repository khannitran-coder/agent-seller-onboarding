# Batch manifest — SIM-BATCH-002 r1

Mô phỏng như SIM-BATCH-001: `batch_id`, `source_id`, `gate0_id` do Claude đặt để chạy thử quy trình, không lấy từ sổ PM. Nguồn là tài liệu người dùng chỉ định qua trang Nhà bán của website Hi1 (công khai).

| Tham số | Giá trị |
|---|---|
| contract_version | hi1-ku-contract/1.1 |
| profile / mode / revision | nocode / A / 1 |
| agent / domain | AI Seller Onboarding / SEL |
| approval_state | UNKNOWN: chưa có sổ nguồn hoặc nhãn duyệt |
| Gate 0 | Không thấy dữ liệu Đỏ trong nội dung đã đọc; chưa đối chiếu sổ → `gate0_unverified` |
| Owner / người duyệt đề xuất | Bắc (Phát triển nhà bán) / Huyền, theo quyết định của người thiết kế agent |

## Inputs

| source_id | Tài liệu | Cách đọc | Tình trạng |
|---|---|---|---|
| SIM-SRC-011 | SỔ TAY NHÀ BÁN.pdf (liên kết từ trang Nhà bán) | Connector Drive, text | Đã xử lý: 12 candidate (c0001–c0012) |
| SIM-SRC-012 | Kính gửi Quý Nhà bán.docx (thư mục Hợp đồng) | Connector Drive, text | Đã xử lý: 1 candidate (c0013) |

## Trang web đã đọc

- Trang Nhà bán và trang Tài liệu của website Hi1: chỉ là danh mục liên kết (tiêu đề, không có nội dung chính sách).
- Không đọc: video (CMS, vận hành đơn hàng, SEO, viết bài) và file mp4 "Hướng dẫn cài phí Affiliate" không trích được nội dung; thư mục Hợp đồng của website (chỉ liệt kê tên file: biểu "Danh mục cung cấp thông tin gửi Đối tác", thư "Kính gửi Quý Nhà bán", "Ủy quyền KTA scan"); file profile, slide, giấy ĐKKD và giấy phép sàn của công ty (không liên quan hoặc chưa cần).

## Checkpoint

```yaml
phase_done: [inventory, extract(T1), split(T2), normalize]
phase_pending: [QA-human, owner-assignment, approval-ledger]
processed: [SIM-SRC-011, SIM-SRC-012]
blocked: []
out_of_scope: ["Ủy quyền KTA scan (người dùng đã loại ở batch 001)"]
pending_human:
  - {owner: "Bắc (owner)", records: "13 record: xác nhận nội dung; trả lời các mâu thuẫn CF-04, CF-05"}
  - {owner: "Huyền (người duyệt)", records: "13 record: quyết định ở review-index"}
```

## Quy tắc Vàng đã áp dụng

Không đưa vào KU: số hotline, địa chỉ văn phòng, liên kết nhóm Zalo. Tên miền CMS (admin.hi1.vn) giữ nguyên vì là địa chỉ hệ thống của Hi1 cần cho hướng dẫn.

## Xác nhận của người dùng ngày 25/11/2026

Người thiết kế agent xác nhận trong hội thoại: Sổ tay nhà bán (SIM-SRC-011) và thư “Kính gửi Quý Nhà bán” (SIM-SRC-012) đã được duyệt. Chưa đối chiếu sổ nguồn. Đây là duyệt tài liệu nguồn, chưa phải phê duyệt từng KU trích xuất; không giải quyết CF-04, CF-05 và các khoảng trống ở gap-log.

