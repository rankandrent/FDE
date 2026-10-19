"""Site generator: writes the plain HTML pages from tools/content/*.py and tools/posts/*.json,
reusing the header, footer and shared sections of services/agentic-fde-pod/index.html.
Run from anywhere: python3 tools/build.py"""
import html, json, pathlib, re, sys

ROOT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent
SRC = (ROOT / 'services/agentic-fde-pod/index.html').read_text()
LINES = SRC.split('\n')

def block(start_pat, end_pat, from_line=0):
    s = next(i for i in range(from_line, len(LINES)) if re.search(start_pat, LINES[i]))
    e = next(i for i in range(s, len(LINES)) if re.search(end_pat, LINES[i]))
    return '\n'.join(LINES[s:e + 1]).lstrip()

HEADER = block(r'<header class="hdr"', r'</header>')
FOOTER = block(r'<footer class="ftr"', r'^    </footer>')
WHY = block(r'id="why-tkxel"', r'^      </section>')
AWARDS = block(r'class="section aw"', r'^      </section>')
FORM = block(r'id="cta-form"', r'^      </section>')

# Header nav: one clean set of top-level links, now that every target page exists.
HEADER = re.sub(r'(</div>\s*</div>\s*</div>)\s*<a href="/services/fde-pods/".*?(</nav>)',
                r'\1\n        <a href="/services/fde-pods/" class="hdr__link">FDE pods</a><a href="/industries/" class="hdr__link">Industries</a><a href="/case-studies/" class="hdr__link">Case studies</a><a href="/blog/" class="hdr__link">Resources</a>\n      \2',
                HEADER, count=1, flags=re.S)

# Mega menu and footer sub-service items link to their pages where one exists.
CHILD_LINKS = {
  'Full-stack FDE pod': '/services/full-stack-fde-pod/',
  'Agentic FDE pod': '/services/agentic-fde-pod/',
  'Data engineering FDE pod': '/services/data-engineering-fde-pod/',
  'Integration &amp; legacy modernization pod': '/services/integration-legacy-modernization-pod/',
  'AI maturity assessment': '/services/ai-readiness-assessment/',
  'Enterprise connectors &amp; MCP integrations': '/services/mcp-enterprise-integrations/',
  'Enterprise knowledge assistant': '/services/enterprise-knowledge-assistant/',
  'Workflow agentification': '/services/workflow-agentification/',
  'AI penetration testing': '/services/ai-penetration-testing/',
}
def link_children(block_html):
    for name, href in CHILD_LINKS.items():
        block_html = block_html.replace(f'<li>{name}</li>', f'<li><a href="{href}">{name}</a></li>')
    return block_html
HEADER = link_children(HEADER)
FOOTER = link_children(FOOTER)

# Office addresses as listed on https://tkxel.com/contact-us/
OFFICES = {
  'USA': '11921 Freedom Drive, Two Fountain Square, Suite 550, Reston, VA 20190',
  'Saudi Arabia': 'Building 4236, King Saud St., An Nawras District, Dammam 32214',
  'Portugal': 'Avenida D. João II, 50, 1990-095 Lisbon',
  'Pakistan': 'One World Building, Babar Block, Garden Town, Lahore 54000',
}
for region, addr in OFFICES.items():
    FOOTER = re.sub(rf'(<span class="eyebrow">{region}</span>\s*<p>)[^<]*(</p>)', lambda m: m.group(1) + html.escape(addr) + m.group(2), FOOTER)

# Final form: hide the Clutch and testimonial blocks until real ones are supplied.
FORM = re.sub(r'\s*<div class="fc__clutch">.*?</div>', '', FORM, flags=re.S)
FORM = re.sub(r'\s*<blockquote class="fc__quote">[^<]*Placeholder.*?</blockquote>', '', FORM, flags=re.S)

# Legal pages live on the main site.
LEGAL = {'href="/privacy-policy/"': 'href="https://tkxel.com/privacy-policy/"', 'href="/terms/"': 'href="https://tkxel.com/terms-of-use/"'}
for a, b in LEGAL.items():
    FOOTER = FOOTER.replace(a, b)
    FORM = FORM.replace(a, b)

e = html.escape
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location('art', pathlib.Path(__file__).parent / 'art.py'); ART = _ilu.module_from_spec(_spec); _spec.loader.exec_module(ART)
PAGE = {'path': '/'}
LOGOS = ['Knowles', 'Sterne Kessler', 'Replenium', 'ABB', 'Barclays', 'Signal', 'Canvs AI', 'AutoConX', 'BBJ La Tavola']  # tkxel clients listed on tkxel.com

def headline(text, tag='h2', cls='h2'):
    parts = [e(p) for p in text.split(' | ')]
    return f'<{tag} class="{cls}">' + '<span class="br"><br /></span> '.join(parts) + f'</{tag}>'

def head(title, desc, path, schema):
    url = f'https://fde.tkxel.com{path}'
    ld = ''.join(f'\n    <script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema)
    return f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{e(title)}</title>
    <meta name="description" content="{e(desc)}" />
    <link rel="canonical" href="{url}" />
    <meta property="og:title" content="{e(title)}" />
    <meta property="og:description" content="{e(desc)}" />
    <meta property="og:url" content="{url}" />
    <meta property="og:type" content="website" />
    <meta property="og:image" content="https://fde.tkxel.com/og-default.png" />
    <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />{ld}
    <link rel="stylesheet" href="/assets/css/styles.css" />
  </head>
  <body>'''

TAIL = '''
    <script src="/assets/js/main.js" defer></script>
  </body>
</html>
'''

def hero(eyebrow, h, sub, cta='Book discovery call'):
    logos = ''.join(f'<span class="hero__logo">{e(l)}</span>' for l in LOGOS) + ''.join(f'<span class="hero__logo" aria-hidden="true">{e(l)}</span>' for l in LOGOS)
    return f'''
      <section class="hero section--gradient on-dark" data-hero>
        <div class="container hero__inner">
          <div class="hero__copy">
            <span class="eyebrow">{e(eyebrow)}</span>
            {headline(h, 'h1', 'display')}
            <p class="hero__sub">{e(sub)}</p>
            <a href="#cta-form" class="btn btn--invert">{e(cta)}</a>
          </div>
          {ART.svg_for(PAGE['path'])}
        </div>
        <div class="container hero__logos">
          <span class="eyebrow">Our clients</span>
          <div class="hero__marquee"><div class="hero__track">{logos}</div></div>
        </div>
      </section>'''

def grid(h, eyebrow, cards, sid='services'):
    out = []
    for c in cards:
        title, body = c[0], c[1]
        href = c[2] if len(c) > 2 else None
        tag, attr = ('a', f'href="{href}"') if href else ('article', 'tabindex="0"')
        out.append(f'''
          <{tag} class="sg__card" {attr}>
            <span class="eyebrow">{e(eyebrow)}</span>
            <h3 class="sg__title">{e(title)}</h3>
            <p class="sg__body">{e(body)}</p>
            <span class="sg__icon" aria-hidden="true"></span>
          </{tag}>''')
    return f'''
      <section class="section sg" id="{sid}">
        <div class="container sg__head">
          <div class="section-head reveal">{headline(h)}</div>
          <div class="sg__arrows">
            <button aria-label="Previous" data-sg-prev>←</button>
            <button aria-label="Next" data-sg-next>→</button>
          </div>
        </div>
        <div class="sg__row" data-sg-row tabindex="0" aria-label="{e(h.replace(' | ', ' '))}">{''.join(out)}
        </div>
      </section>'''

def icb(h, body, cta):
    return f'''
      <section class="icb section--gradient on-dark">
        <div class="container icb__row">
          {headline(h)}
          <div class="icb__right">
            <p>{e(body)}</p>
            <a href="#cta-form" class="btn btn--invert">{e(cta)}</a>
          </div>
        </div>
      </section>'''

def challenges(h, items):
    cells = ''.join(f'''
            <div class="cp__item reveal">
              <h3 class="cp__title">{e(t)}</h3>
              <p class="muted">{e(b)}</p>
            </div>''' for t, b in items)
    return f'''
      <section class="section" id="challenges">
        <div class="container">
          <div class="section-head reveal">{headline(h)}</div>
          <div class="cp" style="--n: {len(items)}">{cells}
          </div>
        </div>
      </section>'''

def process(h, steps):
    n = len(steps)
    layers = ''.join(
        f'<polygon data-pt-layer="{i}" class="pt__layer{" is-active" if i == 0 else ""}" points="150,{40 + (n - 1 - i) * 36} 280,{80 + (n - 1 - i) * 36} 150,{120 + (n - 1 - i) * 36} 20,{80 + (n - 1 - i) * 36}"></polygon>'
        for i in range(n))
    lis = ''.join(f'''
              <li class="pt__step{" is-active" if i == 0 else ""}" data-pt-step="{i}">
                <button class="pt__btn" aria-expanded="{"true" if i == 0 else "false"}">
                  <span class="pt__n">{i + 1:02d}</span><span class="pt__title">{e(t)}</span>
                  <span class="caption pt__time">{e(tm)}</span>
                </button>
                <div class="pt__body">
                  <p>{e(b)}</p>
                  <p class="caption"><strong>Deliverables:</strong> {e(d)}</p>
                </div>
              </li>''' for i, (t, tm, b, d) in enumerate(steps))
    return f'''
      <section class="section pt" id="process" data-pt>
        <div class="container">
          <div class="section-head reveal">{headline(h)}</div>
          <div class="pt__grid">
            <div class="pt__left" aria-hidden="true">
              <span class="pt__num" data-pt-num>01</span>
              <svg viewBox="0 0 300 260" class="pt__stack">{layers}</svg>
            </div>
            <ol class="pt__list">{lis}
            </ol>
          </div>
        </div>
      </section>'''

def comparison(h, intro, cols, rows):
    ths = ''.join(f'<th scope="col"{" class=\"is-hl\"" if i == 2 else ""}>{e(c)}</th>' for i, c in enumerate(cols))
    trs = ''.join(
        '\n                <tr><th scope="row">' + e(r[0]) + '</th>' + ''.join(f'<td{" class=\"is-hl\"" if i == 2 else ""}>{e(v)}</td>' for i, v in enumerate(r[1:])) + '</tr>'
        for r in rows)
    return f'''
      <section class="section section--alt" id="comparison">
        <div class="container">
          <div class="section-head reveal">{headline(h)}<p class="muted">{e(intro)}</p></div>
          <div class="ct__scroll reveal" tabindex="0" role="region" aria-label="Comparison table">
            <table class="ct">
              <thead><tr><th scope="col"><span class="sr-only">Criterion</span></th>{ths}</tr></thead>
              <tbody>{trs}
              </tbody>
            </table>
          </div>
        </div>
      </section>'''

# Case-study tags per page, on top of the blog-topic tags in PATH_TAGS.
CASE_EXTRA = {
  '/industries/financial-services/': ['Financial'], '/industries/technology-saas/': ['SaaS'],
  '/industries/logistics-manufacturing/': ['Manufacturing'], '/industries/healthcare/': ['Healthcare'],
  '/services/fde-for-saas-isvs/': ['SaaS'],
}

def pick_cases(path):
    if path == '/':
        return CASES[:3]
    want = set(PATH_TAGS.get(path, [])) | set(CASE_EXTRA.get(path, []))
    if path.startswith('/industries/') and CASE_EXTRA.get(path):
        want = set(CASE_EXTRA[path])  # industry pages only show same-industry work
    return [c for c in CASES if want & set(c['tags'])][:3]

def case_card(c):
    return f'''
            <article class="csc__card reveal">
              <div class="csc__tags"><span class="eyebrow">{e(c['client'])}</span><span class="eyebrow">{e(c['industry'])}</span></div>
              <h3 class="csc__result">{e(c['result'])}</h3>
              <a href="{c['url']}" class="link-arrow" target="_blank" rel="noopener">Read the case study on tkxel.com</a>
            </article>'''

def cases(path):
    """CASE_STUDY_CAROUSEL (§4.14) with real tkxel.com case studies; omitted when none match."""
    picks = pick_cases(path)
    if not picks:
        return ''
    return f'''
      <section class="section" id="case-studies">
        <div class="container">
          <div class="csc__head reveal"><h2 class="h2">Featured success stories</h2><a href="/case-studies/" class="link-arrow">All case studies</a></div>
          <div class="csc">{''.join(case_card(c) for c in picks)}
          </div>
        </div>
      </section>'''

def form(h):
    return re.sub(r'(<div class="fc__left">\s*)<h2 class="h2">.*?</h2>', lambda m: m.group(1) + f'<h2 class="h2">{e(h)}</h2>', FORM, count=1, flags=re.S)

def faq(items):
    rows = ''.join(f'''
            <details class="faq__item"{" open" if i == 0 else ""}>
              <summary><span>{e(q)}</span><span class="faq__icon" aria-hidden="true"></span></summary>
              <p>{e(a)}</p>
            </details>''' for i, (q, a) in enumerate(items))
    return f'''
      <section class="section" id="faq">
        <div class="container faq">
          <h2 class="h2 reveal">Frequently asked questions</h2>
          <div>{rows}
          </div>
        </div>
      </section>'''

def faq_schema(items):
    return {'@context': 'https://schema.org', '@type': 'FAQPage',
            'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in items]}

def write(path, body_html, title, desc, schema):
    if path in PATH_TAGS:
        picks = [q for q in POSTS if set(q.get('tags', [])) & set(PATH_TAGS[path])][:3]
        if picks:
            body_html += resources(picks, 'Related insights')
    out = head(title, desc, path, schema) + '\n    ' + HEADER + '\n    <main id="main">' + body_html + '\n    </main>\n    ' + FOOTER + TAIL
    dest = ROOT / path.strip('/') / 'index.html' if path != '/404' else ROOT / '404.html'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out)
    print('wrote', dest.relative_to(ROOT))

def pillar(p):
    PAGE['path'] = p['path']
    """Hub page (§6.2) with an inline CTA after the grid so no more than three light sections run together."""
    body = (hero(p['eyebrow'], p['hero'], p['sub'])
            + grid(p['grid_h'], p['eyebrow'], p['cards'])
            + icb(*p['icb'])
            + challenges(p['ch_h'], p['ch'])
            + process(p['pr_h'], p['steps'])
            + (comparison(*p['cmp']) if p.get('cmp') else '')
            + cases(p['path'])
            + '\n      ' + WHY + '\n      ' + AWARDS + '\n      ' + form(p['form_h'])
            + faq(p['faq']))
    write(p['path'], body, p['title'], p['desc'], [faq_schema(p['faq'])])

def benefits(h, items, cta='Book discovery call'):
    check = '<svg class="bl__check" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12l5 5L20 6" fill="none" stroke="#3DDC84" stroke-width="2.5"></path></svg>'
    boxes = ''.join(f'''
            <div class="bl__box reveal">{check}
              <h3 class="h4 bl__title">{e(t)}</h3>
              <p class="bl__body">{e(b)}</p>
            </div>''' for t, b in items)
    return f'''
      <section class="section section--gradient on-dark" id="benefits">
        <div class="container">
          <div class="section-head reveal">{headline(h)}</div>
          <div class="bl">{boxes}
            <div class="bl__cta reveal">
              <p class="h4 bl__title">Ready to see this in your own workflows?</p>
              <a href="#cta-form" class="btn btn--invert">{e(cta)}</a>
            </div>
          </div>
        </div>
      </section>'''

def snav(items):
    links = ''.join(f'<a href="#{a}" data-anchor="{a}">{e(l)}</a>' for l, a in items)
    return f'''
      <nav class="snav" aria-label="On this page" data-snav>
        <div class="container snav__row">{links}</div>
      </nav>'''

def service(p):
    """Canonical service page (§6.1): fixed spine, light/dark alternation already checked."""
    PAGE['path'] = p['path']
    nav = [('Challenges', 'challenges'), ('Services', 'services'), ('Process', 'process'), ('Benefits', 'benefits')]
    if p.get('cmp'): nav.append(('Comparison', 'comparison'))
    nav += ([('Case studies', 'case-studies')] if pick_cases(p['path']) else []) + [('Why tkxel', 'why-tkxel'), ('FAQ', 'faq')]
    body = (hero(p['eyebrow'], p['hero'], p['sub'])
            + snav(nav)
            + challenges(p['ch_h'], p['ch'])
            + grid(p['grid_h'], p['eyebrow'], p['cards'])
            + icb(*p['icb'])
            + process(p['pr_h'], p['steps'])
            + benefits(p['bn_h'], p['benefits'])
            + (comparison(*p['cmp']) if p.get('cmp') else '')
            + cases(p['path'])
            + '\n      ' + WHY + '\n      ' + AWARDS + '\n      ' + form(p['form_h'])
            + faq(p['faq']))
    schema = [faq_schema(p['faq']), {'@context': 'https://schema.org', '@type': 'Service', 'name': p['eyebrow'],
              'description': p['sub'], 'provider': {'@type': 'Organization', 'name': 'tkxel', 'url': 'https://tkxel.com'},
              'url': f"https://fde.tkxel.com{p['path']}"}]
    write(p['path'], body, p['title'], p['desc'], schema)


# In-text linking for articles: first mention of a phrase links once per article.
INTERNAL_LINKS = [
  (r'forward deployed engineering', '/what-is-forward-deployed-engineering/'),
  (r'staff augmentation', '/fde-vs-staff-augmentation-vs-consulting/'),
  (r'FDE pods?', '/services/fde-pods/'),
  (r'agentic FDE pod', '/services/agentic-fde-pod/'),
  (r'AI readiness assessment', '/services/ai-readiness-assessment/'),
  (r'AI (?:penetration testing|red teaming)', '/services/ai-penetration-testing/'),
  (r'knowledge assistant', '/services/enterprise-knowledge-assistant/'),
  (r'workflow (?:automation|agentification)', '/services/workflow-agentification/'),
  (r'MCP (?:servers?|integrations?)', '/services/mcp-enterprise-integrations/'),
  (r'data engineering', '/services/data-engineering-fde-pod/'),
  (r'legacy (?:system )?modernization', '/services/integration-legacy-modernization-pod/'),
  (r'AI governance', '/services/ai-security-governance/'),
  (r'engagement models?', '/engagement-models/'),
  (r'AI strategy', '/services/ai-strategy-readiness/'),
  (r'(?:AI )?training programmes?|AI literacy', '/services/adoption-enablement/'),
  (r'AI agents?', '/services/agentic-fde-pod/'),
  (r'guardrails', '/blog/ai-agent-guardrails/'),
  (r'evaluation sets?|golden datasets?|evals|evaluation', '/blog/how-to-evaluate-ai-agents/'),
  (r'human[- ]in[- ]the[- ]loop|human review', '/blog/human-in-the-loop-ai-agents/'),
  (r'prompt injection', '/blog/prompt-injection-explained/'),
  (r'retrieval[- ]augmented generation|RAG', '/blog/rag-vs-fine-tuning/'),
  (r'fine[- ]tuning', '/blog/rag-vs-fine-tuning/'),
  (r'AI pilots?|proofs? of concept', '/blog/why-ai-pilots-fail-to-reach-production/'),
  (r'readiness checklist|AI readiness', '/blog/ai-readiness-checklist/'),
  (r'build (?:vs\.?|versus|or) buy', '/blog/build-vs-buy-ai-agents/'),
  (r'security reviews?', '/services/ai-security-governance/'),
  (r'team structure|pod structure', '/blog/fde-team-structure/'),
  (r'hiring forward deployed engineers|hire forward deployed engineers', '/blog/how-to-hire-forward-deployed-engineers/'),
  (r'integrations?', '/services/mcp-enterprise-integrations/'),
  (r'review queues?', '/services/workflow-agentification/'),
  (r'vector (?:databases?|stores?|search|index(?:es)?)', '/services/enterprise-knowledge-assistant/'),
  (r'permissions?', '/services/ai-security-governance/'),
  (r'autonomy', '/blog/ai-agent-guardrails/'),
  (r'agents', '/services/agentic-fde-pod/'),
]
EXTERNAL_LINKS = [
  (r'OWASP', 'https://genai.owasp.org/', 'OWASP GenAI Security Project'),
  (r'NIST AI (?:RMF|Risk Management Framework)', 'https://www.nist.gov/itl/ai-risk-management-framework', 'NIST AI Risk Management Framework'),
  (r'Model Context Protocol', 'https://modelcontextprotocol.io/', 'Model Context Protocol documentation'),
  (r'EU AI Act', 'https://eur-lex.europa.eu/eli/reg/2024/1689/oj', 'EU AI Act (Regulation 2024/1689)'),
  (r'ISO/IEC 42001|ISO 42001', 'https://www.iso.org/standard/81230.html', 'ISO/IEC 42001'),
  (r'MITRE ATLAS', 'https://atlas.mitre.org/', 'MITRE ATLAS'),
  (r'HIPAA', 'https://www.hhs.gov/hipaa/index.html', 'HHS: HIPAA'),
]
MAX_INTERNAL = 6

class Linker:
    def __init__(self, self_path):
        self.self_path, self.done, self.internal, self.cited = self_path, set(), 0, []
    def __call__(self, text):
        out = e(text)
        for pat, href in INTERNAL_LINKS:
            if href == self.self_path or href in self.done or self.internal >= MAX_INTERNAL:
                continue
            m = re.search(rf'(?<![\w>/])({pat})(?![\w<])', out, re.I)
            if m and not self._inside_link(out, m.start()):
                out = out[:m.start()] + f'<a href="{href}">{m.group(1)}</a>' + out[m.end():]
                self.done.add(href); self.internal += 1
        for pat, href, label in EXTERNAL_LINKS:
            if href in self.done:
                continue
            m = re.search(rf'(?<![\w>/])({pat})(?![\w<])', out)
            if m and not self._inside_link(out, m.start()):
                out = out[:m.start()] + f'<a href="{href}" target="_blank" rel="noopener">{m.group(1)}</a>' + out[m.end():]
                self.done.add(href); self.cited.append((label, href))
        return out
    @staticmethod
    def _inside_link(html_text, pos):
        return html_text.rfind('<a ', 0, pos) > html_text.rfind('</a>', 0, pos)


def _domain(url):
    return re.sub(r'^https?://(www\.)?', '', url).split('/')[0]

def _title_from_url(url):
    """Readable title from a URL slug, e.g. .../mcp-security-governance-enterprise/ -> 'Mcp security governance enterprise'."""
    path = [x for x in re.sub(r'^https?://[^/]+', '', url).split('/') if x and not x.startswith('?')]
    slug = re.sub(r'\.(html?|php|md)$', '', path[-1]) if path else _domain(url)
    words = re.sub(r'[-_]+', ' ', slug).strip()
    if not words or words.isdigit():
        return _domain(url)
    words = words[:1].upper() + words[1:]
    return re.sub(r'\b(mcp|ai|rag|llms?|fde|api|saas|owasp|nist|crm|erp|roi|faq)\b', lambda m: m.group(1).upper(), words, flags=re.I)

def sources_block(refs, reading):
    def item(title, url, rel):
        return (f'<li><a href="{url}" target="_blank" rel="{rel}" class="src__link">'
                f'<span class="src__title">{e(title)}</span><span class="src__domain">{e(_domain(url))}</span>'
                f'<span class="src__arrow" aria-hidden="true">↗</span></a></li>')
    groups = ''
    if refs:
        groups += '<div class="src__group"><span class="eyebrow">Cited sources</span><ol class="src__list">' + ''.join(item(l, h, 'noopener') for l, h in refs) + '</ol></div>'
    if reading:
        groups += '<div class="src__group"><span class="eyebrow">Further reading</span><ol class="src__list">' + ''.join(item(_title_from_url(u), u, 'noopener nofollow') for u in reading) + '</ol></div>'
    return f'''
          <section class="src" aria-labelledby="sources">
            <h2 class="art__h2 src__h" id="sources">Sources and further reading</h2>
            <p class="caption">External pages open in a new tab. tkxel is not responsible for their content.</p>
            {groups}
          </section>'''

def article(p):
    """Guide / blog article layout. New template (design system §7): tokens only, standard section skeleton."""
    L = Linker(p['path'])
    parts = []
    for s in p['sections']:
        sid = re.sub(r'[^a-z0-9]+', '-', s['h2'].lower()).strip('-')[:48]
        chunk = f'\n          <h2 class="art__h2" id="{sid}">{e(s["h2"])}</h2>'
        chunk += ''.join(f'\n          <p>{L(x)}</p>' for x in s.get('paras', []))
        if s.get('bullets'):
            chunk += '\n          <ul>' + ''.join(f'<li>{L(b)}</li>' for b in s['bullets']) + '</ul>'
        for h3, para in s.get('h3s', []):
            chunk += f'\n          <h3 class="art__h3">{e(h3)}</h3>\n          <p>{L(para)}</p>'
        if s.get('table'):
            cap, heads, rows = s['table']
            chunk += (f'\n          <div class="ct__scroll" tabindex="0" role="region" aria-label="{e(cap)}"><table class="ct art__table"><caption class="sr-only">{e(cap)}</caption><thead><tr>'
                      + ''.join(f'<th scope="col">{e(h)}</th>' for h in heads) + '</tr></thead><tbody>'
                      + ''.join('<tr><th scope="row">' + e(r[0]) + '</th>' + ''.join(f'<td>{e(c)}</td>' for c in r[1:]) + '</tr>' for r in rows)
                      + '</tbody></table></div>')
        parts.append(chunk)
    refs = list(dict.fromkeys([tuple(x) for x in p.get('sources', [])] + L.cited))
    reading = [u for u in p.get('research', {}).get('top_urls', []) if u.startswith('http') and u not in {h for _, h in refs}][:4]
    if refs or reading:
        parts.append(sources_block(refs, reading))
    toc = ''.join(f'<li><a href="#{re.sub(r"[^a-z0-9]+", "-", s["h2"].lower()).strip("-")[:48]}">{e(s["h2"])}</a></li>' for s in p['sections'])
    links = [tuple(x) for x in p.get('related', [])]
    same = [q for q in POSTS if q['path'] != p['path'] and set(q.get('tags', [])) & set(p.get('tags', []))][:3]
    links += [(q['h1'], q['path']) for q in same]
    related = ''
    if links:
        related = '<aside class="art__related"><span class="eyebrow">Related</span><ul>' + ''.join(f'<li><a href="{h}" class="link-arrow">{e(l)}</a></li>' for l, h in links) + '</ul></aside>'
    slug = p['path'].strip('/').split('/')[-1]
    cover = ''
    if p.get('tags'):
        (ROOT / p['path'].strip('/')).mkdir(parents=True, exist_ok=True)
        (ROOT / p['path'].strip('/') / 'cover.svg').write_text(COVERS[p['path']])
        cover = f'<img class="art__cover" src="{p["path"]}cover.svg" alt="" width="1200" height="630" />'
    meta = f'<p class="caption art__meta">{e(p["date_label"])} · {p["read_min"]} min read</p>' if p.get('date_label') else ''
    body = f'''
      <section class="art__hero section--gradient on-dark" data-hero>
        <div class="container{' art__hero-grid' if cover else ' art__narrow'}">
          <div>
            <span class="eyebrow">{e(p['eyebrow'])}</span>
            <h1 class="display art__h1">{e(p['h1'])}</h1>
            {meta}
          </div>
          {cover}
        </div>
      </section>
      <article class="section">
        <div class="container art__layout">
          <nav class="art__toc" aria-label="Contents"><span class="eyebrow">Contents</span><ol>{toc}</ol></nav>
          <div class="art__body">
          <p class="art__lede">{e(p['lede'])}</p>{''.join(parts)}
          {related}
          </div>
        </div>
      </article>''' + icb(*p['cta']) + faq(p['faq']) + '\n      ' + form(p.get('form_h', 'Talk to an FDE lead about your project'))
    schema = [faq_schema(p['faq']), {'@context': 'https://schema.org', '@type': 'Article', 'headline': p['h1'], 'description': p['desc'],
              'author': {'@type': 'Organization', 'name': 'tkxel'}, 'publisher': {'@type': 'Organization', 'name': 'tkxel'},
              **({'datePublished': p['date']} if p.get('date') else {}),
              **({'image': f"https://fde.tkxel.com{p['path']}cover.svg"} if p.get('tags') else {}), 'mainEntityOfPage': f"https://fde.tkxel.com{p['path']}"}]
    write(p['path'], body, p['title'], p['desc'], schema)

def index_page(path, title, desc, eyebrow, h, sub, cards, form_h, intro_h=None):
    """Listing page: hero, card grid, form. cards = [(eyebrow, title, body, href or None)]."""
    PAGE['path'] = path
    items = ''.join(
        (f'<a class="idx__card reveal" href="{href}">' if href else '<div class="idx__card reveal">')
        + f'<span class="eyebrow">{e(ey)}</span><h2 class="idx__title">{e(t)}</h2><p class="muted">{e(b)}</p>'
        + ('<span class="link-arrow">Read more</span></a>' if href else '</div>')
        for ey, t, b, href in cards)
    body = (hero(eyebrow, h, sub)
            + f'''
      <section class="section">
        <div class="container">
          {f'<div class="section-head reveal">{headline(intro_h)}</div>' if intro_h else ''}
          <div class="idx">{items}</div>
        </div>
      </section>'''
            + '\n      ' + form(form_h))
    write(path, body, title, desc, [])

def not_found():
    body = '''
      <section class="hero section--gradient on-dark" data-hero style="min-height:80vh">
        <div class="container">
          <span class="eyebrow">Page not found</span>
          <h1 class="display" style="margin-top:20px">This page isn’t here yet</h1>
          <p class="hero__sub">We are still adding pages to this site. The link you followed may point to one that is on the way, or it may have moved.</p>
          <div style="display:flex;gap:16px;flex-wrap:wrap">
            <a href="/" class="btn btn--invert">Go to home page</a>
            <a href="/#cta-form" class="btn btn--invert">Book discovery call</a>
          </div>
        </div>
      </section>'''
    write('/404', body, 'Page not found | tkxel FDE', 'The page you were looking for could not be found.', [])

def contact(faq_items):
    PAGE['path'] = '/contact/'
    body = (hero('Contact', 'Book a discovery call | with an FDE lead', 'Tell us the outcome you want AI to deliver. An FDE lead replies within one business day to set up a 30-minute call, with no cost or commitment.')
            + '\n      ' + form('Tell us about your project') + faq(faq_items))
    write('/contact/', body, 'Contact tkxel FDE | Book a discovery call', 'Book a free 30-minute discovery call with a tkxel forward deployed engineering lead to discuss your AI, data, or integration project.', [faq_schema(faq_items)])

POSTS = []  # filled in main, newest first
CASES = []  # tkxel.com case studies, filled in main

# Which blog topics are relevant to each service / pillar / industry page.
PATH_TAGS = {
  '/services/fde-pods/': ['FDE'], '/services/full-stack-fde-pod/': ['FDE'], '/services/fde-for-saas-isvs/': ['FDE'],
  '/services/agentic-fde-pod/': ['Agents'], '/services/workflow-agentification/': ['Agents'], '/services/agentic-platforms/': ['Agents', 'Integration'],
  '/services/mcp-enterprise-integrations/': ['Integration'], '/services/integration-legacy-modernization-pod/': ['Integration'],
  '/services/enterprise-knowledge-assistant/': ['Data'], '/services/data-engineering-fde-pod/': ['Data'],
  '/services/ai-strategy-readiness/': ['Strategy'], '/services/ai-readiness-assessment/': ['Strategy'], '/services/adoption-enablement/': ['Strategy'],
  '/services/ai-security-governance/': ['Governance'], '/services/ai-penetration-testing/': ['Governance'], '/services/product-engineering/': ['Strategy', 'Agents'],
  '/industries/financial-services/': ['Governance'], '/industries/healthcare/': ['Governance'], '/industries/technology-saas/': ['FDE'], '/industries/logistics-manufacturing/': ['Agents'],
  '/how-fde-works/': ['FDE'],
}

def resources(posts, h='Latest insights & resources'):
    """RESOURCES_GRID (§4.21): type label, title, link."""
    cards = ''.join(f'''
            <a class="idx__card reveal" href="{q['path']}">
              <img class="idx__thumb" src="{q['path']}cover.svg" alt="" width="1200" height="630" loading="lazy" />
              <span class="eyebrow">{e(', '.join(q.get('tags', [])) or 'Article')}</span>
              <h3 class="idx__title">{e(q['h1'])}</h3>
              <p class="caption">{e(q.get('date_label', ''))} · {q.get('read_min', '')} min read</p>
              <span class="link-arrow">Read article</span>
            </a>''' for q in posts)
    return f'''
      <section class="section section--alt" id="resources">
        <div class="container">
          <div class="csc__head reveal"><h2 class="h2">{e(h)}</h2><a href="/blog/" class="link-arrow">All articles</a></div>
          <div class="idx">{cards}
          </div>
        </div>
      </section>'''

def blog_index(meta, guides, posts):
    PAGE['path'] = meta['path']
    tags = sorted({t for q in posts for t in q.get('tags', [])})
    buttons = '<button class="blog__filter is-active" data-filter="all" aria-pressed="true">All</button>' + ''.join(f'<button class="blog__filter" data-filter="{e(t)}" aria-pressed="false">{e(t)}</button>' for t in tags)
    def card(q, label):
        return (f'<a class="idx__card reveal" href="{q["path"]}" data-tags="{e(" ".join(q.get("tags", ["Guide"])))}">'
                + (f'<img class="idx__thumb" src="{q["path"]}cover.svg" alt="" width="1200" height="630" loading="lazy" />' if q.get('tags') else '')
                + f'<span class="eyebrow">{e(label)}</span><h2 class="idx__title">{e(q["h1"])}</h2><p class="muted">{e(q["desc"])}</p>'
                f'<span class="link-arrow">Read more</span></a>')
    items = ''.join(card(g, 'Guide') for g in guides) + ''.join(card(q, f"{', '.join(q.get('tags', []))} · {q['date_label']}") for q in posts)
    body = (hero(meta['eyebrow'], meta['h'], meta['sub'])
            + f'''
      <section class="section">
        <div class="container">
          <div class="blog__filters" role="group" aria-label="Filter articles by topic">{buttons}</div>
          <div class="idx" data-blog-grid>{items}</div>
        </div>
      </section>''' + '\n      ' + form(meta['form_h']))
    write(meta['path'], body, meta['title'], meta['desc'], [])
    # RSS feed for the blog
    from email.utils import format_datetime
    import datetime
    rows = ''.join(f'''
    <item><title>{e(q['h1'])}</title><link>https://fde.tkxel.com{q['path']}</link><guid>https://fde.tkxel.com{q['path']}</guid><pubDate>{format_datetime(datetime.datetime.fromisoformat(q['date']).replace(tzinfo=datetime.timezone.utc))}</pubDate><description>{e(q['desc'])}</description></item>''' for q in posts)
    (ROOT / 'blog/rss.xml').write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>tkxel FDE insights</title><link>https://fde.tkxel.com/blog/</link><description>{e(meta['desc'])}</description>{rows}
</channel></rss>
''')

def load(name, attr):
    f = pathlib.Path(__file__).parent / 'content' / f'{name}.py'
    if not f.exists():
        print('skip (not ready):', name); return []
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return getattr(m, attr)

def load_posts():
    posts = [json.loads(f.read_text()) for f in (pathlib.Path(__file__).parent / 'posts').glob('*.json')]
    return sorted(posts, key=lambda q: q['date'], reverse=True)

if __name__ == '__main__':
    POSTS[:] = load_posts()
    # Assign covers oldest-first so existing posts keep their art when new posts are added.
    COVERS, recent = {}, []
    for q in sorted(POSTS, key=lambda q: (q['date'], q['path'])):
        COVERS[q['path']] = ART.cover_svg(q['path'].strip('/').split('/')[-1], q.get('tags'), avoid=recent[-6:], title=q.get('h1', ''))
        recent.append(ART.cover_svg.last)
    CASES[:] = load('case_studies', 'CASES')
    written = []
    for p in load('content', 'PILLARS'):
        pillar(p); written.append(p['path'])
    for batch in ('content_svc_a', 'content_svc_b', 'content_svc_c'):
        for p in load(batch, 'SERVICES'):
            service(p); written.append(p['path'])
    for p in load('content_ind', 'INDUSTRIES'):
        pillar(p); written.append(p['path'])
    guides = load('content_guides', 'ARTICLES')
    for p in guides:
        article(p); written.append(p['path'])
    for p in POSTS:
        article(p); written.append(p['path'])

    import types
    C = types.SimpleNamespace(**{k: load('content_company', k) for k in ('HOW', 'CONTACT_FAQ', 'INDUSTRIES_INDEX', 'CASES_INDEX', 'BLOG_INDEX')})
    pillar(C.HOW); written.append(C.HOW['path'])
    contact(C.CONTACT_FAQ); written.append('/contact/')
    ii = C.INDUSTRIES_INDEX
    index_page(ii['path'], ii['title'], ii['desc'], ii['eyebrow'], ii['h'], ii['sub'], ii['cards'], ii['form_h']); written.append(ii['path'])
    ci = C.CASES_INDEX
    case_cards = [(c['industry'], c['client'], c['result'], c['url']) for c in CASES]
    index_page(ci['path'], ci['title'], ci['desc'], ci['eyebrow'], ci['h'], ci['sub'], case_cards, ci['form_h']); written.append(ci['path'])
    blog_index(C.BLOG_INDEX, guides, POSTS); written.append(C.BLOG_INDEX['path'])
    not_found()

    # Hand-made pages (home, agentic pod) get the shared header, footer, legal links, art and insights.
    for f in ['index.html', 'services/agentic-fde-pod/index.html']:
        t = (ROOT / f).read_text()
        t = re.sub(r'\n[ \t]*<header class="hdr" data-hdr>.*?</header>', lambda m: '\n    ' + HEADER, t, count=1, flags=re.S)
        t = re.sub(r'\n[ \t]*<footer class="ftr">.*?\n    </footer>', lambda m: '\n    ' + FOOTER, t, count=1, flags=re.S)
        for a, b in LEGAL.items(): t = t.replace(a, b)
        page_path = '/' if f == 'index.html' else '/' + f.replace('index.html', '')
        t = re.sub(r'<svg class="hero__graphic".*?</svg>', lambda m: ART.svg_for(page_path), t, count=1, flags=re.S)
        track = ''.join(f'<span class="hero__logo">{e(l)}</span>' for l in LOGOS) + ''.join(f'<span class="hero__logo" aria-hidden="true">{e(l)}</span>' for l in LOGOS)
        t = re.sub(r'<div class="hero__track">.*?</div>', lambda m: f'<div class="hero__track">{track}</div>', t, count=1, flags=re.S)
        t = re.sub(r'\s*<div class="fc__clutch">.*?</div>', '', t, count=1, flags=re.S)
        t = re.sub(r'\s*<blockquote class="fc__quote">[^<]*Placeholder.*?</blockquote>', '', t, flags=re.S)
        t = re.sub(r'\n[ \t]*<section class="section" id="case-studies">.*?</section>', lambda m: cases(page_path), t, count=1, flags=re.S)
        t = re.sub(r'\s*<!-- resources:start -->.*?<!-- resources:end -->', '', t, flags=re.S)
        picks = POSTS[:3] if f == 'index.html' else [q for q in POSTS if set(q.get('tags', [])) & set(PATH_TAGS.get(page_path, []))][:3]
        title = 'Latest insights & resources' if f == 'index.html' else 'Related insights'
        if picks:
            t = t.replace('\n    </main>', '\n      <!-- resources:start -->' + resources(picks, title) + '\n      <!-- resources:end -->\n    </main>', 1)
        (ROOT / f).write_text(t)

    paths = ['/', '/services/agentic-fde-pod/'] + written
    urls = '\n'.join(f'  <url><loc>https://fde.tkxel.com{x}</loc></url>' for x in dict.fromkeys(paths))
    (ROOT / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')

    # SEO research notes (not linked from the site).
    notes = ['# SEO research notes', '', 'SERP research without Semrush (no search volume data). Keywords chosen from SERP evidence; confirm volumes once Semrush units are available.', '']
    sources = [p for b, a in [('content_svc_a', 'SERVICES'), ('content_svc_b', 'SERVICES'), ('content_svc_c', 'SERVICES'), ('content_ind', 'INDUSTRIES'), ('content_guides', 'ARTICLES')] for p in load(b, a)] + POSTS
    for p in sources:
        r = p.get('research', {})
        notes += [f"## {p['path']}", f"- Primary: {r.get('primary', '')}", f"- Secondary: {', '.join(r.get('secondary', []))}", '- Top URLs:'] + [f'  - {u}' for u in r.get('top_urls', [])] + [f"- Gaps we cover: {r.get('gaps', '')}", '']
    (ROOT / 'docs').mkdir(exist_ok=True)
    (ROOT / 'docs/seo-research.md').write_text('\n'.join(notes))
    print(len(dict.fromkeys(paths)), 'urls in sitemap')
