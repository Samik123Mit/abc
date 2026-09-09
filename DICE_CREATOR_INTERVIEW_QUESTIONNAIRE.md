# DICE Creator Interview Questionnaire

## Purpose

Identify where value leaks in the creator-to-repeat BPC funnel by reconstructing real recent behavior.

This interview is designed to validate or kill:

- `H1`: Creator x SKU mismatch
- `H2`: Sampling friction
- `H3`: BPC content difficulty
- `H4`: Shopper proof gap
- `H5`: Creator economics
- `H0`: Alternative diagnosis outside the current tree

The interview does not test or promote a proposed solution.

## Interview Design

Recommended duration: `12-15 minutes`

Target:
- 4-6 BPC creators
- 3-4 non-BPC creators for comparison
- Mix of active/inactive creators, audience sizes, languages, and locations where possible

Before starting:
- Ask permission to take notes.
- Ask whether the respondent wants to remain anonymous.
- Do not request passwords, private dashboards, payment screenshots, or confidential Meesho information.
- Do not promise that any answer will affect Meesho or a competition outcome.

## Opening Script

> Hi, I’m Samiksha from IIT Guwahati. I’m researching how creators choose and recommend products for a student case study. This is not a sales pitch, and I’m not asking you to endorse an idea. I’d like to understand what you actually did for a recent product promotion. Your response can be anonymous. May I take notes for research?

If permission is granted:

> Please answer based on a real recent example rather than what you think creators generally do. If you do not remember something, “I don’t know” is completely fine.

## Classification Questions

Use these only to segment the sample. Do not use them as evidence by themselves.

| ID | Question | Capture |
| --- | --- | --- |
| C0.1 | What categories do you usually create content for? | BPC / fashion / home / lifestyle / other |
| C0.2 | Have you promoted or linked a product through Meesho or another affiliate/creator program in the last 90 days? | Yes / no; platform |
| C0.3 | Roughly how many products did you promote in the last 90 days? | Count or range |
| C0.4 | Which best describes your audience? | City/region, language, broad age band, stated audience profile |
| C0.5 | Do you usually create content alone or with a team? | Individual / team; relevant effort context |

## Core Behavioral Walkthrough

Use one specific recent product. For BPC creators, prioritize a beauty/personal-care product. For non-BPC creators, use the most comparable recent product.

| ID | Question | Primary tags | Funnel node |
| --- | --- | --- | --- |
| C1 | Think about the last product you promoted. What was it, and when did you promote it? | `H0-H5` | Product selection |
| C2 | How did you first find or receive that product opportunity? | `H1`, `H0` | Brand -> Creator; discovery |
| C3 | What other products did you consider at the time? | `H1`, `H5`, `H0` | Creator -> SKU |
| C4 | What made you choose this product rather than the alternatives? | `H1`, `H5`, `H0` | Creator -> SKU |
| C5 | What made you reject or ignore the other products? | `H1`, `H2`, `H5`, `H0` | Creator -> SKU; trial |
| C6 | Before posting, did you personally use or test the product? Walk me through what happened. | `H2`, `H3`, `H0` | Product trial |
| C7 | Who paid for or supplied the product, and how long did you have it before posting? | `H2`, `H5`, `H0` | Product trial |
| C8 | What did you need to learn about the product before you felt comfortable recommending it? | `H3`, `H4`, `H0` | Proof creation |
| C9 | What did you actually show or explain in the content? | `H3`, `H4` | Proof creation |
| C10 | How long did the full process take, from deciding to promote through posting? | `H2`, `H3`, `H5` | Creator effort |
| C11 | What questions or objections did viewers ask after seeing the content? | `H4`, `H0` | User decision |
| C12 | What happened after posting: clicks, orders, returns, repeat questions, or no visible response? | `H4`, `H5`, `H0` | Click -> purchase -> repeat |
| C13 | How did you know whether the post worked? | `H5`, `H0` | Attribution |
| C14 | Based on that experience, would you promote a similar product again? Why or why not? | `H1-H5`, `H0` | Retention |

## Neutral Probes

Use only when the initial answer is vague. Do not read the entire list to the respondent.

### Product fit and matching

| Probe | Tags |
| --- | --- |
| What did you know about your audience that influenced the choice? | `H1` |
| Did the seller or platform give you any information about who the product was for? | `H1`, `H0` |
| Did you choose the product because it fit your audience, because it paid well, because it was easy to make content for, or for another reason? | `H1`, `H3`, `H5`, `H0` |
| Can you recall a product that looked suitable but performed poorly with your audience? What happened? | `H1`, `H4`, `H0` |

### Trial and sampling

| Probe | Tags |
| --- | --- |
| Have you ever paid for a product before recommending it? Tell me about the most recent example. | `H2`, `H5` |
| Have you ever received a product but decided not to post about it? Why? | `H2`, `H3`, `H1`, `H0` |
| Did delivery time, product cost, or uncertainty affect whether you tested it? | `H2`, `H0` |
| What usually happens when you cannot try a product before recommending it? | `H2`, `H3`, `H4` |

### Beauty-specific proof

Ask these for BPC creators; ask non-BPC creators the closest equivalent.

| Probe | Tags |
| --- | --- |
| Which product attributes were hardest to judge or explain? | `H3`, `H4` |
| Did viewers ask about shade, undertone, skin type, hair type, ingredients, texture, wear time, results, or authenticity? | `H3`, `H4`, `H0` |
| Which questions could you answer from your own test, and which could you not answer? | `H3`, `H4` |
| Compared with your non-beauty content, what took more or less effort? | `H3`, `N1` |

### Economics and attribution

| Probe | Tags |
| --- | --- |
| What costs did you bear for this promotion, including product, delivery, production, or time? | `H2`, `H5` |
| What did you earn or expect to earn, if you are comfortable sharing a range? | `H5` |
| How clear were the clicks, orders, returns, and payout numbers to you? | `H5`, `H0` |
| What would make you stop promoting a category even if the products were relevant? | `H5`, `H0` |
| What would make you continue promoting a category even if one post performed poorly? | `H5`, `H1`, `H4` |

## H0 Alternative-Diagnosis Prompt

Ask after the behavioral walkthrough, without suggesting a list first:

> Looking back at this workflow, what was the biggest thing that made the promotion harder, less profitable, or less likely to happen again?

Only after the open answer, use the neutral checklist:

- product quality or authenticity
- assortment or lack of suitable products
- price or value
- delivery
- returns
- seller communication or reliability
- creator-platform user experience
- tracking or attribution
- commissions or payout
- weak audience demand
- something else

Record the respondent’s own wording before assigning `H0`.

## Non-BPC Comparison Module

Ask the same creator to compare one BPC and one non-BPC promotion if they have done both.

| ID | Question | Tags |
| --- | --- | --- |
| NC1 | Which promotion required more product testing before you were comfortable posting? | `H2`, `H3`, `N1` |
| NC2 | Which required more explanation to answer audience questions? | `H3`, `H4`, `N1` |
| NC3 | Which was easier to match to your audience, and why? | `H1`, `N1` |
| NC4 | Which was easier to measure or monetize? | `H5`, `H0`, `N1` |
| NC5 | Which would you be more likely to promote again? What drove that decision? | `H1-H5`, `H0`, `N1` |

## Closing Question

> If you could change one part of the current creator-product promotion workflow, what would you change first?

Do not suggest matching, samples, proof modules, AI, commissions, or any other solution before the respondent answers.

## Evidence Capture Sheet

Complete immediately after each interview.

| Field | Entry |
| --- | --- |
| Respondent ID | C-___ |
| Segment | BPC / non-BPC |
| Date | YYYY-MM-DD |
| Consent to notes | Yes / no |
| Anonymous quote permission | Yes / no |
| Recent product example |  |
| Exact behavior observed |  |
| Funnel node | Selection / trial / content / click / purchase / return / repeat / payout |
| Hypothesis tag | H0 / H1 / H2 / H3 / H4 / H5 / N1 / NEW |
| Polarity | Supports / contradicts / neutral |
| Economic outcome | NMV / conversion / return / repeat / retention / brand re-spend / unclear |
| Direct quote | Only with permission |
| Researcher inference | Keep separate from the quote |
| Confidence | Low / medium / high |
| Contradiction to record |  |
| Follow-up needed |  |

## Explicit Kill Criteria

Do not mark a hypothesis “supported” merely because a creator mentions it. Look for concrete behavior and commercial consequence.

### H1: Creator x SKU mismatch

Kill or materially modify H1 if:
- creators consistently describe a reliable, low-friction way to identify relevant SKUs;
- rejected products fail for reasons unrelated to creator/audience fit;
- mismatch does not affect content quality, conversion, repeat, or willingness to promote again.

### H2: Sampling friction

Kill or materially modify H2 if:
- creators routinely obtain relevant products without meaningful cost or delay;
- inability to trial does not change their posting decisions;
- creators say trial access is inconvenient but not economically meaningful.

### H3: Content difficulty

Kill or materially modify H3 if:
- BPC creators report comparable effort and proof requirements to non-BPC creators;
- product testing rarely changes the content;
- the additional content effort has no effect on posting, conversion, or retention.

### H4: Shopper proof gap

Kill or materially modify H4 if:
- creator questions are mainly about price or delivery rather than suitability, authenticity, or expected result;
- creators can already answer the important purchase questions with existing surfaces;
- proof-related uncertainty does not affect observed clicks, orders, returns, or repeat.

### H5: Creator economics

Kill or materially modify H5 if:
- creators choose products primarily for fit or audience demand even when economics vary;
- earnings, costs, and time are not connected to whether they promote again;
- attribution is clear and economics are not a meaningful source of drop-off.

### H0: Alternative diagnosis

Elevate H0 if:
- a non-H1-H5 issue repeatedly appears in real behavior;
- it affects a measurable funnel node or repeat decision;
- it has higher funnel impact and addressability than the leading H1-H5 candidates;
- the issue can be named precisely enough to test in 30 days.

## Interviewer Guardrails

- Do not say “matching engine,” “Beauty Proof,” “smart sampling,” or “decision engine” before the respondent has finished the behavioral walkthrough.
- Do not ask “Would you use this?” or “Would free samples help?” as validation questions.
- Do not convert one creator’s opinion into a market claim.
- Do not delete contradictory answers.
- Do not fill an unanswered field with an assumption.
- Use `Unknown` when the respondent does not know.
