# DICE Shopper Survey

## Purpose

Understand where shoppers lose confidence between discovering and buying an online beauty or personal-care product.

This survey tests:

- `H1`: Creator x SKU mismatch
- `H2`: Sampling/trial friction
- `H3`: BPC content and explanation difficulty
- `H4`: Shopper proof gap
- `H5`: Creator economics as a downstream quality/behavior issue
- `H0`: Alternative diagnosis such as price, quality, delivery, returns, authenticity, assortment, or platform UX

The survey does not mention or test a proposed Meesho solution.

## Survey Design

Target completion time: `under 3 minutes`

Recommended sample:
- People who bought or seriously considered buying an online beauty or personal-care product in the last 6 months.
- Include Meesho and non-Meesho shoppers where possible.
- Record metro/non-metro and broad age band only if needed for segmentation.

Intro text:

> We are studying how people buy beauty and personal-care products online for a student research project. Please answer based on your most recent real experience. This survey is anonymous and should take less than 3 minutes. Please do not share your name, phone number, or order details.

## Questions

### Q1. Eligibility and recent behavior

**When was the last time you bought or seriously considered buying a beauty or personal-care product online?**

Response:
- Within the last 30 days
- 1-3 months ago
- 4-6 months ago
- More than 6 months ago
- I have never bought or seriously considered one online

Tags: `H0-H5`

Use:
- Include the first four responses.
- Exclude or separately label the last response.

### Q2. Product category

**What type of product was it?**

Select one:
- Makeup
- Skincare
- Haircare
- Fragrance
- Grooming
- Personal hygiene
- Other: ______

Tags: `H0`, `H3`, `H4`

### Q3. Discovery source

**How did you first discover or consider this product?**

Select all that apply:
- Search on an ecommerce app or website
- Creator or influencer video/post
- Friend or family recommendation
- Customer review
- Brand social-media content
- Advertisement
- Offline store or prior use
- Other: ______

Tags: `H1`, `H4`, `H0`

### Q4. Decision outcome

**What happened after you first discovered or considered it?**

Select one:
- I bought it
- I bought a different product instead
- I saved or delayed it
- I decided not to buy
- I am still deciding

Tags: `H4`, `H0`

### Q5. Information checked

**Before deciding, which information did you check?**

Select all that apply:
- Price or discount
- Customer ratings/reviews
- Creator or influencer content
- Product ingredients or claims
- Shade, undertone, skin type, hair type, or use-case fit
- Texture, finish, fragrance, or wear
- Before/after or visible results
- Brand or seller authenticity
- Delivery or return policy
- I did not check anything specific
- Other: ______

Tags: `H3`, `H4`, `H0`

### Q6. Main hesitation

**What was the biggest thing that made you hesitate, compare, delay, or choose another product?**

Select one:
- I was unsure it would suit me
- I could not judge the expected result
- I was unsure about authenticity or quality
- The price or value did not feel right
- I could not find enough useful reviews or demonstrations
- I was unsure about ingredients or safety
- Delivery time or returns felt risky
- The product selection was confusing
- I did not have any major hesitation
- Other: ______

Tags: `H0`, `H3`, `H4`

### Q7. Creator usefulness

**If you saw creator/influencer content for the product, what did it help you do?**

Select one:
- Discover the product only
- Understand how it is used
- Judge whether it might suit me
- Compare it with another product
- Decide to buy
- It did not help me
- I did not see creator/influencer content

Tags: `H1`, `H3`, `H4`

### Q8. Similarity signal

**Did you look for a reviewer or creator with a similar context to yours?**

Select one:
- Yes, skin tone or undertone
- Yes, skin type or concern
- Yes, hair type or concern
- Yes, age, location, language, or lifestyle
- No, similarity was not important
- I did not look at creator/reviewer content

Tags: `H1`, `H4`, `H0`

### Q9. Proof gap

**What information, if any, was still missing before you felt ready to buy?**

Select all that apply:
- Whether the shade would match
- Whether it would suit my skin or hair type
- How it looks or feels in real use
- How long the result lasts
- Whether the ingredients or claims are trustworthy
- Whether the product is authentic
- Whether the price is good value
- Nothing important was missing
- Other: ______

Tags: `H3`, `H4`, `H0`

### Q10. Post-purchase outcome

Show only if Q4 = `I bought it`.

**How did the product compare with your expectation?**

Select one:
- Better than expected
- About as expected
- Worse than expected
- Too early to tell

Tags: `H0`, `H4`

### Q11. Return or regret

**Did you return, regret, stop using, or avoid repurchasing the product?**

Select one:
- No
- Yes, it did not suit me
- Yes, the result or appearance was different from expected
- Yes, quality or authenticity was a concern
- Yes, delivery, seller, or return experience was a problem
- Yes, price/value was a problem
- Too early to tell

Tags: `H0`, `H4`

### Q12. Open behavioral explanation

**In one sentence, what most influenced your final decision?**

Short answer.

Tags: `H0-H5`

Coding rule:
- Preserve the respondent’s wording.
- Do not convert an answer into a hypothesis until coding.
- Record `Unknown` if the response is too vague.

## Optional Segmentation

Keep optional fields at the end so they do not reduce completion:

### S1. Usual shopping location

- Metro city
- Tier 2 city
- Tier 3 or smaller town
- Prefer not to say

Tags: `H0`, `H1`, `H4`

### S2. Age band

- Under 18
- 18-24
- 25-34
- 35-44
- 45+
- Prefer not to say

Tags: segmentation only

### S3. Primary shopping platform for the experience

- Meesho
- Amazon
- Nykaa
- Flipkart
- Myntra
- Brand website
- Other
- Prefer not to say

Tags: `H0`, `H4`

## Coding Template

Use one row per response.

| Response ID | Eligibility | Product category | Discovery | Outcome | Main hesitation | Proof missing | Post-purchase issue | H0 | H1 | H2 | H3 | H4 | H5 | Direct evidence | Contradiction | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| U-001 | Pending | Pending | Pending | Pending | Pending | Pending | Pending | - | - | - | - | - | - | Pending | Pending | Low |

Coding values:
- Hypothesis columns: `Supports`, `Contradicts`, `Neutral`, or `Unknown`.
- Direct evidence: respondent’s selected answer or exact wording.
- Inference: stored separately from direct evidence.
- Contradiction: only record when the response conflicts with a current hypothesis.

## H0-H5 Interpretation Rules

### H0: Alternative diagnosis

Elevate H0 when respondents repeatedly identify price, quality, authenticity, delivery, returns, seller reliability, assortment, platform UX, or another issue as the primary decision or regret driver.

Do not use H0 as a generic “other” category. Name the specific issue.

### H1: Creator x SKU mismatch

Support only if shoppers’ behavior shows that creator/product/audience fit affects discovery, consideration, or purchase. Do not treat “I like relatable creators” as proof of a marketplace matching bottleneck.

Kill or weaken if shoppers rarely use creator similarity or product-fit context and purchase decisions are dominated by another factor.

### H2: Sampling/trial friction

This shopper survey can only provide indirect evidence for H2. Use it to record whether lack of real-use evidence or trial opportunity affected purchase confidence.

Do not claim the survey proves creator sampling friction. That requires creator evidence.

Kill or weaken if shoppers report that trial or real-use evidence is not relevant to their category decisions.

### H3: Content difficulty

Support when shoppers consistently need product attributes that are difficult to demonstrate or explain, such as shade, texture, suitability, wear, ingredients, or visible result.

Kill or weaken if shoppers mainly need simple price, delivery, or availability information and do not use richer product proof.

### H4: Shopper proof gap

Support when missing proof appears between discovery and purchase, or when expectation mismatch leads to regret, return, or non-repurchase.

Kill or weaken if shoppers report that available reviews and product information are already sufficient and do not affect decisions.

### H5: Creator economics

This survey cannot directly validate creator payouts or creator retention. It can only provide downstream evidence about whether poor proof or expectation mismatch may reduce repeat demand.

Do not score H5 from shopper responses alone.

### Contradiction rule

For every hypothesis, record both:
- responses that support it;
- responses that weaken or contradict it.

Do not calculate a market-wide percentage from a convenience sample. Report the denominator and sample source, for example:

`14 of 31 eligible respondents selected “unsure it would suit me”; directional sample finding, not a market estimate.`

## Kill Criteria Before Wedge Selection

Do not select a proof-led wedge from this survey unless:

- at least one decision-stage behavior shows missing proof or expectation mismatch;
- the evidence is not explained better by price, quality, delivery, returns, or authenticity;
- the finding is consistent with creator or seller evidence;
- contradictions have been recorded;
- H2 and H5 are not being claimed from shopper data alone.
