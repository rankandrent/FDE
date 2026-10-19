# fde.tkxel.com

Forward Deployed Engineering microsite for tkxel — plain HTML, CSS and JavaScript. No build step.

## Structure
```
index.html                          Home page
services/agentic-fde-pod/index.html Service page
assets/css/styles.css               All styles (design tokens at the top)
assets/js/main.js                   All interactions (header, menus, timeline, form)
sitemap.xml, robots.txt, favicon.svg
```

## Adding a new page
1. Copy an existing page folder, e.g. `services/agentic-fde-pod/` → `services/data-engineering-fde-pod/`.
2. Edit the text inside `index.html`: `<title>`, meta description, canonical URL, then each section.
3. Add the URL to `sitemap.xml`.
4. If the page should appear in the menu, update the header/footer links in every page.

Headline soft line breaks use `<span class="br"><br /></span>` — they hide automatically on mobile.

## Preview locally
Run `python3 -m http.server 8000` in this folder and visit http://localhost:8000.

## Deploy (Cloudflare Pages)
Workers & Pages → Create → Pages → Connect to Git → this repo.
Framework preset **None**, build command **empty**, build output directory **/**. Every push to `main` goes live.

## Before launch (open items)
- Replace `[Placeholder]` case studies, testimonials, Clutch badge, client logos, office addresses
- Lead form posts to `/api/lead` — needs a Cloudflare Pages Function forwarding to HubSpot/CRM/email
- Add `og-default.png`
