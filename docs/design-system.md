# tkxel Page Design System

**Purpose:** given a body of content, produce a fully designed, on-brand tkxel.com page by assembling
sections from the library below. Reuse an existing section whenever the content fits its contract.
Design a new section only when no existing section fits, and only under the rules in §7.

**How to read this document**

- §1–3 are constraints. They apply to every page and are not negotiable per-page.
- §4 is the section library. Each entry has a *content contract* — the fields the section needs.
  If your content can fill the contract, use that section.
- §5 is the routing procedure: content shape → section. Start here when generating a page.
- §6 is page assembly: canonical section order per page type.
- §7 covers designing new sections. §8 is QA. §9 is known anti-patterns.

> **Before first use:** §2.1 has a handful of color tokens (`--tk-surface-alt`, `--tk-accent-soft`,
> `--tk-text`, `--tk-text-muted`, `--tk-border`) still on sensible placeholder values, not pulled from
> the stylesheet. §2.3 layout/spacing values are likewise sensible defaults, not yet confirmed against
> the live site. Everything else in this document — including the rest of §2 — was derived from the
> actual page structures of `/`, `/services/ai-agents-workflows-agentic-os/`, and
> `/services/cloud-migration/`, or confirmed directly from the theme, and can be trusted as-is.

---

## 1. Brand foundations

### 1.1 What tkxel is

An AI-native technology partner for growing and mid-market businesses. Nearly two decades old, ~800
professionals, ~150 in AI. The company sells modernization, AI integration, and custom software as a
*strategic partnership*, not as staff augmentation.

### 1.2 Voice

The site's voice is unusually disciplined for the category. Preserve these traits:

| Trait | What it means in practice |
|---|---|
| **Outcome-anchored** | Every claim resolves to a business metric: time, cost, accuracy, risk, capacity. Never "cutting-edge" or "world-class." |
| **Specific over superlative** | "reduce manual effort by up to 70%" beats "dramatically reduce effort." If you don't have a number, describe the mechanism instead. |
| **Honest about limits** | The Cloud Migration FAQ says outright that zero downtime isn't promised for every workload. Keep this. Hedged, accurate claims are a brand asset. |
| **Sentence case** | Headings are sentence case, not Title Case. `Cloud migration services built for scale` — not `Cloud Migration Services Built For Scale`. Eyebrows are the exception (all caps). |
| **Second person** | "your systems," "your workflows." The reader's business is the subject; tkxel is the verb. |
| **Plain verbs** | assess, migrate, connect, govern, route, validate. Avoid leverage, unlock, empower, revolutionize. |

**Sentence length:** body paragraphs run 1–3 sentences, 20–45 words total. Longer than that and the
card layouts break rhythm.

**Never write:** "In today's fast-paced digital landscape," "game-changing," "seamless" (as filler),
"solutions that scale" without saying what scales.

### 1.3 Content principles

- **One idea per section.** If a section is trying to say two things, it's two sections.
- **Claims carry sources.** Third-party statistics always show the source logo and link out (see
  `CHALLENGE_STATS`). Unsourced statistics do not go in that section.
- **Every section earns its scroll.** If a section only restates the hero, cut it.

---

## 2. Design tokens

### 2.1 Color

`--tk-dark`, `--tk-white`, `--tk-accent`, and `--tk-gradient` are confirmed against the live theme.
`--tk-surface-alt`, `--tk-accent-soft`, `--tk-text`, `--tk-text-muted`, and `--tk-border` are sensible
placeholder values, not yet pulled from the stylesheet — swap them for the real hex/rgba once verified.
The *roles* below are confirmed from page structure and should not change.

| Token | Role | Value |
|---|---|---|
| `--tk-dark` | Primary dark surface. Used for process, final CTA, and other "anchor" sections. | `#1B232E` |
| `--tk-white` | Default light section background; also text on dark surfaces. | `#FFFFFF` |
| `--tk-surface-alt` | Secondary light background, used to separate two adjacent light sections. | `#F7F8FA` |
| `--tk-accent` | Primary brand blue. Buttons, link arrows, active tab underline. | `#0755E9` |
| `--tk-gradient` | Radial gradient, deep navy to accent blue. Hero/dark section backgrounds; stat numbers. | `radial-gradient(140.86% 125.07% at 10.25% 0%, #10347E 0%, #0755E9 100%)` |
| `--tk-accent-soft` | Tint of accent for card hover states and icon backplates. | `rgba(7, 85, 233, 0.10)` |
| `--tk-text` | Body text on light. | `#14181F` |
| `--tk-text-muted` | Secondary text, eyebrows, captions, source attributions. | `#6B7280` |
| `--tk-border` | Card and divider hairlines. | `#E4E7EB` |

**Alternation rule.** Sections alternate between light and dark to segment the page. Never place two
dark sections adjacent. Never run more than three light sections consecutively without a
`--tk-surface-alt` or dark break. On a standard service page the dark sections are: `HERO` (with its
embedded `CLIENT_LOGO_STRIP`), `INLINE_CTA_BAND`, `BENEFITS_LIST`, `DIFFERENTIATORS`, and
`FINAL_CTA_FORM`. **`PROCESS_TIMELINE` is light**, not dark — this reverses the earlier draft of this
doc. Everything else is light. `HERO`, `INLINE_CTA_BAND`, `BENEFITS_LIST`, and `DIFFERENTIATORS` use
`--tk-gradient`; `FINAL_CTA_FORM` uses flat `--tk-dark`. Because there are now five dark sections
instead of three, check adjacency against the actual page order in §6.1 rather than assuming — the
fixed spine keeps them separated, but a reordered or trimmed page could violate this rule if you're not
careful.

### 2.2 Type

**Font families** — Plus Jakarta Sans for all type; IBM Plex Mono reserved for eyebrow labels only
(all caps).

| Role | Usage | Spec |
|---|---|---|
| **Display** | H1 only | 52px desktop / 34px mobile, bold, leading ~1.1 |
| **H2** | Section headings | 44px desktop / 30px mobile, **extrabold**, sentence case |
| **H3** | Card titles, step titles | 32px desktop / 24px mobile, bold |
| **H4** | Sub-card titles, benefit items | 24px, medium |
| **Eyebrow** | Section labels above H2 and category tags on cards | IBM Plex Mono, 14px, ALL CAPS, letter-spacing ~0.08em, `--tk-text-muted` (or `--tk-accent` when active) |
| **Body** | Paragraphs | 18px, regular, leading ~1.6 |
| **Caption** | Source attributions, timelines, deliverables | 14px, `--tk-text-muted` |
| **Stat** | Big numbers in `CHALLENGE_STATS` and `STATS_BAND` | 72px, `--tk-gradient` (gradient-filled text) on light; solid `--tk-white` on dark sections |

**Headline line breaks.** H1 and several H2s use a deliberate soft break to control line ragging
(`Migrate to the Cloud With a Strategy / Built for Stability and ROI`). When generating headlines,
insert the break so lines are of near-equal length and the break falls at a phrase boundary — never
mid-phrase. Breaks must collapse on mobile.

### 2.3 Layout & spacing

| Token | Value |
|---|---|
| Content max width | 1280px |
| Gutter (desktop / mobile) | 40px / 20px |
| Section vertical padding (desktop / mobile) | 96px / 64px |
| Card radius | `0` — sharp corners sitewide |
| Grid | 12-column desktop, 6-column tablet, 1-column mobile |

**Sharp corners.** No rounded corners anywhere: cards, buttons, tags, form fields, the inline CTA
band, cookie consent, tab pills. `--tk-radius` is `0` and every other border-radius in the system
should resolve to it. The one exception is genuinely circular elements — icon backplates, badges, dot
markers — which are a distinct shape, not a rounded corner, and stay circles (`border-radius: 50%`).

**Card grid defaults:** 3-up desktop / 2-up tablet / 1-up mobile for icon and service cards.
`BENEFITS_LIST` runs 3-up (last cell is the CTA); `DIFFERENTIATORS` runs 4-up. Both collapse to
1-up on mobile.

### 2.4 Components

- **Primary button** — filled `--tk-accent`, `--tk-white` label, sentence case, verb-first
  (`Book AI discovery call`, `Discuss cloud migration`, `Plan your cloud migration`).
  Almost always anchors to `#cta-form` rather than navigating away.
  **On dark/gradient backgrounds (`HERO`, `INLINE_CTA_BAND`, `BENEFITS_LIST`, `DIFFERENTIATORS`,
  `FINAL_CTA_FORM`) the button inverts:** filled `--tk-white`, `--tk-dark` label. Never a blue button
  on a dark background, and never a white button on a light one.
  **Height is fixed at 48px** across every instance — header, hero, inline bands, forms, cookie
  consent — regardless of horizontal padding. Don't let a "compact" context (header chrome, cookie
  banner) shrink it.
- **Secondary / text link** — label + right-arrow icon in `--tk-accent`.
- **Card** — `--tk-surface` on `--tk-border` hairline, radius per token, arrow affordance bottom-right
  on interactive cards.
- **Tab rail** — horizontal labels, not boxed/pill tab controls. Plus Jakarta Sans, sentence case
  (`Financial services`, not `FINANCIAL SERVICES`), active item underlined in `--tk-accent`,
  horizontally scrollable on mobile. No background fill or border on individual items — the underline
  is the only active-state affordance. Used by `INDUSTRY_TABS`, `TECH_TABS`, and the optional tab
  variant of `SERVICE_GRID`. **Do not confuse this with `SECTION_NAV`** (§4.3) — that's a different
  component, set in mono/ALL CAPS. Tab rail stays sans/sentence case.
- **Accordion** — full-width row, title left, +/− toggle right.

### 2.5 Motion

Restrained. Scroll-triggered fade-and-rise on section entry, logo marquees on the client strips,
step advance on the process timeline, accordion expand. Respect `prefers-reduced-motion`. Do not add
parallax, counters that count up, or per-card stagger beyond a single subtle sequence.

---

## 3. Global page frame

Every page inherits these. They are not authored per-page.

| Element | Notes |
|---|---|
| **Global header** | Fixed. Transparent over the hero with `--tk-white` text/logo so it reads against the dark hero background; once scrolled past the hero it switches to a solid `--tk-white` background with `--tk-text` and a `--tk-border` hairline. Mega menu across Services (6 categories) / Customers / Company / Careers / Resources, plus search and a `Get in touch` button. Each services flyout carries a SPOTLIGHT resource card. |
| **Global footer** | Full services sitemap by category, Solution Implementation, Business Enablement, Engagement Models, contact details, newsletter signup, four office addresses (USA, Saudi Arabia, Portugal, Pakistan), social, legal row. |
| **Cookie consent** | Standard, with Customize / Accept All. |

**Removed: the bottom-anchored promo bar.** An earlier draft of this doc specified a full-width
strip pinned to the bottom of the viewport promoting the current webinar or the AI workflow discovery
agent. It's been cut — it fought with the cookie consent for the same screen real estate and added a
persistent element with no clean dismissal story. If a page needs to promote a live webinar, route that
content through `RESOURCES_GRID` or a `promo_card` on `CLIENT_LOGO_STRIP` instead.

---

## 4. Section library

Notation: **[R]** = required field, **[O]** = optional.

---

### 4.1 `HERO`

**Used on:** every page. **Background:** dark (gradient).

The eyebrow names the service; the H1 makes the promise; the paragraph qualifies it; one button. The
client logo strip is not a separate section — it's the closing element of the hero itself, sharing the
hero's gradient background with no visual seam between them.

**Content contract**
- `eyebrow` [R] — the service or page name, 2–5 words
- `headline` [R] — 7–12 words, with one soft break
- `subhead` [R] — 1–2 sentences, 20–40 words, stating the mechanism or the guarantee
- `cta_label` [R] — verb-first, 3–5 words
- `cta_target` [R] — usually `#cta-form`
- `graphic` [O] — abstract brand illustration, right side, desktop only
- `client_logos` [R] — see `CLIENT_LOGO_STRIP` contract below; rendered inside the hero, near the
  bottom

**Rules**
- Exactly one CTA. Never a secondary button in the hero.
- The subhead must add information, not restate the headline in other words.
- No stats in the hero. Stats belong to `CHALLENGE_STATS`.
- The CTA button inverts on this dark background: filled `--tk-white`, `--tk-dark` label — not the
  usual `--tk-accent` fill. See §2.4.
- **The hero (copy + graphic + embedded logo strip together) fits in one fold.** `min-height: 100vh`
  with the content vertically centered, so nothing below the logos requires a scroll on a standard
  viewport. Keep vertical spacing tight enough to hold that — this is the one section where the usual
  `--tk-pad` section padding doesn't apply as-is.

---

### 4.2 `CLIENT_LOGO_STRIP`

**Used on:** embedded inside `HERO`, as its closing element — not a standalone section. **Background:**
inherits the hero's dark gradient.

**Content contract**
- `label` [R] — short caps label (`RELATED CLIENTS`, `OUR CLIENTS`, `WE'VE OPTIMIZED FOR`)
- `logos` [R] — 6–14 client logos, full brand color, shown at reduced opacity ("ghosted") against the
  dark background — not monochrome
- `promo_card` [O] — a single resource card inline with the strip (Cloud Migration does this with the
  FinOps webinar)

**Rules:** logos are normalized to a single optical height, rendered in brand color at reduced opacity
rather than monochrome, and marquee continuously with a fade-to-transparent mask on both edges of the
row (not a hard clip). Because it lives inside the hero, it never gets its own section padding or
background — it's the last visual beat of the hero block. **No divider line (border/rule) above the
logo row** — the gap in spacing is what separates it from the hero copy above, not a hairline.

---

### 4.3 `SECTION_NAV`

**Used on:** long service pages. **Background:** light, sticky on scroll.

Anchor jump-links to the major sections below it. Observed sets:
`Challenges · Services · Process · Benefits · Workflow · Use cases · Case studies · Our solution`
`Challenges · Services · Process · Case studies · Why choose us · Partners`

Items are set in `IBM Plex Mono`, **ALL CAPS**, matching the eyebrow treatment — not `Plus Jakarta
Sans`, and not styled as literal pill/tab UI (no background, no border, just an underline on the active
item). This is a typographic and casing distinction from `SERVICE_GRID`'s tab rail or `INDUSTRY_TABS`,
which stay in sentence-case body sans — don't let the two bleed into each other.

**Content contract**
- `items` [R] — 4–8 `{label, anchor}` pairs, in page order

**Rules:** include only sections actually present. Active item highlights on scroll. Horizontally
scrollable on mobile. Omit this section on pages under ~6 sections. Set in `IBM Plex Mono`, ALL CAPS.

---

### 4.4 `CHALLENGE_STATS` — challenges *with* numbers

**Used on:** the problem slot, when third-party data exists. **Background:** light.

Three stat *columns* framing the problem the service solves, each sourced. **Not cards** — there is no
border or fill behind each stat. Each column is marked only by a thin `--tk-accent` rule across its top
edge, and the three columns sit at staggered vertical baselines (one lower, one taller, one in between)
so the row reads like an ascending bar chart. The stagger is a layout offset, not an actual bar height —
content length doesn't need to change.

**Content contract**
- `headline` [R] — posed as a question. `Do these cloud migration challenges sound familiar?` /
  `Are you facing any of these challenges too?`
- `stats` [R] — exactly **3**, each:
  - `value` [R] — `75%`, `3x`, `95%`
  - `claim` [R] — one sentence, ≤25 words, completing the number
  - `source_logo` [R] and `source_label` [R] — e.g. McKinsey, PwC, IBM, Accenture, Flexera, Gartner
  - `source_url` [R] — links to the primary research

**Rules**
- Three stats. Not two, not four — the layout is built for three staggered columns.
- **Every stat is sourced and linked.** This is a hard rule. An unsourced number goes in
  `CHALLENGE_PROSE` instead, phrased as an observation rather than a statistic.
- The claim reads as a continuation of the number, not a standalone sentence.
- Mix framings: two problem-framed stats plus one opportunity-framed stat reads better than three of
  either.
- No card border, background fill, or shadow behind a stat. The top rule is the only container device.

---

### 4.5 `CHALLENGE_PROSE` — challenges *without* numbers

**Used on:** the problem slot, when no citable data exists. **Background:** light.

Same slot and same job as `CHALLENGE_STATS`, without the statistical scaffolding. Use when the
problem is real but the research isn't citable, or when the pain is qualitative. Renders as **separate
segments, each with its own short `--tk-accent` top rule** (matching `CHALLENGE_STATS`) — a real gap
sits between segments so the rule reads as N distinct marks, not one bar spanning the row. **No
vertical divider lines between segments, and no card border, background, or shadow** — the gap itself
is the only separator.

**Content contract**
- `headline` [R] — question-framed, same as above. May contain one `--tk-accent`-highlighted phrase or
  number for rhetorical emphasis (`Why do 90% of machine learning models struggle to reach
  production?`) — this is a framing device in the headline, not a cited statistic, and does not
  reclassify the section as `CHALLENGE_STATS`. Don't attribute a source to it.
- `intro` [O] — 1–2 sentences
- `challenges` [R] — 3–5 items, each:
  - `title` [R] — the pain, named from the reader's side (`Approvals stall between teams`).
    22px, bold — this overrides the generic H4 spec in §2.2, which is too light/small for this slot.
  - `body` [R] — 1–2 sentences on why it happens or what it costs
  - `icon` [O]

**Rules**
- Name symptoms the reader recognizes, not categories. `Nobody can tell which agent touched the
  record` beats `Governance challenges.`
- Do not resolve the pain here. The resolution is the next section.
- Never fabricate a statistic to qualify for `CHALLENGE_STATS`. Use this section instead.
- Segments are separated by gap only — never add a vertical divider hairline between them.

---

### 4.6 `SERVICE_GRID`

**Used on:** every service page, the core offering section. **Background:** light.

Cards rest at title-only: `CATEGORY` eyebrow top-left, then the title — **no custom illustration or
icon, no visible body copy at rest.** On hover, the card fills with the `--tk-gradient` brand gradient,
text inverts to white, the body copy fades in below the title, and the corner affordance flips from an
up-arrow (rest) to a down-arrow (hover) — an expand indicator, not a "go to" link. **Card height is
fixed, not `min-height`** — tall enough to fit the longest title + longest revealed body without
growing, so hovering never resizes the card or reflows its neighbors; the body copy occupies its final
layout space at rest too, just at `opacity: 0`, rather than animating in via height. The grid is
**always a single horizontally scrollable row, never a wrapping multi-row grid** — cards keep a fixed
width and overflow-x scrolls, on desktop as well as mobile. **The row bleeds past the section's
container on the right edge only** — left padding (matching `--tk-gutter`) still aligns the first card
with the rest of the page, but there's no right padding, so the last card can scroll all the way to the
viewport edge instead of being clipped short by the section's right gutter. When the offering has named sub-categories, add a
tab rail above the row (`Tab title 1` / `Tab title 2`, sentence case per §2.4, first active) plus
prev/next carousel arrows top-right next to the headline.

**Content contract**
- `headline` [R] — declarative, states the shape of the offering, or `[Category] services we offer`
  when tabbed
- `tabs` [O] — 2+ category tabs, when the offering splits into named groups
- `services` [R] — 6–11 items, each:
  - `eyebrow` [R] — the category, repeated across all cards (`MIGRATION SERVICE`,
    `AI AGENTS, WORKFLOWS & AGENTIC OS`)
  - `title` [R] — H3, 3–7 words, noun-phrase
  - `body` [R] — 1–3 sentences, ~30–60 words, describing what is actually done — revealed on hover
  - `link` [O] — arrow affordance

**Rules**
- The repeated eyebrow is intentional: it groups the cards as one family. Don't vary it per card.
- Titles are noun phrases (`Database and data platform migration`), not verb phrases.
- Bodies name concrete artifacts and methods — schema conversion, cutover planning, landing zones,
  autonomy boundaries. Vagueness here is the most common failure mode.
- Keep card bodies within ±20 words of each other so the grid doesn't rag.
- Only one card is in the hovered/gradient-filled state at a time.

---

### 4.7 `INLINE_CTA_BAND`

**Used on:** between heavy sections, typically after `SERVICE_GRID`. **Background:** dark (gradient),
**full-bleed** — the band spans edge to edge of the viewport, breaking out of the page container
entirely. Not a contained/rounded card inset within the section.

A breather that converts mid-scroll. Headline sits left, subline + button sit right, both vertically
centered within the band. **The headline is an H2**, same as any other section heading — this section
doesn't get a demoted heading level just because it's compact.

**Content contract**
- `headline` [R] — question or imperative, 6–12 words, rendered as H2
- `body` [O] — one sentence, no more than ~100 characters
- `cta_label` [R], `cta_target` [R]

**Rules**
- At most two of these per page, well separated. The headline should pick up the objection raised by
  the section above it.
- Full-bleed means no side gutters and no card radius — it's the one section allowed to ignore the
  content max-width.
- The CTA button inverts on this dark background: filled `--tk-white`, `--tk-dark` label. See §2.4.

---

### 4.8 `PROCESS_TIMELINE`

**Used on:** every service page. **Background:** light.

Numbered delivery phases, but **not a horizontal stepper** — a split layout. Left column: a large
numeral (`01`, `02`, …) matching the active step, above a decorative isometric stack illustration where
one layer is solid `--tk-accent` (the active layer) and the rest are pale/translucent tints of it. Right
column: a vertical accordion list of every step's numeral + title; only the active step expands to show
its body copy, the rest stay collapsed to a single line, separated by hairlines. **Hovering a step in
the right column expands it and lights up the matching layer in the left illustration** — the two are
linked, not independent. On mobile, the illustration drops and the accordion stacks full-width.

**Content contract**
- `headline` [R] — `A proven path to AI agents that deliver business results` /
  `Our approach for [service]`
- `illustration` [R] — layered/stacked graphic with one highlightable layer per step
- `steps` [R] — 3–6 items, each:
  - `number` [R] — `01`…`06`
  - `title` [R] — 2–4 words, verb-led (`Assess and audit`, `Design and architecture`)
  - `body` [R] — 2–3 sentences, shown only when the step is active/hovered
  - `deliverables` [O] — pipe- or comma-separated list of concrete artifacts
  - `timeline` [O] — `1 day`, `4–6 weeks`, `10 weeks onwards`
  - `substeps` [O] — where a phase contains distinct named engagements, each with its own
    timeline and deliverables (see the AI Agents page)

**Rules**
- **Numbering is only valid because these are genuinely sequential.** Do not reuse the numbered
  treatment for non-sequential content — use `SERVICE_GRID` or `BENEFITS_LIST` instead.
- Exactly one step is expanded/active at a time — first step by default, before any hover.
- Deliverables are nouns the client receives. `Readiness scorecard` — not `Full visibility.`
- Timelines are ranges, and open-ended phases say so (`10 weeks onwards, depending on rollout scope`).
- On touch devices without hover, tap-to-expand replaces hover; keep the illustration-sync behavior.

---

### 4.9 `BENEFITS_LIST`

**Used on:** after the process. **Background:** dark (gradient).

A grid of outlined boxes — each box has its **own full light-white stroke on all four sides**
(`rgba(255,255,255,~0.25)`) and a **transparent fill** (the section's gradient shows through, not a
flat dark fill). Boxes are genuinely separated by a real gap (~24px), not touching or sharing a hairline
— this is not a table/grid-line effect. Each box pairs a green checkmark with an `Outcome N`-style title
and muted body text beneath. The grid runs 3-up; the final cell is not a benefit box but a small "call
to action" label plus the primary button, closing the grid instead of sitting below it. **The CTA
cell's label is set at the same size/weight as the other boxes' titles** — it's a peer of the benefit
titles, not a smaller caption.

**Content contract**
- `headline` [R] — `What a well-planned cloud migration helps you achieve`
- `benefits` [R] — 4–6 items, each:
  - `title` [R] — H4, verb-led outcome (`Migrate with less disruption`, `Keep costs under control`)
  - `body` [R] — one sentence naming the mechanism that produces the outcome
- `cta_label` [R], `cta_target` [R] — rendered as the grid's final cell, not a row below it; label uses
  the same type spec as `benefits[].title`

**Rules**
- Every benefit pairs an outcome with its mechanism. The outcome is the title; the mechanism is the
  body. A benefit with no mechanism is a slogan — cut it.
- Quantify where honest, and hedge where appropriate: *"helping multi-step workflows move 40–60%
  faster where repetitive steps can be automated."* The qualifier is part of the brand voice.
- Boxes are outlined, not filled — full border on every box, transparent background, sharp corners,
  real gap between boxes (not a shared hairline grid).
- The CTA button inverts on this dark background: filled `--tk-white`, `--tk-dark` label. See §2.4.

---

### 4.10 `TYPOLOGY_CARDS`

**Used on:** pages where the offering has distinct *kinds*. **Background:** light. Icon cards, 3-up.

**Content contract**
- `headline` [R] — `Types of AI agents we can build`
- `types` [R] — 4–6 items, each:
  - `icon` [R]
  - `title` [R] — the type name
  - `body` [R] — 2–3 sentences
  - `use_cases` [R] — a labelled inline list: `Use cases: invoice validation, PO processing, …`

**Rules:** the `Use cases:` line is what makes this section land — it converts an abstract category
into recognizable work. Never omit it. 5–8 use cases per card.

---

### 4.11 `CAPABILITY_ACCORDION`

**Used on:** when a platform or framework has named components that need explaining without dominating
the page. **Background:** light.

**Content contract**
- `headline` [R] — `The Agentic OS your AI agents need before they scale`
- `items` [R] — 4–8, each with `icon` [R], `title` [R], `body` [R] (1–2 sentences)

**Rules:** first item expanded by default. Use when the content is reference material the reader
scans rather than reads — otherwise use `SERVICE_GRID`.

---

### 4.12 `INDUSTRY_TABS`

**Used on:** service pages with cross-vertical applicability. **Background:** light.

Tab rail of industries; each panel is a short intro, a bullet list, and an image.

**Content contract**
- `headline` [R] — `AI agent use cases across industries`
- `industries` [R] — 4–8 tabs, each:
  - `name` [R] — Financial services, Healthcare, Retail and ecommerce, Manufacturing, Logistics,
    Legal services, Software and IT
  - `intro` [R] — one sentence on what the service does for this vertical
  - `bullets` [R] — **exactly 5**, each one line, verb-led
  - `image` [R]

**Rules**
- Five bullets per industry. Consistency across tabs is what makes the section scannable.
- The fifth bullet conventionally describes the most advanced/orchestrated application, giving each
  panel the same escalating shape.
- Bullets must be genuinely vertical-specific. If a bullet would read identically under three tabs,
  rewrite it.
- First tab active on load. Horizontally scrollable rail on mobile.

---

### 4.13 `LEAD_MAGNET`

**Used on:** mid-page, once. **Background:** light. Copy + form left, asset cover right.

**Content contract**
- `headline` [R] — `Download the Cloud Migration Readiness Checklist`
- `bullets` [R] — exactly 3, each naming something the asset contains
- `form` [R] — inline, minimal fields
- `cta_label` [R] — `Download now`
- `cover_image` [R] — rendered asset cover

**Rules:** one per page. The three bullets describe contents, not benefits of downloading.

---

### 4.14 `CASE_STUDY_CAROUSEL`

**Used on:** every service page and the homepage. **Background:** light.

**Content contract**
- `headline` [R] — `Success stories in spotlight` / `Featured success stories`
- `link_all` [R] — `All case studies` → `/our-customers/`
- `cases` [R] — 3–5, each:
  - `result_headline` [R] — **leads with the metric**: `48% reduction in migration-related downtime
    through structured sequencing and staged cutovers.`
  - `tags` [R] — industry + capability tags
  - `client_logo` [O] and `thumbnail` [R]
  - `quote` [R] + `attributor_name` [O] + `attributor_role` [R]
  - `link` [O] — to the full case study
  - `video` [O] — play affordance for video testimonials

**Rules**
- Result headline always leads with the number and states the mechanism after it.
- Where a client can't be named, use role-only attribution (`Director of Operations`). Never invent a
  name.
- Filter to cases relevant to the page's service.

---

### 4.15 `DIFFERENTIATORS`

**Used on:** late-page, the "why us" slot. **Background:** dark (gradient).

Headline is centered, not left-aligned, with the primary button directly beneath it — also centered.
Below that, a 4-up grid of translucent "glass" cards (semi-transparent white fill over the gradient,
**no border** — background tint only, sharp corners): title at top, body beneath. No illustration, no
left/right split.
Card title is **24px**. The gap between title and body is not fixed — the title sits at the top of the
card and the body at the bottom, so both edges align across cards of different height (`justify-content:
space-between` on the card, not a fixed margin).

**Content contract**
- `headline` [R] — `Title explaining the benefits of working with tkxel for this service`
- `cta_label` [R], `cta_target` [R] — centered directly beneath the headline
- `points` [R] — exactly 4, each `title` [R] (H4) + `body` [R] (2–3 sentences)

**Rules**
- Four points. The observed pattern covers: *approach/sequencing*, *team composition*,
  *controls and governance*, *measurement*. Keep that spread — it answers the four real buyer
  objections.
- The headline is positioned against a named alternative (`not isolated AI demos`). Keep the contrast.
- Cards are translucent glass, not opaque — the gradient must show through them. **No border, ever** —
  the tint alone separates the card from the background.
- The CTA button inverts on this dark background: filled `--tk-white`, `--tk-dark` label. See §2.4.

---

### 4.16 `PARTNERS`

**Used on:** cloud and platform pages. **Background:** light.

**Content contract**
- `headline` [R] — `Partnered with the world's top cloud providers`
- `partners` [R] — each with `logo` [R], `badge` [O] (certification badge), `body` [R] (2 sentences
  on what the partnership gives the client)

**Rules:** the body describes client benefit, not tkxel's status. Only list partnerships that are
current and verifiable.

---

### 4.17 `TECH_TABS`

**Used on:** technical service pages. **Background:** light. **Centered.**

Headline and tab rail are center-aligned (the one section-head exception to the usual left alignment).
**Unlike every other tab rail, this one has no bottom border/divider line under it** — the rail floats
directly above the tech row with nothing underneath it. Tech items render as a single centered row —
**not individual bordered pill boxes** — separated by thin vertical divider hairlines between columns,
each with a small caps mono label above a centered logo mark.

**Content contract**
- `headline` [R] — `Tools & technologies` / `Our expertise and technologies with [service]`
- `categories` [R] — 2–4 tabs (`LLMs · Agent Frameworks · Vector Stores`,
  `Cloud platforms · Infrastructure · CI/CD & observability`)
- Each tab: 4–8 `{name, logo}` pairs

**Rules**
- Only list technologies actually used in delivery. Logos monochrome or brand-correct, consistently
  one or the other.
- Items are divided by vertical hairlines, not boxed individually — no per-item border or fill.
- If the row overflows on mobile, it scrolls horizontally rather than wrapping to a grid.

---

### 4.18 `AWARDS`

**Used on:** every service page and the homepage. **Background:** `--tk-white` — plain white, not
`--tk-surface-alt`. Global block — same content everywhere.

**Content contract**
- `headline` [R] — `We've been recognized by the best, year after year`, standard H2 (44px/30px,
  extrabold, centered), capped at `max-width: 600px` so it wraps to two lines rather than running the
  full container width
- `awards` [R] — badge + label. Current set: Inc. 5000, Top 15 Inspiring Workplaces,
  Titan Business Platinum (AI & Automation), Financial Times, Mogul People Leader,
  Forbes Coaches Council, ISO 27001, ISO 20000, ISO 9001, CMMI DEV 3.

**Rules:** maintained centrally. Do not author or reorder per page. Don't shrink the headline below
the standard H2 size to fit — the `max-width` is what controls the wrap, not a smaller font.

---

### 4.19 `FINAL_CTA_FORM`

**Used on:** every page, immediately before the FAQ. **Background:** dark.

**Content contract**
- `headline` [R] — page-specific and forward-looking (`Ready to build your next AI agent?`,
  `Start your cloud migration with a clear, actionable strategy`)
- `clutch_badge` [R]
- `testimonials` [R] — rotating; global set (Knowles, Sterne Kessler, Replenium, ABB)
- `form` [R] — fields: interest dropdown, first name*, last name*, work email*, job title*, phone,
  project description, marketing consent, SMS consent. Terms/Privacy line beneath.

**Rules**
- The form is global and identical across pages. Only the headline is authored per page.
- The headline states the next step, not the value proposition again.

---

### 4.20 `FAQ`

**Used on:** every service page. **Background:** light. Accordion.

**Content contract**
- `headline` [R] — `Frequently asked questions`
- `items` [R] — 6–8, each `question` [R] + `answer` [R] (1–2 paragraphs, 50–120 words)

**Rules**
- Questions are the ones buyers actually ask, phrased as they'd ask them
  (`How do I know if my business is ready for cloud migration?`).
- Answers may name methods, frameworks, and specific technologies — this is where technical depth
  and SEO long-tail live.
- **At least one answer should state a limitation or a trade-off.** This is a deliberate brand
  behaviour, not an oversight.
- Mirror into FAQPage schema markup.

---

### 4.21 `RESOURCES_GRID`

**Used on:** page footer area, above global footer. **Background:** light.

**Content contract**
- `headline` [R] — `Latest insights & resources`
- `link_all` [R]
- `items` [R] — 6–20, each `type_label` [R] (Article / Webinar / White paper / Podcast),
  `thumbnail` [R], `title` [R], `link` [R]

**Rules:** filtered by topical relevance to the page. Automated from the CMS, not hand-authored.

---

### 4.22 Homepage-only sections

| Section | Contract |
|---|---|
| `STATS_BAND` | Headline + CTA, then 4 stats: value + two-line label (`18+ / YEARS ON MARKET`, `800+ / PROFESSIONALS ON BOARD`, `150+ / AI Professionals`, `73% / of clients return for long-term partnerships`). |
| `SERVICE_CATEGORY_GRID` | 4 category cards (AI & Data Innovation, Engineering, Cloud & Security, Digital Strategy Consulting), each with icon, title, and 5–8 linked child services. |
| `ENGAGEMENT_MODELS` | 3 cards: icon, title, one sentence, CTA. Dedicated Team / Offshore Development Center / Fixed Price Projects. |
| `PODCAST_RAIL` | Headline + `All podcasts`, then 4 episode cards with guest and host. |
| `FEATURED_RESOURCE_BAND` | Single asset: cover, title, one-line description, download CTA, `Browse all white papers`. |

---

### 4.23 `COMPARISON_TABLE`

**Used on:** service pages where buyers naturally weigh build/buy/partner alternatives. **Background:**
light. New section, added by the AI Customer Support Automation page.

**Content contract**
- `headline` [R] — states the comparison, not a verdict (`Off-the-shelf, in-house, or a partner — the
  honest comparison`)
- `intro` [O] — one sentence framing why the comparison matters
- `columns` [R] — exactly **3**, each `{label}` — the alternatives being compared, ending with tkxel
- `rows` [R] — 5–8, each `{criterion, values: [3 short phrases, one per column]}`
- `highlight_column` [R] — index of the column to visually emphasize (the tkxel column)

**Rules**
- The highlighted column must include a **"fails when" row naming tkxel's own failure mode**, not just
  the alternatives'. This is the section's honesty test — omitting it turns a comparison into an ad.
- Cell values are short phrases (≤6 words), not sentences. The section reads as a scan, not prose; if a
  cell needs a full sentence, the row belongs in `DIFFERENTIATORS` instead.
- Mobile: the table scrolls horizontally inside its own container rather than reflowing to cards —
  reflowing loses the row-by-row comparison that's the point of the section.

---

## 5. Routing: content shape → section

Work through the content in order. For each block, match the **shape** — not the topic.

| If the content is… | Use |
|---|---|
| A promise + qualifier + one action | `HERO` |
| 3 items, each a number + claim + citable source | `CHALLENGE_STATS` |
| 3–5 named problems with no citable data | `CHALLENGE_PROSE` |
| 6–11 peer capabilities in one category, unordered | `SERVICE_GRID` |
| 3–6 **ordered** phases with deliverables and/or timelines | `PROCESS_TIMELINE` |
| 4–6 outcomes, each with a mechanism | `BENEFITS_LIST` |
| 4–6 *kinds* of a thing, each with example applications | `TYPOLOGY_CARDS` |
| 4–8 components of one platform, reference-style | `CAPABILITY_ACCORDION` |
| The same offering restated per vertical | `INDUSTRY_TABS` |
| Named tools grouped into 2–4 categories | `TECH_TABS` |
| 4 reasons to choose tkxel over an alternative | `DIFFERENTIATORS` |
| Named client outcomes with metrics and quotes | `CASE_STUDY_CAROUSEL` |
| A downloadable asset with 3 described contents | `LEAD_MAGNET` |
| Named alliances with client benefit | `PARTNERS` |
| A multi-column comparison of buying paths (e.g. build vs. buy vs. partner) | `COMPARISON_TABLE` |
| Q&A pairs | `FAQ` |
| A single conversion prompt between two dense sections | `INLINE_CTA_BAND` |

**Disambiguation rules**

1. **Ordered vs unordered decides timeline vs grid.** If reordering the items loses information, it's
   `PROCESS_TIMELINE`. If it doesn't, it's `SERVICE_GRID`. Never number a grid.
2. **Sourced vs unsourced decides the challenge variant.** Citable data → `CHALLENGE_STATS`.
   Otherwise → `CHALLENGE_PROSE`. Never invent a source to unlock the stat layout.
3. **Capability vs kind decides grid vs typology.** `SERVICE_GRID` is *what we do*.
   `TYPOLOGY_CARDS` is *what you get*. Content with a natural `Use cases:` line is a typology.
4. **Scanned vs read decides accordion vs grid.** Reference material the reader skims →
   `CAPABILITY_ACCORDION`. Material that carries the argument → `SERVICE_GRID`.
5. **If content overflows a contract's item cap, split or cut — don't stretch the section.** A
   `SERVICE_GRID` with 18 cards is two sections or a shorter list, never one long grid.
6. **If content underfills a contract, don't pad.** Three stats are required; if you have two, use
   `CHALLENGE_PROSE`.

---

## 6. Page assembly

### 6.1 Canonical service page

```
HERO (incl. CLIENT_LOGO_STRIP)   [dark, gradient]
SECTION_NAV                      [light, sticky]
CHALLENGE_STATS |
CHALLENGE_PROSE                  [light]
SERVICE_GRID                     [light]
INLINE_CTA_BAND                  [dark, gradient, full-bleed]
PROCESS_TIMELINE                 [light]
BENEFITS_LIST                    [dark, gradient]
TYPOLOGY_CARDS                   [light]      — optional
CAPABILITY_ACCORDION             [light]      — optional
INDUSTRY_TABS                    [light]      — optional
LEAD_MAGNET                      [light]
CASE_STUDY_CAROUSEL              [light]
DIFFERENTIATORS                  [dark, gradient]
PARTNERS                         [light]      — optional
TECH_TABS                        [light, centered]
AWARDS                           [light]
FINAL_CTA_FORM                   [dark]
FAQ                              [light]
RESOURCES_GRID                   [light]
```

**Fixed spine — never reorder:** `HERO` (with embedded `CLIENT_LOGO_STRIP`) → challenge →
`SERVICE_GRID` → `PROCESS_TIMELINE` → … → `FINAL_CTA_FORM` → `FAQ` → `RESOURCES_GRID`.

The narrative is: *promise → proof of trust → problem → what we do → how we do it → what you get →
who we've done it for → why us → act.* Optional sections slot into the middle without disturbing it.
Five sections are now dark instead of three (`HERO`, `INLINE_CTA_BAND`, `BENEFITS_LIST`,
`DIFFERENTIATORS`, `FINAL_CTA_FORM`) — the order above already keeps at least one light section
between every pair, but re-check the alternation rule if you ever reorder or drop a section.

**Minimum viable service page:** `HERO` (with `CLIENT_LOGO_STRIP`), challenge, `SERVICE_GRID`,
`PROCESS_TIMELINE`, `CASE_STUDY_CAROUSEL`, `AWARDS`, `FINAL_CTA_FORM`, `FAQ`, `RESOURCES_GRID`.

**Length target:** 14–20 sections. Below 10 the page reads thin for the category; above 22 it reads
padded.

### 6.2 Category / hub page

```
HERO (incl. CLIENT_LOGO_STRIP) → SERVICE_GRID (children) → CHALLENGE_* → PROCESS_TIMELINE
→ CASE_STUDY_CAROUSEL → DIFFERENTIATORS → AWARDS → FINAL_CTA_FORM → FAQ → RESOURCES_GRID
```

### 6.3 Homepage

```
HERO → SERVICE_CATEGORY_GRID → STATS_BAND → CLIENT_LOGO_STRIP → CASE_STUDY_CAROUSEL
→ ENGAGEMENT_MODELS → AWARDS → PARTNERS → FEATURED_RESOURCE_BAND → PODCAST_RAIL
→ FINAL_CTA_FORM → RESOURCES_GRID
```

The homepage is the one page where `CLIENT_LOGO_STRIP` still runs as its own standalone (light)
section rather than embedded in the hero — §4.2's hero-embedded treatment is the service-page default.

---

## 7. Designing a new section

Only when no existing section fits the content's shape. Test it: run the content through §5 twice. If
two different sections *almost* fit, one of them fits — pick it.

**Constraints**

1. **Tokens only.** No new colors, type sizes, radii, or spacing values. If the section needs a new
   token, the section is wrong.
2. **Inherit the section skeleton.** Optional eyebrow → H2 (sentence case, optional soft break) →
   optional intro → content → optional CTA. Same vertical padding as its neighbours.
3. **Respect the alternation rule.** Declare light or dark and check both adjacencies.
4. **One new section per page, maximum.** A page with two novel sections is a page that has drifted
   off-brand.
5. **Define a content contract before designing the layout.** Required fields, optional fields, item
   count minimum and maximum. A section without a contract can't be reused, which defeats the point.
6. **Structure must encode meaning.** Numbering means sequence. Tabs mean mutually exclusive
   alternatives. An accordion means reference material. Don't use a structural device decoratively.
7. **Design mobile first.** Every observed section collapses to a single column. Tab rails scroll,
   steppers stack, grids linearize.
8. **Spend novelty in one place.** If the layout is new, keep the type and color treatment
   conventional. If the treatment is new, keep the layout conventional.

**Ship it back into the library.** Any new section that works gets added to §4 with its contract, so
the second page that needs it reuses rather than reinvents.

---

## 8. QA checklist

**Brand**
- [ ] All headings sentence case; eyebrows all caps
- [ ] No banned filler language (§1.2)
- [ ] Every statistic sourced and linked
- [ ] At least one honest limitation stated somewhere (usually FAQ)
- [ ] Every benefit pairs an outcome with a mechanism

**Structure**
- [ ] Fixed spine intact and in order
- [ ] No two dark sections adjacent; no more than three light sections without a break
- [ ] `SECTION_NAV` items match the sections actually present
- [ ] Numbering used only for genuinely sequential content
- [ ] Every section contract fully satisfied — no padded or starved sections
- [ ] Exactly one `LEAD_MAGNET`; at most two `INLINE_CTA_BAND`

**Content**
- [ ] H1 soft break falls at a phrase boundary and collapses on mobile
- [ ] Card bodies within ±20 words of their siblings
- [ ] Industry tabs have exactly 5 bullets each, genuinely vertical-specific
- [ ] Typology cards all carry a `Use cases:` line
- [ ] Case study headlines lead with the metric
- [ ] No invented client names — role-only attribution where unnamed

**Technical**
- [ ] All CTAs resolve (`#cta-form` anchor exists)
- [ ] Single H1; heading levels don't skip
- [ ] Images have descriptive alt text; logos normalized to one optical height
- [ ] Responsive at 375 / 768 / 1440
- [ ] Visible keyboard focus; tabs and accordions keyboard-operable
- [ ] `prefers-reduced-motion` respected
- [ ] Meta title, description, canonical, OG image set
- [ ] FAQ mirrored into FAQPage schema

---

## 9. Anti-patterns

**Raw content dumped below the designed page.** The live Cloud Migration page ends with a run of
unstyled blocks — a bare markdown table of the 6 R's, a bullet list of "Proven Results," a
"Your Migration in 90 Days" list — sitting after the fully designed sections. This content is good;
its treatment isn't. It reads as pasted, it duplicates claims made above with different numbers, and
it breaks the page's rhythm right before conversion. **Never append content that hasn't been routed
through §5.** A comparison table is a real content shape and deserves a real section; build it and
add it to the library.

**Contradicting your own numbers.** That same page states 75% of migrations run over budget in
`CHALLENGE_STATS` and 87% fail on first attempt further down, with different framing and no source.
Statistics on a page must be mutually consistent and sourced once.

**Superlative drift.** "Perfect," "guaranteed," "zero downtime" as blanket promises. The brand's
credibility comes from hedged, mechanism-backed claims. The FAQ that declines to promise zero
downtime is doing more selling than the section that promises it.

**Numbering non-sequences.** The `01/02/03` treatment is earned by `PROCESS_TIMELINE` because the
phases genuinely happen in order. Applied to a capability list it becomes decoration and devalues it
where it matters.

**Every section a card grid.** Alternate structural devices — grid, timeline, tabs, accordion,
split-with-illustration, carousel — so the page has texture. Three consecutive 3-up card grids read
as one long undifferentiated list.

**Restating the hero.** If a section's headline could be swapped with the H1 without loss, cut the
section.
