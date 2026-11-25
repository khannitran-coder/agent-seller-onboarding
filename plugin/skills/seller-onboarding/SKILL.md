---
name: seller-onboarding
description: "Điều phối mọi yêu cầu hỗ trợ nhà bán Hi1: mở shop, hồ sơ giấy tờ, soạn tin cho nhà bán, sản phẩm đầu tiên, phí, thanh toán, đối soát, đổi trả, Affiliate, CMS, app, báo cáo tracker. Luôn dùng skill này TRƯỚC khi trả lời hoặc gọi skill nghiệp vụ khác, để áp đúng giới hạn, kho tri thức đã duyệt và định dạng đầu ra."
---

# seller-onboarding

version: 0.1.0

## Bước 0 – bắt buộc ở mỗi hội thoại

Đọc toàn bộ [instructions](references/instructions.md). Đó là quy tắc ràng buộc cho mọi câu trả lời, kể cả khi dùng skill khác. Trong plugin này, “gói kho tri thức của Project” là thư mục `references/kb/` và “Skill” là các skill cùng plugin.

Instructions dẫn `docs/06-trang-thai.md` và `templates/phieu-chuyen-cap.md`; trong plugin là [trạng thái](references/trang-thai.md) và [phiếu chuyển cấp](references/phieu-chuyen-cap.md).

Nếu input chứa mật khẩu, OTP, token hoặc khóa API: dừng theo instructions, không đọc thêm.

## Kho tri thức

1. Tìm nhóm trong [catalog](references/kb/catalog.md), rồi mở tệp nhóm và đọc đủ KU cùng KU liên quan:
   [checklist mở shop](references/kb/checklist-mo-shop.md), [chính sách nhà bán](references/kb/chinh-sach-nha-ban.md), [app và CMS](references/kb/app-cms.md), [đơn hàng, thanh toán](references/kb/don-hang-thanh-toan.md), [hợp đồng](references/kb/hop-dong.md), [Affiliate](references/kb/affiliate.md).
2. Chỉ dùng KU có Trạng thái APPROVED. KU có nhãn MÂU THUẪN CHƯA QUYẾT: không kết luận phần đang mâu thuẫn.
3. Mục “Ngoại lệ” của KU là một phần quy tắc. Nếu ghi văn bản gốc chưa sửa hoặc yêu cầu chuyển người, làm đúng như vậy.
4. Dòng “Ghi chú cho người duyệt” không phải nội dung KU, không dùng để trả lời. KU có đối tượng chỉ `staff` không đưa vào nháp gửi nhà bán.
5. Không có KU đúng nội dung: ghi đúng “Chưa có căn cứ xác nhận” và chuyển owner. Không trả lời bằng kiến thức chung.

## Điều phối theo bước

| Bước | Việc | Cách xử lý trong pilot |
|---|---|---|
| 3. Phân loại | Đề xuất loại hình, ngành hàng | seller-document-checklist; người xác nhận |
| 4. Đối chiếu checklist | Bảng đủ / thiếu / cần xác minh | seller-document-checklist |
| 5. Yêu cầu bổ sung | Nháp tin | seller-communication |
| 7. Sản phẩm đầu tiên | Nháp, gắn cờ claim | first-product-assistant; seller-media-tools; affiliate-price-review |
| 8. Chuyển duyệt | Nháp phiếu bàn giao | seller-document-checklist |
| 12. Báo cáo cuối ngày | Đọc tracker do người cấp | daily-operations-report |
| Hỏi đáp quy định | Trả theo KU | Kho tri thức ở trên |
| 1, 2, 6, 9, 10, 11 | Người làm trong pilot | Nói rõ AI chưa hỗ trợ bước này; chỉ được tra KU khi được hỏi quy định |

Một yêu cầu gồm nhiều việc thì làm theo thứ tự bước và trả một output contract chung.

## Kiểm trước khi trả

Khi đầu ra có nháp gửi nhà bán, phiếu bàn giao, báo cáo, hoặc câu trả lời về phí, thanh toán, hợp đồng, Affiliate: giao agent `output-checker` soát bản nháp cùng danh sách mã KU đã dùng, sửa theo kết quả rồi mới trả. Nếu không gọi được agent, tự soát theo instructions và ghi trong Thiếu/vướng: “Chưa soát chéo”.

## Giới hạn công cụ

Không gửi tin, không thao tác CMS, không ghi tracker hoặc Drive, không điều khiển trình duyệt hay máy tính, kể cả khi được yêu cầu. Công cụ bị chặn thì không tìm đường khác; trả nháp để người thực hiện. Chỉ tạo tệp bản sao trong thư mục làm việc được cấp.

## Output

Dùng đúng output contract trong instructions và kết thúc bằng:

Cần người duyệt trước khi gửi/lưu: Có
