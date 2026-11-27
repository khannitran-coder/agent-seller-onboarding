# Agent Seller Onboarding (HI1) — v0.5.0

**Cài agent lên tài khoản Claude doanh nghiệp: đọc [CAI-DAT.md](CAI-DAT.md).**

Tác giả: PM - TKC

GIAI ĐOẠN 1 - PHƯƠNG ÁN A: Ưu tiên hiện tại AI Adoption & Rapid Production Claude Cowork + AI Skills + low-code/no-code
Mục tiêu: Đưa AI vào quy trình Phát triển & Hỗ trợ Nhà bán đang vận hành tại HI1.

GIAI ĐOẠN 2 - PHƯƠNG ÁN B:
AI Engineering & Scalable Automation
Backend + API + Database + AI Orchestration
Mục tiêu: Chuyển những workflow đã chứng minh giá trị sang hệ thống tích hợp, tự động hóa và có khả năng mở rộng

Bản phát hành v0.5.0 – pilot, chưa COO duyệt. Mới ở v0.5.0: hai skill bản nháp chuyển vào `skills/` và có trong plugin (vẫn chưa được dùng), repo sắp xếp lại. v0.4.0: AI hỗ trợ thêm bước 1, 6, 9, 11 trong giai đoạn test (xem [Phạm vi AI theo bước](#phạm-vi-ai-theo-bước) và [CHANGELOG](CHANGELOG.md)). Đang lấy góp ý của team trước khi chốt.

Xem [hướng dẫn đọc và góp ý](docs/00-huong-dan-doc-va-gop-y.md) để chọn tài liệu theo vai trò và ghi nhận ý kiến.

## Đọc nhanh theo vai trò

| Vai trò | Đọc gì | Thời gian |
|---|---|---|
| Tất cả | README: phần giới thiệu, Kiến trúc hiện tại, Quyết định đang chờ; docs/01 | 10 phút |
| Nhân viên hỗ trợ nhà bán | docs/07 SOP, docs/02 quy trình 12 bước, skills/seller-communication/templates (mẫu tin A–I), docs/09 xử lý sự cố | 30 phút |
| Trưởng nhóm | Thêm: docs/05 tracker, docs/06 trạng thái, docs/12 mức tự chủ và rủi ro, tests/test-cases.md (ca TC và SAFE) | 45 phút |
| Kiểm duyệt nhà bán, ngành hàng | skills/seller-document-checklist (9 mục giấy tờ), skills/first-product-assistant (nội dung sản phẩm, claim), docs/03 guardrails | 30 phút |
| CEO, COO | README: Kiến trúc hiện tại, Mức tự chủ, Quyết định đang chờ; docs/12 | 20 phút |

## Kiến trúc hiện tại (v0.5.0)

Hệ thống là lớp hỗ trợ soạn thảo đặt cạnh quy trình onboarding nhà bán đang chạy, triển khai bằng plugin Cowork (quyết định 25/11/2026; Claude Project là phương án lùi). AI ở mức tự chủ 3: đọc dữ liệu được cấp, đối chiếu, soạn nháp. Mọi thao tác ghi (gửi tin, sửa CMS, cập nhật tracker) do người thực hiện. Không có tích hợp hệ thống; dữ liệu giữa các thành phần đi qua tay nhân viên. Mức tự chủ được quy định theo từng hành động tại docs/12; hiện tại tất cả ở M3 hoặc thấp hơn.

### Thành phần

| Thành phần | Nền tảng | Trách nhiệm | Giới hạn |
|---|---|---|---|
| Hệ thống nguồn | admin.hi1.vn, App Nhà Bán Hi1 | Trạng thái chính thức của hồ sơ, shop, sản phẩm | v0.1.x: Claude Project không truy cập – do thiết kế, không phải giới hạn kỹ thuật. Mở theo mức D-07a (chỉ đọc) / D-07b (điền trước nút Lưu), xem docs/12 |
| Kênh nhà bán | Zalo | Trao đổi và nhận giấy tờ | Chỉ nhân viên gửi |
| Tracker vận hành | Google Sheet, 26 cột | Theo dõi hồ sơ, owner, hạn, đo KPI | Không phải nguồn chính thức; người ghi |
| Kho tri thức | Thư mục Drive + Project knowledge | Checklist, chính sách, mẫu tin, hướng dẫn giao diện có phiên bản | Chỉ tài liệu APPROVED được nạp |
| Lớp điều phối | Plugin Cowork `hi1-seller-onboarding` (bản test `-test`): skill `seller-onboarding`, agent `output-checker` | Điều phối theo bước, instructions chung (guardrails, chặn dữ liệu Đỏ, output contract), kho tri thức, soát chéo đầu ra | Không có quyền ghi ra ngoài. Phương án lùi: Claude Project "HI1 Seller Onboarding" |
| Lớp chặn | Hooks của plugin (`plugin/hooks/`) | Chặn mật khẩu/OTP/token trong tin nhập; chặn công cụ ghi qua connector và trình duyệt; bắt viết lại đầu ra thiếu contract | Áp cho mọi tác vụ khi plugin bật; chưa xác minh trên Cowork (kiểm khói docs/14 mục 5) |
| Skill | `seller-onboarding` trong plugin/; 8 Skill trong skills/ (6 nghiệp vụ, 2 bản nháp) | Một nghiệp vụ mỗi Skill, phiên bản riêng | Hai bản nháp seller-cms-entry, seller-contract-draft có trong plugin từ 0.5.0 nhưng tự dừng khi bị gọi cho tới D-07a/b, D-08b |
| Báo cáo định kỳ | Scheduled task 17:00 (Asia/Ho_Chi_Minh) | Chạy daily-operations-report trên tracker | Chỉ đọc; bật sau quyết định D-03 |

### Luồng xử lý một hồ sơ

~~~mermaid
flowchart LR
  A[CMS / Zalo] -->|nhân viên trích trường nghiệp vụ| B[Phân lớp dữ liệu]
  B -->|Xanh, Vàng| C[Plugin Cowork: seller-onboarding + Skill]
  B -->|Đỏ| X[Không đưa vào AI]
  C --> D[Nháp + nguồn + phiên bản]
  D --> E{Nhân viên review}
  E -->|duyệt / sửa| F[Nhân viên gửi Zalo, thao tác CMS]
  E -->|bỏ| C
  F --> G[Ghi tracker]
  G --> H[Báo cáo cuối ngày]
  H --> I[Trưởng nhóm]
~~~

### Phạm vi AI theo bước

Theo [quy trình 12 bước](docs/02-quy-trinh-12-buoc.md) và [docs/13 mục 2](docs/13-dieu-kien-chay-thu-ho-so-that.md). Bước 1, 6, 9, 11 thêm ngày 27/11/2026 (quyết định người thiết kế agent), chạy trên bản test với dữ liệu mô phỏng trước, qua 6 ca BX-01…BX-06 rồi mới dùng với hồ sơ thật. Mức tự chủ không đổi: M3.

| Bước | AI trong pilot | Cách làm | Giới hạn chính |
|---|---|---|---|
| 1. Nhận lead | Hỗ trợ (từ 27/11) | Kiểm trường thiếu, nháp mẫu A | Không kiểm trùng; ngoài phạm vi pilot thì chuyển Trưởng nhóm |
| 2. Kiểm trùng | Người làm | — | Cần đọc CMS (A01, đang M0) |
| 3–5. Phân loại, checklist, bổ sung | Hỗ trợ | seller-document-checklist, seller-communication | Người xác nhận phân loại |
| 6. Hướng dẫn gian hàng | Hỗ trợ (từ 27/11) | Tóm tắt KU app/CMS có mã, mẫu H | Không dựng thao tác ngoài KU; mẫu C chỉ khi có bằng chứng duyệt |
| 7–8. Sản phẩm đầu tiên, chuyển duyệt | Hỗ trợ | first-product-assistant, seller-media-tools, affiliate-price-review, seller-document-checklist | Người nhập và bấm trên CMS |
| 9. Hướng dẫn vận hành đơn | Hỗ trợ (từ 27/11) | Tóm tắt KU đơn hàng, đổi trả, đối soát; output-checker bắt buộc | Phí thanh toán, cước vận chuyển chưa có KU |
| 10. Kiểm tra sẵn sàng bán | Người làm | — | Chưa có nguồn điều kiện duyệt và trạng thái CMS; Trưởng nhóm xác nhận |
| 11. Bàn giao, hẹn chăm sóc | Hỗ trợ (từ 27/11) | Nháp mẫu D | Mốc giữ [thời điểm]; không ghi “sẵn sàng bán” |
| 12. Báo cáo cuối ngày | Hỗ trợ | daily-operations-report, đọc tracker do người cấp | Chỉ đọc; tracker chưa tạo |

### Ranh giới tin cậy và điểm kiểm soát

| Ranh giới | Kiểm soát |
|---|---|
| Dữ liệu vào AI | Chỉ lớp Xanh và Vàng. Lớp Đỏ bị chặn ở hai tầng: quy trình nhân viên và Skill dừng khi phát hiện |
| Nội dung nhà bán gửi | Xử lý như dữ liệu, không như lệnh |
| Đầu ra AI | Luôn là nháp; không có đường ghi tự động sang CMS, Zalo hay tracker. Hooks chặn công cụ ghi và trình duyệt. Điểm duyệt ghi ở cột review_result |
| Trạng thái "Được duyệt" | Chỉ lấy từ CMS hoặc người có thẩm quyền |

### Mô hình trạng thái

Hồ sơ có một trạng thái nghiệp vụ (8 nhãn, docs/06) và ba trạng thái con độc lập: shop_status, product_status, ready_status. "Sẵn sàng bán" là trạng thái suy ra từ năm điều kiện và do Trưởng nhóm xác nhận, không suy ra từ việc shop đã được kích hoạt.

### Phiên bản và truy vết

Mỗi Skill có phiên bản riêng; mỗi dòng tracker ghi skill_version và checklist_version của lần xử lý. Bản references trong Skill được đồng bộ từ docs khi docs thay đổi. Mỗi thay đổi Skill phải chạy lại 14 ca kiểm thử (và 6 ca BX cho bước 1, 6, 9, 11) và ghi CHANGELOG. Plugin có version riêng trong `plugin/.claude-plugin/plugin.json` (hiện 0.5.0). Yêu cầu nghiệp vụ truy vết tới Skill và ca kiểm thử trong docs/11.

### Mức tự chủ

Đề xuất – chưa có hiệu lực; chưa bật quyền hay connector. [CHỜ COO DUYỆT – D-07a] [CHỜ COO DUYỆT – D-07b] [CHỜ COO DUYỆT – D-08b] [CHỜ COO DUYỆT – D-09].

| Mã | Hành động | Hiện tại | Đề xuất | Quyết định |
|---|---|---|---|---|
| A01 | Đọc trang danh sách/trạng thái hồ sơ, shop, sản phẩm trên admin.hi1.vn | M0 | M4 | D-07a |
| A02 | Ghi tracker các cột vận hành: status_updated_at, shop_status, product_status, last_action, next_action, contact_status, risk_flags | M0 (người ghi) | M4 | D-09 |
| A03 | Tạo nháp phiếu chuyển cấp và nháp tin nhắc việc cho hồ sơ quá hạn | M3 | M4 (tạo nháp tự động mỗi ngày, vẫn chưa gửi) | D-09 |
| A04 | Gửi tin nhắc việc mẫu D và tin hướng dẫn mẫu H qua Zalo web | M0 | M3+ | D-09 |
| A05 | Điền form tạo đối tác, thương hiệu, sản phẩm trên admin tới TRƯỚC nút Lưu | M0 | M3 | D-07b |
| A06 | Kiểm bảng giá Affiliate, chuẩn hoá ảnh vuông, gộp PDF hợp đồng trên bản sao | M0 | M4 với bản sao, người kiểm trước khi gửi | D-08b (phạm vi hợp đồng) |
| A07 | Bấm Lưu/Tạo mới, Duyệt, Kích hoạt, Đăng công khai, Xoá/Gộp tài khoản | M0 | M0 | Không mở |
| A08 | Nhập mật khẩu, OTP, số tài khoản, CCCD; sửa giá, tồn, xuất xứ, thông tin pháp lý; cam kết ngày duyệt/doanh thu | M0 | M0 | Không mở |

Rủi ro đầy đủ và quy tắc nâng/hạ mức ở docs/12. Tab nhật ký AI riêng trong file tracker theo templates/nhat-ky-ai-header.csv là BẮT BUỘC trước khi bất kỳ hành động nào chạy ở M3+/M4; tracker chính giữ 26 cột.

Xem [ma trận tự chủ và rủi ro](docs/12-ma-tran-tu-chu-va-rui-ro.md).

### Giới hạn đã chấp nhận

- Tracker và CMS đồng bộ thủ công, có thể lệch.
- Google Sheet không phân quyền theo dòng và không có nhật ký bất biến.
- Không nhắc việc theo thời gian thực.
- Kiểm bảng giá Affiliate và chuẩn bị media có Skill chỉ hỗ trợ kiểm/chuẩn bị bản sao; hợp đồng và nhập CMS chỉ có bản nháp chưa kích hoạt, chưa có quyền tự động hoá.
### Hướng phát triển

- v0.2: affiliate-price-review và seller-media-tools cài được để kiểm/chuẩn bị nháp; seller-contract-draft là bản nháp D-08b chưa cài/kích hoạt.
- seller-cms-entry: 07a chỉ đọc trong pilot nếu COO duyệt; 07b điền trước nút Lưu sau pilot; 07c (AI bấm Lưu/Duyệt) không làm.
- Phương án B (khi đạt ngưỡng ở docs/01): backend thay tracker; 26 cột tracker là lược đồ bảng ban đầu.

## Skill

| Tên | Việc làm | Version | Trạng thái |
|---|---|---|---|
| [seller-onboarding](plugin/skills/seller-onboarding/SKILL.md) | Điều phối theo bước, kho tri thức, bước 1, 6, 9, 11 | 0.2.0 | Trong plugin – pilot |
| [seller-document-checklist](skills/seller-document-checklist/SKILL.md) | Đối chiếu 9 mục hồ sơ | 0.1.5 | Cài được – pilot |
| [seller-communication](skills/seller-communication/SKILL.md) | Soạn nháp mẫu tin A–I | 0.1.5 | Cài được – pilot |
| [first-product-assistant](skills/first-product-assistant/SKILL.md) | Nháp sản phẩm, kiểm claim | 0.1.3 | Cài được – pilot |
| [daily-operations-report](skills/daily-operations-report/SKILL.md) | Báo cáo tracker, nháp chuyển cấp | 0.2.2 | Cài được – pilot |
| [affiliate-price-review](skills/affiliate-price-review/SKILL.md) | Kiểm bảng giá Affiliate | 0.1.1 | Cài được – ngoài pilot |
| [seller-media-tools](skills/seller-media-tools/SKILL.md) | Ảnh vuông, gộp PDF bản sao | 0.1.0 | Cài được – ngoài pilot |
| [seller-cms-entry](skills/seller-cms-entry/SKILL.md) | Thiết kế nhập form CMS | 0.0.2 | Bản nháp trong plugin, tự dừng – chờ D-07a,b |
| [seller-contract-draft](skills/seller-contract-draft/SKILL.md) | Thiết kế ghép hợp đồng/phụ lục | 0.0.2 | Bản nháp trong plugin, tự dừng – chờ D-08b |

Cài được không đồng nghĩa đã được cấp quyền hoặc được tự chạy A06. Chỉ dùng phạm vi được duyệt. Hai bản nháp được đóng vào plugin theo quyết định người thiết kế agent ngày 27/11/2026 nhưng không dùng trước quyết định tương ứng; với phương án lùi Claude Project thì không cài hai zip này.

## Quyết định đang chờ

| Mã | Nội dung | Ảnh hưởng tới |
|---|---|---|
| D-01 | Phạm vi pilot và mức quyền AI | Toàn bộ pilot, ranh giới người/AI |
| D-02 | Dữ liệu được đưa vào AI | Phân lớp và che dữ liệu trước dùng |
| D-03 | Gói Claude, tài khoản, connector, lịch báo cáo | Cấu hình môi trường và scheduled task |
| D-04 | Checklist 9 mục, mẫu tin, SLA pilot | Đối chiếu hồ sơ, giao tiếp và nhắc việc |
| D-05 | Trạng thái, điều kiện Sẵn sàng bán, cấp chuyển | Theo dõi và bàn giao vận hành |
| D-06 | Người giữ tracker, quyền review và nghiệm thu | Trách nhiệm cập nhật, kiểm tra kết quả |
| D-07a | AI chỉ đọc CMS | Phạm vi màn hình/quyền xem đề xuất |
| D-07b | AI điền form CMS trước nút Lưu | Bản nháp seller-cms-entry, chưa kích hoạt |
| D-08 | Quy trình cấp thông tin đăng nhập cho shop mới | Bàn giao thông tin theo quy trình bảo mật |
| D-08b | Phạm vi hợp đồng | Bản nháp hợp đồng và phạm vi A06 |
| D-09 | AI ghi tracker, tạo nháp tự động, gửi tin nhắc theo lô | Các quyền đề xuất, nhật ký và hậu kiểm |

Các nội dung [CHỜ COO DUYỆT] là dự thảo, chưa cấp thêm quyền. Mọi thao tác ghi vẫn do người thực hiện; chưa bật connector/quyền mới.

## Cài đặt

Pilot triển khai bằng plugin Cowork (quyết định 25/11/2026): cài theo [CAI-DAT.md](CAI-DAT.md) (zip 0.5.0 trong `releases/`), kiểm khói theo [docs/14](docs/14-trien-khai-cowork.md). Mã plugin ở `plugin/`, đóng gói bằng `python tools/build_plugin.py`, kiểm bằng `python -m unittest discover -s tests/plugin`. Các bước Claude Project dưới đây giữ làm phương án lùi.

Hướng dẫn cài vào tài khoản doanh nghiệp kèm prompt cho Claude desktop: [project/cai-dat-claude.md](project/cai-dat-claude.md).

1. [CHỜ COO DUYỆT – D-03] Kiểm gói Claude Team/Enterprise được cho phép và quyền dữ liệu; không tự thêm connector/quyền AI khi chưa có quyết định COO.
2. Tạo Claude Project “HI1 Seller Onboarding”; dán [instructions](project/claude-project-instructions.md).
3. Chạy `python tools/build_skills.py` → lấy zip trong dist/ (mỗi zip chứa thư mục trùng tên Skill; dist/short/ là bản mô tả ≤200 ký tự dùng khi claude.ai báo mô tả quá dài). Công cụ kiểm trước khi đóng gói và chỉ đóng skills/; tuyệt đối không cài skills-draft/. Cài zip trong mục Skills của giao diện hiện hành và xác minh chúng khả dụng trong Project; không coi nạp knowledge là cài Skill.
4. Nạp chỉ các tài liệu APPROVED hiện hành theo [danh mục](project/knowledge-base-index.md), điền tên/owner/version/ngày hiệu lực sau xác nhận. Không nạp bản pilot như chính sách đã duyệt. Gói nạp được sinh bằng `python tools/export_kb.py`: `project/kb-draft/` chỉ cho Project thử nghiệm, `project/kb/` (khi có tệp phê duyệt) cho Project vận hành; chi tiết ở mục E của danh mục.
5. [CHỜ COO DUYỆT – D-06] Tạo tracker với [header CSV](templates/tracker-header.csv), kiểm kiểu/enum theo [schema](docs/05-tracker-schema.md); AI chỉ đọc, người cập nhật sau duyệt.
6. [CHỜ COO DUYỆT – D-03] Sau khi connector được COO quyết và người cấu hình xác minh quyền chỉ đọc, tạo scheduled task lúc **17:00 Asia/Ho_Chi_Minh** hằng ngày: “Dùng daily-operations-report đọc tracker được cấp quyền, chốt thời điểm và phạm vi, soạn báo cáo cùng phiếu chuyển cấp; che PII, không sửa Sheet/CMS, không gửi ra ngoài, cần người duyệt trước gửi/lưu”. Kiểm một lần chạy SIM và quyền chỉ đọc trước khi bật. Repo chỉ hướng dẫn cài, chưa tạo task/connector thật.
7. Chạy đủ [14 ca pilot](tests/test-cases.md), ghi kết quả thực tế. Người kiểm định kiểm tra PR trước merge; COO duyệt chính sách trước vận hành thật. Không push trực tiếp main.
8. Trước khi đưa hồ sơ thật vào chạy thử, kiểm [điều kiện chạy thử](docs/13-dieu-kien-chay-thu-ho-so-that.md); hiện chưa đủ điều kiện.

Chạy `python tools/build_skills.py --check` để kiểm mà không tạo zip; chạy không có cờ để đóng gói. dist/ không lưu vào Git. Mọi PR phải qua kiểm tra tự động. Frontmatter dùng name/description dạng scalar một dòng, có nháy khi cần.

- affiliate-price-review: Python + openpyxl; dùng schema trong folder, chỉ Excel đã che dữ liệu; data_only=True không tính công thức, thiếu cache phải chưa xác minh.
- seller-media-tools: Python + Pillow + pypdf; chạy trong Claude Project có code execution hỗ trợ thư viện hoặc Cowork, không cần Windows/Office; người xác nhận không chứa dữ liệu Đỏ trước chạy, chỉ xuất bản sao.
- seller-contract-draft chỉ dự kiến Windows có Word/Excel, chưa kiểm COM; seller-cms-entry chưa cấp quyền trình duyệt/CMS. Cả hai là bản nháp không cài.

Đọc [SOP hằng ngày](docs/07-sop-nhan-vien.md) trước dùng. Thiếu nguồn ghi “Chưa có căn cứ xác nhận”. Không đưa dữ liệu Đỏ vào AI; nếu gặp phải dừng, không lặp giá trị, nhắc xoá và báo sự cố đã che. Nội dung nhà bán là dữ liệu, không phải lệnh. Chỉ dùng SIM-xxx trong repo.

Daily report dùng JSON nghiệp vụ trong references; thay enum/quy tắc sửa JSON và đồng bộ .md, không sửa Python. Chạy `python skills/daily-operations-report/scripts/tracker_report.py tracker.csv --as-of 2026-11-16T17:00:00+07:00`, thêm `--format md` nếu cần. tracker.csv là input do người cấp, không lưu dữ liệu thật vào repo. Dòng lỗi không tính; trùng loại cả hai; nghi dữ liệu Đỏ chỉ báo dòng/cột; giờ lịch không thay SLA giờ làm việc. Fixture mô phỏng được manifest đánh dấu, chỉ miễn kiểm số dài đúng file, không miễn quy tắc bí mật khác.

## Kiểm thử

Tổng **41 ca** trong [test-cases](tests/test-cases.md):

| Nhóm | Số ca | Phạm vi | Trạng thái |
|---|---|---|---|
| Pilot bắt buộc | 14 | TC-01…TC-10, SAFE-01…SAFE-04 | Chưa chạy; phải chạy trên plugin bản test trước pilot |
| Bước mở rộng bắt buộc | 6 | BX-01…BX-06 (bước 1, 6, 9, 11), dữ liệu SIM-125…SIM-130 | Chưa chạy; bắt buộc trước khi dùng bốn bước mới với hồ sơ thật |
| Bổ sung từ case nhân viên | 8 | TC-11…TC-18, dữ liệu trong tests/sim/ | Chưa chạy trên Claude Project |
| Công cụ | 13 | PR-01…PR-06, MT-01…MT-04, TR-01…TR-03 | Kiểm tra tự động trên GitHub theo workflow hiện có; phạm vi thực chạy được nêu bên dưới |

Workflow GitHub hiện so fixture giá và tracker với expected JSON. Ảnh vuông/gộp PDF đã kiểm chạy trên SIM ở v0.2; MT-03 là ca dừng ở lớp Skill, chưa chạy kiểm hành vi mô hình và không được coi là đạt chỉ nhờ script. Không phải cả 13 ca công cụ đều đã được tự động hoá trên GitHub; lần này không sửa script/workflow.

Trong mục Kiến trúc giữ nguyên văn, “14 ca kiểm thử” nghĩa là 14 ca pilot bắt buộc; 41 là tổng số ca thiết kế. Kiểm tự động của plugin: `python -m unittest discover -s tests/plugin` (hook và gói, không kiểm hành vi mô hình). Người kiểm định ghi kết quả thực tế, không suy UAT từ kiểm tra tĩnh.

## Cấu trúc thư mục

~~~text
agent-seller-onboarding/
├── README.md, CAI-DAT.md, CHANGELOG.md, AUDIT.md
├── docs/                 00–14: quy trình, guardrails, dữ liệu, SOP, tự chủ, triển khai
├── plugin/               nguồn plugin: manifest, skill seller-onboarding, agent, hooks
├── skills/               8 Skill (6 nghiệp vụ + 2 bản nháp)
├── project/              instructions, gói tri thức kb/ (vận hành) và kb-draft/ (test)
├── kb-workspace/         candidate KU, sổ nguồn, phiếu duyệt KU
├── templates/            tracker, nhật ký AI, phiếu, mẫu kết quả kiểm thử
├── tests/                test-cases.md, sim/, fixtures/, plugin/
├── tools/                build_skills.py, build_plugin.py, export_kb.py
├── plugins/, .claude-plugin/   bản đóng gói để đồng bộ marketplace (sinh tự động)
└── releases/             zip plugin để tải lên (giữ bản cũ để lùi)
~~~

Nguồn để sửa: `docs/`, `plugin/`, `skills/`, `project/`, `kb-workspace/`, `templates/`, `tools/`. Không sửa tay `plugins/`, `.claude-plugin/`, `releases/`: chạy `python tools/build_plugin.py --release`.

| Thư mục / tệp | Nội dung |
|---|---|
| CAI-DAT.md | Cài plugin lên tổ chức Claude Team/Enterprise |
| docs/00–14 | Hướng dẫn góp ý; tổng quan, quy trình, guardrails, dữ liệu, tracker, trạng thái, SOP, thay đổi, sự cố, kho tri thức, truy vết, tự chủ, điều kiện chạy thử hồ sơ thật và triển khai Cowork |
| plugin/ | Nguồn plugin: manifest, skill seller-onboarding, agent output-checker, hooks |
| plugins/, .claude-plugin/ | Hai bản plugin đã đóng gói (vận hành, test) và danh mục marketplace `hi1-noi-bo` để đồng bộ từ GitHub; sinh bằng `tools/build_plugin.py --release` |
| releases/ | Zip plugin để tải lên thủ công; giữ bản trước để lùi |
| project/ | Instructions, hướng dẫn cài đặt, danh mục kho tri thức và gói nạp do export_kb.py sinh: kb-draft/ (Project thử nghiệm), kb/ (Project vận hành) |
| skills/ | Tám Skill: sáu nghiệp vụ và hai bản nháp (seller-cms-entry, seller-contract-draft); references/templates/scripts tự chứa |
| templates/ | Góp ý, tracker 26 cột, nhật ký AI 9 cột, phiếu bàn giao/chuyển cấp, mẫu phê duyệt KU, hàng chờ hỏi owner |
| tests/ | 41 ca thiết kế, input SIM, fixture và expected JSON, test hook/gói plugin; không hồ sơ thật |
| kb-workspace/ | Đầu ra mô phỏng của bước biên tập tri thức (candidate KU DRAFT, log mâu thuẫn/khoảng trống, đối soát label), sổ nguồn và phiếu duyệt KU đang dùng. Không phải kho APPROVED, không nạp Project |
| tools/ | Kiểm và đóng gói Skill (build_skills.py); đóng gói plugin (build_plugin.py); sinh catalog và gói nạp từ candidate KU (export_kb.py) |
| .github/ | Workflow kiểm tra tự động |
| CHANGELOG.md / AUDIT.md | Lịch sử thay đổi / nhật ký kiểm định |

Tài liệu quản trị, ngân sách và phê duyệt PM lưu nội bộ, không đưa vào đây. Xem thêm [xử lý sự cố](docs/09-xu-ly-su-co.md), [quản trị kho tri thức](docs/10-quan-tri-kho-tri-thuc.md), [truy vết yêu cầu](docs/11-truy-vet-yeu-cau.md) và [phiếu bàn giao duyệt](templates/phieu-ban-giao-duyet.md).

## Góp ý

Đọc [hướng dẫn đọc và góp ý](docs/00-huong-dan-doc-va-gop-y.md), ghi mỗi ý kiến một dòng vào [mẫu góp ý](templates/gop-y.csv); gửi PM theo kênh và hạn PM thông báo. Không ghi dữ liệu thật/PII trong góp ý.
