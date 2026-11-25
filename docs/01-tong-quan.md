# Tổng quan

v0.1.0 – pilot, chưa COO duyệt

Nhóm Phát triển & Hỗ trợ Nhà bán Hi1 cần hỗ trợ hồ sơ nhất quán, giảm thao tác và sai sót mà vẫn giữ người chịu trách nhiệm. Mục tiêu pilot: chất lượng checklist, nháp tin, dữ liệu sản phẩm và báo cáo có nguồn; chưa đặt KPI đã phê duyệt.

[CHỜ COO DUYỆT – D-01] Phương án A đang đóng gói: Claude Cowork production-assist, Claude Project, bốn Skill và tracker Google Sheet chỉ đọc với AI. Người kiểm tra, gửi tin, cập nhật hệ thống và quyết định. Phạm vi gồm đúng 12 bước tại [quy trình](02-quy-trinh-12-buoc.md).

[CHỜ COO DUYỆT – D-05] Ba mốc độc lập: **Đã gửi đăng ký ≠ Gian hàng được kích hoạt ≠ Sẵn sàng bán**. Sẵn sàng bán cần shop hợp lệ, ≥1 sản phẩm hiển thị, địa chỉ lấy hàng, vận chuyển, thanh toán và nhà bán biết xử lý đơn; Trưởng nhóm xác nhận. Không suy diễn kích hoạt từ việc nộp hồ sơ.

Phương án B [ĐỊNH HƯỚNG – chưa quyết]: backend FastAPI + PostgreSQL + Claude API + Zalo OA khi đạt ít nhất 2/3 ngưỡng sau 4 tuần vận hành: >15 hồ sơ/ngày, lỗi đồng bộ Sheet–CMS >2%, thao tác thủ công >15 phút/hồ sơ. Tracker schema là schema DB tương lai; cách đo và quyết định chuyển đổi cần COO xác nhận.
