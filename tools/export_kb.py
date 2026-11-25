"""Tác giả: PM - TKC. Tạo catalog và gói nạp Project từ candidate KU trong kb-workspace.

Chỉ dùng thư viện chuẩn. Không ghi vào kho, không tự đặt trạng thái APPROVED:
- Luôn tạo gói DRAFT (project/kb-draft) chỉ để nạp Project thử nghiệm.
- Chỉ tạo gói vận hành (project/kb) khi có file phê duyệt do người duyệt ghi (--approvals),
  và chỉ gồm các dòng decision=APPROVED. KU có cờ conflict cần conflict_resolved=yes, hoặc =hoan kèm mã ở cột mau_thuan_chua_quyet
  (vẫn nạp nhưng gắn nhãn mâu thuẫn, không được kết luận phần đó).
"""
import argparse
import csv
import json
import re
import sys
from pathlib import Path

GROUPS = {
    'checklist-mo-shop': ('Checklist hồ sơ và giấy tờ mở shop', ['001:c0001', '002:c0002', '002:c0004']),
    'chinh-sach-nha-ban': ('Chính sách nhà bán: mô hình F2C, quy định cơ bản, thông điệp phí', ['001:c0021', '002:c0001', '002:c0010']),
    'app-cms': ('Hướng dẫn App Nhà Bán và CMS', ['001:c0019', '002:c0005', '002:c0006', '002:c0007', '002:c0008']),
    'don-hang-thanh-toan': ('Đơn hàng, thanh toán, đối soát, đổi trả', ['001:c0006', '001:c0007', '001:c0008', '002:c0009', '002:c0011', '002:c0012']),
    'hop-dong': ('Hợp đồng hợp tác và phụ lục', ['001:c0002', '001:c0003', '001:c0004', '001:c0005', '001:c0009', '001:c0010', '001:c0011', '002:c0003']),
    'affiliate': ('Chiết khấu Affiliate', ['001:c0012', '001:c0013', '001:c0014', '001:c0015', '001:c0016', '001:c0017', '001:c0018', '002:c0013']),
}
GROUP_OF = {i: g for g, (_, ids) in GROUPS.items() for i in ids}
CONFLICT_TOPICS = {
    'CF-01': 'thời điểm đổi giá bán hoặc tỷ lệ Affiliate có hiệu lực',
    'CF-02': 'ngày đối soát và ngày chi trả hoa hồng Affiliate',
    'CF-03': 'cơ sở tính chiết khấu Affiliate',
    'CF-04': 'xử lý khi nhà bán vi phạm, gỡ sản phẩm, khóa gian hàng',
    'CF-05': 'số ngày chờ thanh toán tiền hàng',
    'CF-06': 'các loại phí nhà bán chịu; không gửi nhà bán câu “0 phí trung gian”',
}
BANNER_DRAFT = ('> **DRAFT – CHỈ NẠP PROJECT THỬ NGHIỆM (dữ liệu mô phỏng).** Gói này cố ý ghi mọi KU là DRAFT để kiểm hành vi; trạng thái duyệt thật xem gói vận hành. '
                'Không dùng để trả lời nhà bán thật; không nạp vào Project vận hành.\n')
BANNER_OK = ('> **Chỉ gồm KU đã APPROVED theo file phê duyệt.** Còn hiệu lực và đúng phạm vi mới được dùng; xem giao thức truy xuất trong knowledge-base-index. KU chưa ghi ngày hiệu lực được dùng từ ngày duyệt (quy tắc pilot). '
             'KU có nhãn MÂU THUẪN CHƯA QUYẾT: không kết luận phần đang mâu thuẫn.\n')


def parse(path):
    text = path.read_text(encoding='utf-8').replace('\r\n', '\n')
    _, head, body = text.split('---', 2)
    meta, refs = {}, []
    for line in head.splitlines():
        if line.startswith('  - '):
            refs.append(json.loads(line[4:]))
        elif line and not line.startswith(' ') and ': ' in line:
            key, value = line.split(': ', 1)
            meta[key] = json.loads(value)
    sections = {}
    for chunk in re.split(r'^## ', body, flags=re.M)[1:]:
        title, _, content = chunk.partition('\n')
        sections[title.strip()] = content.strip()
    meta['refs'] = refs
    meta['sections'] = sections
    meta['title'] = meta.get('title', '')
    return meta


def load(workspace):
    latest = {}
    for path in Path(workspace).glob('SIM-BATCH-*/r*/candidates/c*.md'):
        meta = parse(path)
        short = meta['batch_id'].rsplit('-', 1)[1]
        meta['key'] = f"{short}:{meta['client_record_id']}"
        meta['batch_id_short'] = short
        meta['size'] = len(path.read_text(encoding='utf-8'))
        # Mỗi KU chỉ lấy revision mới nhất.
        if meta['key'] not in latest or meta['revision'] > latest[meta['key']]['revision']:
            latest[meta['key']] = meta
    return [latest[key] for key in sorted(latest)]


def read_sources(workspace):
    """Sổ nguồn: source_id -> ngày xác nhận, chỉ các tài liệu nguồn APPROVED. Không ảnh hưởng trạng thái KU."""
    path = Path(workspace) / 'so-nguon.csv'
    if not path.exists():
        return {}
    with open(path, encoding='utf-8-sig', newline='') as f:
        return {r['source_id']: r['ngay_xac_nhan'] for r in csv.DictReader(f)
                if r['trang_thai_nguon'] == 'APPROVED' and r['ngay_xac_nhan']}


def scope_text(meta):
    facets = {k: v for k, v in meta['scope']['facets'].items() if v is not None}
    return json.dumps(facets, ensure_ascii=False) if facets else 'chưa xác nhận'


def render(meta, approval=None, sources=None):
    s = meta['sections']
    lines = [f"### {meta['key']} — {meta['title']}"]
    if approval:
        state = 'APPROVED (còn mâu thuẫn chưa quyết)' if approval.get('conflict') else 'APPROVED'
        lines.append(f"- Trạng thái: {state}; người duyệt {approval['approver']}; ngày duyệt {approval['approved_at']}; hiệu lực từ {approval['effective_from'] or 'chưa ghi'}")
        if approval.get('conflict'):
            code = approval['conflict']
            others = ', '.join(approval.get('related', [])) or 'mâu thuẫn nằm trong chính KU này'
            lines.append(f"- **MÂU THUẪN CHƯA QUYẾT {code}: {CONFLICT_TOPICS[code]}.** Với đúng nội dung này: không kết luận, không gửi nhà bán; "
                         f"nêu các nguồn đang khác nhau (KU liên quan: {others}), ghi “Chưa có căn cứ xác nhận” và chuyển Bắc. Phần khác của KU được dùng.")
    else:
        lines.append('- Trạng thái: DRAFT (chưa duyệt)')
    lines.append(f"- Phiên bản candidate: r{meta['revision']}")
    lines.append(f"- Loại: {meta['layer']}/{meta['authority_type_proposed']}; đối tượng: {', '.join(meta['audience_proposed'])}; phạm vi: {scope_text(meta)}")
    refs = '; '.join(f"{r['source_id']} ({r['doc_version']}, {r['locator']})" for r in meta['refs'])
    lines.append(f"- Nguồn: {refs}")
    ids = [r['source_id'] for r in meta['refs']]
    if sources and ids and all(i in sources for i in ids):
        lines.append(f"- Tài liệu nguồn: đã duyệt (xác nhận {max(sources[i] for i in ids)}); trạng thái KU ghi ở dòng Trạng thái")
    else:
        lines.append('- Tài liệu nguồn: chưa ghi nhận duyệt trong sổ nguồn')
    flags = list(meta.get('flags', []))
    if approval and approval['effective_from'] and 'missing_effective_date' in flags:
        flags.remove('missing_effective_date')
    if flags:
        lines.append(f"- Cờ: {', '.join(flags)}")
    if meta.get('relations_proposed'):
        rel = '; '.join(f"{r['type']} {r['target'].replace('SIM-BATCH-', '')}" for r in meta['relations_proposed'])
        lines.append(f"- Quan hệ: {rel}")
    for name in ('Điều kiện', 'Nội dung', 'Ngoại lệ', 'Chứng từ'):
        if name in s:
            lines += ['', f'**{name}**', s[name]]
    note = s.get('Ghi chú cho người duyệt (không phải nội dung KU)')
    if note:
        lines += ['', f'> Ghi chú cho người duyệt (không dùng để trả lời nhà bán): {note}']
    return '\n'.join(lines) + '\n'


def status_text(approvals, key):
    if not approvals:
        return 'DRAFT'
    code = approvals[key].get('conflict')
    return f'APPROVED, mâu thuẫn {code} chưa quyết' if code else 'APPROVED'


def write_pack(out_dir, items, banner, approvals=None, sources=None):
    out_dir.mkdir(parents=True, exist_ok=True)
    chosen = [m for m in items if m['key'] in GROUP_OF and (approvals is None or m['key'] in approvals)]
    for old in out_dir.glob('*.md'):
        old.unlink()
    rows = ['| ID tạm | Tiêu đề | Loại | Phạm vi | Hiệu lực | est_tokens | Trạng thái | Cờ | Tệp |', '|---|---|---|---|---|---|---|---|---|']
    for group, (name, ids) in GROUPS.items():
        members = [m for m in chosen if m['key'] in ids]
        if not members:
            continue
        body = [f'# {name}', '', banner]
        for m in members:
            body += [render(m, approvals.get(m['key']) if approvals else None, sources), '']
        (out_dir / f'{group}.md').write_text('\n'.join(body), encoding='utf-8', newline='\n')
        for m in members:
            window = m['effective_window_proposed']
            eff = approvals[m['key']]['effective_from'] if approvals else (window.get('from') or 'chưa có')
            rows.append(f"| {m['key']} | {m['title']} | {m['layer']}/{m['authority_type_proposed']} | {scope_text(m)} | {eff or 'chưa ghi'} | "
                        f"{m['size'] // 3} | {status_text(approvals, m['key'])} | {', '.join(f for f in m.get('flags', []) if f in ('conflict', 'ocr_low'))} | {group}.md |")
    head = ['# Danh mục KU', '', banner, f'Số KU: {len(rows) - 2}. est_tokens ≈ số ký tự / 3 của file candidate.', '']
    (out_dir / 'catalog.md').write_text('\n'.join(head + rows) + '\n', encoding='utf-8', newline='\n')
    return len(rows) - 2


def read_approvals(path, items):
    by_key = {m['key']: m for m in items}
    approved, skipped = {}, []
    with open(path, encoding='utf-8-sig', newline='') as f:
        for row in csv.DictReader(f):
            key = f"{row['batch_id'].rsplit('-', 1)[-1]}:{row['client_record_id']}"
            if row.get('decision', '').strip().upper() != 'APPROVED' or key not in by_key:
                continue
            if not row.get('approver', '').strip() or not row.get('approved_at', '').strip():
                skipped.append((key, 'thiếu approver hoặc approved_at'))
            elif row.get('revision', '').strip().lstrip('r') != str(by_key[key]['revision']):
                skipped.append((key, f"phê duyệt không đúng phiên bản hiện hành r{by_key[key]['revision']}"))
            else:
                entry = {'approver': row['approver'].strip(), 'approved_at': row['approved_at'].strip(),
                         'effective_from': row.get('effective_from', '').strip()}
                if 'conflict' in by_key[key].get('flags', []):
                    resolved = row.get('conflict_resolved', '').strip().lower()
                    code = (row.get('mau_thuan_chua_quyet') or '').strip()
                    if resolved == 'hoan' and code in CONFLICT_TOPICS:
                        entry['conflict'] = code
                    elif resolved != 'yes':
                        skipped.append((key, 'có cờ conflict, cần conflict_resolved=yes, hoặc =hoan kèm mã mâu thuẫn'))
                        continue
                approved[key] = entry
    for key, entry in approved.items():
        if entry.get('conflict'):
            entry['related'] = sorted(k for k, e in approved.items() if k != key and e.get('conflict') == entry['conflict'])
    return approved, skipped


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--workspace', default='kb-workspace/ai-seller-onboarding')
    parser.add_argument('--out', default='project')
    parser.add_argument('--approvals', help='CSV phê duyệt do người duyệt ghi (mẫu: templates/phe-duyet-ku.csv)')
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    items = load(args.workspace)
    sources = read_sources(args.workspace)
    out = Path(args.out)
    print(f'Đọc {len(items)} candidate.')
    print(f"kb-draft: {write_pack(out / 'kb-draft', items, BANNER_DRAFT, sources=sources)} KU (chỉ Project thử nghiệm)")
    if args.approvals:
        approved, skipped = read_approvals(args.approvals, items)
        for key, why in skipped:
            print(f'Bỏ qua {key}: {why}', file=sys.stderr)
        if not any(key in GROUP_OF for key in approved):
            # write_pack xoá tệp cũ trước khi ghi: không để phiếu trống hoặc sai làm mất gói vận hành.
            print('Phiếu duyệt không có KU APPROVED hợp lệ nào: giữ nguyên project/kb, không ghi gì vào gói vận hành.', file=sys.stderr)
            return 2
        print(f"kb: {write_pack(out / 'kb', items, BANNER_OK, approved, sources)} KU APPROVED")
    else:
        print('Không có --approvals: không tạo gói vận hành (project/kb).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
