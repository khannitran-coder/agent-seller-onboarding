# Conflict log — SIM-BATCH-001 r1

Giữ cả hai candidate, không chọn hộ. Người duyệt hoặc owner quyết định.

| Mã | Bên A | Bên B | Khác biệt | Hành động |
|---|---|---|---|---|
| CF-01 | c0002 (Hợp đồng Điều 1, SIM-SRC-003) | c0017 (Phụ lục Điều 11.3, SIM-SRC-004) | Hợp đồng: nhà bán cập nhật trên hệ thống hoặc **thông báo cho Hi1 tối thiểu 24 giờ trước khi áp dụng**. Phụ lục: thay đổi tỷ lệ có hiệu lực khi hệ thống ghi nhận, **không muộn hơn 24 giờ sau** khi nhà bán gửi yêu cầu. Chiều thời gian ngược nhau. | Owner pháp chế/Affiliate xác nhận quy tắc nào áp dụng cho thay đổi giá và thay đổi tỷ lệ Affiliate |
| CF-02 | c0013 (Phụ lục Điều 5.3, 5.4) | chính c0013 | Bảng đối soát gửi "ngày 5 hằng tháng N+1" và nhà bán có 03 ngày làm việc phản hồi, nhưng kỳ chi trả cũng là "ngày 05 của tháng N+1". Thời hạn phản hồi kết thúc sau ngày chi trả. | Owner Tài chính xác nhận mốc gửi đối soát và mốc chi trả |
| CF-03 | c0012 (Phụ lục Điều 3.1) | c0018 (Excel ô LƯU Ý) | Phụ lục: căn cứ tính A là giá bán niêm yết **sau khi trừ giảm giá, mã khuyến mại, voucher do nhà bán tài trợ**. Excel: A tính trên **giá bán hội viên Hi1**, không tính trên giá thị trường. Nguồn không nói giá hội viên đã là giá sau giảm hay chưa. | Owner Affiliate xác nhận cơ sở tính |

## Điểm không phải mâu thuẫn nhưng cần lưu ý

- **Dữ liệu mẫu Excel:** ô Ghi chú dòng 1 (Sản phẩm A) ghi "Affiliate = 80.000 × 37,5% = 30.000", trong khi cùng dòng giá hội viên là 800.000 và chiết khấu 40% = 320.000. Đây là ví dụ lấy từ phần VÍ DỤ, không khớp số liệu dòng. Dữ liệu minh họa nên không thành KU.
- **Ngày văn bản:** hợp đồng mẫu ghi ngày 24 tháng 07 năm 2026, tên file và phụ lục ghi 11.11.2026. Không đủ căn cứ để đặt `effective_window`; mọi record giữ `missing_effective_date`.
- **Mở shop:** văn bản (8 mục) và tờ rơi (7 mục thông tin cộng điều kiện bắt buộc) không mâu thuẫn. Tờ rơi đặt giấy tờ sản phẩm ở phần điều kiện bắt buộc.
