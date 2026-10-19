import type { ServicePageData } from '../types';
import { fdeDifferentiators } from '../shared';

const page: ServicePageData = {
  meta: {
    title: 'Agentic FDE pod | Forward deployed AI engineers | tkxel',
    description: 'An embedded tkxel pod that designs, evaluates, and ships multi-agent systems inside your environment, then hands the codebase and runbooks to your team.',
  },
  hero: {
    eyebrow: 'Agentic FDE pod',
    headline: 'Engineers inside your team who take AI agents | from pilot to production',
    subhead: 'A small forward deployed pod works in your repos, your data, and your approval chains. Every agent ships with evaluations, guardrails, and a handover plan your team can run.',
    cta_label: 'Book discovery call',
  },
  challenges: {
    headline: 'Why do so many AI agent pilots | never reach production?',
    challenges: [
      { title: 'The demo works, the workflow does not', body: 'Pilots run on clean sample data. Real records carry exceptions, missing fields, and approvals the prototype never saw.' },
      { title: 'Nobody can say how good the agent is', body: 'Without evaluation sets, every prompt change is a guess. Teams stall because they cannot prove the agent is safe to widen.' },
      { title: 'Integration is the hard 80%', body: 'Agents need scoped access to ERP, CRM, and document stores. Vendor tools stop at the API boundary your systems actually sit behind.' },
      { title: 'The partner leaves, the knowledge leaves', body: 'Consulting teams hand over slides. Your engineers inherit code they did not write and cannot safely change.' },
    ],
  },
  services: {
    headline: 'What an agentic FDE pod | builds with you',
    services: [
      { eyebrow: 'Agentic FDE pod', title: 'Use-case scoping and autonomy design', body: 'We map the workflow step by step and decide where the agent acts alone, where it drafts for review, and where a human must approve. The output is an autonomy matrix your risk team can sign.' },
      { eyebrow: 'Agentic FDE pod', title: 'Multi-agent system engineering', body: 'Planner, worker, and reviewer agents built on your chosen model and framework, with tool calls, retries, and state handled explicitly. Code lives in your repositories from the first commit.' },
      { eyebrow: 'Agentic FDE pod', title: 'Evaluation harness and quality gates', body: 'Golden datasets drawn from real cases, automated scoring, and regression checks in CI. Every prompt or model change runs against the same bar before it reaches users.' },
      { eyebrow: 'Agentic FDE pod', title: 'Enterprise system connectors', body: 'Scoped, audited connections to ERP, CRM, ticketing, and document stores, including MCP servers where they fit. Agents get least-privilege access that security can review line by line.' },
      { eyebrow: 'Agentic FDE pod', title: 'Guardrails and human-in-the-loop review', body: 'Input and output validation, policy checks, and review queues that route low-confidence actions to people. Reviewers see the agent’s reasoning and sources before approving.' },
      { eyebrow: 'Agentic FDE pod', title: 'Observability and cost controls', body: 'Tracing for every agent run, dashboards for accuracy and latency, and spend alerts per workflow. You see what each agent did, what it cost, and where it failed.' },
      { eyebrow: 'Agentic FDE pod', title: 'Handover and team enablement', body: 'Pairing with your engineers throughout, runbooks for every agent, and a staged transfer of ownership. The pod exits when your team can extend the system without us.' },
    ],
  },
  inlineCta: {
    headline: 'Have a pilot that stalled before production?',
    body: 'Bring it to a discovery call and we will tell you what it needs to ship.',
    cta_label: 'Review my AI pilot',
  },
  process: {
    headline: 'How an agentic FDE pod | moves from workflow to production',
    steps: [
      { title: 'Discover and scope', timeline: '1–2 weeks', body: 'We sit with the people who run the workflow today, collect real cases, and agree on success metrics. We also confirm data access and approval rules before any code is written.', deliverables: 'Workflow map, autonomy matrix, success metrics, evaluation dataset v1' },
      { title: 'Build the first agent', timeline: '3–6 weeks', body: 'The pod builds one agent end to end inside your environment, wired to real systems and scored against the evaluation set. Your engineers pair on the work from day one.', deliverables: 'Working agent in staging, evaluation report, architecture decision record' },
      { title: 'Harden and release', timeline: '2–4 weeks', body: 'We add guardrails, review queues, tracing, and cost alerts, then release to a limited user group. Autonomy widens only when evaluation scores and reviewer feedback support it.', deliverables: 'Production release, monitoring dashboards, incident runbook' },
      { title: 'Scale and hand over', timeline: '8 weeks onwards, depending on scope', body: 'Additional agents reuse the same connectors, evaluation harness, and controls. Ownership moves to your team in stages until the pod is no longer needed.', deliverables: 'Agent backlog, ownership transfer plan, team enablement sessions' },
    ],
  },
  benefits: {
    headline: 'What an embedded agentic pod | helps you achieve',
    benefits: [
      { title: 'Ship agents, not prototypes', body: 'Work happens in your production environment from the start, so there is no rebuild between pilot and release.' },
      { title: 'Prove quality before you widen access', body: 'Evaluation sets and regression checks give risk and business owners evidence instead of anecdotes.' },
      { title: 'Keep humans where judgment matters', body: 'Review queues route uncertain or high-impact actions to people, so automation grows without losing control.' },
      { title: 'Know what every agent costs', body: 'Per-workflow tracing and spend alerts show cost and accuracy side by side, so you scale what pays back.' },
      { title: 'Own the system after we leave', body: 'Your engineers pair throughout and receive runbooks, so the capability stays when the pod exits.' },
    ],
    cta_label: 'Book discovery call',
  },
  comparison: {
    headline: 'Agent platform, in-house, or FDE pod: | the honest comparison',
    intro: 'Each path works for some teams. The right one depends on how specific your workflows are and how much engineering capacity you have today.',
    columns: ['Off-the-shelf agent platform', 'In-house team', 'tkxel agentic FDE pod'],
    rows: [
      { criterion: 'Time to first production agent', values: ['Fast for standard use cases', 'Slow while hiring and learning', 'Weeks, scoped per workflow'] },
      { criterion: 'Fit to your workflows', values: ['Limited to vendor templates', 'Full', 'Full, built in your stack'] },
      { criterion: 'Evaluation and guardrails', values: ['Vendor-defined', 'Built from scratch', 'Included from week one'] },
      { criterion: 'Who owns the code', values: ['Vendor', 'You', 'You, from the first commit'] },
      { criterion: 'Ongoing cost', values: ['Per-seat or per-run licence', 'Full team salaries', 'Time-boxed pod, then your team'] },
      { criterion: 'Fails when', values: ['Workflows leave the template', 'AI talent is hard to hire', 'Nobody internal is ready to take ownership'] },
    ],
  },
  caseStudies: {
    headline: 'Success stories in spotlight',
    cases: [
      { result_headline: '[Placeholder] Metric-led result for an agentic workflow, followed by the mechanism that produced it.', tags: ['Industry', 'Agentic FDE pod'], quote: 'Placeholder quote — replace with a real client quote.', attributor_role: 'Director of Operations' },
      { result_headline: '[Placeholder] Second agent case study headline that leads with the metric.', tags: ['Industry', 'Workflow agentification'], quote: 'Placeholder quote — replace with a real client quote.', attributor_role: 'VP Engineering' },
      { result_headline: '[Placeholder] Third case study headline that leads with the metric.', tags: ['Industry', 'Enterprise connectors'], quote: 'Placeholder quote — replace with a real client quote.', attributor_role: 'Chief Technology Officer' },
    ],
  },
  differentiators: fdeDifferentiators,
  finalCtaHeadline: 'Ready to put your first agent into production?',
  faq: [
    { question: 'What exactly is a forward deployed engineer?', answer: 'A forward deployed engineer works inside the client’s environment rather than from a separate delivery centre. They join your standups, commit to your repositories, and talk directly to the people who run the workflow. The model comes from product companies that embed engineers with customers to make complex software work in real conditions. At tkxel it means a small pod that builds, ships, and then hands over production systems.' },
    { question: 'How is an FDE pod different from staff augmentation?', answer: 'Staff augmentation adds people to your backlog and you direct the work. An FDE pod owns an outcome, such as a specific agent reaching production, and brings its own delivery method, evaluation tooling, and architecture experience. The pod also plans its own exit, so the engagement ends with your team owning the system rather than depending on extra headcount.' },
    { question: 'Which models and frameworks do you use?', answer: 'We work with the model and cloud your organisation has approved, including Claude, GPT, and Gemini models through their APIs or through Amazon Bedrock, Google Vertex AI, and Azure. Framework choice follows the workflow; we use established agent frameworks where they help and plain code where they add complexity. Everything is documented so your team can swap components later.' },
    { question: 'How large is a pod and how long does it stay?', answer: 'A typical pod is three to five people: a lead engineer, one or two AI engineers, and a data or integration engineer, with a delivery lead shared across the engagement. Most first agents reach a limited production release within two to three months. Larger programmes keep the pod longer while ownership transfers in stages.' },
    { question: 'Can you guarantee the agent will be fully autonomous?', answer: 'No, and we would be cautious of anyone who does. Many workflows include decisions that should stay with a person for regulatory, financial, or customer reasons. We design autonomy per step, release with human review where accuracy is not yet proven, and widen it only when evaluation results support the change. Some steps may stay human-approved permanently, and that is often the right outcome.' },
    { question: 'How do you handle our data and security requirements?', answer: 'The pod works inside your environment under your access controls, so data does not leave systems you approve. Connectors use least-privilege, audited access, and we align with your security review process from the first week. tkxel holds ISO 27001 certification, and we can work within SOC 2, HIPAA, or industry-specific controls your organisation already runs.' },
    { question: 'What do we need to have in place before starting?', answer: 'A named business owner for the workflow, access to real examples of the work, and at least one engineer who will eventually own the system. Clean data is helpful but not required; the discovery phase identifies data gaps and whether they block the first release or can be handled with review steps.' },
  ],
};

export default page;
