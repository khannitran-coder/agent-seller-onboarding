"""Tác giả: PM - TKC. Kiểm hook và gói plugin. Mọi giá trị trong tệp là giả. Không kiểm hành vi mô hình."""
import json
import subprocess
import sys
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GUARD = ROOT/'plugin/hooks/guard.py'
FINAL = 'Cần người duyệt trước khi gửi/lưu: Có'
GOOD = '\n'.join(['- Tình trạng: Chưa xác minh', '- Thiếu/vướng: nguồn', '- Việc cần làm: kiểm', '- Ai làm: nhân viên',
                  '- Hạn: Chưa xác nhận', '- Khi nào chuyển cấp: thiếu nguồn', '- Nguồn (tài liệu + phiên bản): Chưa có căn cứ xác nhận',
                  '', FINAL])


def run(mode, payload):
    raw = payload if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False)
    result = subprocess.run([sys.executable, str(GUARD), mode], input=raw.encode('utf-8'), capture_output=True)
    return result.returncode, json.loads(result.stdout) if result.stdout.strip() else None


class PromptTests(unittest.TestCase):
    def test_blocks_secret_values_without_echo(self):
        for prompt, secret in [('Nhà bán nhắn mật khẩu: Gia@dinh99', 'Gia@dinh99'), ('mã OTP là 482913', '482913'),
                               ('mk=abc12345', 'abc12345'), ('khoá sk-abcdefghijklmnop1234', 'abcdefghijklmnop1234')]:
            code, out = run('prompt', {'prompt': prompt})
            self.assertEqual((code, out['decision']), (0, 'block'), prompt)
            self.assertNotIn(secret, out['reason'])

    def test_allows_labels_and_stage_one_data(self):
        for prompt in ['Nhà bán gửi [token mô phỏng], soạn tin phản hồi', 'Quy định về mật khẩu và OTP là gì?',
                       'Số tài khoản công ty: 0123456789, CCCD 012345678901', 'OTP bị chặn từ ngày 2026-11-25']:
            self.assertEqual(run('prompt', {'prompt': prompt}), (0, None), prompt)

    def test_unreadable_input_blocks(self):
        self.assertEqual(run('prompt', 'không phải json')[0], 2)


class ToolTests(unittest.TestCase):
    def test_denies_writes_and_browser(self):
        for name in ['mcp__abc__create_file', 'mcp__abc__slack_send_message', 'mcp__gmail__createDraft', 'mcp__x__trash_file',
                     'mcp__claude-in-chrome__navigate', 'mcp__computer-use__screenshot']:
            out = run('tool', {'tool_name': name})[1]
            self.assertEqual(out['hookSpecificOutput']['permissionDecision'], 'deny', name)

    def test_allows_reads_and_local_tools(self):
        for name in ['mcp__abc__read_file_content', 'mcp__abc__search_files', 'mcp__workspace__bash', 'Read', 'Bash', 'Write']:
            self.assertEqual(run('tool', {'tool_name': name}), (0, None), name)


class StopTests(unittest.TestCase):
    def test_accepts_contract_and_plain_chat(self):
        for message in [GOOD, GOOD.replace('Tình trạng', '**Tình trạng**'), 'Chào bạn.', 'Số tài khoản: 4 số cuối 6789']:
            self.assertEqual(run('stop', {'last_assistant_message': message}), (0, None), message)

    def test_blocks_broken_contract_and_full_numbers(self):
        for message in [GOOD.replace(FINAL, ''), GOOD.replace('- Hạn: Chưa xác nhận\n', ''), 'STK: 0123 4567 8901', 'CCCD 012345678901']:
            out = run('stop', {'last_assistant_message': message})[1]
            self.assertEqual(out['decision'], 'block', message)
            self.assertNotIn('012345678901', out['reason'])

    def test_no_loop(self):
        self.assertEqual(run('stop', {'stop_hook_active': True, 'last_assistant_message': 'CCCD 012345678901'}), (0, None))


class PackageTests(unittest.TestCase):
    def test_both_variants(self):
        for variant, name in [('prod', 'hi1-seller-onboarding'), ('test', 'hi1-seller-onboarding-test')]:
            subprocess.run([sys.executable, str(ROOT/'tools/build_plugin.py'), '--variant', variant], check=True, capture_output=True)
            version = json.loads((ROOT/'plugin/.claude-plugin/plugin.json').read_text(encoding='utf-8'))['version']
            with zipfile.ZipFile(ROOT/'dist'/f'{name}-{version}.zip') as archive:
                names = set(archive.namelist())
                manifest = json.loads(archive.read('.claude-plugin/plugin.json'))
                catalog = archive.read('skills/seller-onboarding/references/kb/catalog.md').decode('utf-8')
            self.assertEqual(manifest['name'], name)
            for needed in ['agents/output-checker.md', 'hooks/hooks.json', 'hooks/guard.py',
                           'skills/seller-onboarding/SKILL.md', 'skills/seller-onboarding/references/instructions.md',
                           'skills/seller-onboarding/references/trang-thai.md', 'skills/seller-onboarding/references/phieu-chuyen-cap.md']:
                self.assertIn(needed, names)
            self.assertEqual(sum(n.startswith('skills/') and n.endswith('/SKILL.md') for n in names), 9)
            with zipfile.ZipFile(ROOT/'dist'/f'{name}-{version}.zip') as archive:
                for draft in ['seller-cms-entry', 'seller-contract-draft']:
                    text = archive.read(f'skills/{draft}/SKILL.md').decode('utf-8')
                    self.assertIn('BẢN NHÁP', text, draft)
                    self.assertIn('Dừng – skill chưa được phép dùng', text, draft)
            self.assertEqual('| DRAFT |' in catalog, variant == 'test')


class ReleaseTests(unittest.TestCase):
    def test_committed_plugins_match_sources(self):
        """plugins/ được commit nên phải khớp bản đóng gói mới; lệch thì chạy build_plugin.py --release."""
        def snapshot(folder):
            return {f.relative_to(folder).as_posix(): f.read_bytes().replace(b'\r\n', b'\n')
                    for f in folder.rglob('*') if f.is_file() and '__pycache__' not in f.parts}

        listed = json.loads((ROOT/'.claude-plugin/marketplace.json').read_text(encoding='utf-8'))['plugins']
        self.assertEqual([p['name'] for p in listed], ['hi1-seller-onboarding', 'hi1-seller-onboarding-test'])
        for variant, entry in zip(['prod', 'test'], listed):
            subprocess.run([sys.executable, str(ROOT/'tools/build_plugin.py'), '--variant', variant], check=True, capture_output=True)
            committed = snapshot(ROOT/entry['source'])
            self.assertEqual(committed, snapshot(ROOT/'dist/plugin'/entry['name']), entry['name'])
            self.assertEqual(entry['version'], json.loads(committed['.claude-plugin/plugin.json'])['version'])
            with zipfile.ZipFile(ROOT/'releases'/f"{entry['name']}-{entry['version']}.zip") as archive:
                zipped = {n: archive.read(n).replace(b'\r\n', b'\n') for n in archive.namelist()}
            self.assertEqual(committed, zipped, f"releases/{entry['name']}")


if __name__ == '__main__':
    unittest.main()
