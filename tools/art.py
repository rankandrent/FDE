"""Per-page hero illustrations. One shared line style (white strokes, one highlighted
shape, one solid dot) so every page is distinct but on-brand. Variation is seeded by
the page path, so two pages with the same motif still differ."""
import hashlib, math, pathlib, random, re

LINE = 'fill="none" stroke="rgba(255,255,255,.35)" stroke-width="1.5"'
HI = 'fill="rgba(255,255,255,.12)" stroke="#fff" stroke-width="1.5"'
DOT = 'fill="#fff"'

def _rng(path):
    return random.Random(int(hashlib.md5(path.encode()).hexdigest()[:8], 16))

def network(r):
    n = r.randint(6, 8); cx, cy, R = 200, 200, 140
    rot = r.uniform(0, math.pi)
    pts = [(cx + R * math.cos(rot + i * 2 * math.pi / n), cy + R * math.sin(rot + i * 2 * math.pi / n)) for i in range(n)]
    s = [f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}"/>' for x, y in pts]
    s += [f'<line x1="{pts[i][0]:.0f}" y1="{pts[i][1]:.0f}" x2="{pts[(i + 1) % n][0]:.0f}" y2="{pts[(i + 1) % n][1]:.0f}"/>' for i in range(n) if r.random() > 0.35]
    s += [f'<circle cx="{x:.0f}" cy="{y:.0f}" r="14"/>' for x, y in pts]
    hx, hy = pts[r.randrange(n)]
    return f'<g {LINE}>{"".join(s)}</g><circle cx="{cx}" cy="{cy}" r="34" {HI}/><circle cx="{hx:.0f}" cy="{hy:.0f}" r="7" {DOT}/>'

def flow(r):
    rows = [(60, 90), (170, 200), (280, 310)]
    s, boxes = [], []
    for i, (x, y) in enumerate(rows):
        w = r.choice([90, 100, 110]); boxes.append((x, y, w))
        s.append(f'<rect x="{x}" y="{y - 30}" width="{w}" height="60"/>')
    for (x1, y1, w1), (x2, y2, _) in zip(boxes, boxes[1:]):
        s.append(f'<path d="M{x1 + w1 // 2} {y1 + 30} V{y2} H{x2}"/>')
    hx, hy, hw = boxes[r.randrange(3)]
    return f'<g {LINE}>{"".join(s)}<rect x="40" y="40" width="320" height="320"/></g><rect x="{hx}" y="{hy - 30}" width="{hw}" height="60" {HI}/><circle cx="{boxes[-1][0] + boxes[-1][2]}" cy="{boxes[-1][1]}" r="7" {DOT}/>'

def pipeline(r):
    s = []
    ys = [100, 200, 300]
    for y in ys:
        s += [f'<ellipse cx="90" cy="{y - 22}" rx="45" ry="12"/>', f'<path d="M45 {y - 22} V{y + 18} A45 12 0 0 0 135 {y + 18} V{y - 22}"/>']
        s.append(f'<path d="M140 {y} C200 {y} 200 200 250 200"/>')
    hi = r.randrange(3)
    return f'<g {LINE}>{"".join(s)}<rect x="250" y="150" width="100" height="100"/><line x1="250" y1="150" x2="290" y2="110"/><line x1="350" y1="150" x2="390" y2="110"/><line x1="290" y1="110" x2="390" y2="110"/><line x1="390" y1="110" x2="390" y2="210"/><line x1="350" y1="250" x2="390" y2="210"/></g><rect x="250" y="150" width="100" height="100" {HI}/><circle cx="90" cy="{ys[hi] - 22}" r="7" {DOT}/>'

def blocks(r):
    s, cells = [], []
    for i in range(3):
        for j in range(3):
            x, y = 70 + j * 95, 70 + i * 95; cells.append((x, y))
            s.append(f'<rect x="{x}" y="{y}" width="70" height="70"/>')
    links = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (7, 8), (0, 3), (3, 6), (1, 4), (4, 7), (2, 5), (5, 8)]
    for a, b in links:
        if r.random() > 0.4:
            (x1, y1), (x2, y2) = cells[a], cells[b]
            s.append(f'<line x1="{x1 + 35}" y1="{y1 + 35}" x2="{x2 + 35}" y2="{y2 + 35}"/>')
    hx, hy = cells[r.choice([1, 3, 4, 5, 7])]
    return f'<g {LINE}>{"".join(s)}</g><rect x="{hx}" y="{hy}" width="70" height="70" {HI}/><circle cx="{hx + 70}" cy="{hy}" r="7" {DOT}/>'

def shield(r):
    def sh(sc):
        w, h = 130 * sc, 160 * sc
        return f'M200 {200 - h} L{200 + w} {200 - h * 0.6} V{200 + h * 0.1} C{200 + w} {200 + h * 0.6} 200 {200 + h} 200 {200 + h} C200 {200 + h} {200 - w} {200 + h * 0.6} {200 - w} {200 + h * 0.1} V{200 - h * 0.6} Z'
    inner = r.choice([0.55, 0.6, 0.65])
    return f'<g {LINE}><path d="{sh(1.1)}"/><path d="{sh(0.85)}"/></g><path d="{sh(inner)}" {HI}/><path d="M165 205 l25 25 l50 -55" fill="none" stroke="#fff" stroke-width="3"/><circle cx="200" cy="{200 - 160 * 1.1:.0f}" r="7" {DOT}/>'

def bars(r):
    hs = sorted(r.sample(range(60, 280, 20), 5))
    s = [f'<rect x="{50 + i * 62}" y="{340 - h}" width="40" height="{h}"/>' for i, h in enumerate(hs)]
    pts = ' '.join(f'{70 + i * 62},{330 - h}' for i, h in enumerate(hs))
    i = 4
    return f'<g {LINE}>{"".join(s[:-1])}<line x1="40" y1="340" x2="370" y2="340"/><polyline points="{pts}"/></g><rect x="{50 + i * 62}" y="{340 - hs[i]}" width="40" height="{hs[i]}" {HI}/><circle cx="{70 + i * 62}" cy="{330 - hs[i]}" r="7" {DOT}/>'

def rings(r):
    radii = [60, 105, 150]
    s = [f'<circle cx="200" cy="200" r="{rr}"/>' for rr in radii]
    dots = []
    for rr in radii:
        for _ in range(r.randint(2, 4)):
            a = r.uniform(0, 2 * math.pi); dots.append((200 + rr * math.cos(a), 200 + rr * math.sin(a)))
    s += [f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9"/>' for x, y in dots]
    hx, hy = dots[-1]
    return f'<g {LINE}>{"".join(s)}</g><circle cx="200" cy="200" r="30" {HI}/><circle cx="{hx:.0f}" cy="{hy:.0f}" r="7" {DOT}/>'

def layers(r):
    s = []
    off = r.choice([28, 34, 40])
    for i in range(4):
        x, y = 70 + i * off, 70 + i * off
        s.append(f'<rect x="{x}" y="{y}" width="200" height="140"/><line x1="{x}" y1="{y + 24}" x2="{x + 200}" y2="{y + 24}"/>')
    x, y = 70 + 3 * off, 70 + 3 * off
    return f'<g {LINE}>{"".join(s[:-1])}</g><rect x="{x}" y="{y}" width="200" height="140" {HI}/><line x1="{x}" y1="{y + 24}" x2="{x + 200}" y2="{y + 24}" stroke="#fff" stroke-width="1.5"/><circle cx="{x + 18}" cy="{y + 12}" r="5" {DOT}/>'

def docs(r):
    s = []
    for i in range(3):
        x, y = 80 + i * 30, 60 + i * 30
        s.append(f'<rect x="{x}" y="{y}" width="170" height="220"/>')
    x, y = 140, 120
    lines = ''.join(f'<line x1="{x + 20}" y1="{y + 40 + k * 26}" x2="{x + 20 + r.choice([90, 110, 130])}" y2="{y + 40 + k * 26}"/>' for k in range(6))
    return f'<g {LINE}>{"".join(s[:2])}{lines}</g><rect x="{x}" y="{y}" width="170" height="220" {HI}/><g {LINE}>{lines}</g><circle cx="300" cy="300" r="40" {HI}/><line x1="328" y1="328" x2="365" y2="365" stroke="#fff" stroke-width="3"/><circle cx="300" cy="300" r="7" {DOT}/>'

def pod(r):
    n = r.choice([4, 5])
    pts = [(200 + 80 * math.cos(i * 2 * math.pi / n - math.pi / 2), 200 + 80 * math.sin(i * 2 * math.pi / n - math.pi / 2)) for i in range(n)]
    s = [f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}"/>' for i, a in enumerate(pts) for b in pts[i + 1:]]
    s += [f'<circle cx="{x:.0f}" cy="{y:.0f}" r="22"/>' for x, y in pts]
    return f'<g {LINE}><rect x="60" y="60" width="280" height="280"/>{"".join(s)}</g><rect x="100" y="100" width="200" height="200" {HI}/><circle cx="{pts[0][0]:.0f}" cy="{pts[0][1]:.0f}" r="7" {DOT}/>'

def pulse(r):
    a = r.choice([70, 90, 110])
    return f'<g {LINE}><rect x="60" y="60" width="280" height="280"/><line x1="60" y1="200" x2="340" y2="200" stroke-dasharray="4 6"/></g><path d="M60 200 H140 L160 {200 - a} L185 {200 + a * 0.7:.0f} L205 170 L220 200 H340" fill="none" stroke="#fff" stroke-width="2.5"/><rect x="170" y="80" width="60" height="20" {HI}/><rect x="190" y="60" width="20" height="60" {HI}/><circle cx="340" cy="200" r="7" {DOT}/>'

def route(r):
    pts = [(70, 300), (150, r.choice([180, 200, 220])), (250, r.choice([260, 280])), (330, 100)]
    path = 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
    s = [f'<rect x="{x - 18}" y="{y - 18}" width="36" height="36"/>' for x, y in pts[:-1]]
    return f'<g {LINE}><path d="{path}" stroke-dasharray="6 6"/>{"".join(s)}<line x1="40" y1="350" x2="360" y2="350"/></g><rect x="{pts[2][0] - 18}" y="{pts[2][1] - 18}" width="36" height="36" {HI}/><circle cx="{pts[-1][0]}" cy="{pts[-1][1]}" r="8" {DOT}/>'

def ledger(r):
    s = [f'<line x1="70" y1="{90 + k * 45}" x2="330" y2="{90 + k * 45}"/>' for k in range(6)]
    s += ['<line x1="160" y1="70" x2="160" y2="330"/>', '<rect x="70" y="70" width="260" height="260"/>']
    k = r.randrange(1, 5)
    return f'<g {LINE}>{"".join(s)}</g><rect x="160" y="{90 + k * 45}" width="170" height="45" {HI}/><circle cx="330" cy="{90 + k * 45}" r="7" {DOT}/><path d="M290 60 l40 -30 l40 30" fill="none" stroke="#fff" stroke-width="1.5"/>'

def cube(r):
    return f'<g {LINE}><rect x="60" y="60" width="200" height="200"/><rect x="100" y="100" width="200" height="200"/><line x1="60" y1="60" x2="140" y2="140"/><line x1="260" y1="60" x2="340" y2="140"/><line x1="60" y1="260" x2="140" y2="340"/><line x1="260" y1="260" x2="340" y2="340"/></g><rect x="140" y="140" width="200" height="200" {HI}/><circle cx="340" cy="140" r="6" {DOT}/>'

def target(r):
    s = [f'<circle cx="200" cy="200" r="{rr}"/>' for rr in (150, 110, 70)]
    s += ['<line x1="200" y1="30" x2="200" y2="370"/>', '<line x1="30" y1="200" x2="370" y2="200"/>']
    a = r.uniform(0.6, 1.2)
    hx, hy = 200 + 90 * math.cos(-a), 200 + 90 * math.sin(-a)
    return f'<g {LINE}>{"".join(s)}</g><circle cx="200" cy="200" r="30" {HI}/><path d="M{hx - 14:.0f} {hy - 14:.0f} l28 28 M{hx + 14:.0f} {hy - 14:.0f} l-28 28" stroke="#fff" stroke-width="2.5"/><circle cx="200" cy="200" r="6" {DOT}/>'

def spokes(r):
    n = r.choice([5, 6])
    out = [(200 + 150 * math.cos(math.pi * (0.15 + 0.7 * i / (n - 1))), 60 + 0 * i) for i in range(n)]
    xs = [60 + i * (280 / (n - 1)) for i in range(n)]
    s = [f'<rect x="{x - 22:.0f}" y="290" width="44" height="44"/><path d="M200 180 C200 240 {x:.0f} 240 {x:.0f} 290"/>' for x in xs]
    return f'<g {LINE}>{"".join(s)}</g><rect x="130" y="70" width="140" height="110" {HI}/><line x1="130" y1="96" x2="270" y2="96" stroke="#fff" stroke-width="1.5"/><circle cx="{xs[-1]:.0f}" cy="290" r="7" {DOT}/>'

def stack3(r):
    labels = [(80, 'ui'), (175, 'api'), (270, 'db')]
    s = []
    for y, _ in labels:
        s.append(f'<rect x="80" y="{y}" width="240" height="60"/>')
    s += ['<line x1="200" y1="140" x2="200" y2="175"/>', '<line x1="200" y1="235" x2="200" y2="270"/>']
    k = r.randrange(3)
    y = labels[k][0]
    return f'<g {LINE}>{"".join(s)}<path d="M120 105 l-15 5 l15 5 M150 105 l15 5 l-15 5"/></g><rect x="80" y="{y}" width="240" height="60" {HI}/><circle cx="320" cy="{y}" r="7" {DOT}/>'

def dashboard(r):
    hs = [r.randint(30, 110) for _ in range(6)]
    bars = ''.join(f'<rect x="{90 + i * 36}" y="{300 - h}" width="22" height="{h}"/>' for i, h in enumerate(hs))
    return f'<g {LINE}><rect x="50" y="70" width="300" height="260"/><line x1="50" y1="105" x2="350" y2="105"/><rect x="250" y="125" width="80" height="60"/>{bars}</g><rect x="250" y="125" width="80" height="60" {HI}/><circle cx="70" cy="88" r="6" {DOT}/>'

def milestones(r):
    pts = [(60, 320), (140, r.choice([250, 270])), (220, r.choice([200, 220])), (300, 140), (350, 70)]
    line = ' '.join(f'{x},{y}' for x, y in pts)
    s = [f'<circle cx="{x}" cy="{y}" r="16"/><line x1="{x}" y1="{y + 16}" x2="{x}" y2="350" stroke-dasharray="3 5"/>' for x, y in pts[:-1]]
    return f'<g {LINE}><polyline points="{line}"/>{"".join(s)}<line x1="40" y1="350" x2="370" y2="350"/></g><circle cx="{pts[3][0]}" cy="{pts[3][1]}" r="16" {HI}/><circle cx="{pts[-1][0]}" cy="{pts[-1][1]}" r="8" {DOT}/>'

def gauge(r):
    a = math.pi * r.uniform(0.2, 0.4)
    ticks = ''.join(f'<line x1="{200 + 130 * math.cos(math.pi + k * math.pi / 8):.0f}" y1="{260 + 130 * math.sin(math.pi + k * math.pi / 8):.0f}" x2="{200 + 150 * math.cos(math.pi + k * math.pi / 8):.0f}" y2="{260 + 150 * math.sin(math.pi + k * math.pi / 8):.0f}"/>' for k in range(9))
    nx, ny = 200 + 110 * math.cos(-a), 260 + 110 * math.sin(-a)
    return f'<g {LINE}><path d="M50 260 A150 150 0 0 1 350 260"/><path d="M90 260 A110 110 0 0 1 310 260"/>{ticks}<line x1="50" y1="300" x2="350" y2="300"/></g><path d="M200 260 L{nx:.0f} {ny:.0f}" stroke="#fff" stroke-width="3"/><circle cx="200" cy="260" r="26" {HI}/><circle cx="{nx:.0f}" cy="{ny:.0f}" r="7" {DOT}/>'

def hierarchy(r):
    n = r.choice([3, 4])
    xs = [200 + (i - (n - 1) / 2) * 90 for i in range(n)]
    s = [f'<path d="M200 130 V170 H{x:.0f} V200"/><rect x="{x - 30:.0f}" y="200" width="60" height="50"/><path d="M{x:.0f} 250 V290 H200"/>' for x in xs]
    return f'<g {LINE}>{"".join(s)}<rect x="160" y="290" width="80" height="60"/></g><rect x="150" y="70" width="100" height="60" {HI}/><circle cx="250" cy="70" r="7" {DOT}/>'

def envelope(r):
    return f'<g {LINE}><rect x="60" y="100" width="280" height="190"/><path d="M60 100 L200 210 L340 100"/><path d="M60 290 L165 185 M340 290 L235 185"/><circle cx="300" cy="90" r="{r.choice([30, 34])}"/></g><path d="M60 100 L200 210 L340 100 Z" {HI}/><circle cx="300" cy="90" r="8" {DOT}/>'

def cycle(r):
    n = 5; R = 130
    pts = [(200 + R * math.cos(-math.pi / 2 + i * 2 * math.pi / n), 200 + R * math.sin(-math.pi / 2 + i * 2 * math.pi / n)) for i in range(n)]
    arcs = ''.join(f'<path d="M{a[0]:.0f} {a[1]:.0f} A{R} {R} 0 0 1 {b[0]:.0f} {b[1]:.0f}"/>' for a, b in zip(pts, pts[1:] + pts[:1]))
    nodes = ''.join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="20"/>' for x, y in pts)
    k = r.randrange(n)
    return f'<g {LINE}>{arcs}{nodes}</g><circle cx="{pts[k][0]:.0f}" cy="{pts[k][1]:.0f}" r="20" {HI}/><circle cx="200" cy="200" r="7" {DOT}/>'

def quad(r):
    cells = [(70, 70), (210, 70), (70, 210), (210, 210)]
    inner = [
        '<path d="M90 160 L120 120 L150 140 L180 95"/>',
        '<path d="M230 140 H260 L270 110 L285 170 L295 140 H330"/>',
        '<rect x="95" y="235" width="25" height="25"/><rect x="135" y="235" width="25" height="25"/><rect x="95" y="275" width="25" height="25"/>',
        '<path d="M230 310 L270 250 L300 290 L330 240"/>',
    ]
    k = r.randrange(4)
    return f'<g {LINE}>{"".join(f"<rect x=\"{x}\" y=\"{y}\" width=\"120\" height=\"120\"/>" for x, y in cells)}{"".join(inner)}</g><rect x="{cells[k][0]}" y="{cells[k][1]}" width="120" height="120" {HI}/><circle cx="{cells[k][0] + 120}" cy="{cells[k][1]}" r="7" {DOT}/>'

def cards(r):
    s = []
    for i in range(3):
        x = 60 + i * 100
        h = r.choice([180, 200, 220])
        s.append(f'<rect x="{x}" y="{340 - h}" width="80" height="{h}"/><rect x="{x + 10}" y="{350 - h}" width="60" height="45"/><line x1="{x + 10}" y1="{410 - h}" x2="{x + 70}" y2="{410 - h}"/><line x1="{x + 10}" y1="{425 - h}" x2="{x + 55}" y2="{425 - h}"/>')
    return f'<g {LINE}>{"".join(s)}</g><rect x="160" y="140" width="80" height="200" {HI}/><circle cx="240" cy="140" r="7" {DOT}/>'

def platform(r):
    xs = [110, 200, 290]
    top = ''.join(f'<circle cx="{x}" cy="{r.choice([110, 130, 150])}" r="24"/>' for x in xs)
    links = ''.join(f'<line x1="{x}" y1="180" x2="{x}" y2="250"/>' for x in xs) + '<line x1="110" y1="130" x2="290" y2="130" stroke-dasharray="4 6"/>'
    return f'<g {LINE}>{top}{links}<path d="M60 300 L200 340 L340 300"/></g><path d="M60 270 L200 230 L340 270 L200 310 Z" {HI}/><circle cx="200" cy="270" r="7" {DOT}/>'

def connector(r):
    ys = [90, 160, 230, 300][:r.choice([3, 4])]
    sys_ = ''.join(f'<rect x="290" y="{y - 22}" width="70" height="44"/><path d="M230 200 C260 200 260 {y} 290 {y}"/>' for y in ys)
    return f'<g {LINE}><circle cx="80" cy="200" r="40"/><line x1="120" y1="200" x2="170" y2="200"/>{sys_}</g><rect x="170" y="160" width="60" height="80" {HI}/><circle cx="80" cy="200" r="7" {DOT}/>'

RULES = [  # first match wins
    ('contact', envelope), ('how-fde-works', cycle), ('agentic-platforms', platform), ('blog', cards),
    ('fde-pods', pod), ('agentic-fde-pod', hierarchy), ('fde-for-saas', spokes), ('full-stack', stack3),
    ('penetration', target), ('ai-readiness-assessment', gauge), ('case-studies', milestones), ('industries/technology', dashboard), ('agentification', flow), ('how-fde-works', flow),
    ('agentic-platforms', network), ('knowledge', docs), ('blog', docs), ('mcp', connector), ('integration', blocks),
    ('industries/financial', ledger), ('industries/healthcare', pulse), ('industries/technology', layers),
    ('industries/logistics', route), ('data-engineering', pipeline),
    ('security', shield), ('penetration', shield), ('strategy', bars), ('readiness', bars), ('case-studies', bars),
    ('adoption', rings), ('product', layers), ('saas', layers), ('industries/', quad),
]

def svg_for(path):
    fn = next((f for key, f in RULES if key in path), network if path == '/' else cube)
    return f'<svg class="hero__graphic" viewBox="0 0 400 400" aria-hidden="true">{fn(_rng(path))}</svg>'

# Official white tkxel logo, embedded in covers.
_logo = (pathlib.Path(__file__).resolve().parent.parent / 'assets/img/tkxel-logo-dark-bg.svg').read_text()
LOGO_VIEWBOX = re.search(r'viewBox="([^"]+)"', _logo).group(1)
LOGO_BODY = re.search(r'(<style>.*?</style>.*)</svg>', _logo, re.S).group(1).replace('.st0', '.lg0').replace('.st1', '.lg1').replace('class="st0"', 'class="lg0"').replace('class="st1"', 'class="lg1"')

# Blog cover images: standalone SVG (gradient background + topic motif), one per post.
COVER_MOTIFS = {
    'Agents': [network, hierarchy, flow, platform], 'Governance': [shield, target, ledger],
    'Data': [pipeline, docs, dashboard], 'Integration': [connector, blocks, route],
    'Strategy': [bars, gauge, milestones, quad], 'FDE': [pod, cycle, rings, stack3],
}

def cover_svg(slug, tags, avoid=(), title=''):
    """Editorial blog cover (1200x630): gradient, soft glows, dot grid, a frosted panel holding the
    topic motif in heavier strokes, and a topic label. avoid: motif names used by recent posts."""
    r = _rng('/blog/' + slug)
    pool = [m for t in (tags or ['FDE']) for m in COVER_MOTIFS.get(t, [])] or [cube]
    r.shuffle(pool)
    every = [m for ms in COVER_MOTIFS.values() for m in ms]
    motif = next((m for m in pool + every if m.__name__ not in avoid), pool[0])
    cover_svg.last = motif.__name__
    label = ' · '.join(t.upper() for t in (tags or ['FDE'])[:2])
    g1 = (r.randint(60, 340), r.randint(40, 200))
    g2 = (r.randint(820, 1140), r.randint(380, 600))
    side = r.choice(['right', 'left'])
    px = 680 if side == 'right' else 80
    tx = 80 if side == 'right' else 600
    # Post title (part before a colon), wrapped to at most 4 lines of ~16 characters (fits a 520px column).
    short = (re.split(r'[:,]', title)[0] if title else slug.replace('-', ' ')).strip()
    lines, cur = [], ''
    for w in short.split():
        if len(cur) + len(w) + 1 > 16 and cur:
            lines.append(cur); cur = w
        else:
            cur = (cur + ' ' + w).strip()
    lines.append(cur)
    if len(lines) > 4:
        lines = lines[:4]; lines[-1] = lines[-1].rstrip('.,') + '…'
    esc = lambda t: t.replace('&', '&amp;').replace('<', '&lt;')
    deco = ''.join(f'<text x="{tx}" y="{262 + i * 64}" font-family="Plus Jakarta Sans, Helvetica, Arial, sans-serif" font-size="50" font-weight="800" fill="#fff">{esc(l)}</text>' for i, l in enumerate(lines))
    deco += f'<rect x="{tx}" y="{262 + len(lines) * 64 - 18}" width="72" height="5" fill="#fff"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" role="img" aria-label="{label} illustration">
<defs>
<radialGradient id="bg" cx="10%" cy="0%" r="140%"><stop offset="0" stop-color="#10347E"/><stop offset="1" stop-color="#0755E9"/></radialGradient>
<radialGradient id="glow"><stop offset="0" stop-color="#fff" stop-opacity=".28"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.4" fill="rgba(255,255,255,.16)"/></pattern>
<style>.m * {{ stroke-width: 3px; }} .m [fill="rgba(255,255,255,.12)"] {{ fill: rgba(255,255,255,.22); }}</style>
</defs>
<rect width="1200" height="630" fill="url(#bg)"/>
<circle cx="{g1[0]}" cy="{g1[1]}" r="320" fill="url(#glow)"/>
<circle cx="{g2[0]}" cy="{g2[1]}" r="260" fill="url(#glow)"/>
<rect width="1200" height="630" fill="url(#dots)"/>
<rect x="{px + 18}" y="78" width="440" height="440" fill="rgba(4,24,77,.35)"/>
<rect x="{px}" y="60" width="440" height="440" fill="rgba(255,255,255,.10)" stroke="rgba(255,255,255,.45)" stroke-width="2"/>
<g class="m" transform="translate({px + 30} 90) scale(0.95)">{motif(r)}</g>
{deco}
<rect x="{tx}" y="72" width="{24 + len(label) * 15}" height="40" fill="#fff"/>
<text x="{tx + 12}" y="98" font-family="IBM Plex Mono, Menlo, Consolas, monospace" font-size="18" letter-spacing="2" fill="#0B2A6B">{label}</text>
<svg x="{tx}" y="158" width="84" height="30" viewBox="{LOGO_VIEWBOX}">{LOGO_BODY}</svg>
<text x="{tx + 96}" y="186" font-family="IBM Plex Mono, Menlo, monospace" font-size="16" fill="rgba(255,255,255,.75)">FDE INSIGHTS</text>
</svg>'''
