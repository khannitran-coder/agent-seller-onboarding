# Hướng dẫn đọc và góp ý

Tác giả: PM - TKC

Mục đích: team nghiệp vụ đọc thiết kế AI hỗ trợ nhà bán, chỉ ra chỗ sai với thực tế, chỗ cần sửa và đề xuất cải tiến trước khi chạy pilot. Không cần đọc code.

## 1. Đọc gì (theo vai trò)

| Vai trò | Đọc | Thời gian |
|---|---|---|
| Tất cả | README: phần giới thiệu, Kiến trúc hiện tại, Quyết định đang chờ; docs/01 | 10 phút |
| Nhóm hỗ trợ và phát triển nhà bán | docs/07 SOP, docs/02 quy trình 12 bước, skills/seller-communication/templates (mẫu tin A–I), docs/09 xử lý sự cố | 30 phút |
|  Nhóm hỗ trợ và phát triển nhà bán | Thêm: docs/05 tracker, docs/06 trạng thái, docs/12 mức tự chủ và rủi ro, tests/test-cases.md (ca TC và SAFE) | 45 phút |
|  Nhóm hỗ trợ và phát triển nhà bán| skills/seller-document-checklist (9 mục giấy tờ), skills/first-product-assistant (nội dung sản phẩm, claim), docs/03 guardrails | 30 phút |
| COO | README: Kiến trúc hiện tại, Mức tự chủ, Quyết định đang chờ; docs/12 | 20 phút |

Không cần đọc: tools/, các thư mục scripts/, tests/fixtures/, .github/.

## 2. Khi đọc, tự hỏi 5 câu

1. Có đúng cách mình đang làm không (bước, giấy tờ, tên menu, mẫu tin)?
2. Thiếu bước hoặc tình huống nào hay gặp?
3. Quy tắc nào khó làm hoặc làm chậm việc?
4. Câu nào trong mẫu tin không gửi được cho nhà bán?
5. Việc nào nên để AI làm thêm, việc nào AI không nên đụng tới?

## 3. Ghi góp ý theo mẫu

Mỗi góp ý một dòng theo templates/gop-y.csv:

| File | Mục / dòng | Loại | Nội dung hiện tại | Đề xuất | Lý do hoặc ví dụ thực tế |
|---|---|---|---|---|---|

Loại: Đính chính (sai thực tế) · Chỉnh sửa (thiếu, khó hiểu) · Đề xuất (cải tiến).

## 4. Lưu ý

- Ví dụ thực tế phải che dữ liệu: không ghi CCCD, số tài khoản, SĐT, tên nhà bán thật.
- Nội dung gắn nhãn [CHỜ COO DUYỆT] là dự thảo: vẫn góp ý được, quyết định thuộc COO.
- Góp ý gửi Chi/HUyền theo kênh và hạn Chi thông báo. Huyền tổng hợp, phản hồi từng góp ý, cập nhật phiên bản mới và ghi CHANGELOG.
