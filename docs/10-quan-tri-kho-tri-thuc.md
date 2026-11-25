# Quản trị kho tri thức

v0.1.2 – pilot, chưa COO duyệt

[CHỜ COO DUYỆT – D-04] Nội dung checklist/chính sách; [CHỜ COO DUYỆT – D-06] owner và quyền review.

| Trạng thái | Cách sử dụng |
|---|---|
| DRAFT | Bản nháp, không nạp Project và không dùng tư vấn |
| VERIFIED | Đã xác minh, còn chờ duyệt; không nạp Project hoặc dùng tư vấn |
| APPROVED | Chỉ bản đã duyệt, còn hiệu lực mới được nạp Project và dùng tư vấn |

Vòng đời: DRAFT → VERIFIED → APPROVED. Không tự coi VERIFIED là đã phê duyệt. Owner duy trì hồ sơ mỗi tài liệu gồm: id, loại chủ thể/ngành hàng, phiên bản, ngày hiệu lực, người duyệt, nguồn, bản thay thế, owner, ngày rà soát tiếp. Các thông tin chưa xác nhận để trống, không bịa ngày/owner.

Bổ sung theo kiến trúc Data Pipeline Tri thức v1.0 (đề xuất, chờ PM xác nhận; chưa có hiệu lực): hồ sơ mỗi KU có thêm các trường sau, để khớp 12 trường metadata của kiến trúc.

| Trường | Giá trị | Ghi chú |
|---|---|---|
| layer | L1 quy định/SOP · L2 case · L3 ngoại lệ/bài học | Nói tri thức thuộc loại nào |
| authority_type | RULE · CASE · LESSON | Quyền dùng để tư vấn; không phải trạng thái duyệt. Case đã APPROVED vẫn chỉ là case |
| scope | Phòng ban, loại nhà bán (DN/HKD/HTX), ngành hàng, kênh | Nguồn im lặng về phạm vi thì ghi “chưa xác nhận”, không ghi “áp dụng chung” |
| sensitivity | Đỏ · Vàng · Xanh | Theo [phân loại dữ liệu](04-phan-loai-du-lieu.md). Đỏ không vào kho |
| approval_state của nguồn | APPROVED · PENDING · UNKNOWN | Lấy từ sổ nguồn hoặc nhãn trong tài liệu. Nhãn [CHỜ COO DUYỆT] tương ứng PENDING; không có nhãn hoặc sổ thì UNKNOWN. Đây là trạng thái của nguồn, tách khỏi status của KU |

KU do công cụ soạn ra chỉ là đề xuất ở trạng thái DRAFT. Mã KU chính thức, người duyệt và trạng thái do sổ KU của PM ghi sau khi người duyệt chấp nhận; sổ nguồn (mã nguồn, phiên bản, hash, vị trí, mã Gate 0) và sổ KU lưu nội bộ, không đưa vào repo. Kho tri thức chỉ nạp KU APPROVED; chưa có release manifest và quy trình thu hồi trong repo này.

Khi checklist đổi phiên bản, kết quả kiểm cũ hết giá trị (SA-BR-16); dừng sử dụng kết quả cũ và đối chiếu lại theo bản APPROVED hiện hành. Khi policy/giao diện hết hiệu lực, ngừng hướng dẫn phụ thuộc và nhờ owner cập nhật. Không đặt kỳ rà soát mặc định khi chưa có căn cứ.

Bài học/sự cố chỉ vào kho dưới dạng case đã ẩn danh; không đưa case thật có PII lên cloud. Chỉ dùng mã SIM-xxx trong repo. Theo dõi danh mục tại [knowledge-base-index](../project/knowledge-base-index.md); không nạp bản pilot thành chính sách APPROVED.

Nguồn: HI1-P1A-SOL-001 v0.1 mục §8; BRD HI1-AI-BRD-SD-1.2 mục NFR-05/NFR-07; SA-BR-16 (chưa cung cấp tài liệu/phiên bản riêng).
