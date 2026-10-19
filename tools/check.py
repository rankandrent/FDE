"""Site checks, run after tools/build.py. Exits non-zero if anything fails.
Checks: post JSON shape, internal links resolve to files, JSON-LD parses,
titles are unique, and no banned filler words (design system §1.2)."""
import collections, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BAN = re.compile(r'\b(seamless|cutting-edge|world-class|game-changing|leverage|unlock|empower|revolutioni[sz]e)\b', re.I)
POST_KEYS = {'path': str, 'title': str, 'desc': str, 'eyebrow': str, 'h1': str, 'lede': str, 'date': str, 'date_label': str,
             'read_min': int, 'sections': list, 'related': list, 'cta': list, 'faq': list, 'form_h': str, 'research': dict, 'tags': list}
TAGS = {'FDE', 'Agents', 'Governance', 'Data', 'Strategy', 'Integration'}
errors = []

for f in sorted((ROOT / 'tools/posts').glob('*.json')):
    try:
        p = json.loads(f.read_text())
    except Exception as ex:
        errors.append(f'{f.name}: invalid JSON ({ex})'); continue
    for k, t in POST_KEYS.items():
        if not isinstance(p.get(k), t):
            errors.append(f'{f.name}: missing or wrong type for "{k}"')
    if p.get('path') != f'/blog/{f.stem}/':
        errors.append(f'{f.name}: path must be /blog/{f.stem}/')
    if not set(p.get('tags', [])) <= TAGS:
        errors.append(f'{f.name}: tags must come from {sorted(TAGS)}')
    if len(p.get('title', '')) > 65:
        errors.append(f'{f.name}: title longer than 65 characters')
    if not 120 <= len(p.get('desc', '')) <= 165:
        errors.append(f'{f.name}: description should be 120–165 characters')

titles = collections.Counter()
for page in sorted(ROOT.rglob('*.html')):
    if '.git' in page.parts or 'tools' in page.parts:
        continue
    rel = page.relative_to(ROOT)
    h = page.read_text()
    m = re.search(r'<title>(.*?)</title>', h)
    if m: titles[m.group(1)] += 1
    for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try: json.loads(blob)
        except Exception as ex: errors.append(f'{rel}: bad JSON-LD ({str(ex)[:50]})')
    text = re.sub(r'<[^>]+>', ' ', re.sub(r'<script.*?</script>', '', h, flags=re.S))
    for w in set(x.group(0).lower() for x in BAN.finditer(text)):
        errors.append(f'{rel}: banned word "{w}"')
    for href in set(re.findall(r'href="(/[^"#?]*)', h)):
        target = ROOT / href.lstrip('/')
        if not (target.is_file() or (target / 'index.html').is_file()):
            errors.append(f'{rel}: broken link {href}')

errors += [f'duplicate title: {t}' for t, c in titles.items() if c > 1]

if errors:
    print('\n'.join(errors)); print(f'\nFAILED: {len(errors)} problem(s)'); sys.exit(1)
print(f'OK: {sum(titles.values())} pages checked')
