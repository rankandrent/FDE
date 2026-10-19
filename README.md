# fde.tkxel.com

Forward Deployed Engineering microsite for tkxel. Astro static build → plain HTML in `dist/`, hosted on Cloudflare Pages.

## Commands
- `npm install`
- `npm run dev` — local dev server at http://localhost:4321
- `npm run build` — static HTML to `dist/`
- `npm run preview` — serve the built site

## How pages are built
- Design tokens: `src/styles/global.css` (design system §2)
- Sections: `src/components/sections/` — one component per design-system §4 section
- Service pages: add a data file in `src/data/services/<slug>.ts` (typed by `src/data/types.ts`)
  and a 4-line route in `src/pages/services/<slug>.astro`. `ServicePage.astro` fixes the §6.1 order.
- Headline soft break: write ` | ` in a headline string; it collapses on mobile.

## Before launch (open items)
- Replace `[Placeholder]` case studies, testimonials, Clutch badge, client logos, office addresses
- Lead form posts to `/api/lead` — add a Cloudflare Pages Function that forwards to HubSpot/CRM/email
- Add `public/og-default.png`
- Confirm placeholder color tokens (§2.1)

## Deploy (Cloudflare Pages)
1. Push this repo to GitHub, then Cloudflare → Pages → Connect repo
2. Build command `npm run build`, output directory `dist`
3. Custom domain `fde.tkxel.com` (CNAME `fde` → `<project>.pages.dev` if DNS is outside Cloudflare)
