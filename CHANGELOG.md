# Lịch sử thay đổi

## v0.1.0 — 2026-11-16

- Người thực hiện: PM - TKC.
- Lý do: đóng gói Phương án A cho nhóm Phát triển & Hỗ trợ Nhà bán Hi1.
- Thay đổi: tài liệu vận hành, bốn Skill v0.1.0, mẫu tin, schema tracker, instructions và 14 ca giả lập.
- Trạng thái: pilot [CHỜ COO DUYỆT – D-01]; chưa có chính sách APPROVED được cung cấp; chưa vận hành thật.
- Kiểm tra tĩnh: xem kết quả xác thực trong PR; không thay thế kiểm thử hành vi trên Claude Project.
- Chạy lại 14 ca trên Claude Project: chưa chạy. Người kiểm định kiểm tra và người kiểm ghi kết quả thực tế; không suy kết quả từ kiểm tra tĩnh.

Khi đổi Skill: ghi ngày, người, tên Skill + version trước/sau, lý do và kết quả chạy lại 14 ca (hoặc ghi chưa chạy).

## Sửa theo audit PR #1 — 2026-11-16

- Người thực hiện: PM - TKC.
- F1: đóng gói guardrails vào references của cả bốn Skill; thêm schema và phiếu chuyển cấp nội bộ cho daily-operations-report; bổ sung quy tắc đồng bộ.
- F2: description 300–600 ký tự, có cụm từ kích hoạt và trường hợp không dùng.
- F3: thêm created_at và first_contact_at sau source_channel, tổng 25 cột; cập nhật công thức tuổi hồ sơ/phản hồi đầu và TC-09.
- F4–F5: ánh xạ nhãn D-01…D-06 theo chủ đề, Phương án B là định hướng chưa quyết; xoá dòng trống thừa.
- Ghi nguyên kết quả kiểm định vào AUDIT.md; F7 do PM chuyển repo sang private trước merge, chưa xác nhận hoàn tất.
- Kiểm tra tĩnh: frontmatter, độ dài description, đường dẫn và file trong từng zip Skill, header 25 cột, bản sao đồng bộ, quét dữ liệu nhạy cảm và diff whitespace (kết quả cụ thể trong PR).
- F6: 14 ca chưa chạy trên Claude Project; kết quả chạy sẽ ghi CHANGELOG ở tuần 1. Không suy kết quả hành vi từ kiểm tra tĩnh. Chưa merge, chờ người kiểm định kiểm tra lại commit mới.

## v0.1.1 — 2026-11-16

- Người thực hiện: PM - TKC.
- G1–G6: thêm ma trận 10 sự cố, vòng đời kho tri thức, phiếu bàn giao duyệt, skill_version (26 cột), SOP một hồ sơ 8 bước và truy vết 15 FR/12 BR.
- Bốn Skill v0.1.0 → v0.1.1; bổ sung Rủi ro trong Tình trạng nếu có, giữ contract COO; giữ phân loại dữ liệu theo v1.3 (L1/L2).
- Đồng bộ references fail-safe/schema và template đóng gói; không sửa AUDIT.md; không đổi phần KHỚP đã được xác nhận qua kiểm định.
- Kiểm tra tĩnh: zip độc lập, frontmatter/description, schema/CSV 26 cột, đủ 15 FR/12 BR, bản sao đồng bộ, quét PII và whitespace (kết quả trong PR).
- Chạy lại 14 ca trên Claude Project: chưa chạy, ghi kết quả ở tuần 1; bảng truy vết chỉ ra phạm vi chưa được ca hiện có kiểm trực tiếp.
- Chưa có trích WF-A01…A06 hoặc toàn văn PLAN-001/v0.2 trong lần QC này; không tự dựng nội dung hoặc thêm tài liệu quản trị. Giữ điều kiện Sẵn sàng bán tại docs/06.

## v0.1.2 — 2026-11-16

- Người thực hiện: PM - TKC.
- seller-document-checklist, seller-communication, first-product-assistant: v0.1.1 → v0.1.2. Checklist 9 mục và điều kiện chủ thể; mẫu E–I, không chứa thông tin đăng nhập; khung SEO và chuẩn bị ảnh/khối lượng.
- Thêm 2 sự cố trong docs/09 và đồng bộ 4 bản references/guardrails.md; ghi backlog v0.2 trong docs/11.
- daily-operations-report giữ version 0.1.1 vì quy trình không đổi; reference an toàn được đồng bộ theo F1.
- README giữ nguyên phần giới thiệu PM và hướng dẫn cũ; chèn nguyên văn kiến trúc v0.1.2 (chỉ chuẩn hoá Markdown).
- Kiểm tra tĩnh: zip Skill tự chứa, YAML/description, schema 26 cột, quét chuỗi cấm/PII và whitespace; xem kết quả trong PR.
- Chạy lại 14 ca trên Claude Project: chưa chạy, chờ người kiểm định thực hiện; không tuyên bố đạt kiểm thử hành vi.
- Chưa COO duyệt D-04/D-07/D-08; không triển khai quyền ghi CMS hoặc gửi tin bằng AI. Không merge, chờ người kiểm định kiểm tra.

### Sửa F8 theo kiểm định — 2026-11-16

- Người thực hiện: PM - TKC.
- Tách phần “Tin gửi nhà bán” và “Ghi chú cho nhân viên (không gửi)” ở đủ chín mẫu A–I; metadata, nhãn duyệt và ghi chú nội bộ nằm sau phân cách.
- Kiểm tra tĩnh và quét chuỗi bí mật lại trước merge; 14 ca hành vi trên Claude Project vẫn chưa chạy. Giữ phiên bản đợt sửa trước merge v0.1.2.

## v0.1.3 — 2026-11-16

- Người thực hiện: PM - TKC.
- Thêm ma trận tự chủ M0–M5, A01–A08, điều kiện nâng/hạ, nút dừng, nhật ký và rủi ro R01–R09: ĐỀ XUẤT, chưa có hiệu lực.
- README làm rõ giới hạn theo thiết kế, mức theo hành động và lộ trình D-07a/D-07b; docs/03 trỏ đề xuất; docs/11 truy vết hành động/quyết định.
- Không đổi hành vi hoặc version bốn Skill; không bật connector/quyền, không đổi schema tracker 26 cột. Không triển khai cơ chế nhật ký hoặc hậu kiểm trong lần này.
- Kiểm tra tĩnh: mã hành động/quyết định, liên kết, quét chuỗi bí mật và diff whitespace; không cần chạy lại 14 ca hành vi vì chỉ sửa tài liệu, không sửa Skill.
- Chưa merge; chờ người kiểm định kiểm tra. Lộ trình từ M0 được làm rõ trong cập nhật dưới đây; đánh giá rủi ro và người theo dõi là đề xuất.

### Chuẩn hoá tài liệu và lộ trình — 2026-11-16

- Người thực hiện: PM - TKC.
- Cho phép công khai ma trận; R09 chỉ mô tả tổng quát quy trình cấp/bàn giao thông tin đăng nhập theo D-08.
- M0 chỉ vào M3 sau COO duyệt; ≥30 lượt tại M3 trước nâng lên M3+/M4; giữ trần A04/A05 và cấm A07/A08.
- Thêm mẫu nhật ký AI 9 cột ở tab riêng, bắt buộc trước M3+/M4; tracker chính vẫn 26 cột. Chưa bật quyền hoặc connector.
- Chuẩn hoá tác giả và vai trò PM trong nội dung tệp, đồng bộ references; không đổi hành vi hoặc version bốn Skill, không sửa lịch sử commit.
- Kiểm tra: quét dấu vết tác giả/công cụ soạn và chuỗi bí mật; kiểm gói Skill, schema và liên kết. 14 ca hành vi chưa chạy.

## v0.2.0 — 2026-11-16

- Người thực hiện: PM - TKC.
- Hai Skill cài được version 0.1.0: affiliate-price-review (Excel chỉ đọc) và seller-media-tools (ảnh/PDF bản sao); references tự chứa, không thay quyền A06.
- Hai Skill bản nháp version 0.0.1 trong skills-draft/: seller-contract-draft (D-08b) và seller-cms-entry (D-07a/D-07b), chưa cài/kích hoạt. Script Windows/Office chỉ là bản nháp chưa chạy.
- Fixture bảng giá SIM và script tạo; thêm PR-01…PR-06/MT-01…MT-04; cập nhật README, docs/02, docs/11, docs/12.
- Đã chạy công cụ ảnh vuông nền mờ/nền trắng, gộp 3 PDF SIM và kiểm thứ tự 6 trang; kiểm chống ghi đè và nguồn không đổi; fixture báo đúng sáu lỗi. Thiếu cache và dòng trống được kiểm thêm; kết quả trong PR.
- MT-03 và các ca hành vi mô hình chưa chạy; không coi kiểm script là xác nhận chặn dữ liệu Đỏ. Bốn Skill cũ giữ nguyên; chưa merge, chờ kiểm định.

Nguồn: skill vận hành nội bộ của nhóm (bản 11/2026), đã lược thông tin nội bộ

### Sửa K1 — 2026-11-16

- Người thực hiện: PM - TKC.
- Map mặc định theo Bang_Nhap_Affiliate và cột mẫu thực tế; alias chuẩn hoá hoa thường/dấu/khoảng trắng, --map cho mẫu khác. Thiếu cột trả danh sách cụ thể.
- PR-03 dùng trạng thái lệch giá và công thức cho người kiểm, không bắt cột Cơ sở tính. % nhà bán tuỳ chọn; PR-02 đọc dòng KIỂM TRA khi không có cột này.
- Giữ fixture cũ + map SIM riêng; thêm fixture tiêu đề mẫu thật, generator tạo cả hai, không ghi đè. Ghi rõ PM cần đối chiếu file mẫu trống theo D-04.
- Kết quả chạy hai fixture và nhánh lỗi/alias/công thức ghi trong PR. Giữ version 0.1.0 trong đợt sửa trước merge; không bật quyền mới.

## v0.2.1 — 2026-11-16

- Người thực hiện: PM - TKC.
- Thêm JSON nghiệp vụ và tracker_report.py (thư viện chuẩn, dưới 250 dòng), xuất JSON/Markdown, không in ô lỗi hoặc tính dòng lỗi.
- daily-operations-report v0.1.1 → v0.2.1: có code phải chạy script và dùng nguyên số liệu; không có code ghi “số liệu chưa qua script”. Các Skill khác không đổi.
- tools/build_skills.py kiểm/zip skills/ bằng thư viện chuẩn; không đóng bản nháp, dist/ bị Git bỏ qua. Tên tác giả hai bản nháp theo quyết định PM được giữ nguyên, không làm lỗi kiểm tra.
- Workflow pull_request và push main kiểm gói, so hai fixture giá và hai fixture tracker với expected JSON. Fixture dữ liệu Đỏ chỉ mô phỏng và được manifest đánh dấu.
- Giữ nguyên các commit PM 0a7661f, 0654406; không sửa tác giả bản nháp, không viết lại lịch sử.
- Chưa bật connector/quyền; kết quả tự kiểm/workflow ghi tại PR.

## v0.2.2 — 2026-11-16

- Người thực hiện: PM - TKC.
- Bản tài liệu cho vòng góp ý của team/CEO trước khi chốt pilot; README theo vai trò, bảng tám Skill và quyết định đang chờ; thêm docs/00 và mẫu góp ý.
- Giữ nguyên giới thiệu PM, toàn bộ kiến trúc (chỉ đổi tiêu đề v0.2.2); không sửa Skill/script/workflow hoặc version Skill; giữ tác giả hai bản nháp.
- Làm rõ 27 ca thiết kế gồm 14 ca pilot và 13 ca công cụ; workflow hiện có chỉ chạy giá/tracker, MT-03 chưa kiểm hành vi mô hình. Không nâng trạng thái ca chưa chạy thành đạt.
- Các đoạn nhật ký/version lẻ dưới đây chuyển nguyên văn từ README; là lịch sử, không thay trạng thái bản phát hành v0.2.2.

### Thông tin chuyển từ README

v0.1.1 – pilot, chưa COO duyệt

Gói tài liệu dùng cho nhóm Phát triển & Hỗ trợ Nhà bán Hi1: Claude Cowork production-assist, mức tự chủ 3 (AI chỉ đọc và soạn nháp; người duyệt trước gửi/lưu). [CHỜ COO DUYỆT – D-01] Trạng thái **v0.1.1 – pilot, chưa COO duyệt**. Chỉ dùng giả lập SIM-xxx trước khi có nguồn và quyền được duyệt. Không có dữ liệu thật/PII trong repo.

**Chưa merge:** PM chuyển repo sang private trước khi merge theo F7; sau khi sửa F1–F3 và xử lý F7, chờ người kiểm định kiểm tra lại commit mới.

Bản v0.1.1 bổ sung theo kết quả kiểm định nguồn. 14 ca vẫn chưa chạy trên Claude Project. Không tự thêm trường ngoài schema 26 cột đã yêu cầu.

Chỉ đóng gói từng folder trong skills/. Hai Skill mới version 0.1.0; bốn Skill cũ giữ version. Bản nháp skills-draft/ version 0.0.1 không phải Skill dùng được; không cài hoặc chạy cho tới khi COO duyệt mã ghi ở đầu bản nháp.

Hai bản nháp vẫn chưa cài/kích hoạt;tên tác giả trong chúng được giữ theo quyết định PM, không thuộc tiêu chí lỗi của công cụ.

Nguồn của phần công cụ v0.2: skill vận hành nội bộ của nhóm (bản 11/2026), đã lược thông tin nội bộ.

## Đối soát label theo kiến trúc Data Pipeline v1.0 — 2026-11-22

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- Lý do: đối soát repo với kiến trúc Data Pipeline Tri thức v1.0 sau khi xử lý batch mô phỏng SIM-BATCH-001 (20 candidate KU DRAFT trong kb-workspace); chỉ gắn nhãn và thêm khung trống, không điền nội dung từ candidate vào kho.
- docs/10 v0.1.1 → v0.1.2: thêm layer, authority_type, scope, sensitivity và approval_state của nguồn (đề xuất, chưa hiệu lực).
- docs/04 v0.1.0 → v0.1.1: thêm mục Gate 0; merchant_id xếp Vàng [CHỜ COO DUYỆT – D-02].
- project/knowledge-base-index v0.1.0 → v0.1.1: thêm 3 dòng nhóm tài liệu (hợp đồng và phụ lục; chiết khấu Affiliate; SOP 12 bước/bàn giao/sự cố), để trống.
- Ghi chú nguồn: Mẫu F (mục 9 và dòng Tammi chưa có nguồn), checklist seller-document-checklist (mục 9, ATVSTP/OCOP chưa có nguồn), bang-gia-schema (cơ sở tính chiết khấu chờ owner xác nhận). Chỉ là ghi chú, không đổi nghiệp vụ; version Skill giữ nguyên (seller-communication 0.1.2, seller-document-checklist 0.1.2, affiliate-price-review 0.1.0).
- README: thêm dòng kb-workspace/ trong bảng cấu trúc.
- Chạy lại 14 ca trên Claude Project: chưa chạy; không tuyên bố đạt. Kiểm tra tĩnh bằng công cụ kiểm gói Skill, xem kết quả trong PR.
- Chưa có tài liệu APPROVED nào; 20 candidate chưa được dùng làm căn cứ trả lời. Ba mâu thuẫn CF-01…CF-03 chờ owner.

## Danh mục kho tri thức v0.2.0 và điều kiện chạy thử — 2026-11-22

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- Lý do: đối chiếu mục tiêu dự án với bảng trả lời đào tạo của COO và chuẩn bị điều kiện chạy thử hồ sơ thật.
- project/knowledge-base-index v0.1.1 → v0.2.0: thêm giao thức truy xuất, ghi tài liệu hiện có và trạng thái cho 11 nhóm, ánh xạ ý định (lấy từ câu nói thường gặp của COO) → nhóm, điều kiện nạp. Mọi dòng vẫn DRAFT hoặc chưa có nguồn; chưa có dòng APPROVED; owner đề xuất ghi riêng chờ D-06; không điền người duyệt, ngày hiệu lực.
- Thêm docs/13 (v0.1.0): danh sách kiểm 13 điều kiện trước khi chạy hồ sơ thật, điều kiện dừng và ánh xạ 8 thông tin COO phải xác nhận với D-01…D-09. Kết luận ghi trong tài liệu: hiện chưa đủ điều kiện.
- README: thêm docs/13 vào bảng cấu trúc và bước 8 mục Cài đặt.
- Không đổi Skill, schema, workflow; 14 ca vẫn chưa chạy.

## Quyết định giai đoạn 1, owner/người duyệt và batch Sổ tay — 2026-11-22

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- Quyết định của người thiết kế agent: giai đoạn 1 không cần COO ký; owner tri thức là Bắc (Phát triển nhà bán), người duyệt là Huyền; hồ sơ nhà bán được xử lý kèm số CCCD và số tài khoản trong workspace doanh nghiệp.
- Dữ liệu: docs/03, docs/04, project instructions và guardrails của bốn Skill cho xử lý tên, SĐT, email, MST, địa chỉ, số CCCD, số tài khoản; không lặp lại đầy đủ số CCCD/số tài khoản trong đầu ra, tracker, log, repo. Vẫn dừng với mật khẩu, OTP, token, khóa API. seller-media-tools, affiliate-price-review và skills-draft giữ nguyên quy tắc cũ (công cụ không cần dữ liệu giấy tờ).
- Skill: seller-communication, seller-document-checklist, first-product-assistant v0.1.2 → v0.1.3; daily-operations-report v0.2.1 → v0.2.2. docs/03 v0.1.1, docs/04 v0.1.2, project instructions v0.1.2, test-cases v0.1.1 (SAFE-02 và SIM-113 đổi theo quyết định).
- Chạy lại 14 ca trên Claude Project: chưa chạy; không tuyên bố đạt. Các Skill đã đổi hành vi nên bắt buộc chạy lại trước khi dùng hồ sơ thật. Sau khi tích hợp nhánh upstream, TC-14 và SIM-120 (STK trong tin Zalo) đổi theo quyết định giai đoạn 1; tám ca bổ sung TC-11…TC-18 chưa chạy.
- Thêm kb-workspace/ai-seller-onboarding/SIM-BATCH-002: 13 candidate KU DRAFT từ Sổ tay nhà bán và thư thông báo Affiliate; thêm CF-04, CF-05 và gap G-21…G-28.
- knowledge-base-index v0.2.0 → v0.3.0 (owner → duyệt, nguồn batch 002, ánh xạ ý định, mâu thuẫn). docs/13 v0.1.0 → v0.2.0 (phạm vi pilot đề xuất, điều kiện cập nhật).
- Chưa có tài liệu APPROVED; 26 KU chưa được duyệt.

## SOP pilot và quy trình hỏi owner — 2026-11-25

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- docs/07 v0.1.0 → v0.2.0: thêm trang SOP pilot, quy trình Hỏi owner làm tay (pilot chưa nối công cụ gửi tin), gửi ảnh hướng dẫn app theo quyết định người thiết kế agent kèm điều kiện xác nhận đã đổi mật khẩu; sửa các chỗ trái quyết định dữ liệu giai đoạn 1; mẫu tin A–I; tab nhật ký AI.
- Thêm templates/hang-cho-hoi-owner.csv. SIM-BATCH-001 r4: c0019 sửa ghi chú, phiếu duyệt đổi sang r4.
- Chưa gán người ghi sự cố, nhân viên pilot; chưa xác nhận đổi mật khẩu. 14 ca chưa chạy.

## Hoãn xử lý mâu thuẫn, chạy pilot trước — 2026-11-25

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- Quyết định của người thiết kế agent: CF-01…CF-06 xử lý sau; pilot chạy với 22 KU không mâu thuẫn sau khi người duyệt ghi phiếu. docs/13 điều kiện 6 cập nhật. Đã thử sinh gói vận hành 22 KU bằng phiếu giả ngoài repo; chưa có phê duyệt thật. 14 ca chưa chạy.

## Xác nhận duyệt nguồn Drive và phiếu duyệt KU — 2026-11-25

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- Người dùng xác nhận trong hội thoại: tài liệu Drive gửi cập nhật ngày 25/11 đã được duyệt. Ghi ở SIM-BATCH-001 r3 manifest và đầu knowledge-base-index (v0.5.1). Chưa KU nào chuyển APPROVED; chờ phiếu duyệt của người duyệt.
- SIM-BATCH-001 r3: c0004 và c0007 gắn cờ conflict còn thiếu (CF-04, CF-05); nội dung không đổi.
- Tạo phiếu duyệt điền sẵn cho 20 KU nguồn Drive (11 không mâu thuẫn, 9 có mâu thuẫn); tệp lưu cục bộ, Git bỏ qua.
- Người dùng xác nhận thêm Sổ tay nhà bán và thư Affiliate đã được duyệt: ghi ở SIM-BATCH-002 manifest; phiếu thêm 13 KU (11 không mâu thuẫn, 2 có mâu thuẫn). Chưa KU nào APPROVED.

## Đóng gói cho claude.ai và hướng dẫn cài đặt — 2026-11-25

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- tools/build_skills.py: zip chứa thư mục trùng tên Skill (trước đây SKILL.md ở gốc zip, không đúng cấu trúc claude.ai yêu cầu); thêm dist/short/ dùng mô tả ≤200 ký tự từ tools/claude-ai-descriptions.json. Không đổi SKILL.md.
- Thêm project/cai-dat-claude.md (hướng dẫn và prompt cài đặt); README trỏ tới.
- Chưa thử tải lên claude.ai; 14 ca chưa chạy.

## Đối chiếu Drive, revision r2 và nơi đặt tài liệu — 2026-11-25

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- Đối chiếu thư mục Drive: không có file mới hoặc sửa sau 21/11/2026. Xem trực tiếp ảnh: SIM-BATCH-001 r2 sửa c0001, c0019 (thêm nhận diện ứng dụng), c0006 (cờ conflict), thêm c0021 và mâu thuẫn CF-06 về “0 phí trung gian”.
- Sự cố: ảnh hướng dẫn tải app trên Drive hiển thị thông tin đăng nhập (G-29). Không ghi giá trị vào repo; ảnh gốc không được nạp hoặc gửi cho tới khi đổi mật khẩu và che.
- seller-communication v0.1.3 → v0.1.4: Mẫu F thêm bản ngắn theo văn bản mở shop trên Drive. 14 ca chưa chạy.
- tools/export_kb.py: lấy revision mới nhất; phê duyệt bắt buộc đúng revision (templates/phe-duyet-ku.csv thêm cột revision). kb-draft: 33 KU.
- knowledge-base-index v0.4.0 → v0.5.0: thêm c0021, CF-06 và mục F (nơi đặt tài liệu).

## Danh mục kho tri thức v0.4.0 và công cụ sinh gói nạp — 2026-11-23

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- project/knowledge-base-index v0.3.0 → v0.4.0: cột Nạp Project chỉ rõ tệp thử nghiệm cho từng nhóm; thêm mục E (hai Project, cách tạo gói, quy tắc tệp phê duyệt).
- Thêm tools/export_kb.py (thư viện chuẩn): đọc candidate trong kb-workspace và sinh project/kb-draft (catalog và 6 tệp nhóm, 32 KU, khoảng 24.000 token, chỉ Project thử nghiệm). Với --approvals, chỉ sinh project/kb từ các dòng APPROVED có người duyệt và ngày duyệt; KU có cờ conflict cần conflict_resolved=yes. Công cụ không tự đặt trạng thái APPROVED.
- Thêm templates/phe-duyet-ku.csv; .gitignore bỏ các tệp phe-duyet-*.csv (chứa tên người duyệt).
- Đã thử luồng APPROVED trên tệp phê duyệt thử: đúng các dòng bị bỏ khi thiếu người duyệt hoặc conflict chưa quyết. Chưa có phê duyệt thật nên chưa có project/kb. 14 ca vẫn chưa chạy.

## Chốt phạm vi pilot — 2026-11-23

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- docs/13 mục 2: người thiết kế agent chốt phạm vi pilot theo bảng đề xuất: DN/HTX/HKD có MST và hóa đơn; hàng thông thường (nhóm có điều kiện chỉ đối chiếu giấy tờ và chuyển kiểm duyệt); AI hỗ trợ bước 3, 4, 5, 7, 8, 12; 10–15 hồ sơ, 2–4 tuần, 2–3 nhân viên; chạy song song, AI chỉ soạn nháp.
- Ngày bắt đầu pilot: 24/11/2026 (chốt 2026-11-23); kết thúc dự kiến 08/12 đến 22/12/2026. Chưa chọn tên nhân viên tham gia; điều kiện chạy thử ở mục 3 của docs/13 chưa đạt tại thời điểm chốt, nên hồ sơ thật chỉ nhận khi đạt. Không đổi Skill; 14 ca chưa chạy.

## Trạng thái duyệt tài liệu nguồn — 2026-11-25

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- Lý do: người thiết kế agent xác nhận mọi tài liệu nguồn đã được duyệt.
- Thay đổi: thêm sổ nguồn `kb-workspace/ai-seller-onboarding/so-nguon.csv` (10 tài liệu APPROVED, 2 không dùng); danh mục v0.5.2 tách cột duyệt tài liệu nguồn khỏi trạng thái KU; gói `kb-draft` ghi trạng thái tài liệu nguồn từng KU; docs/07 v0.2.1; docs/13 v0.2.1 (sửa số KU thành 33).
- Skill: seller-document-checklist v0.1.3 → v0.1.4 (chỉ nhãn nguồn, không đổi quy trình). 14 ca chưa chạy.
- Không đổi: chưa KU nào APPROVED, chưa có gói `project/kb/`; CF-01…CF-06 còn hoãn; candidate giữ nguyên revision nên phiếu duyệt đang chờ vẫn dùng được.

## Duyệt 33 KU cho pilot — 2026-11-25

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận). Người quyết: người thiết kế agent.
- Lý do: có kho tri thức dùng được để chạy pilot.
- Thay đổi: 33 KU APPROVED cho pilot, sinh `project/kb/`; 11 KU mâu thuẫn nạp kèm nhãn (thay quyết định hoãn nạp cùng ngày). Công cụ nhận `conflict_resolved=hoan`; mẫu phiếu thêm cột `mau_thuan_chua_quyet`. Danh mục v0.6.0, instructions v0.1.3, docs/07 v0.2.2, docs/13 v0.2.2, hướng dẫn cài đặt v0.1.1.
- Skill: seller-document-checklist v0.1.4 → v0.1.5 (chỉ ghi chú nguồn). 14 ca và hành vi với KU mâu thuẫn chưa chạy.
- Giới hạn: người duyệt được chỉ định (Huyền) chưa duyệt; chưa đối chiếu từng KU với nguồn; CF-01…CF-06 chưa quyết.

## Sửa lỗi sau rà soát repo — 2026-11-25

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- tools/export_kb.py: phiếu duyệt không có KU APPROVED hợp lệ thì dừng với exit 2 và giữ nguyên `project/kb/`; trước đó công cụ xoá 6 tệp nhóm.
- SIM-BATCH-001 r5: KU c0001 bỏ câu quy tắc xử lý số tài khoản trái quyết định giai đoạn 1 (22/11/2026); sinh lại `project/kb-draft/`. Người thiết kế agent duyệt r5 cho pilot cùng ngày (chưa đối chiếu lại với nguồn), đã sinh lại `project/kb/` đủ 33 KU.
- README, docs/11 v0.1.2 và tests/test-cases.md v0.1.2: sửa tổng số ca thành 35, cập nhật mô tả project/, templates/, tests/.
- Project instructions v0.1.3 → v0.1.4: mẫu tin A–I, thêm điều hướng affiliate-price-review và seller-media-tools. Cần dán lại vào Project đã tạo. Danh mục v0.6.1 ghi revision và phê duyệt của c0001.
- Không đổi Skill. 14 ca chưa chạy.

## Plugin Cowork và quyết định mâu thuẫn — 2026-11-25

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận). Người quyết: người thiết kế agent (nhận thẩm quyền owner).
- Lý do: đưa agent vào pilot hồ sơ thật bằng plugin Cowork.
- Quyết định: CF-02 chi hoa hồng ngày 05 tháng N+2; CF-03 giá hội viên trừ voucher nhà bán tài trợ; CF-04 theo hợp đồng; CF-05 05 ngày lịch, không kết luận thời điểm tiền vào ví; CF-06 tư vấn theo hợp đồng; CF-01 để mở. Nguồn chưa có (điều kiện duyệt, ngành hàng cấm, SLA, trạng thái CMS, biểu phí) chạy với khoảng trống.
- KU: SIM-BATCH-001 r6 (c0004, c0006, c0007, c0012, c0013, c0018, c0021), SIM-BATCH-002 r2 (c0010, c0011); duyệt cho pilot; sinh lại `project/kb/` (33 KU, 2 KU mâu thuẫn) và `project/kb-draft/`. CF-02 và CF-03 khác văn bản Phụ lục Affiliate hiện hành.
- Mới: `plugin/` 0.3.0 (skill seller-onboarding 0.1.0, agent output-checker, hooks), `tools/build_plugin.py`, `tests/plugin/`, docs/14, templates/ket-qua-kiem-thu.csv.
- Skill: affiliate-price-review 0.1.0 → 0.1.1 (chỉ ghi chú cơ sở tính). Danh mục v0.7.0, docs/13 v0.3.0, hướng dẫn cài đặt v0.1.2.
- Kiểm: test hook và gói plugin, kiểm gói Skill. Chưa tải lên Cowork, chưa kiểm khói, 14 ca chưa chạy.

## v0.3.0 — Agent Seller Onboarding — 2026-11-25

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận).
- Lý do: gom một chỗ để cài agent lên tài khoản Claude doanh nghiệp.
- Thay đổi: `.claude-plugin/marketplace.json` và `plugins/` (bản vận hành và bản test 0.3.0) sinh bằng `tools/build_plugin.py --release`; CAI-DAT.md; test khớp nguồn. Repo mới bắt đầu bằng một commit, lịch sử cũ ở repo gốc.
- Chưa tải lên Claude, chưa kiểm khói, 14 ca chưa chạy.
- Bổ sung cùng ngày: thư mục `releases/` chứa zip hai bản plugin để tải lên không cần Python; `--release` sinh và test đối chiếu.

## v0.4.0 — Mở rộng bước AI hỗ trợ: 1, 6, 9, 11 — 2026-11-27

- Người thực hiện: PM - TKC (đề xuất, chờ PM xác nhận). Người quyết: người thiết kế agent, 27/11/2026.
- Lý do: đưa bước 1 (nhận lead), 6 (hướng dẫn gian hàng), 9 (hướng dẫn vận hành đơn), 11 (bàn giao, hẹn chăm sóc) vào giai đoạn test. Bước 2 (kiểm trùng) và 10 (kiểm tra sẵn sàng bán) vẫn người làm: kiểm trùng cần đọc CMS (A01, M0); điều kiện sẵn sàng bán và nhãn trạng thái CMS chưa có nguồn.
- Không đổi mức tự chủ: vẫn M3, người duyệt từng lần. Không bật connector, quyền ghi hay trình duyệt; hooks giữ nguyên. AI không đọc CMS; đọc tracker vẫn theo daily-operations-report và chỉ khi tracker được tạo (docs/13 điều kiện 9).
- Skill: seller-onboarding 0.1.0 → 0.2.0 (bảng điều phối và mục “Bước 1, 6, 9, 11”: bước 6 và 9 chỉ tóm tắt KU có mã, phí và cước chưa có KU ghi “Chưa có căn cứ xác nhận”, bước 9 bắt buộc output-checker, bước 11 giữ [thời điểm], không ghi “sẵn sàng bán”); seller-communication 0.1.4 → 0.1.5 (mẫu theo bước). Project instructions v0.1.4 → v0.1.5 (cần dán lại nếu dùng phương án lùi Project).
- Plugin 0.3.0 → 0.4.0: sinh lại `plugins/`, `.claude-plugin/marketplace.json`, thêm `releases/*-0.4.0.zip`; giữ zip 0.3.0 để lùi bản.
- Tài liệu: docs/02 v0.2.0 (cột Pilot), docs/07 v0.2.3, docs/11 v0.1.3, docs/13 v0.4.0, docs/14 v0.2.0, CAI-DAT v0.4.0 (mục nâng bản), README.
- Kiểm thử: thêm 6 ca BX-01…BX-06 (`tests/sim/SIM-125.md`…`SIM-130.md`), bắt buộc trước khi dùng bốn bước mới với hồ sơ thật; tổng 41 ca. `build_skills.py --check` đạt; `unittest tests/plugin` 10/10 đạt. Chưa tải 0.4.0 lên Cowork, kiểm khói và 14 ca + 6 ca BX chưa chạy.
