# DICE Gate 1 Audit Workbook

## Audit Objective

Execute three artifact audits without inventing findings:

1. Meesho BPC product/PDP experience.
2. Public creator-content evidence.
3. Competitor creator-to-commerce flows.

Status labels:
- `Verified`: directly observed from the cited artifact.
- `Blocked`: attempted but inaccessible or not sufficiently verifiable.
- `Pending`: not yet audited.
- `Inference`: interpretation that must not be presented as direct observation.

No row becomes a conclusion until the artifact, date, and observation are recorded.

Audit date: `2026-09-09`

## Gate 1 Status

| Stream | Target | Verified rows | Blocked rows | Status |
| --- | ---: | ---: | ---: | --- |
| Meesho BPC category/PDP | 30 listings/pages | 1 category page | 1 PDP access failure | In progress |
| Public creator content | 15-30 watched artifacts preferred over arbitrary quota | 15 user-supplied manual audits; 15 metadata-only leads | 0 timestamp markers; screenshots pending | Manual audit received; independent artifact verification pending |
| Competitor flows | 5 platforms | 3 public program artifacts; 1 verified end-to-end flow | 0 | In progress |
| Scholarly context | 5-10 relevant papers | 4 directional sources | - | Secondary evidence only |
| Primary respondents | Creators, shoppers, sellers | 0 | - | Outreach pending |

## Stream A: Meesho BPC Product/PDP Audit

### Coding fields

For each product/listing, capture:

- product/category
- price and discount
- rating and review count
- delivery promise
- seller/brand identity
- authenticity or trust signals
- shade/undertone information
- skin/hair suitability information
- ingredient/claim information
- visual demonstration or creator proof
- returns/COD information
- reviewer-generated evidence
- direct URL and access date

### Verified artifacts

| Artifact ID | Surface | URL | Direct observation | H0-H5 tags | Status |
| --- | --- | --- | --- | --- | --- |
| M-CAT-001 | Meesho BPC category page | `https://www.meesho.com/beauty-products/pl/9on` | The public category page displayed Beauty Products with `10,000+ products`; the visible listing grid showed product title, price, crossed-out MRP/discount, rating/review count, and delivery/promise text on listings. | `H0`, `H3`, `H4` | Verified |
| M-PDP-001 | Meesho product detail page | Linked from M-CAT-001 | The linked product-detail request returned `403 Forbidden` during the audit. Product-level fields could not be verified from this environment. | `H0` | Blocked |

### What this does and does not establish

Established:
- Meesho has a large public BPC category surface.
- Listing cards visibly expose price/discount, social rating/review count, and delivery-related cues.

Not established:
- Whether product pages expose sufficient shade, skin/hair, ingredient, authenticity, or creator-proof information.
- Whether users can filter or discover by suitability context.
- Whether creator content is integrated into the BPC PDP.
- Whether the category’s listing-level information changes purchase behavior.

Next Meesho audit action:
- Manually open 30 product pages in a normal browser session.
- Record screenshots and URLs.
- Sample makeup, skincare, haircare, grooming, and personal hygiene.
- Do not substitute the category page for a PDP audit.

## Stream B: Public Creator-Content Audit

### Sampling design

Target 100 publicly accessible posts/videos:
- 40 BPC creator posts
- 30 non-BPC creator posts
- 20 Meesho-linked creator posts
- 10 comparison/control posts from another marketplace or affiliate context

Stratify where observable by:
- language
- creator size
- category
- platform
- product price band

### Coding fields

| Field | Coding |
| --- | --- |
| Creator/content ID | Public URL and date accessed |
| Category | Makeup / skincare / haircare / grooming / other |
| Product price | Exact price or `Unknown` |
| Product trial visible | Yes / no / unclear |
| Shade/undertone proof | Yes / no / not applicable |
| Skin/hair suitability | Yes / no / not applicable |
| Ingredients/claims | Yes / no |
| Texture/finish/wear/result | Yes / no |
| Authenticity disclosure | Yes / no / unclear |
| Audience fit cue | Yes / no / unclear |
| CTA destination | Meesho / other marketplace / brand site / unknown |
| Comment questions | Exact recurring themes |
| Engagement metrics | Record displayed metrics only |
| H tags | H0-H5/N1 |
| Evidence status | Verified / blocked |

### Creator-content ledger

| Artifact ID | Public URL | Category | Direct observation | H0-H5 tags | Status |
| --- | --- | --- | --- | --- | --- |
| CCA-001 | `https://www.youtube.com/watch?v=znnr8HlCbPM` | Makeup/skincare/beauty | Title/description identifies an Indian beauty creator PR haul containing makeup, skincare, tools, and new launches. | `H2`, `H3` | Metadata verified |
| CCA-002 | `https://www.youtube.com/watch?v=GuelNFAXMjo` | Makeup/skincare | Title identifies current beauty favourites; description explicitly mentions affiliate links that can generate creator earnings. | `H4`, `H5` | Metadata verified |
| CCA-003 | `https://www.youtube.com/watch?v=lCNVjbVdbFk` | Makeup | Title/description identifies testing viral makeup products used by influencers and an explicit “worth it or not” review frame. | `H3`, `H4` | Metadata verified |
| CCA-004 | `https://www.youtube.com/watch?v=dNskGxbf0bg` | Skincare/haircare/makeup | Title identifies a Nykaa beauty haul by Chetali Chadha; source metadata describes Indian-skin-tailored skincare context. | `H3`, `H4` | Metadata verified |
| CCA-005 | `https://www.youtube.com/watch?v=I5La7dwMgks` | Makeup/skincare/haircare | Title identifies a beauty haul; description explicitly mentions affiliate links helping creator earnings. | `H5` | Metadata verified |
| CCA-006 | `https://www.youtube.com/watch?v=ZxeCR0iSztw` | Makeup | Title/description identifies an Indian makeup creator and reviews, hauls, skincare videos, and tutorials. | `H3`, `H4` | Metadata verified |
| CCA-007 | `https://www.youtube.com/watch?v=i3m6-GqNTsE` | Makeup/skincare/bodycare | Title/description identifies de-influencing and stopping purchases of viral beauty bestsellers. | `H4`, `H0` | Metadata verified |
| CCA-008 | `https://www.youtube.com/watch?v=Znj5FcksR-g` | Skincare | Title/description identifies an affordable Indian skincare brand review and an impressed/quality evaluation. | `H0`, `H4` | Metadata verified |
| CCA-009 | `https://www.youtube.com/watch?v=ahh_JbMPPF4` | Skincare/haircare | Title identifies Indian skin and haircare recommendations; description includes best-of product recommendations and review references. | `H3`, `H4` | Metadata verified |
| CCA-010 | `https://www.youtube.com/watch?v=vJ594PhrIL4` | Makeup | Title/description identifies affordable Zudio makeup haul and honest testing/review. | `H0`, `H3`, `H4` | Metadata verified |
| CCA-011 | `https://www.youtube.com/watch?v=3vYBEdkNLbY` | Makeup/skincare/haircare | Description identifies makeup, skincare, and haircare products recently picked up from Amazon India. | `H0`, `H4` | Metadata verified |
| CCA-012 | `https://www.youtube.com/watch?v=2KhzvyWnwIE` | Makeup | Title/description identifies a Dream Beauty haul with foundation, blush, lip gloss, and kajal plus an honest experience/review frame. | `H3`, `H4` | Metadata verified |
| CCA-013 | `https://www.youtube.com/watch?v=C8KSGs_lbIU` | Makeup | Title/description identifies an Indian makeup brand founder reviewing their own products. | `H0`, `H4` | Metadata verified |
| CCA-014 | `https://www.youtube.com/watch?v=pNin-trNAuY` | Makeup | Description identifies an indie makeup review and review of a limited-edition makeup product. | `H3`, `H4` | Metadata verified |
| CCA-015 | `https://www.youtube.com/watch?v=DWoY8tFCQ1s` | Makeup | Title/description identifies testing affordable Zudio makeup to judge whether it is worth the money. | `H0`, `H3`, `H4` | Metadata verified |
| CCA-016 | `https://www.youtube.com/watch?v=1-RLjp9lOvo` | Makeup | Search metadata identifies Aashi Adani and Swiss Beauty/festive makeup review content with a budget framing. | `H0`, `H3`, `H4` | Metadata verified |
| CCA-017 | `https://www.youtube.com/watch?v=qeht5rLhPgo` | Makeup/skincare/bodycare/haircare | Title identifies a Nykaa Hot Pink Sale haul with review and swatches, including Zudio makeup. | `H3`, `H4` | Metadata verified |
| CCA-018 | `https://www.youtube.com/watch?v=cfSgdguYkEA` | Makeup/skincare | Title identifies authentic Indian drugstore makeup/skincare for older women; description includes a Lakme product link. | `H1`, `H3`, `H4` | Metadata verified |
| CCA-019 | `https://www.youtube.com/watch?v=4UKr_mnL3gI` | Makeup | Title identifies clean Indian makeup brands and speed reviews; description includes a Nykaa product link. | `H3`, `H4`, `H5` | Metadata verified |
| CCA-020 | `https://www.youtube.com/watch?v=Dr9TrPSj3xE` | Makeup | Title identifies an Indian-vs-Western makeup comparison; description includes a product link. | `H0`, `H3`, `H4` | Metadata verified |
| CCA-021 | `https://www.youtube.com/watch?v=nyQFzJdgIdA` | Makeup | Title identifies nude makeup for Indian skin under Rs 500; description mentions prices and mini reviews. | `H1`, `H0`, `H3`, `H4` | Metadata verified |
| CCA-022 | `https://www.youtube.com/watch?v=9Ats1Z8HXko` | Makeup | Title identifies an Indian bridal base review/tutorial and affordable makeup products. | `H0`, `H3`, `H4` | Metadata verified |
| CCA-023 | `https://www.youtube.com/watch?v=uhPYc_Mcd_o` | Makeup | Title identifies a beginner makeup kit for dry skin; description contains a Nykaa brush link. | `H1`, `H3`, `H4`, `H5` | Metadata verified |
| CCA-024 | `https://www.youtube.com/watch?v=LnNmcEMPVz0` | Makeup | Title identifies a Nykaa Skin Genius foundation review and a foundation-for-Indian-skin framing. | `H1`, `H3`, `H4` | Metadata verified |
| CCA-025 | `https://www.youtube.com/watch?v=fGNtKatTLVg` | Makeup | Title identifies an affordable drugstore makeup tutorial by Chandni Singh. | `H0`, `H3` | Metadata verified |
| CCA-026 | `https://www.youtube.com/watch?v=JZgHA54zKr0` | Makeup | Title identifies a review of five makeup foundations; description includes an Amazon affiliate link and price. | `H3`, `H4`, `H5` | Metadata verified |
| CCA-027 | `https://www.youtube.com/watch?v=KmeGTAj_jno` | Makeup | Title/description identifies clean Indian makeup brands and a concealer product. | `H0`, `H3` | Metadata verified |
| CCA-028 | `https://www.youtube.com/watch?v=UT_S7_Q2d-U` | Makeup/skincare | Title identifies a critique of beauty-industry virality and fake virality versus what makes products go viral. | `H0`, `H4` | Metadata verified |
| CCA-029 | `https://www.youtube.com/watch?v=GFPF-Ms_yo0` | Beauty creator commerce | Title identifies how a small creator obtains free beauty products; description is explicitly creator/PR-oriented. | `H2`, `H5` | Metadata verified |
| CCA-030 | `https://www.youtube.com/watch?v=uuLM_J6jErs` | Beauty creator commerce | Title/description identifies how creators get onto beauty-brand PR lists and mentions affiliate links. | `H2`, `H5` | Metadata verified |

### Manual-quality audit supplied by team

Source status: `User-supplied manual audit received 2026-09-09`.

Integrity note:
- The observations below were supplied by the team after manual viewing/transcript review.
- ByteAsk has not independently replayed the videos in this environment.
- Exact `mm:ss` timestamps were intentionally not invented because transcript output did not provide line-level time markers.
- `Unknown` means the supplied audit did not establish the field.
- Screenshot paths are pending.

| ID | Creator | Platform | Category | Timestamp status | Product/proof observation | Suitability/shade/texture | Outcome/quality observation | CTA/destination | Disclosure/PR | H tags | Strength | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CCA-001 | Paawni Behl | YouTube | Makeup/skincare/beauty | Transcript-sequential; no mm:ss | November PR haul/unboxing | Unknown | First-impression/haul; long-term outcome not established | Unknown | PR signal; disclosure unknown | `H2`, `H3` | Medium | 20+ PR-package pattern supplied by team |
| CCA-002 | Aanam C | YouTube | Beauty | Transcript-sequential; no mm:ss | Current beauty favourites; product discussion | Suitability/texture not fully coded | Sponsored Perfora integration reported | Unknown | Sponsored integration | `H3`, `H4`, `H5` | Medium | Monetization signal, not conversion evidence |
| CCA-003 | Ronak Qureshi | YouTube | Makeup | Transcript-sequential; no mm:ss | Viral influencer makeup testing | Product experience/“worth it” framing | Actual-use review frame | Unknown | Disclosure unknown | `H3`, `H4` | Medium | Viral hype versus experience test |
| CCA-004 | Chetali Chadha | YouTube | Makeup/skincare | Transcript-sequential; no mm:ss | Nykaa Hot Pink Sale haul | Suitability/texture not fully coded | Haul/first-impression format | Nykaa context; exact CTA unknown | PR volume signal supplied; disclosure unknown | `H2`, `H3`, `H4` | Medium | 20+ PR-package pattern supplied by team |
| CCA-005 | Aanam C | YouTube | Makeup/skincare/haircare | Transcript-sequential; no mm:ss | Target and Ulta beauty haul | Suitability/texture not fully coded | Haul/first-impression format | Unknown | Affiliate/PR status partly unknown; PR volume signal supplied | `H2`, `H3`, `H5` | Medium | Do not infer conversion from haul |
| CCA-006 | Prakriti Singh | YouTube | Makeup | Transcript-sequential; no mm:ss | Minimal Indian makeup demonstration | Lakme Nude Twist washes out without base; shade/fit issue directly reported | Visible shade-performance mismatch | Unknown | Disclosure unknown | `H0`, `H3`, `H4` | High | Indian-skin suitability observation |
| CCA-007 | Shweta Vijay | YouTube | Makeup/skincare | Transcript-sequential; no mm:ss | De-influencing and product testing | Charlotte Tilbury Pillow Talk cool pink reported poor on Indian skin | Smashbox drying; Rare Beauty pot contamination; viral-product downside examples | Unknown | Disclosure unknown | `H0`, `H3`, `H4` | High | Contradicts simple viral-awareness assumption |
| CCA-008 | Shreya Jain | YouTube | Skincare | Transcript-sequential; no mm:ss | PhD Skincare brand spotlight | Suitability/texture not fully coded | Sponsored brand spotlight | Unknown | Sponsored integration | `H3`, `H4`, `H5` | Medium | Sponsored content is not proof of sales |
| CCA-009 | Shweta Vijay | YouTube | Natural BPC | Transcript-sequential; no mm:ss | Top 15 Indian natural BPC recommendations | Indian-skin/hair context present; exact fields unknown | Recommendation/list format | Unknown | Affiliate code `ShwetaBJ` reported | `H1`, `H3`, `H4`, `H5` | High | Affiliate signal; earnings not observed |
| CCA-010 | Esther Benedict | YouTube | Makeup | Transcript-sequential; no mm:ss | Zudio full-face testing | Product-level suitability not fully coded | Rs 99 eyeliner/sponges strong; bullet lipsticks grainy/dry | Unknown | Disclosure unknown | `H0`, `H3`, `H4` | High | Price does not predict performance uniformly |
| CCA-011 | stayprettywithpaayal | YouTube | Makeup/skincare/haircare | Transcript-sequential; no mm:ss | Amazon beauty haul | Srosky Rs 1399 setting-spray nozzle produced water streams | Packaging/mechanical defect directly reported | Amazon context; exact CTA unknown | Disclosure unknown | `H0`, `H3`, `H4` | High | Product-quality/packaging H0 signal |
| CCA-012 | Kirty Gupta Lifestyle | YouTube | Makeup | Transcript-sequential; no mm:ss | Dream Beauty haul | Dream Beauty Rs 999 foundation gave white cast | Pump failed to dispense; packaging defect | Unknown | Disclosure unknown | `H0`, `H3`, `H4` | High | Suitability plus reliability issue |
| CCA-013 | Nidhi Katiyar | YouTube | Makeup | Transcript-sequential; no mm:ss | Founder review of competitor brands | Kiro Peach Ivory foundation turned ashy | DM Beauty lip-oil logo rubbed after five uses; commission/marketing-cost claims discussed | Unknown | Founder/business disclosure | `H0`, `H3`, `H4`, `H5` | High | Financial figures require separate source verification |
| CCA-014 | Heather Austin | YouTube | Makeup/beauty collaboration | Transcript-sequential; no mm:ss | Game Beauty Persona 5 collaboration | Suitability/texture not fully coded | Product review/experience fields incomplete | Unknown | Affiliate code `Heather` reported | `H5` | Medium | Affiliate disclosure signal only |
| CCA-015 | Vibewithsafia | YouTube | Makeup | Transcript-sequential; no mm:ss | Zudio beauty testing | Suitability not fully coded | Budget-line performance fragmented; eyeliner/sponges stronger than grainy/dry bullet lipsticks | Unknown | Disclosure unknown | `H0`, `H3`, `H4` | High | Replicates CCA-010 quality-disparity signal |

### Manual-audit fields still missing

| Field | Status |
| --- | --- |
| Exact mm:ss timestamps | Not available from transcript output |
| Screenshot paths | Pending |
| Exact CTA destination for every video | Partially known; otherwise `Unknown` |
| Audience comment questions | Not supplied for all 15 |
| Full claims/disclosure wording | Partially supplied |
| Independent replay by ByteAsk | Not possible in current environment |

Do not calculate prevalence from this batch until the raw transcript/audit notes and denominators are attached. The observations can be used as a directional, user-supplied audit layer, not as independently verified timestamp evidence.

### Creator-content coding limitations

These 30 rows are metadata/description-level exploratory leads. They can help select a smaller manual-watch sample, but they are not decision-grade evidence. They do not establish:
- whether the full video contains the claimed proof;
- whether a product link generated a purchase;
- whether the creator is a Meesho creator;
- whether the content caused conversion or repeat;
- whether the absence of a field in a snippet means the field is absent from the video.

### Full-video access log

| Access batch | Attempt | Result | Evidence consequence |
| --- | --- | --- | --- |
| FVC-001 | Direct YouTube page fetch for CCA-001 | Online fetch throttled; no video page or transcript retrieved | No timestamp or video-level observation added |
| FVC-002 | Direct YouTube oEmbed request for CCA-001 | Network/DNS unavailable in execution environment | No metadata beyond the previously captured search result |
| FVC-003 | Full-video pass for CCA-001 through CCA-030 | Not executable from this environment | All 30 remain metadata-only |

Decision-grade next pass:
- use an accessible browser or user-assisted session;
- select 15 diverse videos from this lead list;
- capture timestamps for proof elements;
- record CTA/link destination and visible comments;
- code visible demonstrations, suitability explanations, and comment questions;
- only then promote an artifact from exploratory to decision-grade.

## Stream B2: Scholarly Context Audit

Scholar research is used to sharpen hypotheses and coding fields. It is not a substitute for Meesho-specific evidence, creator interviews, shopper responses, or seller interviews.

| Artifact ID | Paper/source | Directly relevant concept | H0-H5 use | Status |
| --- | --- | --- | --- | --- |
| SCH-001 | Leong et al., `Predicting purchase intention of mobile social commerce: A two-stage SEM-neural network approach` | Social-commerce purchase intention is studied through trust and platform/user factors. | H4; supports testing trust/proof as a mechanism, not as a Meesho finding. | Verified secondary source |
| SCH-002 | `The impact of social commerce constructs on social commerce intention` | Social-commerce constructs and trust are linked to intention in prior literature. | H4; supports a neutral proof/trust question set. | Verified secondary source |
| SCH-003 | Djafarova & Rushworth, `Exploring the credibility of online celebrities' Instagram profiles in influencing the purchase decisions of young female users` | Perceived credibility and relatability are relevant to influencer purchase decisions. | H1/H4; supports testing creator-audience fit and proof. | Verified secondary source |
| SCH-004 | Lou & Yuan, `Influencer Marketing: How Message Value and Credibility Affect Consumer Trust of Branded Content on Social Media` | Message value and influencer credibility are studied as drivers of trust in branded content. | H3/H4; supports coding content usefulness and credibility cues. | Verified secondary source |

Scholar evidence rules:
- Do not turn a literature relationship into a Meesho metric.
- Do not claim causality in this case from a literature review.
- Use papers to design questions and fields, not to select the winner.
- Record the paper title, authors, year, DOI or stable URL, and exact construct used.

## Stream C: Competitor Creator-to-Commerce Audit

### Platforms

- Nykaa
- Amazon India
- Flipkart
- Myntra
- YouTube/Instagram creator-to-commerce flow

### Audit tasks

For each platform, document:

1. How a creator or brand finds the creator program.
2. Whether product/SKU matching is visible.
3. Whether sampling or product access is visible.
4. Whether creator proof appears on the product page.
5. Whether suitability attributes are structured.
6. Whether attribution and repeat purchase are visible.
7. Whether the feature is a public capability or an inferred absence.

### Competitor ledger

| Artifact ID | Platform | URL | Direct observation | H0-H5 tags | Status |
| --- | --- | --- | --- | --- | --- |
| COMP-FLOW-001 | YouTube Shopping Affiliate | `https://support.google.com/youtube/answer/13376398?co=GENIE.Platform%3DAndroid&hl=en` | Official flow: eligible creator joins through YouTube Studio; opens Earn -> Shopping -> Explore affiliate offers; reviews products, seller offers, commission rates, and samples; tags products in content; viewers see product/pricing information and check out on the retailer site; creator tracks campaign metrics/earnings in Studio. | `H1`, `H2`, `H4`, `H5` | Verified end-to-end platform flow |
| COMP-001 | Myntra | `https://www.facebook.com/myntra/videos/1378524336580044/` | Public Myntra creator-program post advertises a one-million-member Ultimate Glam Clan milestone. This establishes creator-program scale messaging, not creator conversion or matching quality. | `H1`, `H5` | Verified public program artifact |
| COMP-002 | YouTube Shopping / Nykaa | `https://blog.google/intl/en-in/products/inside-google/youtube-shopping-expands-in-india-with-new-affiliate-partners-and-creator-tools/` | Google describes YouTube Shopping expansion in India with affiliate partners including Nykaa and Purplle, plus creator shopping tools. This establishes ecosystem capability, not measured BPC uplift. | `H1`, `H4`, `H5` | Verified public program artifact |
| COMP-003 | YouTube Shopping / Flipkart | `https://blog.google/intl/en-in/products/inside-google/youtube-shopping-expands-in-india-with-new-affiliate-partners-and-creator-tools/` | The same public announcement lists Flipkart among India affiliate partners. It supports competitor access to creator-commerce distribution, not proof of product/SKU fit. | `H1`, `H5` | Verified public program artifact |
| COMP-004 | Amazon India | Pending verified URL | No direct program artifact verified in this run. | - | Pending |
| COMP-005 | Instagram/Meta commerce | Pending verified URL | No direct creator-commerce flow verified in this run. | - | Pending |

### Competitor audit interpretation

Verified competitor artifacts establish that creator-commerce distribution and creator tooling are active competitive investments. They do not establish:
- that any competitor has solved creator x SKU x audience matching;
- that creator content improves BPC conversion;
- that Meesho is behind on any specific metric;
- that commissions are the dominant creator barrier.

The next competitor step is a manual flow audit with screenshots, only where the complete journey is accessible:
- enter the creator/affiliate program;
- inspect product selection and creator tooling;
- inspect product-page proof;
- record attribution and repeat signals;
- preserve each screen and access date.

If a platform exposes only a press release or program landing page, keep it as a public-program artifact and do not call it an end-to-end flow.

## Audit Integrity Rules

- A visible category page is not evidence about an inaccessible PDP.
- A creator recruitment post is not evidence of creator conversion performance.
- A competitor marketing claim is not evidence of feature adoption or impact.
- Do not code missing information as “No”; use `Not visible`, `Unknown`, or `Blocked`.
- Preserve screenshots and URLs for every verified artifact.
- Record access date because pages and programs change.
- Do not calculate percentages until the denominator contains only verified, comparable artifacts.
- Contradictions must be retained in the ledger.

## Evidence Promotion Rule

An audit observation may enter the H0-H5 scoreboard only when:

- the artifact is directly accessible or preserved with a screenshot;
- the observation is written separately from the interpretation;
- the funnel node is explicit;
- the sample denominator is known;
- access limitations are disclosed;
- at least one contradictory or neutral observation has been checked where practical.
