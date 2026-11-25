"""Tác giả: PM - TKC. Ghép plugin/, skills/, instructions và gói tri thức thành zip plugin. Không cài hay tải lên.

Nguồn duy nhất vẫn là skills/, project/ và plugin/; dist/ là đầu ra sinh lại được.
--release ghi thêm plugins/ và .claude-plugin/marketplace.json để Claude đồng bộ thẳng từ repo. skills-draft/ không bao giờ được đóng gói.
"""
import argparse
import json
import shutil
import sys
import zipfile
from pathlib import Path

import build_skills

ROOT = build_skills.ROOT
IGNORE = shutil.ignore_patterns('__pycache__', '*.pyc')


MARKETPLACE = 'hi1-noi-bo'


def build(variant):
    _, issues = build_skills.check()
    if issues:
        raise SystemExit('\n'.join(issues))
    manifest = json.loads((ROOT/'plugin/.claude-plugin/plugin.json').read_text(encoding='utf-8'))
    kb = ROOT/'project'/('kb' if variant == 'prod' else 'kb-draft')
    if variant == 'test':
        manifest['name'] += '-test'
        manifest['description'] = 'CHỈ THỬ NGHIỆM với dữ liệu mô phỏng. ' + manifest['description']
    files = sorted(kb.glob('*.md'))
    if len(files) < 2:
        raise SystemExit(f'Thiếu gói tri thức trong {kb.relative_to(ROOT).as_posix()}: chạy tools/export_kb.py trước.')

    out = ROOT/'dist'/'plugin'/manifest['name']
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(ROOT/'plugin', out, ignore=IGNORE)
    for folder in sorted((ROOT/'skills').iterdir()):
        if folder.is_dir() and folder.name != '__pycache__':
            shutil.copytree(folder, out/'skills'/folder.name, ignore=IGNORE)
    references = out/'skills'/'seller-onboarding'/'references'
    (references/'kb').mkdir(parents=True)
    shutil.copyfile(ROOT/'project/claude-project-instructions.md', references/'instructions.md')
    for file in files:
        shutil.copyfile(file, references/'kb'/file.name)
    # Hai tệp instructions dẫn tới.
    shutil.copyfile(ROOT/'docs/06-trang-thai.md', references/'trang-thai.md')
    shutil.copyfile(ROOT/'templates/phieu-chuyen-cap.md', references/'phieu-chuyen-cap.md')
    (out/'.claude-plugin/plugin.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')

    archive_path = ROOT/'dist'/f"{manifest['name']}-{manifest['version']}.zip"
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as archive:
        for file in sorted(out.rglob('*')):
            if file.is_file():
                archive.write(file, file.relative_to(out).as_posix())
    return out, archive_path


def release():
    """Chép hai bản đã đóng gói vào plugins/ và ghi danh mục marketplace. Cả hai được commit vào repo."""
    entries = []
    for variant in ('prod', 'test'):
        out, _ = build(variant)
        target = ROOT/'plugins'/out.name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(out, target)
        manifest = json.loads((target/'.claude-plugin/plugin.json').read_text(encoding='utf-8'))
        entries.append({'name': manifest['name'], 'source': f"./plugins/{manifest['name']}",
                        'description': manifest['description'], 'version': manifest['version']})
    marketplace = {'name': MARKETPLACE, 'description': 'Agent Seller Onboarding của Hi1 (nội bộ).',
                   'owner': {'name': 'PM - TKC'}, 'plugins': entries}
    path = ROOT/'.claude-plugin/marketplace.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(marketplace, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    return entries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--variant', choices=['prod', 'test'], default='prod',
                        help='prod dùng project/kb (đã duyệt); test dùng project/kb-draft, chỉ dữ liệu mô phỏng')
    parser.add_argument('--release', action='store_true', help='ghi cả hai bản vào plugins/ và marketplace.json')
    args = parser.parse_args()
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8')
    if args.release:
        for entry in release():
            print(f"{entry['source']} {entry['version']}")
        return 0
    out, archive_path = build(args.variant)
    print(f'Thư mục: {out.relative_to(ROOT).as_posix()}')
    print(f'Zip: {archive_path.relative_to(ROOT).as_posix()}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
