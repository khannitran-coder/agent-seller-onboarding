"""Tác giả: PM - TKC. CSV chỉ đọc, không phản hồi giá trị của ô lỗi."""
import argparse
import csv
import json
import math
import re
import statistics
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def iso(value):
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:\d{2})', value):
        raise ValueError('ISO 8601 phải có giờ và múi giờ')
    return datetime.fromisoformat(value.replace('Z', '+00:00'))


def mean(values):
    return round(statistics.mean(values), 6) if values else None


def report(file, schema, as_of):
    errors, records, bad = [], [], set()
    total_rows = 0
    rules = schema['rules']
    patterns = [re.compile(v) for v in rules['suspected_red_patterns']]

    def error(line, column, reason):
        errors.append({'dòng': line, 'cột': column, 'lỗi': reason})
        bad.add(line)

    with Path(file).open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.reader(stream)
        header = next(reader, [])
        if header != schema['columns']:
            error(1, '(header)', 'Sai thứ tự, thiếu hoặc thừa cột; đối chiếu schema')
        seen = {}
        for line, cells in enumerate(reader, 2):
            total_rows += 1
            if len(cells) != len(schema['columns']):
                error(line, '(row)', 'Sai số cột')
            if header != schema['columns'] or len(cells) != len(schema['columns']):
                # Never echo malformed headers or values, but still screen all cells.
                for index, value in enumerate(cells):
                    if any(p.search(value) for p in patterns):
                        error(line, f'vị trí {index+1}', 'Nghi dữ liệu Đỏ')
                continue
            row = dict(zip(header, (v.strip() for v in cells)))
            for column, value in row.items():
                if any(p.search(value) for p in patterns):
                    error(line, column, 'Nghi dữ liệu Đỏ')
            for column in schema['required']:
                if not row[column]:
                    error(line, column, 'Thiếu giá trị bắt buộc')
            merchant = row['merchant_id']
            if merchant:
                if merchant in seen:
                    error(line, 'merchant_id', 'Mã hồ sơ trùng')
                    if seen[merchant] not in bad:
                        error(seen[merchant], 'merchant_id', 'Mã hồ sơ trùng')
                    else:
                        # Include duplicate cause even when that row has another error.
                        if not any(e['dòng'] == seen[merchant] and e['lỗi'] == 'Mã hồ sơ trùng' for e in errors):
                            error(seen[merchant], 'merchant_id', 'Mã hồ sơ trùng')
                else:
                    seen[merchant] = line
            for column, allowed in schema['enums'].items():
                value = row[column]
                parts = value.split(schema['list_columns'][column]) if column in schema['list_columns'] else [value]
                if value and any(part.strip() not in allowed for part in parts):
                    error(line, column, 'Ngoài enum')
            times = {}
            for column in schema['time_columns']:
                if row[column]:
                    try:
                        times[column] = iso(row[column])
                    except ValueError:
                        error(line, column, 'Thời gian sai ISO 8601 hoặc thiếu múi giờ')
            created, contact = times.get('created_at'), times.get('first_contact_at')
            if created and created > as_of:
                error(line, 'created_at', 'Sau thời điểm chốt')
            if created and contact and contact < created:
                error(line, 'first_contact_at', 'Trước thời điểm nhận lead')
            condition = rules['ready_condition']
            if row['ready_status'] == condition['ready_status']:
                for column in ('shop_status', 'product_status'):
                    if row[column] != condition[column]:
                        error(line, column, 'Không đủ điều kiện sẵn sàng bán')
            handling = None
            if row['handling_minutes']:
                try:
                    handling = float(row['handling_minutes'])
                    if not math.isfinite(handling) or handling < rules['handling_minimum']:
                        raise ValueError
                except ValueError:
                    handling = None
                    error(line, 'handling_minutes', 'Phải là số hữu hạn không âm')
            records.append((line, row, times, handling))
    valid = [(line, row, times, h) for line, row, times, h in records if line not in bad]
    metrics = {'số dòng đọc': total_rows, 'số dòng hợp lệ': len(valid),
               'số dòng loại khỏi số liệu': total_rows-len(valid)}
    for column in ('status', 'shop_status', 'product_status', 'ready_status'):
        counts = Counter(row[column] for _, row, _, _ in valid)
        metrics[column] = {value: counts[value] for value in schema['enums'][column]}
        metrics[column]['chưa ghi'] = counts['']
    ages, responses, handling_values, overdue = [], [], [], []
    for _, row, times, handling in valid:
        age = round((as_of-times['created_at']).total_seconds()/86400, 6)
        ages.append({'merchant_id': row['merchant_id'], 'tuổi hồ sơ (ngày)': age})
        if times.get('first_contact_at'):
            responses.append((times['first_contact_at']-times['created_at']).total_seconds()/3600)
        if handling is not None:
            handling_values.append(handling)
        if times.get('next_due_at') and times['next_due_at'] < as_of and row['status'] not in rules['overdue_excluded_status']:
            overdue.append({key: row[key] for key in ('merchant_id', 'owner_role', 'status')}
                           | {'tuổi hồ sơ (ngày)': age}
                           | {key: row[key] for key in ('next_action', 'next_due_at')})
    ai_rows = [row for _, row, _, _ in valid if row['ai_used'] == rules['ai_true']]
    reviews = Counter(row['review_result'] for row in ai_rows)
    metrics.update({'quá hạn': len(overdue), 'tuổi hồ sơ (ngày)': ages,
                    'phản hồi đầu (giờ)': {'số hồ sơ có mốc': len(responses), 'trung bình': mean(responses),
                                           'trung vị': round(statistics.median(responses), 6) if responses else None},
                    'handling_minutes': {'số hồ sơ có số phút': len(handling_values), 'tổng': round(sum(handling_values), 6),
                                         'trung bình': mean(handling_values)},
                    'review_result trên ai_used=true': {'mẫu số': len(ai_rows),
                        'số lượng': {v: reviews[v] for v in schema['enums']['review_result']},
                        'tỷ lệ': {v: round(reviews[v]/len(ai_rows), 6) if ai_rows else None for v in schema['enums']['review_result']},
                        'chưa ghi': reviews['']}})
    errors.sort(key=lambda e: (e['dòng'], e['cột'], e['lỗi']))
    return {'thời điểm chốt': as_of.isoformat(), 'lỗi dữ liệu': errors, 'số liệu': metrics,
            'danh sách quá hạn': overdue,
            'phạm vi': 'Chỉ tính dòng hợp lệ; loại cả hai dòng trùng. Không phải SLA giờ làm việc. Dữ liệu Đỏ: chỉ báo dòng/cột, không giá trị.'}


def markdown(data):
    # Escape free text so source data cannot create Markdown tables or HTML.
    def safe(value):
        return str(value).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '&#124;').replace('\n', ' ')
    lines = ['# Báo cáo tracker', '', f"Thời điểm chốt: {safe(data['thời điểm chốt'])}", '', '## Lỗi dữ liệu', '']
    for e in data['lỗi dữ liệu']:
        lines.append(f"- Dòng {e['dòng']}, cột {safe(e['cột'])}: {safe(e['lỗi'])}")
    if not data['lỗi dữ liệu']:
        lines.append('Không có.')
    lines += ['', '## Số liệu', '', '```json', json.dumps(data['số liệu'], ensure_ascii=False, indent=2).replace('`', '\\u0060'), '```', '', '## Danh sách quá hạn', '']
    keys = ['merchant_id', 'owner_role', 'status', 'tuổi hồ sơ (ngày)', 'next_action', 'next_due_at']
    lines += ['| '+' | '.join(keys)+' |', '| '+' | '.join(['---']*len(keys))+' |']
    lines += ['| '+' | '.join(safe(row[key]) for key in keys)+' |' for row in data['danh sách quá hạn']]
    return '\n'.join(lines)+ '\n\n'+data['phạm vi']+'\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_file', type=Path)
    parser.add_argument('--as-of')
    parser.add_argument('--schema', type=Path, default=Path(__file__).parent.parent/'references/tracker-schema.json')
    parser.add_argument('--format', choices=['json', 'md'], default='json')
    args = parser.parse_args()
    try:
        schema = json.loads(args.schema.read_text(encoding='utf-8'))
        as_of = iso(args.as_of) if args.as_of else datetime.now(ZoneInfo(schema['timezone']))
        data = report(args.csv_file, schema, as_of)
    except (ValueError, OSError, KeyError, csv.Error) as exc:
        parser.exit(2, f'Không thể báo cáo: {type(exc).__name__}; kiểm file/schema/thời điểm, không in dữ liệu nguồn.\n')
    print(markdown(data) if args.format == 'md' else json.dumps(data, ensure_ascii=False, indent=2))
    return 2 if data['lỗi dữ liệu'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
