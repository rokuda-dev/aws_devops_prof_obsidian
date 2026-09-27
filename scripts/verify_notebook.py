"""Read-only notebook checks and optional HTTP reference audit (standard library)."""
import argparse
import concurrent.futures
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / 'AWS-DOP-C02-Notebook'

def active(text):
    return re.sub(r'^(```|~~~).*?^\1[^\n]*$', '', text, flags=re.M | re.S)

def inventory():
    notes = sorted(VAULT.rglob('*.md'))
    return {'notes': {p.relative_to(VAULT).as_posix(): {
        'sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
        'read': re.findall(r'^read:\s*(true|false)\s*$', p.read_text(encoding='utf-8-sig'), re.M)
    } for p in notes}, 'obsidian': {p.relative_to(VAULT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in (VAULT / '.obsidian').rglob('*') if p.is_file()}}

def inspect():
    notes = sorted(VAULT.rglob('*.md'))
    by_name = {}
    errors, urls, links = [], {}, 0
    texts = {p: active(p.read_text(encoding='utf-8-sig')) for p in notes}
    for p in notes:
        by_name.setdefault(p.stem, []).append(p)
    for name, paths in by_name.items():
        if len(paths) != 1:
            errors.append(f'Duplicate basename: {name}')
    for p, text in texts.items():
        rel = p.relative_to(VAULT).as_posix()
        front = re.match(r'\A---\r?\n(.*?)\r?\n---', text, re.S)
        if not front:
            errors.append(f'{rel}: missing front matter')
        elif len(re.findall(r'^read:\s*(true|false)\s*$', front[1], re.M)) != 1:
            errors.append(f'{rel}: read property is missing, repeated or non-Boolean')
        if front:
            keys = re.findall(r'^([A-Za-z_][\w-]*):', front[1], re.M)
            if len(keys) != len(set(keys)):
                errors.append(f'{rel}: duplicate front-matter key')
        headings = re.findall(r'^#{1,6}\s+(.+)$', text, re.M)
        if len(headings) != len(set(headings)):
            errors.append(f'{rel}: duplicate heading')
        for target in re.findall(r'\[\[([^\]]+)\]\]', text):
            links += 1
            target = target.split('|')[0]
            note, _, heading = target.partition('#')
            candidates = by_name.get(Path(note).name.removesuffix('.md'), []) if note else [p]
            if not candidates:
                errors.append(f'{rel}: missing link {target}')
            elif heading and not any(heading == h.strip().rstrip('#').strip() for h in re.findall(r'^#{1,6}\s+(.+)$', texts[candidates[0]], re.M)):
                errors.append(f'{rel}: missing heading {target}')
        for url in re.findall(r'https?://[^\s<>\]\)"`]+', text):
            url = url.rstrip('.,;')
            urls.setdefault(url, set()).add(rel)
    service_names = {p.stem for p in (VAULT/'Services').glob('*.md')}
    index = texts.get(VAULT/'Service Index.md', '')
    first_column = re.findall(r'^\|\s*\[\[([^\]]+)\]\]', index, re.M)
    for name in service_names:
        if first_column.count(name) != 1:
            errors.append(f'Service Index: {name} does not occur exactly once in the first column')
    return {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
            'notes': len(notes), 'service_pages': len(service_names),
            'active_wiki_links': links, 'errors': errors,
            'front_matter_scope': 'Delimiter, duplicate top-level key, and Boolean read checks; not a complete YAML parser',
            'references': {u: sorted(paths) for u, paths in sorted(urls.items())}}

def check_url(item):
    url, pages = item
    request = urllib.request.Request(url, headers={'User-Agent': 'NotebookReferenceAudit/1.0'})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            body = response.read(250000).decode('utf-8', errors='replace')
            title = re.search(r'<title[^>]*>(.*?)</title>', body, re.I | re.S)
            canonical = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)', body, re.I)
            return {'url': url, 'status': response.status, 'final_url': response.url,
                    'title': re.sub(r'\s+', ' ', title[1]).strip() if title else '',
                    'canonical': canonical[1] if canonical else '', 'pages': pages}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {'url': url, 'error': str(exc), 'pages': pages}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--http', action='store_true')
    parser.add_argument('--snapshot', action='store_true')
    parser.add_argument('--baseline')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    result = inventory() if args.snapshot else inspect()
    if args.baseline:
        baseline = json.loads((ROOT / args.baseline).read_text(encoding='utf-8'))
        current = inventory()
        result['preservation'] = {
            'missing_notes': sorted(set(baseline['notes']) - set(current['notes'])),
            'read_changes': [p for p in baseline['notes'] if p in current['notes'] and baseline['notes'][p]['read'] != current['notes'][p]['read']],
            'obsidian_changes': [p for p in baseline['obsidian'] if baseline['obsidian'][p] != current['obsidian'].get(p)],
            'baseline_note_count': len(baseline['notes']),
            'baseline_read_true': sum(v['read'] == ['true'] for v in baseline['notes'].values()),
        }
    if args.http:
        with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
            result['http'] = list(pool.map(check_url, result['references'].items()))
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps({'output': str(output), 'notes': len(result['notes']) if args.snapshot else result['notes'],
                      'errors': result.get('errors', []), 'unique_urls': len(result.get('references', {})),
                      'http_checked': len(result.get('http', [])), 'preservation': result.get('preservation')}))

if __name__ == '__main__':
    main()
