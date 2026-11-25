"""Tác giả: PM - TKC. Hook chặn của plugin: prompt | tool | stop.

Lớp bổ sung cho instructions, không thay người duyệt. Giới hạn: chỉ thấy chữ trong prompt (không đọc tệp
đính kèm), nhận diện theo mẫu nên có thể sót, và chỉ có tác dụng khi môi trường chạy được hook và Python.
Không bao giờ in lại giá trị bị phát hiện. Chỉ dùng thư viện chuẩn.
"""
import json
import re
import sys
import unicodedata

FINAL_LINE = 'Cần người duyệt trước khi gửi/lưu: Có'
CONTRACT = ['Tình trạng', 'Thiếu/vướng', 'Việc cần làm', 'Ai làm', 'Hạn', 'Khi nào chuyển cấp', 'Nguồn (tài liệu + phiên bản)']

SECRETS = [
    ('mật khẩu', r'(?:mật\s*khẩu|mat\s*khau|password|passwd|\bpass\b|\bmk\b)\s*(?:là|:|=)\s*(?=\S*[\d!@#$%^&*])\S{4,}'),
    ('OTP', r'(?:\botp\b|mã\s+xác\s+(?:thực|nhận|minh))[^\d\n]{0,20}(?<!\d)\d{4,8}(?![\d/\-])'),
    ('token hoặc khóa API', r'\bsk-[A-Za-z0-9_\-]{16,}|\bAKIA[0-9A-Z]{16}\b|\bgh[pousr]_[A-Za-z0-9]{20,}'
                            r'|\beyJ[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}|\bbearer\s+[A-Za-z0-9._\-]{20,}'
                            r'|-----BEGIN [A-Z ]*PRIVATE KEY-----'
                            r'|(?:api[ _\-]?key|access[ _\-]?token|\btoken\b|secret)\s*(?:là|:|=)\s*(?=\S*\d)[A-Za-z0-9._\-]{12,}'),
]
ID_NUMBER = r'(?:cccd|căn\s+cước|số\s+tài\s+khoản|\bstk\b)[^\d\n]{0,40}(?:\d[ .\-]?){8,}\d'

# Server nội bộ của môi trường chạy agent: không phải connector ra ngoài. Xác nhận tên thật khi kiểm thử trên Cowork.
INTERNAL_SERVERS = {'cowork', 'workspace', 'visualize', 'plugins', 'skills', 'mcp-registry'}
BROWSER_SERVERS = re.compile(r'chrome|browser|computer', re.I)
WRITE_VERBS = {'add', 'append', 'archive', 'batch', 'copy', 'create', 'delete', 'draft', 'edit', 'insert', 'invite', 'modify',
               'move', 'post', 'publish', 'remove', 'reply', 'schedule', 'send', 'set', 'share', 'submit', 'trash', 'update',
               'upload', 'write'}


def normalize(text):
    return unicodedata.normalize('NFC', text)


def find_secrets(text):
    text = normalize(text)
    return [name for name, pattern in SECRETS if re.search(pattern, text, re.I)]


def check_prompt(data):
    found = find_secrets(str(data.get('prompt', '')))
    if found:
        return {'decision': 'block', 'reason': (
            f"Đã chặn: tin nhắn có dấu hiệu chứa {', '.join(found)}. Không đưa loại dữ liệu này vào AI. "
            'Xoá khỏi nội dung, đổi giá trị đã lộ và báo người phụ trách ghi sự cố (chỉ ghi mã hồ sơ và loại sự cố).')}
    return None


def denied_tool(name):
    parts = name.split('__')
    if len(parts) < 3 or parts[0] != 'mcp':
        return False
    server, action = parts[1], parts[-1]
    if BROWSER_SERVERS.search(server):
        return True
    if server.lower() in INTERNAL_SERVERS:
        return False
    words = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', action)
    return any(word.lower() in WRITE_VERBS for word in re.split(r'[^A-Za-z0-9]+', words))


def check_tool(data):
    if denied_tool(str(data.get('tool_name', ''))):
        return {'hookSpecificOutput': {'hookEventName': 'PreToolUse', 'permissionDecision': 'deny', 'permissionDecisionReason': (
            'Pilot mức tự chủ 3: AI không gửi, ghi, sửa, xoá qua connector và không điều khiển trình duyệt hay máy tính. '
            'Trả bản nháp để người thực hiện.')}}
    return None


def output_issues(message):
    text = normalize(message)
    issues = []
    if re.search(ID_NUMBER, text, re.I):
        issues.append('có vẻ lặp đầy đủ số CCCD hoặc số tài khoản; thay bằng “đã nhận” hoặc 4 số cuối')
    if find_secrets(text):
        issues.append('có dấu hiệu lặp mật khẩu, OTP hoặc token; xoá giá trị')
    plain = text.replace('*', '')
    if re.search(r'^\s*(?:[-#]+\s*)?Tình trạng\s*:', plain, re.M):
        missing = [field for field in CONTRACT if not re.search(rf'^\s*(?:[-#]+\s*)?{re.escape(field)}\s*:', plain, re.M)]
        if missing:
            issues.append('thiếu mục output contract: ' + ', '.join(missing))
        if not plain.rstrip().endswith(FINAL_LINE):
            issues.append(f'dòng cuối phải đúng là “{FINAL_LINE}”')
    return issues


def check_stop(data):
    if data.get('stop_hook_active'):
        return None  # Đã yêu cầu sửa một lần; không lặp vô hạn.
    issues = output_issues(str(data.get('last_assistant_message') or ''))
    if issues:
        return {'decision': 'block', 'reason': 'Viết lại câu trả lời, không lặp giá trị nhạy cảm: ' + '; '.join(issues) + '.'}
    return None


def main():
    checks = {'prompt': check_prompt, 'tool': check_tool, 'stop': check_stop}
    mode = sys.argv[1] if len(sys.argv) > 1 else ''
    if mode not in checks:
        print('guard.py: cần tham số prompt, tool hoặc stop', file=sys.stderr)
        return 2
    raw = sys.stdin.buffer.read().decode('utf-8', errors='replace')
    try:
        data = json.loads(raw) if raw.strip() else {}
        if not isinstance(data, dict):
            raise ValueError('không phải đối tượng JSON')
    except ValueError:
        print('guard.py: không đọc được input của hook', file=sys.stderr)
        return 2  # Chặn khi không kiểm được.
    result = checks[mode](data)
    if result:
        print(json.dumps(result))  # ASCII để không phụ thuộc mã hoá của console.
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
