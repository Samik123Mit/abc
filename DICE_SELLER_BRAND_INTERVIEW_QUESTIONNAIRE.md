# DICE Seller / Brand Interview Questionnaire

## Purpose

Understand how BPC sellers, brands, creator managers, and agencies make real creator and SKU decisions.

This interview tests:

- `H1`: Creator x SKU mismatch
- `H2`: Sampling friction
- `H3`: BPC content difficulty
- `H4`: Shopper proof gap
- `H5`: Creator economics and attribution
- `H0`: Alternative diagnosis outside the current tree

The interview does not describe or validate a proposed Meesho solution.

## Interview Design

Recommended duration: `12-15 minutes`

Target:
- 3-5 BPC sellers, brands, creator managers, or influencer agencies
- Prefer respondents who have personally selected creators, approved products, allocated samples, or reviewed campaign performance
- Include different price bands and seller/brand sizes where possible

Before starting:
- Ask permission to take notes.
- Offer anonymity.
- Do not request confidential dashboards, customer data, margins, or non-public Meesho information.
- Ask for ranges or directional answers where exact figures are sensitive.

## Opening Script

> Hi, I’m Samiksha from IIT Guwahati. I’m researching creator-led beauty commerce for a student case study. I’m not selling a service or asking you to endorse an idea. I’d like to understand how you actually choose creators and products for campaigns. We can keep your response anonymous. May I take notes?

If permission is granted:

> Please use one recent real campaign or product decision as the example. If you cannot share a detail, “I can’t share that” is completely fine.

## Classification Questions

Use these for segmentation only.

| ID | Question | Capture |
| --- | --- | --- |
| B0.1 | What type of organization or role are you in? | Seller / brand / agency / creator manager / other |
| B0.2 | Which BPC categories do you work with? | Makeup / skincare / haircare / grooming / fragrance / hygiene / other |
| B0.3 | What price bands do you usually work in? | Under Rs 250 / Rs 250-500 / Rs 500-1000 / above Rs 1000 |
| B0.4 | Which creator types do you usually work with? | Nano / micro / mid-tier / macro / mixed |
| B0.5 | Which channels do you use for creator commerce? | Meesho / Instagram / YouTube / marketplace affiliate / agency / other |

## Core Behavioral Walkthrough

Ask the respondent to choose one recent BPC creator campaign or SKU-promotion decision.

| ID | Question | Primary tags | Funnel node |
| --- | --- | --- | --- |
| B1 | Think about the last BPC product for which you selected or approved creators. What was the product and what were you trying to achieve? | `H0-H5` | SKU and campaign objective |
| B2 | How did you identify the creators you considered? | `H1`, `H0` | Brand -> Creator |
| B3 | Which creators did you reject or not shortlist, and why? | `H1`, `H5`, `H0` | Brand -> Creator |
| B4 | What information did you use to decide whether a creator was a fit for that SKU? | `H1`, `H4`, `H0` | Brand -> Creator; SKU -> Audience |
| B5 | How did you decide which SKU or product variant each creator should promote? | `H1`, `H3`, `H0` | Creator -> SKU |
| B6 | Did the creator use or test the product before creating content? Walk me through what happened. | `H2`, `H3`, `H0` | Sampling and trial |
| B7 | Who paid for or supplied the product, and what affected the decision to send or not send it? | `H2`, `H5`, `H0` | Sampling |
| B8 | What did you ask creators to explain or demonstrate in the content? | `H3`, `H4` | Proof creation |
| B9 | What questions, objections, or comments did shoppers generate after seeing the content? | `H4`, `H0` | Shopper decision |
| B10 | What happened after the content went live: clicks, orders, returns, repeat, or no measurable response? | `H4`, `H5`, `H0` | Conversion and repeat |
| B11 | How did you attribute performance to a creator? | `H5`, `H0` | Attribution |
| B12 | What determined whether you repeated spend with that creator or SKU? | `H1`, `H4`, `H5`, `H0` | Re-spend and retention |
| B13 | Looking back, what was the biggest source of wasted effort, sample cost, or missed sales? | `H0-H5` | Economic leakage |

## Neutral Probes

Use only when the initial answer is incomplete. Do not imply that any option is the expected answer.

### Creator selection and fit

| Probe | Tags |
| --- | --- |
| Which mattered more in that decision: audience profile, prior sales, engagement, language, geography, price band, content quality, or something else? | `H1`, `H5`, `H0` |
| Did you have a reliable way to identify which creators could sell that SKU? | `H1`, `H0` |
| Can you recall a creator who looked suitable but did not perform? What did you learn? | `H1`, `H4`, `H0` |
| Did the product or variant change based on the creator’s audience? | `H1`, `H3` |
| What audience information was missing when you made the choice? | `H1`, `H0` |

### Sampling and product access

| Probe | Tags |
| --- | --- |
| How many products were sent, self-funded, or skipped before content was produced? | `H2`, `H5` |
| What caused a sample to be sent, withheld, delayed, or wasted? | `H2`, `H0` |
| Did the product need real use before a credible recommendation was possible? | `H2`, `H3` |
| Did any creator receive a product but decide not to post? Why? | `H2`, `H3`, `H1`, `H0` |

### Content and proof

| Probe | Tags |
| --- | --- |
| Which product claims were easy to demonstrate, and which were difficult to demonstrate? | `H3`, `H4` |
| Did you need content about shade, undertone, skin type, hair type, ingredients, texture, wear, results, or authenticity? | `H3`, `H4`, `H0` |
| What information did creators ask for before they were comfortable posting? | `H3`, `H4`, `H0` |
| Did the content answer the questions shoppers actually asked? | `H4` |
| What happened when the content generated views but few orders? | `H4`, `H5`, `H0` |

### Conversion, returns, and repeat

| Probe | Tags |
| --- | --- |
| Where did shoppers appear to drop out: content, click, product page, payment, delivery, or after use? | `H4`, `H0` |
| What were the common reasons for returns, complaints, or low ratings? | `H0`, `H4` |
| Which signals made you confident that a creator drove incremental sales rather than only reach? | `H5`, `H0` |
| Did repeat purchase or adjacent-category purchase affect the campaign decision? | `H4`, `H5` |

### Economics and attribution

| Probe | Tags |
| --- | --- |
| What costs did the campaign create besides commission: product, shipping, content production, management, returns, or discounts? | `H2`, `H5`, `H0` |
| What performance threshold made a creator or SKU worth repeating? | `H5`, `H1` |
| Which numbers were available quickly, and which were delayed or unavailable? | `H5`, `H0` |
| Did payout, commission, or attribution limitations change creator selection? | `H5`, `H0` |

## H0 Alternative-Diagnosis Prompt

Ask after the core walkthrough:

> Looking back at this campaign, what was the biggest factor that made creator-led BPC growth harder than expected?

Only after the open response, use the neutral checklist:

- product quality or authenticity
- assortment or product availability
- price or value
- delivery
- returns
- seller reliability or communication
- creator discovery or platform UX
- attribution or reporting
- commission or payout
- weak demand in a specific subcategory
- content quality or proof
- something else

Record the respondent’s wording before assigning `H0`.

## Closing Questions

| ID | Question | Tags |
| --- | --- | --- |
| B14 | What is one recent creator/SKU decision you would make differently today? | `H0-H5` |
| B15 | What information would have changed that decision at the time? | `H1`, `H3`, `H4`, `H5`, `H0` |
| B16 | What have I not asked that materially affects creator-led BPC performance? | `H0-H5` |

Do not suggest matching, proof modules, samples, AI, commissions, or any other solution before the respondent answers.

## Evidence Capture Sheet

Complete immediately after each interview.

| Field | Entry |
| --- | --- |
| Respondent ID | B-___ |
| Role | Seller / brand / agency / creator manager |
| Category and price band |  |
| Date | YYYY-MM-DD |
| Consent to notes | Yes / no |
| Anonymous quote permission | Yes / no |
| Recent campaign/SKU example |  |
| Exact behavior observed |  |
| Funnel node | Selection / SKU / sample / content / click / purchase / return / repeat / payout |
| Hypothesis tag | H0 / H1 / H2 / H3 / H4 / H5 / NEW |
| Polarity | Supports / contradicts / neutral |
| Economic outcome | NMV / conversion / return / repeat / creator retention / brand re-spend / unclear |
| Direct quote | Only with permission |
| Researcher inference | Keep separate from the quote |
| Confidence | Low / medium / high |
| Contradiction to record |  |
| Follow-up needed |  |

## Explicit Kill Criteria

### H1: Creator x SKU mismatch

Kill or materially modify H1 if:
- brands reliably identify suitable creators with existing data or manual processes;
- rejected creators fail for reasons unrelated to SKU/audience fit;
- mismatch does not affect content quality, conversion, repeat, or re-spend.

### H2: Sampling friction

Kill or materially modify H2 if:
- sampling is already easy, inexpensive, and rarely wasted;
- creators generally receive or self-fund products without this affecting activation;
- sample access does not affect content creation or creator willingness to continue.

### H3: Content difficulty

Kill or materially modify H3 if:
- BPC content requires no more proof or effort than comparable categories;
- creators already have a standard, sufficient content format;
- content effort does not affect posting, conversion, returns, or re-spend.

### H4: Shopper proof gap

Kill or materially modify H4 if:
- shopper objections are mainly price, delivery, or availability;
- existing content and product pages answer the important decision questions;
- proof quality does not affect conversion, returns, repeat, or campaign re-spend.

### H5: Creator economics and attribution

Kill or materially modify H5 if:
- creator selection and repeat spend are driven mainly by fit or demand, not economics;
- commission, payout, and attribution are sufficiently clear;
- economics do not explain creator inactivity or brand budget withdrawal.

### H0: Alternative diagnosis

Elevate H0 if:
- a non-H1-H5 issue repeatedly appears in real campaign decisions;
- it affects a measurable funnel node or re-spend decision;
- it has higher funnel impact and addressability than the leading H1-H5 candidates;
- it can be named precisely enough to test in 30 days.

## Interviewer Guardrails

- Do not say “matching engine,” “Beauty Proof,” “smart sampling,” or “decision engine” before the behavioral walkthrough is complete.
- Do not ask “Would you use this?” or “Would more samples help?” as validation questions.
- Do not request confidential company metrics.
- Do not turn one respondent’s opinion into a market claim.
- Do not discard contradictions or inconvenient evidence.
- Use `Unknown` when the respondent does not know.
