# Truy vết yêu cầu → tài liệu/Skill → ca test

v0.1.2 – pilot, chưa COO duyệt

[CHỜ COO DUYỆT – D-01] Phạm vi pilot; các nhãn D theo tài liệu đích tiếp tục áp dụng. Đây là truy vết tài liệu vận hành, không xác nhận nghiệm thu. Nội dung yêu cầu đối chiếu theo BRD, không suy thêm đầy đủ ngoài yêu cầu.

Cột ca test chỉ ánh xạ thiết kế; 14 ca pilot chưa chạy trên Claude Project. “Liên quan/chưa phủ” không đồng nghĩa được kiểm đủ. FR-06 và FR-09 không có Skill riêng: Project instructions + kho tri thức xử lý; đây là lựa chọn đã ghi nhận, không phải lỗi.

| ID | Yêu cầu (1 dòng) | Bước | Skill/file | Ca test |
|---|---|---|---|---|
| PDHB-FR-01 | Tiếp nhận/ghi nhận lead | 1 | seller-communication; docs/05 | TC-01 (liên quan, chưa kiểm ghi hệ thống) |
| PDHB-FR-02 | Gắn cờ nghi trùng | 2 | docs/02; docs/09 | TC-03 |
| PDHB-FR-03 | Phân loại nhà bán/ngành hàng | 3 | seller-document-checklist | TC-01 (liên quan, chưa phủ mọi loại hình) |
| PDHB-FR-04 | Đối chiếu checklist | 4 | seller-document-checklist | TC-01, TC-02, TC-10 |
| PDHB-FR-05 | Nháp yêu cầu bổ sung/nhắc việc | 5 | seller-communication | TC-02 (liên quan; chưa kiểm đủ mẫu B/D) |
| PDHB-FR-06 | Hướng dẫn thao tác shop có phiên bản | 6 | Project instructions + kho tri thức; không có Skill riêng ở v0.1.0, giữ ở v0.1.1 | SAFE-04 (đổi phiên bản; chưa phủ thao tác shop) |
| PDHB-FR-07 | Hỗ trợ sản phẩm đầu tiên | 7 | first-product-assistant | TC-06 |
| PDHB-FR-08 | Chuyển đúng người duyệt, lưu nguyên văn kết quả | 8 | seller-document-checklist; templates/phieu-ban-giao-duyet.md | TC-08 (quyền; chưa phủ điền phiếu/lưu lý do) |
| PDHB-FR-09 | Hướng dẫn vận hành đơn | 9 | Project instructions + kho tri thức; không có Skill riêng ở v0.1.0, giữ ở v0.1.1 | SAFE-04 (nguồn; chưa phủ vận hành đơn) |
| PDHB-FR-10 | Đánh giá sẵn sàng bán độc lập | 10 | docs/06; daily-operations-report | TC-07 |
| PDHB-FR-11 | Bàn giao + follow-up | 11 | seller-communication (D); docs/02 | Chưa có ca trực tiếp trong 14 ca pilot |
| PDHB-FR-12 | Báo cáo tồn/ngoại lệ | 12 | daily-operations-report | TC-09 |
| PDHB-FR-13 | Theo dõi trạng thái đa lớp | 1–12 | docs/05; docs/06 | TC-07 (một nhánh) |
| PDHB-FR-14 | Phiếu chuyển cấp | ngoại lệ | templates/phieu-chuyen-cap.md; daily-operations-report | TC-08, TC-09 (liên quan, chưa phủ mọi cấp) |
| PDHB-FR-15 | Kết luận có nguồn | 1–12 | 4 Skill; Project instructions | TC-10, SAFE-04 |
| PDHB-BR-01 | Ba mốc khác nhau | 6/10 | docs/06 | TC-07 |
| PDHB-BR-02 | Mỗi hồ sơ một mã + owner | 1 | docs/05; docs/07 | TC-01 (liên quan, chưa phủ tính duy nhất) |
| PDHB-BR-03 | Chỉ theo checklist APPROVED có version | 4 | seller-document-checklist; docs/10 | TC-10, SAFE-04 |
| PDHB-BR-04 | Người duyệt trước gửi/ghi | mọi bước | 4 Skill; Project instructions; docs/07 | TC-01, TC-08 |
| PDHB-BR-05 | Được duyệt chỉ từ CMS/người có quyền | 8 | docs/06; seller-communication (C) | TC-07, TC-08 |
| PDHB-BR-06 | Không nhận OTP/mật khẩu/token | mọi bước | 4 Skill; references/guardrails.md | TC-05, SAFE-02 |
| PDHB-BR-07 | Không đổi trường pháp lý/tài chính/giá/tồn/xuất xứ | mọi bước | docs/03; 4 Skill | TC-06, TC-08 (chưa phủ mọi trường) |
| PDHB-BR-08 | Không công bố trước duyệt | 7/8 | docs/03; first-product-assistant | TC-08 (liên quan; chưa phủ đăng sản phẩm) |
| PDHB-BR-09 | Claim cần chứng cứ | 7 | first-product-assistant | TC-06 |
| PDHB-BR-10 | Rủi ro pháp lý/thanh toán/giả mạo phải chuyển cấp | ngoại lệ | docs/03; docs/09; phiếu chuyển cấp | TC-02, TC-09 (liên quan; chưa phủ mọi rủi ro) |
| PDHB-BR-11 | Không Ready khi thiếu một mục | 10 | docs/06 | TC-07 (sản phẩm ẩn; chưa phủ mọi điều kiện) |
| PDHB-BR-12 | SLA chỉ là pilot | 12 | daily-operations-report | TC-09 |

Chưa có trích nội dung WF-A01…A06/ánh xạ FR trong kết quả QC được cung cấp; không tự đặt tên hoặc suy ánh xạ workflow. Bảng trên chỉ dùng 12 bước repo và danh sách FR/BR đã xác định.


Nguồn: BRD HI1-AI-BRD-SD-1.2 mục PDHB-FR-01…15 và PDHB-BR-01…12.


## Khâu thực tế và trạng thái đóng gói

| Khâu | Trạng thái | Phụ thuộc |
|---|---|---|
| Tạo đối tác/thương hiệu trên CMS | seller-cms-entry: bản nháp, không cài/dùng | D-07a/D-07b |
| Bộ hợp đồng + phụ lục Affiliate + bảng giá | seller-contract-draft: bản nháp, không cài/dùng | D-08b |
| Nhập sản phẩm lên CMS | seller-cms-entry: bản nháp, không cài/dùng | D-07b |
| Kiểm bảng giá Affiliate | affiliate-price-review: cài được, kiểm nháp, chưa tự bật A06 | D-04/D-08b |

[CHỜ COO DUYỆT – D-07] Quyền CMS; [CHỜ COO DUYỆT – D-08] quy trình bảo mật liên quan. Chưa cấp quyền hoặc triển khai các khâu này trong v0.1.2.

Nguồn: skill vận hành nội bộ của nhóm (bản 11/2026), đã lược thông tin nội bộ

## Truy vết đề xuất tự chủ A01–A08

Chỉ là đề xuất chưa có hiệu lực. Bốn Skill hiện hành không đổi. Đây là mã hành động, không phải mã WF-A01…A06; không suy ánh xạ workflow nguồn. Ca kiểm thử quyền mới chưa được thiết kế/chạy.

| ID | Yêu cầu (1 dòng) | Bước | Skill/file | Ca test | Quyết định |
|---|---|---|---|---|---|
| A01 | Đọc trang danh sách/trạng thái hồ sơ, shop, sản phẩm trên admin.hi1.vn | theo hành động | docs/12-ma-tran-tu-chu-va-rui-ro.md; chưa triển khai | Chưa có ca cho quyền đề xuất | D-07a |
| A02 | Ghi tracker các cột vận hành: status_updated_at, shop_status, product_status, last_action, next_action, contact_status, risk_flags | theo hành động | docs/12-ma-tran-tu-chu-va-rui-ro.md; chưa triển khai | Chưa có ca cho quyền đề xuất | D-09 |
| A03 | Tạo nháp phiếu chuyển cấp và nháp tin nhắc việc cho hồ sơ quá hạn | theo hành động | docs/12-ma-tran-tu-chu-va-rui-ro.md; chưa triển khai | Chưa có ca cho quyền đề xuất | D-09 |
| A04 | Gửi tin nhắc việc mẫu D và tin hướng dẫn mẫu H qua Zalo web | theo hành động | docs/12-ma-tran-tu-chu-va-rui-ro.md; chưa triển khai | Chưa có ca cho quyền đề xuất | D-09 |
| A05 | Điền form tạo đối tác, thương hiệu, sản phẩm trên admin tới TRƯỚC nút Lưu | theo hành động | docs/12-ma-tran-tu-chu-va-rui-ro.md; chưa triển khai | Chưa có ca cho quyền đề xuất | D-07b |
| A06 | Kiểm bảng giá Affiliate, chuẩn hoá ảnh vuông, gộp PDF hợp đồng trên bản sao | theo hành động | docs/12-ma-tran-tu-chu-va-rui-ro.md; chưa triển khai | Chưa có ca cho quyền đề xuất | D-08b (phạm vi hợp đồng) |
| A07 | Bấm Lưu/Tạo mới, Duyệt, Kích hoạt, Đăng công khai, Xoá/Gộp tài khoản | theo hành động | docs/12-ma-tran-tu-chu-va-rui-ro.md; chưa triển khai | Chưa có ca cho quyền đề xuất | Không mở |
| A08 | Nhập mật khẩu, OTP, số tài khoản, CCCD; sửa giá, tồn, xuất xứ, thông tin pháp lý; cam kết ngày duyệt/doanh thu | theo hành động | docs/12-ma-tran-tu-chu-va-rui-ro.md; chưa triển khai | Chưa có ca cho quyền đề xuất | Không mở |

## Bổ sung truy vết v0.2.0

| Skill | Yêu cầu / bước | Hành động | Ca test | Trạng thái / quyết định |
|---|---|---|---|---|
| affiliate-price-review | FR-07/FR-08, chuẩn bị bảng giá bước 7–8 | A06 | PR-01…PR-06 | Cài được, chỉ kiểm nháp; D-04, D-08b; chưa tự bật A06 |
| seller-media-tools | FR-07/FR-08, ảnh/PDF bước 7–8 | A06 | MT-01…MT-04 | Cài được, chỉ bản sao; người kiểm; chưa tự bật A06 |
| seller-contract-draft | FR-08, chuẩn bị bộ hợp đồng | A06 | Không viết ca cho bản nháp | skills-draft/, 0.0.1; KHÔNG cài/dùng trước D-08b |
| seller-cms-entry | FR-06/FR-07, chuẩn bị form | A01/A05 | Không viết ca cho bản nháp | skills-draft/, 0.0.1; KHÔNG cài/dùng trước D-07a/D-07b |

Bảng này bổ sung phương tiện hỗ trợ, không mở rộng quyền hiện hành. Trạng thái đóng gói ở trên không phải phê duyệt quyền tự động hoá.

Nguồn: skill vận hành nội bộ của nhóm (bản 11/2026), đã lược thông tin nội bộ

Tổng bộ kiểm thử là 35 ca thiết kế: 14 ca pilot bắt buộc (TC-01…TC-10, SAFE), 8 ca bổ sung (TC-11…TC-18, chưa ánh xạ trong tài liệu này) và 13 ca công cụ (PR/MT/TR). Trạng thái chạy thực tế xem tests/test-cases.md và README; ánh xạ không thay kết quả kiểm định.
