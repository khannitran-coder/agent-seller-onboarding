# Quy tắc thay đổi

v0.1.0 – pilot, chưa COO duyệt

| Loại thay đổi | Người thực hiện / phê duyệt |
|---|---|
| Diễn đạt, prompt không đổi nghiệp vụ | PM sửa, Trưởng nhóm kiểm |
| Checklist, điều kiện trạng thái, nội dung cam kết | COO duyệt trước khi áp dụng |
| Quyền AI, nguồn dữ liệu, connector | COO quyết trước khi cấu hình |
| Lỗi nghiêm trọng | Dừng workflow, báo Trưởng nhóm, rollback bản an toàn, kiểm thử lại |

Version theo từng Skill: ten-skill v0.1.0 → v0.1.1; sửa version trong thân, ghi CHANGELOG ngày, người, lý do, kết quả chạy lại đủ 14 ca. Nếu chưa chạy ghi rõ chưa chạy; không ghi đạt thay người kiểm thử. Chỉ áp dụng bản đã được duyệt phù hợp, không dùng nhãn pilot như bằng chứng phê duyệt. Khi chính sách/giao diện đổi, dừng hướng dẫn theo bản cũ và nhờ owner xác nhận bản mới. Tài liệu quản trị và phê duyệt lưu nội bộ do PM quản lý, không đưa vào repo.

## Đồng bộ bản đóng gói Skill

Khi sửa docs/03-guardrails.md hoặc docs/05-tracker-schema.md, phải đồng bộ references tương ứng trong các Skill, kiểm tra từng zip độc lập và ghi CHANGELOG. Giữ khối chặn dữ liệu Đỏ và output contract đồng bộ giữa bốn Skill và project instructions. Khi sửa phiếu chuyển cấp, đồng bộ template trong daily-operations-report. Owner duy trì đề xuất là PM, chờ xác nhận [CHỜ COO DUYỆT – D-06]. Thay prompt/diễn đạt do PM sửa, Trưởng nhóm kiểm; đổi quyền/nguồn/connector cần COO quyết [CHỜ COO DUYỆT – D-03].

Khi đổi ma trận sự cố, đồng bộ phần fail-safe trong references/guardrails.md của cả bốn Skill. Khi đổi phiếu bàn giao duyệt, đồng bộ templates/phieu-ban-giao-duyet.md và bản trong seller-document-checklist. Ghi version Skill thực tế sinh nháp vào skill_version; không sửa lịch sử phiên bản của nháp cũ.
