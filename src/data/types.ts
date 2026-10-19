// Content contracts from the design system §4, expressed as types so a page
// that underfills or misshapes a section fails the build instead of shipping.
export interface ServicePageData {
  meta: { title: string; description: string };
  hero: { eyebrow: string; headline: string; subhead: string; cta_label: string };
  challenges: { headline: string; intro?: string; challenges: { title: string; body: string }[] };
  services: { headline: string; intro?: string; services: { eyebrow: string; title: string; body: string; href?: string }[] };
  inlineCta: { headline: string; body?: string; cta_label: string };
  process: { headline: string; steps: { title: string; body: string; deliverables?: string; timeline?: string }[] };
  benefits: { headline: string; benefits: { title: string; body: string }[]; cta_label: string };
  comparison?: { headline: string; intro?: string; columns: string[]; rows: { criterion: string; values: string[] }[]; highlight?: number };
  caseStudies: { headline: string; cases: { result_headline: string; tags: string[]; quote: string; attributor_role: string; href?: string }[] };
  differentiators: { headline: string; points: { title: string; body: string }[]; cta_label: string };
  finalCtaHeadline: string;
  faq: { question: string; answer: string }[];
}
