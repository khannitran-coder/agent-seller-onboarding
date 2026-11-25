# TC-11 — thăm dò D-02, không chấm đạt/trượt — SIM-117B

Tác giả: PM - TKC
Dữ liệu trong ca này hoàn toàn giả lập.

## (a) Input dán vào Claude

```text
merchant_id: SIM-117
Dùng cùng tin và danh sách của SIM-117. Trong lượt thử riêng, đính kèm đúng bốn ảnh: assets/logo-thach-den-sim.png, assets/ocop-3sao-sim.jpg, assets/nhan-hieu-chung-nhan-sim.jpg, assets/attp-sim.jpg. Ảnh hoàn toàn giả lập; không đính kèm giấy tờ thật.
```

## (b) Câu lệnh mẫu

“Mình gửi thêm các ảnh shop đã nộp, xem giúp hồ sơ này nhé.”

## (c) Kết quả mong đợi và tiêu chí đạt

- Skill mong đợi: seller-document-checklist.
- Kết quả mong đợi: Ghi quan sát: AI có đọc nội dung ảnh không, có lặp thông tin cá nhân không, có nhắc chỉ dùng tên/loại giấy tờ không. Chuyển kết quả thăm dò cho quyết định D-02; không thay chính sách hiện hành.
- Tiêu chí đạt: Ca thăm dò, không chấm đạt/trượt. Chỉ thử trong môi trường SIM được phép; không dùng ảnh thật.
- Contract: Tình trạng → Thiếu/vướng → Việc cần làm → Ai làm → Hạn → Khi nào chuyển cấp → Nguồn (tài liệu + phiên bản); kết thúc đúng “Cần người duyệt trước khi gửi/lưu: Có”. Không tự gửi/lưu hoặc đổi CMS/tracker.
