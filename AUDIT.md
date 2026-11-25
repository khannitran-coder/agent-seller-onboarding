# Nhật ký kiểm định

Ngày audit: 16/11/2026 · Người kiểm định: PM - TKC · Đối tượng: nhánh feat/seller-onboarding-package, commit 0b3352e

## Phạm vi
4 Skill, project instructions, docs 01–08, templates, tracker schema, 14 ca test. Audit tĩnh (đọc nội dung, kiểm cấu trúc, frontmatter, dữ liệu nhạy cảm). Chưa chạy Skill trên Claude Project.

## Phát hiện
| Mã | Mức | Nội dung | Xử lý |
|---|---|---|---|
| F1 | Chặn merge | Skill tham chiếu file ngoài folder, gãy khi upload zip | Đóng gói references/templates vào từng Skill |
| F2 | Chặn merge | description quá ngắn, khó kích hoạt đúng Skill | Viết lại 300–600 ký tự kèm cụm từ người dùng |
| F3 | Chặn merge | Thiếu created_at, first_contact_at để đo KPI và tuổi hồ sơ | Thêm 2 cột, tổng 25 cột |
| F4 | Nên sửa | Mọi nhãn chờ duyệt đều là D-04 | Ánh xạ D-01…D-06 đúng chủ đề |
| F5 | Nhỏ | Dòng trống thừa | Xoá |
| F6 | Ghi nhận | 14 ca chưa chạy; nội dung an toàn lặp ở 4 Skill | Chạy ở tuần 1; giữ đồng bộ qua quy tắc thay đổi |
| F7 | Chặn vận hành | Repo đang public; chứa quy tắc vận hành và cơ chế chống prompt injection nội bộ | PM chuyển repo sang private trước khi merge |

Điểm tốt: không có dữ liệu thật/PII; guardrails đầy đủ và đúng BRD; xử lý dữ liệu Đỏ, prompt injection, ngoài quyền nhất quán; Skill 04 không bịa tuổi hồ sơ/SLA; test case có tiêu chí đạt rõ.

## Câu hỏi
- Ai là owner duy trì bản references trong Skill khi docs thay đổi? (đề xuất: PM)
- Tracker dùng Google Sheet nào, ai có quyền ghi? (chờ D-06)

## Kết luận
Chưa merge. Merge sau khi F1–F3 đã sửa, F7 đã xử lý và người kiểm định kiểm tra lại commit mới.

## Audit lại – 16/11/2026

Đối tượng: commit 43961cf (sửa F1–F5) và fb53c15 (bổ sung theo QC nguồn). Nguồn đối chiếu: BRD HI1-AI-BRD-SD-1.2, Architecture Review v1.3, HI1-P1A-SOL-001 v0.1, bảng hỏi COO.

| Mã | Kết quả |
|---|---|
| F1 | Đạt – 4 folder Skill tự chứa, không còn tham chiếu ra ngoài |
| F2 | Đạt – description 441–455 ký tự, có cụm từ người dùng |
| F3 | Đạt – có created_at, first_contact_at; Skill 04 tính tuổi hồ sơ và phản hồi đầu |
| F4 | Đạt – nhãn tách D-01…D-06; Phương án B ghi định hướng |
| F5 | Đạt |
| G1 | Đạt – docs/09 ma trận 10 sự cố |
| G2 | Đạt – docs/10 vòng đời DRAFT/VERIFIED/APPROVED; index thêm 3 cột |
| G3 | Đạt – phiếu bàn giao duyệt, 2 bản đồng bộ |
| G4 | Đạt – cột skill_version, CSV 26 cột |
| G5 | Đạt – SOP xử lý một hồ sơ 8 bước |
| G6 | Đạt – docs/11 phủ đủ FR-01…15, BR-01…12 |
| L1, L2 | Chấp nhận – giữ khung COO II.C (thêm dòng Rủi ro) và phân loại dữ liệu theo v1.3 |

Còn mở: F6 – 14 ca chưa chạy trên Claude Project (chạy tuần 1 theo plan); F7 – repo còn public; FR-06, FR-09 chưa có Skill riêng (xử lý bằng Project instructions + kho tri thức, theo dõi khi pilot).

Kết luận: Nội dung đạt. Ngày 16/11/2026 PM quyết định merge khi repo còn public và chuyển repo sang private ngay sau đó; F7 chuyển thành việc của PM.
