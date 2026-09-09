# DICE Evidence Database

## Purpose

This is the working evidence ledger for the Meesho DICE BPC case.

Rules:
- `Observed` means directly stated or visibly documented by the cited source.
- `Inference` means our interpretation of one or more observations.
- `Pending primary` means it requires a real creator, user, seller, or product-flow observation.
- No fabricated respondents, quotes, percentages, or Meesho internal metrics.
- Every deck claim must point to one or more evidence IDs.

## Current Research Gate

| Item | Status |
| --- | --- |
| Strategic architecture | Locked: Creator x SKU x Audience Decision Engine |
| Diagnosis | Provisional |
| H0-H5 validation | Not complete |
| Primary interviews | 0 completed and intentionally unrepresented |
| User survey | 0 completed and intentionally unrepresented |
| Seller/brand interviews | 0 completed and intentionally unrepresented |
| Desk evidence | Seeded below |
| Wedge | Pending evidence |
| PPT | Frozen |

## Evidence Ledger

| ID | Source type | Observation | Supports / weakens | Status | Source |
| --- | --- | --- | --- | --- | --- |
| S-001 | Case brief | The case frames BPC as meaningful in total NMV but smaller in affiliate NMV, creating an affiliate-growth problem to solve. | Supports problem existence; does not identify root cause. | Observed from primary case document | `DICE Challenge S3  CC Case studies.pdf` |
| S-002 | Case brief | The brief names shade matching, skin/hair suitability, ingredient awareness, and counterfeit fear as first-purchase barriers. | Supports H3 and H4; category-specific proof burden. | Observed from primary case document | `DICE Challenge S3  CC Case studies.pdf` |
| S-003 | Case brief | The brief requires a three-sided solution spanning brands, creators, and users, plus activation, sampling, incentives, trust, attribution, technology, NMV, and retention. | Supports marketplace/value-chain framing. | Observed from primary case document | `DICE Challenge S3  CC Case studies.pdf` |
| S-004 | Case brief | The case asks teams to speak with beauty and non-beauty creators. | Supports the beauty-vs-non-beauty control design. | Observed from primary case document | `DICE Challenge S3  CC Case studies.pdf` |
| S-005 | Public Meesho coverage | Meesho has publicly described Creator Club/content-commerce infrastructure, including creator collaboration, analytics, and payout mechanics. | Weakens “Meesho only needs more creators”; supports a capability-extension thesis. | Desk observation; verify against current product flow | [Meesho Creator Club coverage](https://www.indianretailer.com/news/meesho-launches-creator-club-boost-content-commerce-growth) |
| S-006 | Public Meesho promotion | A Meesho promotional post advertises Creator Club weekly commissions and says it is trusted by 3L+ creators. | Supports H5 as an open question, not a proven bottleneck; commissions are already a visible lever. | Desk observation; marketing claim, not independently audited | [Meesho promotional post](https://www.facebook.com/meeshosupply/posts/become-a-successful-content-creator-with-meesho-creator-club-weekly-commissions-/1196137755979722/) |
| S-007 | Public competitor signal | Myntra’s Ultimate Glam Clan was reported at more than one million registrations in June 2025. | Supports competitor investment in creator-led commerce; does not prove superior conversion. | Secondary observation | [Economic Times](https://economictimes.indiatimes.com/tech/startups/myntras-creator-programme-recorded-over-1-million-registrations-ceo-nandita-sinha/articleshow/122160270.cms) |
| S-008 | Public competitor signal | Nykaa and Snapchat launched a Gen Z beauty creator incubator in October 2025. | Supports category-specific creator infrastructure as a competitive pattern. | Secondary observation | [Times of India](https://timesofindia.indiatimes.com/life-style/beauty/first-gen-z-beauty-creator-incubator-program-launched-in-india/articleshow/124737023.cms) |
| S-009 | Public program signal | Public Nykaa affiliate creator content describes commission eligibility, campaigns, and product/PR access. | Supports competitor emphasis on creator monetization and product access; exact terms require direct program audit. | Directional desk observation | [Nykaa affiliate content](https://www.instagram.com/reel/DaFMF3ON4c4/) |
| S-010 | Public creator signal | Public Myntra creator content advertises a one-million-member milestone for Ultimate Glam Clan. | Reinforces that creator scale is not itself a Meesho differentiator. | Directional desk observation | [Myntra public post](https://www.facebook.com/myntra/videos/were-officially-a-clan-of-1-million-the-ultimate-glam-clan-just-hit-a-major-mile/1378524336580044/) |
| S-011 | Desk inference | If creator supply, payouts, and content-commerce distribution already exist, a creator-acquisition-only solution is unlikely to explain the BPC affiliate gap. | Weakens “just acquire creators”; keeps H1-H4 open. | Inference from S-001, S-005, S-006 | S-001, S-005, S-006 |
| S-012 | Desk inference | The strongest current candidate is a category-specific capability that connects creator/SKU/audience fit with proof and measurable outcomes. | Supports strategic architecture; does not validate the wedge. | Inference; pending primary validation | S-001 through S-011 |
| M-CAT-001 | Product audit | The public Meesho Beauty Products category page displayed `10,000+ products`; visible listings showed title, price, discount/MRP, rating/review count, and delivery/promise cues. | Supports the need to inspect what is and is not visible at listing/PDP level; does not prove a proof gap. | Verified public artifact, accessed 2026-09-09 | [Meesho Beauty Products](https://www.meesho.com/beauty-products/pl/9on) |
| M-PDP-001 | Product audit | A linked Meesho product-detail request returned `403 Forbidden` in the audit environment. Product-level suitability, ingredient, authenticity, and creator-proof fields remain unverified. | Supports H0 as an audit-access limitation only; no product-quality inference permitted. | Blocked artifact, accessed 2026-09-09 | Linked from M-CAT-001 |
| COMP-001 | Competitor public program audit | Myntra publicly advertises a one-million-member Ultimate Glam Clan milestone. | Supports competitor creator-program scale; does not prove matching or conversion impact. | Verified public program artifact, accessed 2026-09-09 | [Myntra public post](https://www.facebook.com/myntra/videos/1378524336580044/) |
| COMP-002 | Competitor public program audit | Google describes YouTube Shopping expansion in India with affiliate partners including Nykaa and Purplle and creator shopping tools. | Supports competitor creator-commerce infrastructure; does not prove BPC uplift. | Verified public program artifact, accessed 2026-09-09 | [Google India announcement](https://blog.google/intl/en-in/products/inside-google/youtube-shopping-expands-in-india-with-new-affiliate-partners-and-creator-tools/) |
| COMP-003 | Competitor public program audit | The same Google announcement lists Flipkart among India affiliate partners. | Supports competitor distribution access; does not prove creator-SKU matching. | Verified public program artifact, accessed 2026-09-09 | [Google India announcement](https://blog.google/intl/en-in/products/inside-google/youtube-shopping-expands-in-india-with-new-affiliate-partners-and-creator-tools/) |
| COMP-FLOW-001 | Competitor end-to-end flow audit | YouTube’s official Shopping documentation exposes a creator flow from eligibility and Studio onboarding to affiliate offer discovery, product/commission/sample review, product tagging, retailer checkout, and creator metrics/earnings. | Demonstrates a real integrated creator-commerce flow with product access, attribution, and economics; does not prove BPC conversion or Meesho gap. | Verified official flow, accessed 2026-09-09 | [YouTube Shopping Affiliate Program](https://support.google.com/youtube/answer/13376398?co=GENIE.Platform%3DAndroid&hl=en) |

## H0-H5 Scoreboard

Populate only after real evidence is captured. The current values are intentionally blank.

| Hypothesis | Evidence IDs | Contradictions | Strength 1-5 | Funnel impact 1-5 | Addressability 1-5 | Meesho advantage 1-5 | Data/moat 1-5 | Verdict |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| H1: Creator x SKU mismatch | S-001, S-005, S-011 | Pending primary | - | - | - | - | Open |
| H2: Sampling friction | S-002, S-003 | Pending primary | - | - | - | - | Open |
| H3: Content difficulty | S-002, S-003 | Pending primary | - | - | - | - | Open |
| H4: User proof gap | S-002, S-003 | Pending primary | - | - | - | - | Open |
| H5: Weak creator economics | S-003, S-006 | Pending primary | - | - | - | - | Open |
| H0: Alternative diagnosis | None yet | Pending desk and primary audit | - | - | - | - | Open |

Priority formula:

`20% evidence strength + 10% frequency + 25% funnel impact + 20% addressability + 15% Meesho advantage + 10% data/moat potential`

## Missing Evidence That Blocks The Wedge

| Missing fact | Why it matters | Collection method |
| --- | --- | --- |
| How creators choose BPC products today | Distinguishes H1 from H5 and generic friction | Creator interviews |
| Whether BPC requires materially more trial/content effort than non-BPC | Distinguishes H2/H3 from generic creator friction | Matched creator interviews and content audit |
| Which proof fields users actually use before purchase | Distinguishes H4 from assumed beauty-trust narrative | Last-purchase interviews and survey |
| How brands select creators and allocate samples | Validates Brand -> Creator relationship | Seller/brand interviews |
| Whether Meesho product pages visibly lack category-specific proof | Tests H4 and H0 alternatives | Manual PDP audit |
| Whether commission economics or attribution dominate creator behavior | Tests H5 | Creator interviews and payout/time model |
| Whether assortment, quality, price, delivery, or returns dominate | Tests H0 | User, seller, and product-flow audit |
| Whether listing-level fields transfer into a usable BPC PDP decision | Tests H3/H4/H0 | 30-page Meesho PDP audit with screenshots |
| Whether creator posts visibly demonstrate suitability and result | Tests H3/H4/N1 | 100-post public creator-content audit |
| Which competitor funnel capability is genuinely observable | Tests H1-H5 | Five-platform creator-to-commerce audit |

## Research Integrity Log

- No primary interviews completed as of 2026-09-09.
- No survey sample is being represented as completed.
- No Meesho internal data is available in this workspace.
- Public marketing claims are not treated as independently audited operating metrics.
- The evidence pack must be updated before any final deck claim is promoted from hypothesis to finding.
