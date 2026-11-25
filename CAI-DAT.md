# Cài Agent Seller Onboarding lên tài khoản Claude doanh nghiệp

v0.3.0 – pilot, chưa COO duyệt. Dành cho Owner hoặc admin của tổ chức Claude (Team/Enterprise). Tên menu theo tài liệu hỗ trợ của Claude tra ngày 25/11/2026 ([quản lý plugin cho tổ chức](https://support.claude.com/en/articles/13837433-manage-claude-cowork-plugins-for-your-organization)); giao diện khác thì theo giao diện và ghi lại.

Repo này có nội dung hợp đồng và quy định nội bộ, nên để **Private**. Đồng bộ plugin từ GitHub (bước 2, cách A) chỉ nhận repo Private hoặc internal; khi repo chưa ở chế độ đó, dùng cách B.

## Trong repo có gì

| Cần khi cài | Ở đâu |
|---|---|
| Plugin vận hành (KU đã duyệt) | `plugins/hi1-seller-onboarding/` |
| Plugin thử nghiệm (KU DRAFT, chỉ dữ liệu mô phỏng) | `plugins/hi1-seller-onboarding-test/` |
| Danh mục để Claude đồng bộ | `.claude-plugin/marketplace.json` |
| Zip để tải lên thủ công | `releases/` |
| Kiểm khói và cổng Chạy/Không chạy | [docs/14](docs/14-trien-khai-cowork.md) |
| 14 ca pilot và mẫu ghi kết quả | [test-cases](tests/test-cases.md), [mẫu](templates/ket-qua-kiem-thu.csv), dữ liệu ở `tests/sim/` |
| Tracker và nhật ký AI | [header 26 cột](templates/tracker-header.csv), [header nhật ký](templates/nhat-ky-ai-header.csv) |
| Hướng dẫn nhân viên và sự cố | [SOP](docs/07-sop-nhan-vien.md), [xử lý sự cố](docs/09-xu-ly-su-co.md) |
| Mã nguồn để sửa | `plugin/`, `skills/`, `project/`, `kb-workspace/`, `tools/` |

Phiếu duyệt KU đang dùng: `phe-duyet-ku-pilot-2026-11-25-r2.csv` ở gốc repo, ghi vai trò người duyệt, không ghi tên cá nhân. Đưa vào repo này theo quyết định của người dùng ngày 25/11/2026, là ngoại lệ so với quy tắc lưu nội bộ; phiếu có tên người duyệt thì không commit. Sinh lại gói tri thức: `python tools/export_kb.py --approvals phe-duyet-ku-pilot-2026-11-25-r2.csv`.

## Bước 1. Bật tính năng

Organization settings > Plugins & skills, tab Policy: bật Cowork, Skills và code execution.

## Bước 2. Đưa plugin vào tổ chức

Cách A, đồng bộ từ repo (nên dùng):

1. Cài Claude GitHub App cho đúng repo này.
2. Organization settings > Plugins & skills > tab Marketplaces > Add plugins > Sync from GitHub, nhập `<chủ repo>/<tên repo>`.
3. Kiểm thấy hai plugin phiên bản 0.3.0.

Cách B, tải zip (không cần Python):

1. Trên GitHub mở thư mục [releases](releases/), mở `hi1-seller-onboarding-test-0.3.0.zip`, bấm Download raw file. Không dùng nút Code > Download ZIP: đó là cả repo, không phải plugin. Không giải nén.
2. Organization settings > Plugins & skills > Add > Upload a plugin.
3. Bản vận hành `hi1-seller-onboarding-0.3.0.zip` tải tương tự, sau khi bản test đạt.

## Bước 3. Cấp quyền

Với từng plugin, tab Inventory > menu > Default access > Install:

- Toàn tổ chức: “Not available”, rồi cấp cho nhóm pilot bằng Group access (Enterprise). Gói Team: “Available to install” và chỉ người pilot cài.
- Không dùng “Installed by default” hoặc “Required”.
- Người pilot chỉ bật MỘT trong hai bản. Hooks chặn gửi/ghi qua connector ở mọi tác vụ khi plugin đang bật.
- Không bật connector ghi; tracker cấp quyền chỉ xem cho Claude.

## Bước 4. Kiểm khói và kiểm thử

1. Bật bản test, chạy dòng 1–7 ở [docs/14 mục 5](docs/14-trien-khai-cowork.md). Dòng 1–3 không đạt thì dừng: lớp chặn không hoạt động.
2. Chạy 14 ca pilot, ghi vào bản sao của mẫu kết quả, lưu ngoài repo.

## Bước 5. Chuẩn bị vận hành

1. Tạo tracker từ hai header CSV (tracker và tab nhật ký AI), giao người giữ.
2. Người pilot đọc SOP; chốt người ghi sự cố và kênh chuyển cấp.
3. Kiểm các điều kiện bắt buộc ở [docs/13](docs/13-dieu-kien-chay-thu-ho-so-that.md) và ghi ngày bắt đầu mới.

## Bước 6. Chạy thật

Tắt bản test, bật bản vận hành, chạy dòng 8–11 ở docs/14 mục 5. Đạt hết mới nhận hồ sơ thật.

## Việc còn mở

- CF-01 (hiệu lực đổi giá hoặc tỷ lệ Affiliate) chưa quyết.
- Phụ lục Affiliate (Điều 3, Điều 5.4), Sổ tay (ngày thanh toán) và tờ rơi (“0 phí trung gian”) chưa sửa theo quyết định 25/11/2026.
- Chưa có nguồn cho điều kiện duyệt nhà bán, ngành hàng cấm, trạng thái CMS, SLA, biểu phí thanh toán.
- Hooks chưa được xác minh trên Cowork.

## Cập nhật sau này

Sửa nguồn → `python tools/build_skills.py --check` → tăng `version` trong `plugin/.claude-plugin/plugin.json` → `python tools/build_plugin.py --release` → `python -m unittest discover -s tests/plugin` → commit cả `plugins/`, `releases/`, `.claude-plugin/` → mở PR và merge vào nhánh mặc định. Đồng bộ tự động chỉ chạy khi merge PR có tăng version; đẩy thẳng thì bấm đồng bộ lại.
