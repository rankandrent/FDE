# Daily blog post procedure

Followed by the scheduled routine once per day. Output: one pull request adding one blog post. Never push to `main`.

## 1. Pick the topic
- Open `tools/topics.md` and take the first line that starts with `- [ ]`.
- Parse `slug | primary keyword | tags`. If `tools/posts/<slug>.json` already exists, mark the line `- [x]` and take the next one.
- If no unchecked topics remain, open a PR that only adds 15 new topics to `tools/topics.md` (same format, distinct keywords) and stop.

## 2. SERP research (no search volumes — never invent them)
- WebSearch (mode "standard") the primary keyword, plus 1–2 variants and one question-style phrasing.
- Try WebFetch on the 3–5 best non-academic results. If WebFetch fails, work from search summaries and say so in the PR.
- Note the H2/H3 topics the top results cover, the questions they answer, and what they miss.
- Statistics are allowed only if a source states them; name the source in the same sentence. Never invent clients, results or quotes.

## 3. Write `tools/posts/<slug>.json`
Copy the shape of an existing file such as `tools/posts/how-to-evaluate-ai-agents.json`. Required keys:
- `path`: `/blog/<slug>/`
- `title`: ≤65 characters, contains the primary keyword, ends with `| tkxel FDE`
- `desc`: 140–160 characters, contains the primary keyword
- `eyebrow`: `Article`; `h1`: sentence case, contains the primary keyword
- `lede`: 40–60 words, a direct answer that starts with the subject (AI Overview friendly)
- `date`: today, ISO `YYYY-MM-DD`; `date_label`: e.g. `October 21, 2026`; `read_min`: integer
- `tags`: from the topic line (allowed: FDE, Agents, Governance, Data, Strategy, Integration)
- `sections`: 5–8 objects `{ "h2", "paras": [...], optional "bullets", optional "h3s": [[h3, para]], optional "table": [caption, [headers], [[row label, ...cells]]] }`, 1,100–1,800 words in total. Each section opens with a direct answer sentence.
- `related`: 2–3 `[label, href]` pairs pointing to existing service or guide pages (check the file exists).
- `cta`: `[headline 6–12 words, body ≤100 chars, button label 3–5 words verb-first]`
- `faq`: 5–6 `[question, answer]`; questions phrased the way people search; first sentence of each answer answers directly; 50–110 words each
- `form_h`: forward-looking headline
- `research`: `{ "primary", "secondary": [...], "top_urls": [...], "gaps" }`

### Voice (design system §1.2)
- Sentence case headings. Second person ("your team"). Plain verbs: assess, build, connect, govern.
- Outcome-anchored and specific. Describe mechanisms rather than superlatives.
- Never use: seamless, cutting-edge, world-class, game-changing, leverage, unlock, empower, revolutionize, "In today's fast-paced".
- Paragraphs 2–4 sentences. State at least one honest limitation or trade-off.
- tkxel facts you may use: AI-native technology partner, about 18 years, about 800 professionals, about 150 in AI, offices in the USA, Saudi Arabia, Portugal and Pakistan, ISO 27001. FDE pods are 3–5 engineers who own one outcome inside the client environment and hand over.
- Use the typographic apostrophe ’ inside text.

## 4. Build and check
```
python3 tools/build.py
python3 tools/check.py
```
Fix every problem `check.py` reports, then re-run both until it prints `OK`.

## 5. Mark the topic and open the PR
- Change the topic line to `- [x]`.
- Branch `blog/<slug>`, commit everything (post JSON, regenerated HTML, sitemap, rss, topics.md).
- Open a PR to `main` titled `Blog: <h1>`. In the body list: primary keyword, top URLs, whether WebFetch worked, every statistic with its source, and anything a reviewer should verify.
- The site goes live only when the PR is merged.
