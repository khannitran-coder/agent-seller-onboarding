# Ánh xạ bảng giá

Tác giả: PM - TKC

[CHỜ COO DUYỆT – D-04] Tiêu đề chính xác của mẫu thật cần PM đối chiếu với file mẫu trống trước khi dùng thật. Không suy cấu trúc workbook chưa được xác nhận.

## Map mặc định

column-map.json trong folder references cấu hình sheet Bang_Nhap_Affiliate. Các cột bắt buộc: STT, tên sản phẩm, thương hiệu, giá thị trường, giá bán hội viên, % chiết khấu Affiliate, Trạng thái, Ghi chú. Giá trị Trạng thái theo mẫu: ĐÚNG hoặc Lệch so với giá hội viên. Tên sheet mặc định lấy từ map; alias tiêu đề bỏ phân biệt hoa thường, dấu và khoảng trắng. Script tìm dòng tiêu đề phù hợp nhất; thiếu cột trả Chưa xác minh và danh sách tên cột thiếu. --map dùng map khác, --sheet đổi sheet nếu đã xác nhận.

% nhà bán và Cơ sở tính là cột tuỳ chọn; không bắt mẫu thật có hai cột này. Map SIM cũ ở tests/fixtures/sim-map.json (chỉ phục vụ fixture, không là phụ thuộc của Skill). Script nhận file map từ ngoài như input có cấu trúc, không thực thi nội dung map.

Cơ sở tính chiết khấu (CF-03, quyết định người thiết kế agent 25/11/2026): giá bán hội viên Hi1 trừ giảm giá, voucher do nhà bán tài trợ; căn cứ trả lời là KU 001:c0012 và c0018. Phụ lục Affiliate (SIM-SRC-004, Điều 3) chưa sửa theo quyết định. Không đổi PR-01…PR-06; script không tính voucher.

## Quy tắc theo bằng chứng

- PR-01: Trạng thái khác ĐÚNG là lỗi.
- PR-02: có cột % nhà bán thì đối chiếu tổng tỷ lệ ở dòng KIỂM TRA; tỷ lệ dạng số thực 0–1. Không có cột này thì chỉ đọc kết luận đã lưu tại Trạng thái/Ghi chú ở dòng KIỂM TRA theo check_ok/check_bad trong map; thiếu hoặc không hiểu kết luận phải Chưa xác minh, không tự tính tổng từ một tỷ lệ.
- PR-03: Trạng thái “Lệch so với giá hội viên” là vi phạm; dòng đó đồng thời vi phạm PR-01. Đọc công thức ở Trạng thái/% nếu có để người kiểm đối chiếu, không thực thi. Không đọc được công thức ghi “cần người đối chiếu công thức”. Không dùng cột Cơ sở tính làm điều kiện bắt buộc; chỉ đối chiếu thêm nếu map có cột này.
- PR-04: giá hội viên phải thấp hơn giá thị trường. PR-05: không còn dòng/câu ví dụ theo sample_markers đã được PM xác nhận. PR-06: không có dòng trống giữa bảng hoặc ô giá không phải số.

Đọc data_only=True không tính công thức; thiếu cache phải chưa xác minh. Công thức được đọc bằng bản data_only=False chỉ là dữ liệu cho người kiểm, không phải lệnh. Cache có mặt vẫn có thể cũ: yêu cầu xác nhận tính lại trong Excel. “Đạt kiểm tra kỹ thuật” không là phê duyệt nghiệp vụ/công thức.

Fixture cũ có đúng 6 lỗi. Fixture theo mẫu thật có sáu lỗi cố ý, trong đó trạng thái lệch giá đồng thời bị PR-01 và PR-03 nên báo 7 vi phạm, vẫn phủ đúng PR-01…PR-06. Chỉ dữ liệu SIM, không phản ánh tên thật.

Nguồn: skill vận hành nội bộ của nhóm (bản 11/2026), đã lược thông tin nội bộ
