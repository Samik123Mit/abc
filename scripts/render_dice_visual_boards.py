from __future__ import annotations

from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

from PIL import Image, ImageDraw, ImageFont


ROOT = Path("/workspaces/abc")
TEMPLATE = ROOT / "DICE Challenge S3  Template for Case studies submission  (Presentation).pptx"
OUT = ROOT / "generated_boards"
OUT.mkdir(exist_ok=True)

W, H = 1920, 1080
PLUM = "#65064e"
PLUM_DARK = "#470039"
ORANGE = "#ff9d00"
PINK = "#f05a79"
CREAM = "#fff7e4"
SOFT = "#fff0d4"
LILAC = "#f7eff8"
PALE = "#f2f3f4"
CYAN = "#bceef2"
OLIVE = "#d9dc83"
INK = "#171016"
MUTED = "#656066"
WHITE = "#ffffff"
GRID = "#e7e0e0"


def font(size: int, bold: bool = False):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(path, size)


def asset(name: str) -> Image.Image:
    with ZipFile(TEMPLATE) as z:
        return Image.open(BytesIO(z.read("ppt/media/" + name))).convert("RGBA")


DICE_LOGO = asset("image5.png")
COVER_ART = asset("image3.png")


def new_board(bg=WHITE):
    return Image.new("RGB", (W, H), bg)


def rounded(draw, box, fill, radius=18, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, value, size=24, fill=INK, bold=False, anchor=None):
    draw.text(xy, value, font=font(size, bold), fill=fill, anchor=anchor)


def wrap(draw, value, width, size=20, bold=False):
    f = font(size, bold)
    words = value.split()
    lines, current = [], ""
    for word in words:
        candidate = (current + " " + word).strip()
        if draw.textbbox((0, 0), candidate, font=f)[2] <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def paragraph(draw, xy, value, width, size=18, fill=INK, bold=False, line_gap=7):
    x, y = xy
    lines = wrap(draw, value, width, size, bold)
    for line in lines:
        draw.text((x, y), line, font=font(size, bold), fill=fill)
        y += size + line_gap
    return y


def logo_header(draw, title, kicker, dark=False):
    if dark:
        draw.rectangle((0, 0, W, H), fill=PLUM_DARK)
        draw.bitmap((52, 24), DICE_LOGO, fill=WHITE)
        text(draw, (W - 65, 42), "m", 48, ORANGE, True, "ra")
        text(draw, (W - 65, 81), "meesho", 14, WHITE, True, "ra")
        return
    draw.rectangle((0, 0, W, 92), fill=WHITE)
    logo = DICE_LOGO.copy()
    logo.thumbnail((145, 66))
    draw._image.paste(logo, (42, 14), logo)
    text(draw, (218, 22), kicker, 18, PINK, True)
    text(draw, (218, 49), title, 38, PLUM_DARK, True)
    rounded(draw, (1780, 17, 1870, 77), PLUM_DARK, 16)
    text(draw, (1825, 40), "m", 45, ORANGE, True, "mm")
    text(draw, (1825, 69), "meesho", 11, WHITE, True, "mm")
    draw.rectangle((42, 92, 1878, 96), fill=GRID)


def section(draw, x, y, w, label, fill=PLUM_DARK):
    rounded(draw, (x, y, x + w, y + 42), fill, 14)
    text(draw, (x + w // 2, y + 21), label.upper(), 19, WHITE, True, "mm")


def pill(draw, x, y, w, label, fill=ORANGE, txt=PLUM_DARK, size=15):
    rounded(draw, (x, y, x + w, y + 34), fill, 17)
    text(draw, (x + w // 2, y + 17), label, size, txt, True, "mm")


def metric(draw, x, y, w, value, label, fill):
    rounded(draw, (x, y, x + w, y + 75), fill, 16)
    text(draw, (x + 20, y + 16), value, 33, WHITE, True)
    text(draw, (x + 145, y + 28), label, 15, WHITE, True)


def chevron(draw, x, y, w, label, sub, fill, active=False):
    points = [(x, y), (x + w - 28, y), (x + w, y + 36), (x + w - 28, y + 72), (x, y + 72), (x + 25, y + 36)]
    draw.polygon(points, fill=fill if active else PLUM_DARK, outline=WHITE)
    text(draw, (x + w // 2 - 5, y + 27), label, 17, WHITE, True, "mm")
    text(draw, (x + w // 2 - 5, y + 51), sub, 12, CREAM, False, "mm")


def card(draw, x, y, w, h, title, body, accent=PLUM_DARK, tag=None):
    rounded(draw, (x, y, x + w, y + h), WHITE, 14, GRID, 2)
    draw.rectangle((x, y, x + 10, y + h), fill=accent)
    text(draw, (x + 24, y + 24), title, 18, PLUM_DARK, True)
    paragraph(draw, (x + 24, y + 54), body, w - 48, 14, INK)
    if tag:
        pill(draw, x + w - 94, y + 14, 76, tag, accent, WHITE, 11)


def evidence_tag(draw, x, y, label, fill=ORANGE):
    pill(draw, x, y, 92, label, fill, PLUM_DARK if fill in [ORANGE, OLIVE, CYAN] else WHITE, 12)


def footer(draw, value):
    draw.rectangle((0, 1046, W, H), fill=PLUM_DARK)
    text(draw, (44, 1063), value, 12, WHITE)


def side_label(draw, x, y, h, label, fill=ORANGE):
    rounded(draw, (x, y, x + 42, y + h), fill, 16)
    layer = Image.new("RGBA", (h, 42), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.text((h // 2, 21), label, font=font(17, True), fill=PLUM_DARK, anchor="mm")
    layer = layer.rotate(90, expand=True)
    draw._image.paste(layer, (x, y + (h - layer.height) // 2), layer)


def icon_circle(draw, x, y, label, fill=PLUM_DARK, diameter=42, txt=WHITE):
    draw.ellipse((x, y, x + diameter, y + diameter), fill=fill)
    text(draw, (x + diameter // 2, y + diameter // 2), label, 16, txt, True, "mm")


def tiny_bar(draw, x, y, w, level, fill=PLUM_DARK, bg="#eaddea", h=12):
    rounded(draw, (x, y, x + w, y + h), bg, h // 2)
    rounded(draw, (x, y, x + int(w * level), y + h), fill, h // 2)


def quote_card(draw, x, y, w, h, quote, source, accent=PINK):
    rounded(draw, (x, y, x + w, y + h), PALE, 14)
    draw.rectangle((x, y, x + 8, y + h), fill=accent)
    text(draw, (x + 24, y + 18), '"', 34, accent, True)
    paragraph(draw, (x + 50, y + 18), quote, w - 74, 15, INK, True, 4)
    text(draw, (x + 50, y + h - 25), source, 11, MUTED, True)


def mini_matrix_cell(draw, x, y, w, label, level, color):
    rounded(draw, (x, y, x + w, y + 54), WHITE, 8, GRID, 1)
    text(draw, (x + 12, y + 11), label, 11, MUTED, True)
    tiny_bar(draw, x + 12, y + 31, w - 24, level, color, h=10)


def board_cover():
    board = COVER_ART.resize((W, H), Image.Resampling.LANCZOS).convert("RGBA")
    overlay = Image.new("RGBA", (W, H), (71, 0, 57, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 1040, H), fill=(71, 0, 57, 178))
    board.alpha_composite(overlay)
    d = ImageDraw.Draw(board)
    rounded(d, (80, 70, 400, 112), ORANGE, 20)
    text(d, (240, 91), "MEESHO DICE CHALLENGE | S3", 16, PLUM_DARK, True, "mm")
    text(d, (84, 218), "Beauty proof is abundant.", 58, WHITE, True)
    text(d, (84, 286), "Commerce handoff is not.", 58, WHITE, True)
    text(d, (88, 360), "PS: Growing Beauty & Personal Care through Influencers", 15, ORANGE, True)
    text(d, (88, 392), "A measured bridge from creator evidence", 26, CREAM, True)
    text(d, (88, 431), "to confident Meesho purchase.", 26, CREAM, True)
    rounded(d, (84, 525, 730, 680), SOFT, 20)
    text(d, (115, 558), "PROPOSED 30-DAY WEDGE", 16, PINK, True)
    text(d, (115, 604), "Beauty Proof Bridge", 36, PLUM_DARK, True)
    text(d, (88, 900), "Team Slayed it", 24, WHITE, True)
    text(d, (88, 945), "Samiksha Mitra | IIT Guwahati", 18, CREAM)
    text(d, (88, 1002), "Evidence cut: 09 September 2026 | Appendix included", 13, CREAM)
    return board.convert("RGB")


def board_value_chain():
    b, d = new_board(CREAM), None
    d = ImageDraw.Draw(b)
    logo_header(d, "The leak is not beauty proof: it is the proof handoff.", "ROUND 1 | VALUE CHAIN")
    text(d, (44, 116), "Creators already explain fit, shade, texture and outcomes. The unresolved value leak begins when useful proof leaves the video and enters a generic transaction surface.", 17, MUTED)
    section(d, 44, 158, 1834, "The creator → SKU → audience → commerce chain")
    stages = [
        ("BRAND / SKU", "claim + cohort", ORANGE), ("CREATOR MATCH", "credibility + fit", PINK),
        ("TRIAL", "access + use", PLUM), ("PROOF", "shade + result", PINK),
        ("DISTRIBUTION", "reach + context", "#20aebd"), ("MEESHO SURFACE", "decision support", "#879327"),
        ("PURCHASE", "order + return", PLUM), ("REPEAT / PAYOUT", "learning loop", ORANGE),
    ]
    x = 44
    for i, (head, sub, color) in enumerate(stages):
        chevron(d, x, 210, 224, head, sub, color, active=head == "MEESHO SURFACE")
        x += 227
    pill(d, 1330, 290, 132, "LEAK TO TEST", PINK, WHITE, 12)
    text(d, (1498, 307), "proof → click → order", 15, PINK, True)
    section(d, 44, 338, 1196, "What the evidence makes visible | team audit: 28 accessible public creator-content leads")
    cards = [
        ("26/28", "product demos", PLUM, "CCA"),
        ("24/28", "suitability discussions", PINK, "CCA"),
        ("23/28", "visible outcomes", "#20aebd", "CCA"),
        ("25/28", "audience-specific recs", ORANGE, "CCA"),
        ("28/28", "personal experience", "#879327", "CCA"),
    ]
    for i, (head, body, color, tag) in enumerate(cards):
        xx = 44 + i * 240
        rounded(d, (xx, 390, xx + 224, 500), WHITE, 14, color, 2)
        evidence_tag(d, xx + 14, 404, tag, color)
        text(d, (xx + 14, 454), head, 29, color, True)
        text(d, (xx + 14, 484), body, 12, PLUM_DARK, True)
    rounded(d, (44, 516, 1240, 548), PALE, 8)
    text(d, (58, 532), "Observed proof fields", 11, MUTED, True)
    for i, label in enumerate(["shade", "skin fit", "texture", "comparison", "outcome", "CTA"]):
        pill(d, 218 + i * 158, 520, 138, label.upper(), CYAN if i < 3 else PINK, WHITE, 9)
    rounded(d, (44, 572, 1240, 762), PLUM_DARK, 18)
    text(d, (72, 600), "DIAGNOSIS", 16, ORANGE, True)
    paragraph(d, (72, 636), "The strongest defensible problem is not “creators lack proof.” It is that Meesho has not yet shown a measurable, reusable handoff for proof that already exists.", 1130, 23, WHITE, True, 8)
    section(d, 44, 788, 1240, "The exact leak to test", ORANGE)
    leak_cards = [
        ("PROOF EXISTS", "Creator explains fit, shade, texture and result.", PLUM),
        ("CONTEXT BREAKS", "Useful evidence is not yet carried into a Meesho decision surface.", PINK),
        ("VALUE IS UNKNOWN", "No observed click → order → repeat bridge in the workspace.", "#20aebd"),
    ]
    for i, (head, body, color) in enumerate(leak_cards):
        card(d, 44 + i * 414, 842, 392, 142, head, body, color)
    section(d, 1306, 338, 572, "Reality check", ORANGE)
    metrics = [("28", "accessible creator audits", PLUM_DARK), ("0/28", "routed to Meesho in sample", PINK), ("1", "public-source flow capability", "#20aebd"), ("0", "primary respondents in tracker", PINK)]
    for i, (value, label, color) in enumerate(metrics):
        metric(d, 1306, 390 + i * 88, 572, value, label, color)
    section(d, 1306, 754, 572, "Competitor context | public artifact only", ORANGE)
    rounded(d, (1306, 806, 1878, 858), WHITE, 12, GRID, 1)
    text(d, (1322, 832), "Creator content → product surface → attribution → payout", 13, PLUM_DARK, True, "lm")
    tiny_bar(d, 1322, 872, 520, .72, "#20aebd", h=12)
    text(d, (1322, 902), "Evidence exists for capability; Meesho-specific handoff remains the test.", 12, MUTED, True)
    footer(d, "Evidence: CCA-001–030; M-CAT-001; M-PDP-001; COMP-FLOW-001 | Diagnosis remains a pilot hypothesis.")
    return b


def board_prioritization():
    b, d = new_board(CREAM), None
    d = ImageDraw.Draw(b)
    logo_header(d, "Prioritize the bridge before the engine.", "ROUND 1 | PRIORITIZATION")
    text(d, (44, 116), "Decision rule: choose the smallest lever that serves creators, shoppers and sellers while producing the missing transaction evidence.", 16, MUTED)
    section(d, 44, 158, 1360, "Prioritising what moves the needle | evidence-led lever screen")
    section(d, 1430, 158, 448, "30-day acceleration plan", ORANGE)
    side_label(d, 8, 208, 698, "LEVER SCREEN")
    cols = [225, 285, 140, 130, 130, 130, 150]
    headers = ["LEVER", "DESCRIPTION", "REACH", "IMPACT", "CONFIDENCE", "EFFORT", "DECISION"]
    x = 44
    for h, w in zip(headers, cols):
        rounded(d, (x, 210, x + w, 260), ORANGE, 18)
        text(d, (x + w // 2, 235), h, 12, PLUM_DARK, True, "mm")
        x += w
    rows = [
        ("Creator acquisition", "More supply, not proof transfer", .70, .55, .35, .45, "DEFER", PINK),
        ("Commission uplift", "Change effort, not decision quality", .45, .45, .25, .55, "DEFER", PINK),
        ("Broad sampling", "Create volume before fit is known", .60, .55, .40, .65, "NARROW", ORANGE),
        ("Beauty Proof Bridge", "Carry useful proof into Meesho", .85, .85, .75, .45, "PILOT", "#20aebd"),
        ("PDP suitability", "Make fit legible at decision point", .65, .75, .40, .55, "PAIR", "#879327"),
        ("Full matching engine", "Allocate creator x SKU x audience", .90, .90, .25, .85, "LATER", PLUM),
        ("Quality / authenticity", "Reduce bad orders and returns", .70, .80, .35, .70, "PARALLEL", PINK),
    ]
    y = 266
    for name, desc, reach, impact, confidence, effort, decision, color in rows:
        fill = CYAN if name == "Beauty Proof Bridge" else WHITE
        border = PLUM_DARK if name == "Beauty Proof Bridge" else GRID
        x = 44
        values = [name, desc]
        for j, value in enumerate(values):
            w = cols[j]
            rounded(d, (x, y, x + w, y + 70), fill, 0, border, 2)
            text(d, (x + 14, y + 35), value, 14 if j == 0 else 12, PLUM_DARK if name == "Beauty Proof Bridge" else INK, j == 0, "lm")
            x += w
        for label, level, w in [("R", reach, cols[2]), ("I", impact, cols[3]), ("C", confidence, cols[4]), ("E", effort, cols[5])]:
            rounded(d, (x, y, x + w, y + 70), fill, 0, border, 2)
            text(d, (x + 14, y + 18), label, 11, MUTED, True)
            tiny_bar(d, x + 14, y + 42, w - 28, level, color if name == "Beauty Proof Bridge" else PLUM_DARK, h=11)
            x += w
        w = cols[6]
        rounded(d, (x, y, x + w, y + 70), fill, 0, border, 2)
        text(d, (x + w // 2, y + 35), decision, 13, PLUM_DARK if name == "Beauty Proof Bridge" else INK, True, "mm")
        y += 74
    rounded(d, (44, 804, 1404, 930), PLUM_DARK, 18)
    text(d, (70, 830), "WINNING MOVE", 15, ORANGE, True)
    paragraph(d, (70, 862), "Pilot Beauty Proof Bridge first. It uses proof creators already produce, tests the actual commerce leak, and creates the data moat needed before a matching engine.", 1280, 18, WHITE, True, 3)

    side_label(d, 1410, 210, 190, "PROBLEM", PINK)
    rounded(d, (1464, 210, 1878, 400), WHITE, 16, GRID, 2)
    text(d, (1490, 228), "THE UNRESOLVED LEAK", 13, PINK, True)
    paragraph(d, (1490, 260), "Useful creator proof exists. The workspace does not yet show that it survives the click into Meesho, gets attributed, or earns a repeatable payout.", 350, 15, INK, True, 5)
    side_label(d, 1410, 420, 260, "SOLUTION LEVERS", ORANGE)
    levers = [("01", "Structured proof fields", PINK), ("02", "Tagged commerce handoff", "#20aebd"), ("03", "Creator / SKU IDs", ORANGE)]
    for i, (num, label, color) in enumerate(levers):
        xx = 1464 + i * 134
        rounded(d, (xx, 458, xx + 122, 548), color, 18)
        icon_circle(d, xx + 40, 470, num, PLUM_DARK if color in [ORANGE, "#20aebd"] else WHITE, 42, ORANGE if color in [ORANGE, "#20aebd"] else WHITE)
        paragraph(d, (xx + 10, 520), label, 102, 12, PLUM_DARK if color in [ORANGE, "#20aebd"] else WHITE, True, 2)
    section(d, 1464, 574, 414, "Why this wins now", PLUM_DARK)
    why = [
        "No need to assume creators need more education.",
        "The pilot creates observable evidence, not a promise.",
        "Can be killed without a platform-scale build.",
    ]
    y = 622
    for item in why:
        icon_circle(d, 1478, y + 2, "✓", "#20aebd", 28, PLUM_DARK)
        paragraph(d, (1520, y), item, 330, 12, INK, True, 2)
        y += 48
    section(d, 1464, 730, 414, "Action roadmap", ORANGE)
    roadmap = [("W1–2", "select fit-ready SKUs"), ("W2–3", "structure proof + handoff"), ("W4", "measure / scale / kill")]
    y = 782
    for week, action in roadmap:
        pill(d, 1478, y, 72, week, ORANGE, PLUM_DARK, 11)
        text(d, (1570, y + 17), action, 13, INK, True)
        y += 44
    footer(d, "C = creator | S = shopper | B = brand/seller | Prioritization is strategic, not a completed hypothesis score.")
    return b


def board_quick_win():
    b, d = new_board(CREAM), None
    d = ImageDraw.Draw(b)
    logo_header(d, "30 days to prove whether proof transfer moves BPC commerce.", "ROUND 1 | QUICK WIN")
    rounded(d, (44, 116, 1878, 180), PLUM_DARK, 18)
    text(d, (961, 148), "BEAUTY PROOF BRIDGE  =  structured proof + attributable handoff + a killable experiment", 22, WHITE, True, "mm")
    section(d, 44, 202, 1834, "Operating model | one small cohort, one measurable handoff")
    side_label(d, 8, 252, 674, "OPERATING PLAN")
    weeks = [
        ("01", "SELECT", "10–20 hero SKUs\n10 sellers\nfit criteria", ORANGE),
        ("02", "MATCH + SAMPLE", "25–50 creators\nrelevant audience\nlogged cost", PINK),
        ("03", "STRUCTURE + SURFACE", "proof fields\ndisclosure\nMeesho decision asset", "#20aebd"),
        ("04", "MEASURE + DECIDE", "click → order\nreturn → repeat\ncreator payout", "#879327"),
    ]
    x = 44
    for week, head, body, color in weeks:
        rounded(d, (x, 252, x + 438, 408), WHITE, 16, color, 3)
        d.rectangle((x, 252, x + 438, 298), fill=color)
        icon_circle(d, x + 17, 260, week, PLUM_DARK if color in [ORANGE, "#879327"] else WHITE, 30, ORANGE if color in [ORANGE, "#879327"] else WHITE)
        text(d, (x + 72, 274), head, 16, WHITE, True)
        paragraph(d, (x + 32, 324), body, 374, 17, INK, True, 5)
        x += 464
    section(d, 44, 438, 1192, "Three-sided workflow")
    lanes = [
        ("CREATOR", "Receive relevant SKU", "publish structured proof", "tag / link", "see attributed outcomes", PINK),
        ("SELLER / BRAND", "Nominate fit-ready SKU", "fund or approve trial", "see quality", "see demand signal", ORANGE),
        ("SHOPPER", "Discover proof", "resolve fit / shade / texture", "click → buy", "rate / reorder", "#20aebd"),
    ]
    y = 490
    for head, a, b1, c, e, color in lanes:
        rounded(d, (44, y, 1236, y + 76), WHITE, 14, GRID, 2)
        pill(d, 62, y + 21, 162, head, color, WHITE, 11)
        for j, value in enumerate([a, b1, c, e]):
            xx = 252 + j * 244
            rounded(d, (xx, y + 13, xx + 220, y + 50), PALE if j % 2 else SOFT, 10)
            text(d, (xx + 10, y + 31), value, 11, INK, True, "mm")
        y += 91
    section(d, 1306, 438, 572, "Instrumentation + kill rule", ORANGE)
    instruments = [
        ("IDs", "creator / SKU / audience / treatment"),
        ("EVENTS", "view → click → PDP → order → return"),
        ("EFFORT", "sample cost + creator time + payout"),
        ("QUALITY", "rating + defect + repeat signal"),
    ]
    y = 492
    for head, body in instruments:
        rounded(d, (1310, y, 1872, y + 70), WHITE, 14, GRID, 2)
        pill(d, 1332, y + 17, 82, head, ORANGE, PLUM_DARK, 10)
        text(d, (1432, y + 35), body, 13, INK, True, "lm")
        y += 80
    rounded(d, (1306, 834, 1878, 960), PLUM_DARK, 18)
    text(d, (1592, 862), "KILL / SCALE", 15, ORANGE, True, "mm")
    paragraph(d, (1334, 895), "Scale only if treatment beats control on the handoff without uneconomic creator effort or sample cost.", 510, 16, WHITE, True, 4)
    rounded(d, (44, 818, 1236, 960), SOFT, 18)
    text(d, (70, 842), "PILOT FUNNEL | TARGET / ASSUMPTION, NOT OBSERVED RESULT", 13, PLUM_DARK, True)
    funnel = [
        ("CREATORS", "recruited", .85, PINK),
        ("CONTENT", "created", .70, "#20aebd"),
        ("REACH", "viewers", .62, ORANGE),
        ("CLICKS", "product taps", .45, PLUM),
        ("ORDERS", "completed", .30, "#879327"),
        ("REPEAT", "reorder", .16, PINK),
    ]
    x = 70
    for label, sub, level, color in funnel:
        rounded(d, (x, 870, x + 174, 934), WHITE, 10, GRID, 1)
        text(d, (x + 12, 883), label, 10, PLUM_DARK, True)
        tiny_bar(d, x + 12, 907, 150, level, color, h=9)
        text(d, (x + 12, 928), sub, 9, MUTED, True)
        x += 190
    text(d, (640, 950), "Measure the full chain before scaling creator supply.", 12, MUTED, True, "mm")
    pill(d, 1610, 975, 240, "LIVE PROTOTYPE ↗", PINK, WHITE, 11)
    footer(d, "All cohort sizes and metrics are proposed operating parameters. The pilot exists to generate Meesho-specific evidence.")
    return b


def board_appendix(title, kicker, subtitle):
    b, d = new_board(CREAM), None
    d = ImageDraw.Draw(b)
    logo_header(d, title, kicker)
    text(d, (44, 116), subtitle, 17, MUTED)
    return b, d


def board_evidence():
    b, d = board_appendix("Evidence architecture: every claim has a status.", "APPENDIX | RESEARCH QUALITY", "We separate what was seen, what is public, what is inferred and what is still missing so the case stays defensible under challenge.")
    section(d, 44, 158, 1250, "Research status board")
    section(d, 1330, 158, 548, "Submission guardrails", ORANGE)
    tiers = [("DIRECT OBSERVATION", "CCA manual-quality content audit: 28 accessible records.", "May support capability claims", PLUM), ("PUBLIC ARTIFACT", "Official program / platform documentation and public pages.", "May support capability existence", "#20aebd"), ("INFERENCE", "Proof handoff is a plausible addressable leak.", "Must be labelled diagnosis", ORANGE), ("PENDING", "Meesho conversion, repeat, earnings, respondent evidence.", "Cannot be called validated", PINK)]
    y = 218
    for head, body, rule, color in tiers:
        rounded(d, (44, y, 278, y + 86), color, 16)
        text(d, (161, y + 43), head, 15, WHITE, True, "mm")
        rounded(d, (306, y, 760, y + 86), WHITE, 16, GRID, 2)
        paragraph(d, (330, y + 19), body, 390, 15, INK)
        rounded(d, (786, y, 1294, y + 86), LILAC if color == PLUM else SOFT, 16)
        paragraph(d, (810, y + 19), rule, 450, 15, PLUM_DARK, True)
        y += 105
    side_label(d, 8, 218, 450, "EVIDENCE LADDER")
    section(d, 44, 666, 1250, "Claim promotion rule", ORANGE)
    promotion = [
        ("1", "Artifact", "source record exists", PLUM),
        ("2", "Replay", "independent observer can reproduce it", CYAN),
        ("3", "Triangulation", "second source or cohort confirms it", ORANGE),
        ("4", "Decision", "claim earns a place in the core story", PINK),
    ]
    x = 44
    for num, head, body, color in promotion:
        rounded(d, (x, 718, x + 292, 812), WHITE, 14, color, 2)
        icon_circle(d, x + 16, 733, num, color, 34, PLUM_DARK if color in [ORANGE, CYAN] else WHITE)
        text(d, (x + 62, 736), head, 14, PLUM_DARK, True)
        text(d, (x + 62, 765), body, 12, INK)
        x += 310
    section(d, 44, 842, 1250, "Source-to-claim mapping", PLUM_DARK)
    claim_map = [
        ("A", "Meesho surface", "category page visible; PDP blocked", "#20aebd"),
        ("B", "Creator capability", "28 accessible audits; descriptive only", PINK),
        ("C", "Competitor benchmark", "one capability + artifacts + pending", ORANGE),
        ("P", "Primary research", "tracker exists; respondent count = 0", PLUM),
    ]
    x = 44
    for code, head, body, color in claim_map:
        rounded(d, (x, 894, x + 292, 1018), WHITE, 14, color, 2)
        icon_circle(d, x + 14, 910, code, color, 30, PLUM_DARK if color == ORANGE else WHITE)
        text(d, (x + 58, 910), head, 12, PLUM_DARK, True)
        paragraph(d, (x + 14, 950), body, 262, 11, INK, True, 2)
        x += 310
    guards = [("NO FABRICATED TIMESTAMPS", "Sequential transcript logs are not line-level timecodes."), ("NO FABRICATED RESPONDENTS", "Primary tracker count remains 0 unless independently recorded."), ("NO INVENTED UPLIFT", "Pilot metrics are proposed, not observed results."), ("NO H0–H5 SCORE", "Hypotheses remain open until primary research and transaction evidence.")]
    y = 220
    for head, body in guards:
        rounded(d, (1330, y, 1878, y + 86), WHITE, 16, ORANGE, 2)
        text(d, (1360, y + 18), head, 15, PLUM_DARK, True)
        paragraph(d, (1360, y + 46), body, 480, 13, INK)
        y += 105
    rounded(d, (1330, 665, 1878, 815), PLUM_DARK, 18)
    text(d, (1604, 710), "Research position today:\nstrong creator-proof evidence,\nweak Meesho handoff evidence.", 21, WHITE, True, "mm")
    section(d, 1330, 842, 548, "Current evidence ledger", ORANGE)
    ledger = [("A", "1 category page / 1 blocked PDP", "#20aebd"), ("B", "28 accessible audits / 2 blocked", PINK), ("C", "1 capability / artifacts / pending", ORANGE), ("P", "0 primary respondents", PLUM)]
    y = 894
    for code, value, color in ledger:
        icon_circle(d, 1342, y, code, color, 26, PLUM_DARK if color == ORANGE else WHITE)
        text(d, (1382, y + 13), value, 12, INK, True)
        y += 31
    footer(d, "Source files: DICE_GATE1_AUDIT_WORKBOOK.md | DICE_EVIDENCE_DATABASE.md | DICE_PRIMARY_RESEARCH_TRACKER.md.")
    return b


def board_creator():
    b, d = board_appendix("Creator proof is already decision-grade in many cases.", "APPENDIX | STREAM B", "The audit weakens a generic “content difficulty” diagnosis. It strengthens the question: where does useful proof leak before purchase.")
    metrics = [("26/28", "live product demonstrations", PLUM_DARK), ("24/28", "suitability discussions", PINK), ("22/28", "shade / colour fit", ORANGE), ("23/28", "visible outcomes", "#20aebd"), ("0/28", "routed to Meesho in sample", PINK)]
    x = 44
    for value, label, color in metrics:
        metric(d, x, 158, 340 if x < 1390 else 488, value, label, color)
        x += 360 if x < 1390 else 0
    section(d, 44, 252, 1238, "Evidence cards | observed content capability")
    examples = [("CCA-006", "Shade warning", "Lakme Nude Twist washed out without base.", ORANGE), ("CCA-007", "Viral reality check", "Pillow Talk / cult products failed on Indian-skin fit or comfort.", PINK), ("CCA-010", "Budget quality split", "Zudio eyeliner worked; bullet lipsticks were grainy and dry.", "#879327"), ("CCA-023", "Suitability matching", "Dry-skin kit explains cream-vs-powder mechanics and oxidation.", "#20aebd"), ("CCA-024", "Undertone proof", "Professional swatching across 15 shades makes fit legible.", PLUM), ("CCA-028", "Trust economics", "Fake virality and paid scripts expose review constraints.", PINK)]
    y = 304
    for eid, title, body, color in examples:
        evidence_tag(d, 58, y + 15, eid, color)
        card(d, 170, y, 1090, 72, title, body, color)
        y += 82
    section(d, 44, 814, 1238, "What travels well | what breaks at the handoff", ORANGE)
    travel = [
        ("TRAVELS", "shade / undertone", "creator shows the comparison", "#20aebd"),
        ("TRAVELS", "texture / finish", "creator applies and narrates", "#20aebd"),
        ("BREAKS", "proof → SKU identity", "no Meesho-linked route in sample", PINK),
        ("BREAKS", "proof → attribution", "no Meesho conversion / earnings evidence", PINK),
    ]
    x = 44
    for status, label, body, color in travel:
        rounded(d, (x, 868, x + 292, 984), WHITE, 14, color, 2)
        pill(d, x + 14, 884, 88, status, color, PLUM_DARK if color == "#20aebd" else WHITE, 10)
        text(d, (x + 116, 900), label, 12, PLUM_DARK, True)
        paragraph(d, (x + 14, 928), body, 262, 11, INK, True, 2)
        x += 310
    section(d, 1320, 252, 558, "What the audit does not prove", PINK)
    gaps = ["No Meesho-specific conversion or attribution.", "No repeat purchase or creator earnings.", "No longitudinal skin outcome tracking.", "No line-level timestamps where caption stream lacked them.", "No evidence that proof is portable into a PDP."]
    y = 314
    for gap in gaps:
        rounded(d, (1330, y, 1870, y + 66), WHITE, 14, GRID, 2)
        pill(d, 1350, y + 16, 36, "!", PINK, WHITE, 17)
        text(d, (1410, y + 33), gap, 14, INK, True, "lm")
        y += 78
    rounded(d, (1320, 760, 1878, 900), PLUM_DARK, 18)
    text(d, (1599, 808), "The evidence changes the problem statement:\nnot content creation — proof transfer.", 20, WHITE, True, "mm")
    quote_card(d, 1320, 910, 558, 76, "Useful proof is observable. Its commerce value is not yet observable.", "Synthesis from CCA audit | inference", ORANGE)
    footer(d, "Evidence tier: user-supplied manual audit layer. Counts are descriptive and do not establish transaction impact.")
    return b


def board_competitor():
    b, d = board_appendix("Competitor benchmark: separate capability from verified journey.", "APPENDIX | STREAM C", "The corrected record is more credible: one public-source capability, public artifacts, and pending flows—not five independently verified journeys.")
    section(d, 44, 158, 1834, "Seven-stage flow audit")
    stages = ["DISCOVERY", "SELECTION", "INFO", "PROOF", "SHOPPING", "ATTRIBUTION", "EARNINGS"]
    x = 44
    for i, st in enumerate(stages):
        chevron(d, x, 210, 257, st, "stage " + str(i + 1), [PLUM, ORANGE, PINK, PINK, "#20aebd", "#879327", PLUM][i], st == "SHOPPING")
        x += 260
    side_label(d, 8, 310, 430, "SOURCE STATUS")
    records = [("FLOW-001", "YouTube Shopping", "PUBLIC-SOURCE EVIDENCED", "Official documentation supports a capability map; authenticated dashboards and replayed creator journey are not in workspace.", PLUM), ("COMP-001", "Myntra / creator program", "PUBLIC PROGRAM ARTIFACT", "Program existence is evidenced; full stage-by-stage conversion and earnings flow is not.", ORANGE), ("COMP-002/3", "Google partner announcement", "PUBLIC PARTNER ARTIFACT", "Partner access is evidenced; SKU selection, attribution and payout details remain unverified.", "#20aebd"), ("COMP-004/5", "Amazon / Meta", "PENDING", "No complete workspace source record supporting all seven stages.", PINK)]
    y = 310
    for eid, name, status, limitation, color in records:
        evidence_tag(d, 58, y + 18, eid, color)
        rounded(d, (170, y, 505, y + 78), WHITE, 14, GRID, 2)
        text(d, (188, y + 39), name, 16, PLUM_DARK, True, "lm")
        rounded(d, (525, y, 865, y + 78), CYAN if status != "PENDING" else SOFT, 14)
        text(d, (695, y + 39), status, 13, PLUM_DARK, True, "mm")
        rounded(d, (885, y, 1878, y + 78), WHITE, 14, GRID, 2)
        paragraph(d, (910, y + 15), limitation, 940, 14, INK)
        y += 91
    section(d, 44, 704, 1834, "What is and is not independently verifiable", ORANGE)
    matrix_headers = ["FLOW", "DISCOVERY", "SELECTION", "INFO", "PROOF", "SHOPPING", "ATTRIBUTION", "EARNINGS"]
    widths = [180, 205, 205, 205, 205, 205, 205, 205]
    x = 44
    for h, w in zip(matrix_headers, widths):
        rounded(d, (x, 756, x + w, 788), PLUM_DARK, 0)
        text(d, (x + w // 2, 772), h, 10, WHITE, True, "mm")
        x += w
    matrix_rows = [
        ("FLOW-001", ["PUBLIC", "PUBLIC", "PUBLIC", "PUBLIC", "PUBLIC", "PRIVATE", "PRIVATE"], PLUM),
        ("COMP-001/3", ["PUBLIC", "PUBLIC", "PUBLIC", "PUBLIC", "INFER", "INFER", "PRIVATE"], ORANGE),
        ("COMP-004/5", ["PENDING", "PENDING", "PENDING", "PENDING", "PENDING", "PENDING", "PENDING"], PINK),
    ]
    y = 796
    for flow, statuses, color in matrix_rows:
        x = 44
        rounded(d, (x, y, x + widths[0], y + 38), WHITE, 0, GRID, 1)
        text(d, (x + 12, y + 19), flow, 11, PLUM_DARK, True, "lm")
        x += widths[0]
        for status, w in zip(statuses, widths[1:]):
            fill = CYAN if status == "PUBLIC" else SOFT if status in ["INFER", "PRIVATE"] else WHITE
            rounded(d, (x, y, x + w, y + 38), fill, 0, GRID, 1)
            text(d, (x + w // 2, y + 19), status, 9, PLUM_DARK if status != "PRIVATE" else MUTED, True, "mm")
            x += w
        y += 42
    rounded(d, (44, 926, 1878, 1018), PLUM_DARK, 18)
    paragraph(d, (80, 948), "Benchmark implication  →  Meesho does not need to copy every competitor feature. It needs one measurable proof-to-commerce bridge, then the interaction data to decide what to build next.", 1760, 18, WHITE, True, 4)
    footer(d, "Stream C status: 1 public-source capability record; 3 public artifacts; 2 pending. Authenticated/private claims are not independently verifiable.")
    return b


def board_hypothesis():
    b, d = board_appendix("H0–H5 remain open; the research now tells us what to test.", "APPENDIX | HYPOTHESIS STATUS", "We do not score hypotheses from descriptive creator content alone. We preserve contradictions and define the next evidence needed.")
    section(d, 44, 158, 1834, "Evidence / contradiction / next test")
    side_label(d, 8, 210, 520, "HYPOTHESIS BOARD")
    cols = [230, 410, 420, 550, 224]
    headers = ["HYPOTHESIS", "SUPPORTING SIGNAL", "CONTRADICTION / LIMIT", "NEXT TEST", "STATUS"]
    x = 44
    for h, w in zip(headers, cols):
        rounded(d, (x, 210, x + w, 254), PLUM_DARK, 0)
        text(d, (x + w // 2, 232), h, 14, WHITE, True, "mm")
        x += w
    rows = [("H0 | quality / trust", "Defects, viral mismatch and PR pressure appear.", "Cannot size returns or authenticity impact.", "Seller + shopper interviews; returns / ratings pilot.", "OPEN", PINK), ("H1 | creator-SKU fit", "Specialist creators make undertone and suitability legible.", "May be true only for specialist formats.", "Creator interview: matching, selection and effort.", "OPEN", PINK), ("H2 | sampling", "PR volume and waste are directly visible.", "Gifting may create bias and uneconomic effort.", "Seller economics + targeted sample test.", "OPEN", ORANGE), ("H3 | proof difficulty", "26/28 demos; 24/28 suitability discussions.", "Proof quality does not prove transaction transfer.", "Shopper test: which fields change confidence/click.", "CHALLENGED", "#20aebd"), ("H4 | decision support", "Shade, texture and outcome proof recur.", "No Meesho PDP / conversion evidence.", "Treatment vs control proof handoff.", "OPEN", "#879327"), ("H5 | creator economics", "Affiliate codes, PR pressure and commissions observed.", "Earnings and conversion logs are absent.", "Creator interviews + attributed pilot earnings.", "OPEN", PLUM)]
    y = 260
    for row in rows:
        x = 44
        for j, (value, w) in enumerate(zip(row[:5], cols)):
            fill = CYAN if row[4] == "CHALLENGED" else WHITE
            rounded(d, (x, y, x + w, y + 78), fill, 0, GRID, 2)
            text(d, (x + 12 if j < 4 else x + w // 2, y + 39), value, 14 if j else 15, PLUM_DARK if j == 0 else INK, j == 0 or j == 4, "lm" if j < 4 else "mm")
            x += w
        y += 83
    section(d, 44, 772, 1160, "Contradiction that changes the case", ORANGE)
    quote_card(d, 44, 820, 1160, 120, "Creators can already make fit, shade, texture and outcome legible. The next test is not whether proof exists; it is whether proof transfer changes behaviour.", "H3 challenged by CCA-001–030 descriptive audit", "#20aebd")
    section(d, 1240, 772, 638, "Next evidence required", PINK)
    next_tests = [("CREATORS", "effort + attribution + payout", PINK), ("SHOPPERS", "confidence + click + fit", "#20aebd"), ("SELLERS", "quality + return + repeat", ORANGE)]
    y = 824
    for head, body, color in next_tests:
        pill(d, 1260, y, 112, head, color, PLUM_DARK if color == ORANGE else WHITE, 10)
        text(d, (1390, y + 17), body, 12, INK, True)
        y += 42
    footer(d, "No hypothesis has been statistically scored or declared validated.")
    return b


def board_engine():
    b, d = board_appendix("The long-term moat is a learning loop, not a sample box.", "APPENDIX | FUTURE ENGINE", "The wedge is intentionally small. Its output is the interaction data required for Creator x SKU x Audience allocation.")
    section(d, 44, 158, 1834, "Decision engine wireframe")
    section(d, 70, 210, 390, "INPUTS", ORANGE)
    items = [("CREATOR", "audience / credibility / effort"), ("SKU", "category / margin / authenticity"), ("AUDIENCE", "concern / budget / context"), ("PROOF", "shade / texture / outcome / caveat")]
    y = 260
    for head, body in items:
        card(d, 70, y, 390, 75, head, body, ORANGE)
        y += 88
    rounded(d, (530, 210, 1375, 650), PLUM_DARK, 20)
    text(d, (952, 252), "BEAUTY PROOF BRIDGE", 24, ORANGE, True, "mm")
    nodes = [("MATCH", "relevant creator ↔ SKU", PINK), ("CAPTURE", "structured proof fields", "#20aebd"), ("SURFACE", "contextual Meesho decision point", ORANGE), ("ATTRIBUTE", "creator / SKU / audience IDs", "#879327"), ("LEARN", "click, order, return, repeat, payout", PINK)]
    y = 302
    for i, (head, body, color) in enumerate(nodes):
        rounded(d, (650, y, 1255, y + 54), color, 16)
        text(d, (682, y + 27), head, 14, PLUM_DARK if color in [ORANGE, "#879327"] else WHITE, True, "lm")
        text(d, (860, y + 27), body, 15, PLUM_DARK if color in [ORANGE, "#879327"] else WHITE, True, "lm")
        y += 68
    section(d, 1430, 210, 448, "OUTPUTS", "#20aebd")
    outputs = [("SHOPPER", "faster fit decision"), ("SELLER", "better SKU demand signal"), ("CREATOR", "clearer attribution + payout"), ("MEESHO", "better allocation data")]
    y = 260
    for head, body in outputs:
        card(d, 1430, y, 448, 86, head, body, "#20aebd")
        y += 98
    section(d, 530, 694, 845, "Meesho proof surface | low-fi wireframe", ORANGE)
    rounded(d, (562, 748, 1342, 920), WHITE, 16, GRID, 2)
    rounded(d, (586, 768, 824, 900), PALE, 12)
    text(d, (706, 792), "CREATOR PROOF", 12, PLUM_DARK, True, "mm")
    rounded(d, (612, 824, 798, 850), CYAN, 8)
    text(d, (705, 837), "Shade: warm olive", 10, PLUM_DARK, True, "mm")
    rounded(d, (612, 862, 798, 888), PINK, 8)
    text(d, (705, 875), "Texture: light / blendable", 10, WHITE, True, "mm")
    text(d, (850, 786), "Creator: relevant reviewer", 12, INK, True)
    text(d, (850, 818), "Fit for: dry skin | medium tone", 11, MUTED)
    text(d, (850, 850), "Observed caveat: oxidises slightly", 11, MUTED)
    rounded(d, (850, 876, 1082, 906), ORANGE, 10)
    text(d, (966, 891), "SEE PROOF / SHOP", 11, PLUM_DARK, True, "mm")
    rounded(d, (1102, 776, 1318, 900), PLUM_DARK, 12)
    text(d, (1210, 804), "ATTRIBUTION", 11, ORANGE, True, "mm")
    text(d, (1210, 842), "creator / SKU /\naudience ID", 13, WHITE, True, "mm")
    rounded(d, (70, 942, 1848, 1010), SOFT, 18)
    text(d, (959, 976), "Do not build the engine first. Build the first data-generating wedge that earns the right to build it.", 19, PLUM_DARK, True, "mm")
    footer(d, "Future-state architecture; not a claim that Meesho currently has these matching signals.")
    return b


def board_economics():
    b, d = board_appendix("Measurement turns the idea into a business case.", "APPENDIX | PILOT ECONOMICS", "We will size the opportunity from observed pilot deltas—not invented market-response percentages.")
    rounded(d, (44, 158, 1878, 240), PLUM_DARK, 18)
    text(d, (961, 199), "BPC NMV = active creators × relevant proof × click-through × PDP-to-order × AOV × repeat", 25, WHITE, True, "mm")
    section(d, 44, 270, 930, "Measurement stack")
    section(d, 1000, 270, 878, "What becomes knowable")
    drivers = [("ACTIVE CREATORS", "sample-to-post\nretention"), ("RELEVANT PROOF", "completeness\nusefulness"), ("CLICK-THROUGH", "placement\nCTA quality"), ("CONVERSION", "fit confidence\nPDP support"), ("REPEAT", "quality\nreturns / reorder")]
    x = 44
    for head, body in drivers:
        rounded(d, (x, 324, x + 170, 450), WHITE, 16, PLUM, 2)
        text(d, (x + 85, 354), head, 10, PLUM_DARK, True, "mm")
        text(d, (x + 85, 407), body, 15, INK, True, "mm")
        x += 178
    bullets = ["Unique creator / SKU / audience / treatment IDs.", "Tagged click, PDP, order and return events.", "Sample cost, creator time and payout.", "Rating, defect and repeat cohort."]
    y = 512
    for item in bullets:
        pill(d, 68, y, 32, "•", ORANGE, PLUM_DARK, 18)
        text(d, (120, y + 17), item, 18, INK, True, "lm")
        y += 55
    know = [("Which proof fields correlate with clicks and orders?", "#20aebd"), ("Which creators produce efficient, credible proof?", PINK), ("Do targeted samples beat broad gifting?", ORANGE), ("Does the bridge deserve scale or a kill?", "#879327")]
    y = 326
    for label, color in know:
        rounded(d, (1000, y, 1878, y + 70), WHITE, 16, color, 2)
        pill(d, 1024, y + 18, 38, "→", color, PLUM_DARK if color in [ORANGE, "#879327"] else WHITE, 18)
        text(d, (1085, y + 35), label, 17, INK, True, "lm")
        y += 85
    rounded(d, (1000, 690, 1878, 790), PLUM_DARK, 18)
    text(d, (1439, 740), "No uplift is claimed. The pilot generates the evidence to size uplift.", 20, WHITE, True, "mm")
    section(d, 44, 782, 1834, "Pilot event spine | the data that turns a story into a business case", ORANGE)
    events = [
        ("01", "VIEW", "proof shown", PLUM),
        ("02", "CLICK", "tag / CTA", PINK),
        ("03", "PDP", "fit resolved", "#20aebd"),
        ("04", "ORDER", "transaction", ORANGE),
        ("05", "RETURN", "quality signal", "#879327"),
        ("06", "REPEAT", "retention", PLUM),
    ]
    x = 44
    for i, (num, head, body, color) in enumerate(events):
        rounded(d, (x, 838, x + 278, 928), WHITE, 14, color, 2)
        icon_circle(d, x + 14, 852, num, color, 28, PLUM_DARK if color in [ORANGE, "#879327"] else WHITE)
        text(d, (x + 56, 854), head, 13, PLUM_DARK, True)
        text(d, (x + 56, 883), body, 11, MUTED, True)
        if i < len(events) - 1:
            text(d, (x + 282, 882), "→", 20, PINK, True, "mm")
        x += 304
    owners = [("CREATOR", "time + payout", PINK), ("SHOPPER", "confidence + fit", "#20aebd"), ("SELLER", "quality + margin", ORANGE), ("MEESHO", "allocation + NMV", "#879327")]
    x = 44
    for head, body, color in owners:
        rounded(d, (x, 946, x + 438, 1016), PALE, 12)
        pill(d, x + 14, 963, 92, head, color, PLUM_DARK if color in [ORANGE, "#879327"] else WHITE, 9)
        text(d, (x + 126, 980), body, 12, INK, True, "lm")
        x += 458
    footer(d, "Illustrative measurement model only. No conversion, NMV, repeat or retention result is claimed.")
    return b


def board_risks():
    b, d = board_appendix("A credible case makes disproof visible.", "APPENDIX | RISKS + ROADMAP", "The bridge is only a winner if it survives creator, shopper, seller and economics reality.")
    section(d, 44, 158, 1020, "Kill criteria")
    section(d, 1100, 158, 778, "Scale path")
    risks = [("Proof does not move orders", "Kill or redesign; investigate price, quality, delivery and PDP UX.", PINK), ("Creators reject effort", "Shift toward economics, lighter formats or better matching.", PINK), ("Sampling is uneconomic", "Narrow SKU set; require seller co-funding or repeat potential.", ORANGE), ("PDP cannot carry proof", "Use a landing/storefront surface while integration is built.", "#20aebd"), ("Quality dominates returns", "Move trust / authenticity to the front of the roadmap.", "#879327")]
    y = 214
    for head, body, color in risks:
        rounded(d, (44, y, 1064, y + 74), WHITE, 14, color, 2)
        pill(d, 64, y + 20, 280, head.upper(), color, WHITE, 12)
        text(d, (374, y + 37), body, 15, INK, True, "lm")
        y += 86
    roadmap = [("30 DAYS", "Pilot bridge; instrument the full handoff.", "#20aebd"), ("60 DAYS", "Add reusable proof fields and seller reporting.", PINK), ("90 DAYS", "Use interaction data to rank creator–SKU–audience matches.", ORANGE)]
    y = 220
    for head, body, color in roadmap:
        rounded(d, (1120, y, 1858, y + 104), WHITE, 16, color, 2)
        pill(d, 1142, y + 35, 145, head, color, PLUM_DARK if color == ORANGE else WHITE, 13)
        text(d, (1320, y + 52), body, 16, INK, True, "lm")
        y += 122
    rounded(d, (1120, 620, 1858, 760), PLUM_DARK, 18)
    text(d, (1489, 690), "North star:\nmore BPC NMV from better proof transfer.", 23, WHITE, True, "mm")
    rounded(d, (44, 760, 1064, 848), SOFT, 18)
    text(d, (554, 804), "Research next: creators + shoppers + sellers before scale.", 20, PLUM_DARK, True, "mm")
    section(d, 44, 872, 1814, "Decision gates | what the next sprint must produce", ORANGE)
    gates = [
        ("CREATOR", "real effort + payout path", "interview / pilot log", PINK),
        ("SHOPPER", "proof field that changes confidence", "task test / click proxy", "#20aebd"),
        ("SELLER", "SKU quality + economics", "campaign / return record", ORANGE),
        ("MEESHO", "measurable handoff surface", "instrumented pilot", "#879327"),
    ]
    x = 44
    for head, need, artifact, color in gates:
        rounded(d, (x, 920, x + 438, 1008), WHITE, 14, color, 2)
        pill(d, x + 16, 934, 104, head, color, PLUM_DARK if color in [ORANGE, "#879327"] else WHITE, 10)
        text(d, (x + 136, 938), need, 12, PLUM_DARK, True)
        text(d, (x + 136, 969), artifact, 11, MUTED, True)
        x += 458
    footer(d, "Team: Samiksha Mitra | Slayed it | IIT Guwahati | Full source ledger remains in the workspace.")
    return b


def board_sources():
    b, d = board_appendix("The claim stack is traceable from evidence to pilot.", "APPENDIX | SOURCE LEDGER", "The case is intentionally bounded: every important statement is tagged to an evidence family, a limitation and a next decision.")
    section(d, 44, 158, 1834, "Source ledger | what each evidence family can and cannot support")
    side_label(d, 8, 210, 708, "TRACEABILITY")
    headers = ["FAMILY", "SOURCE / ARTIFACT", "SUPPORTS", "DOES NOT SUPPORT", "NEXT DECISION"]
    widths = [190, 340, 405, 440, 415]
    x = 44
    for h, w in zip(headers, widths):
        rounded(d, (x, 210, x + w, 252), PLUM_DARK, 0)
        text(d, (x + w // 2, 231), h, 11, WHITE, True, "mm")
        x += w
    rows = [
        ("A | Meesho", "M-CAT-001 category page; M-PDP-001 403 record", "Public category cues; access limitation", "PDP proof, conversion, return or repeat", "Secure replayable PDP evidence"),
        ("B | Creator", "CCA-001–030; 28 accessible audits", "Proof capability, suitability, shade, outcome, CTA patterns", "Meesho routing, transaction impact, earnings", "Test proof transfer with real cohorts"),
        ("C | Competitor", "COMP-FLOW-001 + public artifacts", "Capability existence and benchmark structure", "Five verified end-to-end journeys; private economics", "Replay one complete flow independently"),
        ("P | Primary", "DICE_PRIMARY_RESEARCH_TRACKER.md", "Interview / survey design and lead pipeline", "Any respondent finding; any H0–H5 score", "Acquire genuine creator, shopper and seller responses"),
    ]
    y = 264
    colors = [CYAN, PINK, ORANGE, PLUM]
    for i, row in enumerate(rows):
        color = colors[i]
        x = 44
        for j, (value, w) in enumerate(zip(row, widths)):
            fill = CYAN if i == 1 and j == 2 else WHITE
            rounded(d, (x, y, x + w, y + 84), fill, 0, color if j == 0 else GRID, 2 if j == 0 else 1)
            text(d, (x + 12, y + 16), value, 12 if j == 0 else 11, PLUM_DARK if j == 0 else INK, j == 0 or j == 4, "lm")
            x += w
        y += 92
    section(d, 44, 650, 1160, "Evidence-strength legend", ORANGE)
    legend = [
        ("DIRECT", "observed in the workspace", PLUM),
        ("PUBLIC", "official / public-source artifact", CYAN),
        ("INFERRED", "diagnosis or model, labelled", ORANGE),
        ("PENDING", "primary / private evidence needed", PINK),
    ]
    x = 44
    for label, body, color in legend:
        rounded(d, (x, 704, x + 274, 790), WHITE, 14, color, 2)
        pill(d, x + 14, 718, 82, label, color, PLUM_DARK if color in [ORANGE, CYAN] else WHITE, 9)
        text(d, (x + 112, 742), body, 10, INK, True)
        x += 292
    section(d, 44, 816, 1160, "Decision rule for the next sprint", PLUM_DARK)
    quote_card(d, 44, 864, 1160, 126, "Promote the Beauty Proof Bridge only if independent respondents and a real instrumented handoff show that proof changes measurable commerce behaviour.", "Core case rule | pilot hypothesis, not current fact", "#20aebd")
    section(d, 1240, 650, 638, "Open evidence queue", PINK)
    queue = [
        ("01", "Creators", "effort, selection, attribution, payout", PINK),
        ("02", "Shoppers", "confidence, click, purchase, fit regret", "#20aebd"),
        ("03", "Sellers", "SKU quality, returns, creator ROI", ORANGE),
        ("04", "Meesho", "PDP / tracking / cohort instrumentation", PLUM),
    ]
    y = 706
    for num, head, body, color in queue:
        rounded(d, (1240, y, 1878, y + 72), WHITE, 14, color, 2)
        icon_circle(d, 1256, y + 18, num, color, 34, PLUM_DARK if color == ORANGE else WHITE)
        text(d, (1306, y + 15), head, 13, PLUM_DARK, True)
        text(d, (1306, y + 41), body, 10, INK, True)
        y += 82
    rounded(d, (1240, 105, 1878, 140), SOFT, 10)
    text(d, (1559, 122), "12-slide finalist-length submission", 11, PLUM_DARK, True, "mm")
    footer(d, "Source ledger: DICE_MASTER_DOC.md | DICE_EVIDENCE_DATABASE.md | DICE_GATE1_AUDIT_WORKBOOK.md | DICE_PRIMARY_RESEARCH_TRACKER.md.")
    return b


def source_ref(draw, x, y, value, color=MUTED, width=400):
    text(draw, (x, y), value, 10, color, True)


def research_tile(draw, x, y, w, value, label, source, color):
    rounded(draw, (x, y, x + w, y + 82), WHITE, 12, color, 2)
    text(draw, (x + 14, y + 12), value, 29, color, True)
    text(draw, (x + 14, y + 48), label.upper(), 10, PLUM_DARK, True)
    text(draw, (x + w - 14, y + 13), source, 9, MUTED, True, "ra")


def status_dot(draw, x, y, status, color):
    draw.ellipse((x, y, x + 22, y + 22), fill=color)
    text(draw, (x + 11, y + 11), status, 10, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, True, "mm")


def evidence_chip(draw, x, y, w, eid, title, body, color):
    rounded(draw, (x, y, x + w, y + 92), WHITE, 12, color, 2)
    pill(draw, x + 12, y + 12, 84, eid, color, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, 9)
    text(draw, (x + 110, y + 14), title, 12, PLUM_DARK, True)
    paragraph(draw, (x + 14, y + 47), body, w - 28, 11, INK, False, 2)


def methodology_band(draw, x, y, w):
    labels = [
        ("DESK", "market + literature", PLUM),
        ("A", "Meesho surface", CYAN),
        ("B", "28 creator audits", PINK),
        ("C", "competitor artifacts", ORANGE),
        ("P", "primary next", OLIVE),
    ]
    text(draw, (x, y - 20), "RESEARCH METHOD | COMPLETED EVIDENCE IN COLOR; PRIMARY RESEARCH REMAINS OPEN", 10, MUTED, True)
    xx = x
    for head, body, color in labels:
        rounded(draw, (xx, y, xx + 210, y + 48), color, 10)
        text(draw, (xx + 12, y + 10), head, 12, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, True)
        text(draw, (xx + 52, y + 11), body, 10, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, True)
        xx += 220
    rounded(draw, (xx, y, x + w, y + 48), WHITE, 10, PINK, 2)
    text(draw, (xx + 14, y + 11), "NEXT", 11, PINK, True)
    text(draw, (xx + 60, y + 11), "creator + shopper + seller interviews", 10, INK, True)


def board_cover():
    board = COVER_ART.resize((W, H), Image.Resampling.LANCZOS).convert("RGBA")
    overlay = Image.new("RGBA", (W, H), (71, 0, 57, 0))
    od = ImageDraw.Draw(overlay)
    od.rectangle((0, 0, 1040, H), fill=(71, 0, 57, 178))
    board.alpha_composite(overlay)
    d = ImageDraw.Draw(board)
    rounded(d, (80, 70, 400, 112), ORANGE, 20)
    text(d, (240, 91), "MEESHO DICE CHALLENGE | S3", 16, PLUM_DARK, True, "mm")
    text(d, (84, 218), "Beauty proof is abundant.", 58, WHITE, True)
    text(d, (84, 286), "Commerce handoff is not.", 58, WHITE, True)
    text(d, (88, 360), "PS: Growing Beauty & Personal Care through Influencers", 15, ORANGE, True)
    text(d, (88, 392), "A measured bridge from creator evidence", 26, CREAM, True)
    text(d, (88, 431), "to confident Meesho purchase.", 26, CREAM, True)
    rounded(d, (84, 525, 730, 680), SOFT, 20)
    text(d, (115, 558), "PROPOSED PRODUCT CAPABILITY", 16, PINK, True)
    text(d, (115, 604), "Creator x SKU x Audience", 32, PLUM_DARK, True)
    text(d, (115, 642), "Decision Engine", 32, PLUM_DARK, True)
    rounded(d, (1110, 130, 1840, 820), WHITE, 22)
    text(d, (1160, 176), "RESEARCH BASE", 19, PINK, True)
    text(d, (1160, 210), "The recommendation is built from visible evidence, not a generic influencer thesis.", 17, INK, True)
    cover_rows = [
        ("28", "accessible creator-content audits", PINK),
        ("26/28", "product demonstrations", PLUM),
        ("24/28", "suitability discussions", CYAN),
        ("1 + 3 + 2", "Stream C: capability + artifacts + pending", ORANGE),
        ("1 / 1", "Meesho category page / blocked PDP", OLIVE),
        ("0", "primary respondents in tracker", PINK),
    ]
    y = 290
    for value, label, color in cover_rows:
        rounded(d, (1160, y, 1790, y + 70), CREAM, 12, color, 2)
        text(d, (1182, y + 12), value, 26, color, True)
        text(d, (1350, y + 25), label, 13, PLUM_DARK, True)
        y += 82
    rounded(d, (1160, 726, 1790, 786), PLUM_DARK, 12)
    text(d, (1475, 756), "Evidence -> insight -> engine -> pilot", 14, WHITE, True, "mm")
    text(d, (88, 900), "Team Slayed it", 24, WHITE, True)
    text(d, (88, 945), "Samiksha Mitra | IIT Guwahati", 18, CREAM)
    text(d, (88, 1002), "Evidence cut: 10 September 2026 | 13-slide finalist-length submission", 13, CREAM)
    return board.convert("RGB")


def board_value_chain():
    b = new_board(CREAM)
    d = ImageDraw.Draw(b)
    logo_header(d, "Proof exists. The handoff breaks before commerce.", "ROUND 1 | EVIDENCE EXHIBIT")
    text(d, (44, 116), "A dense evidence map of what creators already do, what Meesho can observe, and where the value chain becomes unmeasurable.", 16, MUTED)
    methodology_band(d, 44, 150, 1834)
    tiles = [
        ("28", "creator audits", "CCA-001–030", PINK),
        ("26/28", "product demos", "Team audit", PLUM),
        ("24/28", "suitability", "Team audit", CYAN),
        ("23/28", "outcome proof", "Team audit", ORANGE),
        ("0/28", "Meesho CTA", "sample only", OLIVE),
    ]
    x = 44
    for value, label, source, color in tiles:
        research_tile(d, x, 220, 340, value, label, source, color)
        x += 360
    section(d, 44, 326, 1515, "Evidence map | from creator decision support to measurable commerce")
    section(d, 1580, 326, 298, "Artifact wall", ORANGE)
    stages = [
        ("CREATOR", "audience + niche", "DIRECT", PINK),
        ("SKU", "shade + price + quality", "DIRECT", ORANGE),
        ("TRIAL", "use before recommendation", "DIRECT", PLUM),
        ("PROOF", "demo + fit + outcome", "DIRECT", CYAN),
        ("SURFACE", "Meesho decision point", "PENDING", OLIVE),
        ("ORDER", "click -> PDP -> buy", "PENDING", PINK),
        ("REPEAT", "return + reorder + payout", "PENDING", PLUM),
    ]
    x = 64
    y = 390
    widths = [200, 200, 200, 220, 220, 220, 220]
    for i, (head, sub, status, color) in enumerate(stages):
        w = widths[i]
        rounded(d, (x, y, x + w, y + 126), WHITE if status != "PENDING" else SOFT, 14, color, 3)
        pill(d, x + 14, y + 14, 78, status, color, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, 8)
        text(d, (x + 14, y + 54), head, 17, PLUM_DARK, True)
        text(d, (x + 14, y + 84), sub, 11, INK, True)
        if i < len(stages) - 1:
            text(d, (x + w + 7, y + 62), ">", 22, PINK, True, "mm")
        x += w + 16
    lanes = [
        ("WHAT WE CAN SEE", "CCA-023 / CCA-024: dry-skin mechanics + 15-shade undertone proof", CYAN),
        ("WHAT BREAKS", "CCA-028 / CCA-029 / CCA-030: PR waste, pressure and unclear payout", PINK),
        ("WHAT IS UNKNOWN", "M-CAT-001 visible; M-PDP-001 blocked; no Meesho conversion bridge", OLIVE),
    ]
    y = 544
    for head, body, color in lanes:
        rounded(d, (64, y, 1538, y + 62), WHITE, 10, color, 2)
        pill(d, 80, y + 14, 160, head, color, PLUM_DARK if color in [CYAN, OLIVE] else WHITE, 9)
        text(d, (266, y + 23), body, 13, INK, True)
        y += 74
    artifact_data = [
        ("CCA-024", "15 shade swatches", PLUM),
        ("CCA-023", "dry skin kit", CYAN),
        ("CCA-028", "fake virality", PINK),
        ("COMP-001", "public artifact", ORANGE),
        ("M-PDP-001", "403 blocked", OLIVE),
    ]
    y = 390
    for eid, label, color in artifact_data:
        rounded(d, (1600, y, 1858, y + 68), WHITE, 10, color, 2)
        pill(d, 1612, y + 17, 72, eid, color, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, 8)
        text(d, (1700, y + 24), label, 11, INK, True)
        y += 78
    rounded(d, (1600, 790, 1858, 936), PLUM_DARK, 14)
    text(d, (1729, 820), "DIAGNOSIS", 12, ORANGE, True, "mm")
    paragraph(d, (1620, 850), "Creators already create decision support. Meesho-specific proof transfer remains the test.", 218, 13, WHITE, True, 4)
    section(d, 44, 800, 1515, "Synthesis | the opportunity is not more content; it is a measurable handoff for content that already exists.", ORANGE)
    boxes = [
        ("PROOF EXISTS", "shade / texture / suitability / outcome", PLUM),
        ("CONTEXT BREAKS", "creator evidence is not tied to a Meesho SKU surface", PINK),
        ("VALUE LEAKS", "click, order, return, repeat and payout are not observed", CYAN),
    ]
    x = 44
    for head, body, color in boxes:
        rounded(d, (x, 854, x + 485, 970), WHITE, 12, color, 2)
        text(d, (x + 16, 874), head, 13, color, True)
        text(d, (x + 16, 908), body, 12, INK, True)
        x += 510
    footer(d, "Sources ↗ Team creator-content audit CCA-001–030 | M-CAT-001 | M-PDP-001 | Stream C evidence ledger. Counts are descriptive.")
    return b


def board_prioritization():
    b = new_board(CREAM)
    d = ImageDraw.Draw(b)
    logo_header(d, "The winning priority is the smallest bridge that creates the missing data.", "ROUND 1 | STRATEGY EXHIBIT")
    text(d, (44, 116), "We screened alternative explanations before choosing the Creator x SKU x Audience commerce connection as the 30-day pilot wedge.", 16, MUTED)
    section(d, 44, 158, 452, "H0-H5 candidate problem areas")
    section(d, 516, 158, 820, "Priority matrix | directional, not statistical")
    section(d, 1356, 158, 522, "Competitive benchmark")
    hyps = [
        ("H0", "quality / trust", "returns, defects, fake virality", PINK),
        ("H1", "creator-SKU fit", "undertone + audience matching", ORANGE),
        ("H2", "sampling economics", "PR waste + creator effort", CYAN),
        ("H3", "proof difficulty", "challenged by 26/28 demos", PLUM),
        ("H4", "decision support", "shade / texture / outcomes", OLIVE),
        ("H5", "creator economics", "payout + attribution unknown", PINK),
    ]
    y = 216
    for code, head, body, color in hyps:
        rounded(d, (44, y, 496, y + 82), WHITE if code != "H3" else CYAN, 10, color, 2)
        pill(d, 58, y + 22, 48, code, color, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, 10)
        text(d, (124, y + 14), head, 13, PLUM_DARK, True)
        text(d, (124, y + 42), body, 11, INK, True)
        text(d, (466, y + 31), "OPEN" if code != "H3" else "CHALL", 9, color, True, "ra")
        y += 91
    rounded(d, (516, 216, 1336, 726), WHITE, 14, GRID, 2)
    draw = d
    # Quadrant backdrop
    draw.line((926, 250, 926, 700), fill=GRID, width=2)
    draw.line((556, 510, 1296, 510), fill=GRID, width=2)
    text(d, (582, 238), "LOW ADDRESSABILITY", 10, MUTED, True)
    text(d, (1112, 238), "HIGH ADDRESSABILITY", 10, MUTED, True)
    text(d, (548, 274), "HIGH IMPACT", 10, MUTED, True)
    text(d, (548, 666), "LOW IMPACT", 10, MUTED, True)
    bubbles = [
        ("QUALITY / TRUST", 720, 344, 56, PINK, "parallel"),
        ("BROAD SAMPLING", 798, 560, 44, ORANGE, "narrow"),
        ("PROOF BRIDGE", 1106, 364, 82, PLUM, "PILOT"),
        ("PDP SUPPORT", 1010, 446, 58, CYAN, "pair"),
        ("FULL ENGINE", 1214, 282, 68, OLIVE, "later"),
        ("COMMISSION", 720, 602, 36, PINK, "defer"),
    ]
    for label, cx, cy, r, color, tag in bubbles:
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color, outline=WHITE, width=3)
        text(d, (cx, cy - 7), label, 10 if len(label) < 14 else 8, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, True, "mm")
        text(d, (cx, cy + 18), tag, 9, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, True, "mm")
    rounded(d, (516, 748, 1336, 936), PLUM_DARK, 14)
    text(d, (544, 776), "WINNING MOVE", 13, ORANGE, True)
    paragraph(d, (544, 810), "Pilot proof transfer first. It uses capability creators already demonstrate, tests the live commerce leak, and creates the interaction data needed before a full matching engine.", 760, 18, WHITE, True, 4)
    bench_headers = ["PLATFORM", "PROOF", "SURFACE", "ATTRIB.", "MEASURE"]
    widths = [170, 82, 82, 82, 82]
    x = 1356
    for h, w in zip(bench_headers, widths):
        rounded(d, (x, 216, x + w, 250), PLUM_DARK, 0)
        text(d, (x + w // 2, 233), h, 8, WHITE, True, "mm")
        x += w
    bench = [
        ("YouTube", [CYAN, CYAN, CYAN, SOFT], "public"),
        ("Amazon", [CYAN, CYAN, SOFT, SOFT], "artifact"),
        ("Nykaa", [CYAN, CYAN, SOFT, SOFT], "artifact"),
        ("Flipkart", [CYAN, CYAN, SOFT, SOFT], "artifact"),
        ("Myntra", [CYAN, CYAN, SOFT, SOFT], "artifact"),
        ("Meesho", [WHITE, WHITE, WHITE, WHITE], "gap"),
    ]
    y = 260
    for name, fills, tag in bench:
        rounded(d, (1356, y, 1526, y + 54), WHITE, 0, GRID, 1)
        text(d, (1366, y + 27), name, 10, PLUM_DARK, True, "lm")
        x = 1526
        for fill in fills:
            rounded(d, (x, y, x + 82, y + 54), fill, 0, GRID, 1)
            status_dot(d, x + 30, y + 16, "P" if fill == CYAN else "?", CYAN if fill == CYAN else PINK)
            x += 82
        y += 59
    rounded(d, (1356, 626, 1878, 726), SOFT, 10)
    text(d, (1374, 644), "Status legend", 10, PLUM_DARK, True)
    text(d, (1374, 672), "P = public artifact / ? = not independently verified", 10, INK, True)
    section(d, 1356, 748, 522, "Why Meesho | why now", ORANGE)
    why = [
        ("WHY MEESHO", "marketplace + seller breadth + transaction data"),
        ("WHY NOW", "creator proof is abundant; handoff evidence is missing"),
        ("MOAT", "more interactions -> better matching -> more data"),
    ]
    y = 800
    for head, body in why:
        rounded(d, (1356, y, 1878, y + 45), WHITE, 8, ORANGE, 1)
        pill(d, 1368, y + 7, 98, head, ORANGE, PLUM_DARK, 8)
        text(d, (1482, y + 14), body, 10, INK, True)
        y += 52
    footer(d, "Sources: CCA audit; Stream C corrected evidence ledger; H0–H5 status board. Prioritization is directional and not a completed hypothesis score.")
    return b


def board_quick_win():
    b = new_board(CREAM)
    d = ImageDraw.Draw(b)
    logo_header(d, "Slayed It turns creator proof into a learning commerce loop.", "ROUND 1 | SOLUTION BLUEPRINT")
    text(d, (44, 116), "Right creator x right SKU x right audience -> targeted proof -> measurable commerce -> the next better match.", 17, MUTED)
    # Compact evidence band: reference-style density without turning the slide into prose.
    evidence_row = [
        ("28", "accessible creator audits", "TEAM AUDIT", PINK),
        ("26/28", "product demonstrations", "OBSERVED", PLUM),
        ("24/28", "suitability discussions", "OBSERVED", CYAN),
        ("0/28", "sampled Meesho CTA destinations", "DIRECTIONAL", ORANGE),
    ]
    x = 44
    for value, label, tag, color in evidence_row:
        rounded(d, (x, 150, x + 442, 202), WHITE, 9, color, 2)
        text(d, (x + 14, 160), value, 23, color, True)
        text(d, (x + 112, 162), label.upper(), 10, PLUM_DARK, True)
        text(d, (x + 428, 184), tag, 8, color, True, "ra")
        x += 466
    rounded(d, (44, 220, 1878, 302), PLUM_DARK, 18)
    text(d, (961, 261), "RIGHT CREATOR  x  RIGHT SKU  x  RIGHT AUDIENCE  =  DECISION-GRADE DISCOVERY -> MEASURABLE COMMERCE", 23, WHITE, True, "mm")
    section(d, 44, 334, 1240, "Core system | a marketplace decision engine, not an influencer campaign")
    section(d, 1310, 334, 568, "Product moment | proposed internal tool", ORANGE)
    # Left engine
    rounded(d, (44, 390, 1284, 842), WHITE, 18, PLUM, 3)
    # Inputs
    input_cards = [
        ("CREATOR", "audience profile\nniche / style\ntrust / effort", PINK, 78),
        ("SKU", "shade / price\nclaims / quality\nseller signal", ORANGE, 392),
        ("AUDIENCE", "need / budget\ncontext / fit\nrisk tolerance", CYAN, 706),
    ]
    for head, body, color, xx in input_cards:
        rounded(d, (xx, 420, xx + 260, 560), color, 16)
        text(d, (xx + 130, 450), head, 16, PLUM_DARK if color in [ORANGE, CYAN] else WHITE, True, "mm")
        text(d, (xx + 130, 505), body, 13, PLUM_DARK if color in [ORANGE, CYAN] else WHITE, True, "mm")
        text(d, (xx + 130, 582), "+", 24, PINK, True, "mm")
    # Engine center
    rounded(d, (210, 598, 1118, 758), PLUM_DARK, 24)
    text(d, (664, 632), "MEESHO BPC DECISION ENGINE", 22, ORANGE, True, "mm")
    text(d, (664, 668), "FIT SIGNAL  ->  TARGETED SAMPLE  ->  STRUCTURED PROOF", 13, WHITE, True, "mm")
    stages = [("MATCH", PINK), ("SAMPLE", ORANGE), ("CREATE", CYAN), ("SURFACE", OLIVE), ("MEASURE", PLUM), ("LEARN", PINK)]
    x = 270
    for i, (label, color) in enumerate(stages):
        rounded(d, (x, 704, x + 115, 744), color, 10)
        text(d, (x + 57, 724), label, 10, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, True, "mm")
        if i < len(stages) - 1:
            text(d, (x + 125, 724), ">", 16, PINK, True, "mm")
        x += 140
    # Outputs
    output_cards = [
        ("SHOPPER", "better confidence\nfewer fit surprises", CYAN, 88),
        ("CREATOR", "clearer attribution\nrepeatable payout", PINK, 396),
        ("SELLER", "better SKU demand\nquality signal", ORANGE, 704),
        ("MEESHO", "transaction data\nnext better match", OLIVE, 1012),
    ]
    for head, body, color, xx in output_cards:
        rounded(d, (xx, 770, xx + 250, 852), WHITE, 12, color, 2)
        pill(d, xx + 14, 784, 92, head, color, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, 8)
        text(d, (xx + 14, 818), body, 11, INK, True)
    # Right product UI mockup. All values are explicitly illustrative, not observed.
    rounded(d, (1310, 390, 1878, 842), WHITE, 14, PLUM, 2)
    rounded(d, (1310, 390, 1878, 440), PLUM_DARK, 14)
    d.rectangle((1310, 420, 1878, 440), fill=PLUM_DARK)
    text(d, (1332, 408), "meesho. SLAYED IT", 14, WHITE, True)
    text(d, (1854, 408), "ILLUSTRATIVE", 9, ORANGE, True, "ra")
    text(d, (1332, 460), "CREATOR COMMERCE DECISION ENGINE", 9, PINK, True)
    # Match inputs
    ui_fields = [
        ("AUDIENCE", "Dry / sensitive skin", CYAN),
        ("CREATOR", "Aarohi | dry-skin specialist", PINK),
        ("SKU", "Hydrating skin tint | INR 399", ORANGE),
    ]
    y = 488
    for label, value, color in ui_fields:
        rounded(d, (1332, y, 1660, y + 48), CREAM, 8, color, 1)
        text(d, (1344, y + 8), label, 8, color, True)
        text(d, (1344, y + 25), value, 10, INK, True)
        y += 58
    rounded(d, (1680, 488, 1854, 164 + 488), LILAC, 10, PINK, 2)
    text(d, (1767, 508), "MATCH", 9, PINK, True, "mm")
    text(d, (1767, 532), "92", 35, PLUM_DARK, True, "mm")
    text(d, (1767, 568), "/ 100", 9, MUTED, True, "mm")
    # Why-match mini-bars
    text(d, (1332, 670), "WHY THIS MATCH?", 9, PLUM_DARK, True)
    reasons = [("audience fit", .94, CYAN), ("proof depth", .91, PINK), ("SKU suitability", .89, ORANGE), ("commerce fit", .84, PLUM)]
    y = 694
    for label, level, color in reasons:
        text(d, (1332, y), label, 9, INK, True)
        tiny_bar(d, 1470, y + 2, 145, level, color, h=8)
        text(d, (1630, y), f"{int(level*100)}%", 9, color, True)
        y += 27
    rounded(d, (1680, 650, 1854, 724), PINK, 10)
    text(d, (1767, 668), "NEXT ACTION", 8, WHITE, True, "mm")
    text(d, (1767, 697), "TARGETED SAMPLE", 10, WHITE, True, "mm")
    rounded(d, (1332, 818, 1854, 830), SOFT, 6)
    text(d, (1593, 824), "Brief: show texture • state who should avoid • compare finish • add Meesho CTA", 8, PLUM_DARK, True, "mm")
    section(d, 44, 862, 1240, "30-day launch spine | a killable wedge", ORANGE)
    weeks = [("W1", "10–20 SKUs\nfit criteria", ORANGE), ("W2", "creator match\nsample + log", PINK), ("W3", "proof + surface\nIDs + CTA", CYAN), ("W4", "orders + returns\nscale / kill", OLIVE)]
    x = 44
    for week, body, color in weeks:
        rounded(d, (x, 918, x + 286, 1000), WHITE, 10, color, 2)
        pill(d, x + 12, 934, 56, week, color, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, 9)
        text(d, (x + 84, 934), body, 11, INK, True)
        if x < 900:
            text(d, (x + 292, 956), ">", 18, PINK, True, "mm")
        x += 310
    rounded(d, (1310, 862, 1878, 1000), WHITE, 12, PLUM, 2)
    text(d, (1332, 880), "PILOT KPIs", 11, PLUM, True)
    text(d, (1332, 912), "Creator: activation / payout", 10, INK, True)
    text(d, (1332, 938), "Shopper: CTR / order / repeat", 10, INK, True)
    text(d, (1332, 964), "Seller: NMV / returns / quality", 10, INK, True)
    footer(d, "Pilot hypothesis: structured proof plus attributable handoff. Cohort sizes and outcomes are proposed, not observed.")
    return b


def board_evidence():
    b, d = board_appendix("Research is broad; claim strength stays bounded.", "APPENDIX | METHOD + SOURCE QUALITY", "A compact research dossier showing completed streams, limitations and the rule for promoting claims into the core story.")
    methodology_band(d, 44, 158, 1834)
    section(d, 44, 246, 980, "Research base | what is actually in hand")
    section(d, 1050, 246, 828, "Claim guardrails", ORANGE)
    base = [
        ("A", "Meesho surface", "1 category page; 1 PDP blocked", CYAN),
        ("B", "Creator content", "28 accessible / 2 blocked", PINK),
        ("C", "Competitor flows", "1 capability + 3 artifacts + 2 pending", ORANGE),
        ("P", "Primary research", "0 respondents in tracker", PLUM),
    ]
    y = 302
    for code, head, body, color in base:
        rounded(d, (44, y, 1000, y + 82), WHITE, 12, color, 2)
        icon_circle(d, 62, y + 22, code, color, 38, PLUM_DARK if color in [ORANGE, CYAN] else WHITE)
        text(d, (122, y + 18), head, 14, PLUM_DARK, True)
        text(d, (122, y + 48), body, 12, INK, True)
        y += 96
    guards = [
        ("DIRECT", "team audit observed in workspace", PLUM),
        ("PUBLIC", "official or public-source artifact", CYAN),
        ("INFERRED", "diagnosis, not validation", ORANGE),
        ("PENDING", "primary / authenticated evidence needed", PINK),
    ]
    y = 302
    for head, body, color in guards:
        rounded(d, (1050, y, 1878, y + 82), WHITE, 12, color, 2)
        pill(d, 1070, y + 24, 100, head, color, PLUM_DARK if color in [ORANGE, CYAN] else WHITE, 9)
        text(d, (1192, y + 31), body, 12, INK, True)
        y += 96
    section(d, 44, 718, 1834, "Claim promotion ladder | artifact -> replay -> triangulation -> decision", ORANGE)
    steps = [
        ("01", "ARTIFACT", "record / URL / workbook row exists", PLUM),
        ("02", "REPLAY", "independent observer can reproduce", CYAN),
        ("03", "TRIANGULATE", "second source or cohort agrees", ORANGE),
        ("04", "DECISION", "claim earns a place in the core story", PINK),
    ]
    x = 44
    for num, head, body, color in steps:
        rounded(d, (x, 774, x + 430, 874), WHITE, 12, color, 2)
        icon_circle(d, x + 16, 792, num, color, 34, PLUM_DARK if color in [ORANGE, CYAN] else WHITE)
        text(d, (x + 64, 792), head, 13, PLUM_DARK, True)
        text(d, (x + 64, 824), body, 11, INK, True)
        x += 454
    rounded(d, (44, 902, 1200, 996), PLUM_DARK, 12)
    text(d, (64, 924), "RESEARCH POSITION", 11, ORANGE, True)
    text(d, (64, 952), "Strong creator-proof evidence; weak Meesho-specific handoff evidence; no H0–H5 score.", 16, WHITE, True)
    rounded(d, (1240, 902, 1878, 996), SOFT, 12)
    text(d, (1260, 924), "NEXT EVIDENCE", 11, PINK, True)
    text(d, (1260, 952), "Creator + shopper + seller conversations and instrumented pilot.", 13, INK, True)
    footer(d, "Sources: DICE_GATE1_AUDIT_WORKBOOK.md; DICE_EVIDENCE_DATABASE.md; DICE_PRIMARY_RESEARCH_TRACKER.md. No fabricated respondents or uplift.")
    return b


def board_creator():
    b, d = board_appendix("Stream B is a lived evidence wall, not a content-count slide.", "APPENDIX | STREAM B | CCA-001–030", "Twenty-eight accessible public creator-content audits show repeated, concrete decision-support behaviors across makeup, skincare, mature skin and creator economics.")
    section(d, 44, 158, 1834, "Creator proof capability | descriptive audit counts")
    stats = [("26/28", "product demo", PLUM), ("24/28", "suitability", PINK), ("22/28", "shade / colour", ORANGE), ("23/28", "outcome proof", CYAN), ("25/28", "audience rec.", OLIVE), ("28/28", "personal review", PLUM_DARK)]
    x = 44
    for value, label, color in stats:
        research_tile(d, x, 214, 292, value, label, "CCA audit", color)
        x += 306
    section(d, 44, 326, 1040, "Observed evidence artifacts", PINK)
    section(d, 1120, 326, 758, "Handoff breaks | what the audit cannot prove", ORANGE)
    artifacts = [
        ("CCA-023", "Dry-skin mechanics", "Creams over powders; hydrating concealer; avoid matte cake.", CYAN),
        ("CCA-024", "Undertone discipline", "15 foundation shades swatched with pink / yellow / olive logic.", PLUM),
        ("CCA-016", "Texture truth", "Stick foundation dry; concealer palette thick / cakey / creasing.", ORANGE),
        ("CCA-019", "Multi-use trade-off", "Brow gel succeeds; mascara fails. Cheek tint succeeds; lip transfer.", PINK),
        ("CCA-028", "Virality mechanics", "Fake scarcity, paid scripts and real vs claimed sales signals.", OLIVE),
        ("CCA-029/030", "PR economics", "Free product pressure, wasteful shade ranges and gifted campaign asks.", PLUM_DARK),
    ]
    y = 382
    for eid, head, body, color in artifacts:
        evidence_chip(d, 44, y, 1040, eid, head, body, color)
        y += 100
    gaps = [
        ("NOT OBSERVED", "Meesho-specific CTA routing", PINK),
        ("NOT OBSERVED", "click -> order -> return", PINK),
        ("NOT OBSERVED", "creator earnings / payout", ORANGE),
        ("NOT OBSERVED", "30-day skin outcome", CYAN),
        ("ACCESS BLOCKED", "CCA-021 / CCA-022 captions", OLIVE),
    ]
    y = 382
    for head, body, color in gaps:
        rounded(d, (1120, y, 1878, y + 68), WHITE, 10, color, 2)
        pill(d, 1138, y + 17, 116, head, color, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, 8)
        text(d, (1272, y + 24), body, 12, INK, True)
        y += 82
    rounded(d, (1120, 810, 1878, 930), PLUM_DARK, 12)
    text(d, (1144, 834), "THE SHIFT", 11, ORANGE, True)
    text(d, (1144, 862), "The case should not solve content creation. It should solve proof transfer.", 16, WHITE, True)
    source_ref(d, 44, 1008, "Source: Team manual-quality audit | sample = 28 accessible public leads from 30 | descriptive only")
    footer(d, "Evidence IDs shown on-slide are from the audit workbook; no transaction impact is claimed.")
    return b


def board_competitor():
    b, d = board_appendix(
        "Competitors expose the bridge from content to learning.",
        "APPENDIX | STREAM C | CAPABILITY BENCHMARK",
        "The corrected audit distinguishes one public-source capability record, three public artifacts and two pending flows. Private dashboards remain unverified.",
    )
    section(d, 44, 158, 1834, "Benchmark grid | what is public, what is authenticated, what remains unverified")
    headers = ["PLATFORM", "DISCOVERY", "SKU / INFO", "PROOF", "SHOPPING", "ATTRIB.", "EARNINGS", "WORKSPACE RECORD"]
    widths = [250, 205, 205, 205, 205, 205, 205, 354]
    x = 44
    for h, w in zip(headers, widths):
        rounded(d, (x, 216, x + w, 258), PLUM_DARK, 0)
        text(d, (x + w // 2, 237), h, 9.5, WHITE, True, "mm")
        x += w
    rows = [
        ("YouTube Shopping", ["PUBLIC", "PUBLIC", "PUBLIC", "PUBLIC", "PRIVATE", "PRIVATE"], "COMP-FLOW-001\n1 capability record", PLUM),
        ("Amazon India", ["PUBLIC", "PUBLIC", "PUBLIC", "PUBLIC", "PRIVATE", "PRIVATE"], "COMP-003\npublic program artifact", ORANGE),
        ("Nykaa Affiliate", ["PUBLIC", "PUBLIC", "PUBLIC", "PUBLIC", "PRIVATE", "PRIVATE"], "COMP-002\npublic program artifact", CYAN),
        ("Flipkart Affiliate", ["PUBLIC", "PUBLIC", "PUBLIC", "PUBLIC", "PRIVATE", "PRIVATE"], "COMP-003\npublic partner artifact", PINK),
        ("Myntra Glam Clan", ["PUBLIC", "PUBLIC", "PUBLIC", "PUBLIC", "PRIVATE", "PRIVATE"], "COMP-001\npublic program artifact", OLIVE),
        ("Meesho", ["UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN"], "Target to test\nnot evidenced", PLUM_DARK),
    ]
    y = 270
    for name, statuses, status, color in rows:
        x = 44
        platform_fill = LILAC if name != "Meesho" else SOFT
        rounded(d, (x, y, x + widths[0], y + 74), platform_fill, 0, color, 2)
        d.rectangle((x, y, x + 10, y + 74), fill=color)
        text(d, (x + 22, y + 37), name, 12.5, PLUM_DARK, True, "lm")
        x += widths[0]
        for st, w in zip(statuses, widths[1:-1]):
            fill = CYAN if st == "PUBLIC" else SOFT if st == "PRIVATE" else WHITE
            rounded(d, (x, y, x + w, y + 74), fill, 0, GRID, 1)
            label = "PUBLIC" if st == "PUBLIC" else "AUTH" if st == "PRIVATE" else "OPEN"
            pill(
                d,
                x + 38,
                y + 22,
                w - 76,
                label,
                CYAN if st == "PUBLIC" else ORANGE if st == "PRIVATE" else PINK,
                PLUM_DARK if st in ["PUBLIC", "PRIVATE"] else WHITE,
                8,
            )
            x += w
        record_fill = LILAC if color in [PLUM, PLUM_DARK] else SOFT if color in [ORANGE, OLIVE] else CYAN
        rounded(d, (x, y, x + widths[-1], y + 74), record_fill, 0, color, 1)
        record_color = PLUM_DARK if color in [CYAN, ORANGE, OLIVE] else color
        text(d, (x + 14, y + 12), status, 9.8, record_color, True)
        y += 82

    section(d, 44, 792, 590, "How to read the grid", ORANGE)
    legend = [
        ("PUBLIC", "official page or program artifact", CYAN),
        ("AUTH", "private dashboard / login required", ORANGE),
        ("OPEN", "not evidenced in workspace", PINK),
    ]
    x = 56
    for label, body, color in legend:
        rounded(d, (x, 842, x + 176, 930), WHITE, 12, color, 2)
        pill(d, x + 12, 854, 72, label, color, PLUM_DARK if color in [CYAN, ORANGE] else WHITE, 8)
        paragraph(d, (x + 12, 889), body, 152, 10.5, INK, True, 2)
        x += 190

    section(d, 662, 792, 590, "Evidence count | Stream C", PLUM_DARK)
    counts = [("1", "public-source capability", PLUM), ("3", "public artifacts", ORANGE), ("2", "pending records", PINK)]
    x = 674
    for value, label, color in counts:
        rounded(d, (x, 842, x + 174, 930), WHITE, 12, color, 2)
        text(d, (x + 14, 858), value, 27, color, True)
        paragraph(d, (x + 14, 898), label, 146, 10.5, PLUM_DARK, True, 2)
        x += 190

    section(d, 1280, 792, 598, "Benchmark implication", PINK)
    rounded(d, (1292, 842, 1878, 930), PLUM_DARK, 12)
    paragraph(
        d,
        (1310, 859),
        "The benchmark validates the shape of the bridge, not Meesho conversion. Build one measurable proof-to-commerce handoff, then learn.",
        550,
        13,
        WHITE,
        True,
        3,
    )
    footer(d, "Clickable platform sources ↗ YouTube Shopping | Amazon | Nykaa | Flipkart | Myntra. Stream C: 1 capability + 3 artifacts + 2 pending.")
    return b


def board_close():
    b = new_board(PLUM_DARK)
    d = ImageDraw.Draw(b)
    draw = ImageDraw.Draw(b, "RGBA")
    draw.rectangle((0, 0, W, H), fill=(71, 0, 57, 255))
    draw.ellipse((1120, -180, 2050, 740), fill=(130, 20, 100, 130))
    draw.ellipse((1310, 260, 1930, 900), outline=(255, 157, 0, 150), width=6)
    draw.ellipse((1410, 360, 1830, 780), outline=(240, 90, 121, 150), width=5)
    text(d, (88, 92), "MEESHO DICE CHALLENGE | S3", 15, ORANGE, True)
    text(d, (88, 198), "The case in one line:", 22, CREAM, True)
    text(d, (88, 252), "Proof already exists.", 51, WHITE, True)
    text(d, (88, 314), "Now measure the handoff.", 51, WHITE, True)
    rounded(d, (88, 450, 1010, 710), SOFT, 22)
    text(d, (126, 486), "THE PROPOSED WEDGE", 14, PINK, True)
    text(d, (126, 536), "Beauty Proof Bridge", 36, PLUM_DARK, True)
    text(d, (126, 598), "Creator × SKU × Audience", 24, PLUM_DARK, True)
    text(d, (126, 640), "MATCH → SAMPLE → CREATE → SURFACE → MEASURE → LEARN", 14, PLUM_DARK, True)
    text(d, (88, 832), "Thank you", 33, WHITE, True)
    text(d, (88, 886), "Appendix follows: evidence, benchmark, hypothesis ledger, pilot model and source links.", 17, CREAM, True)
    text(d, (88, 1004), "Team Slayed it | Samiksha Mitra | IIT Guwahati | 09 September 2026", 12, CREAM)
    rounded(d, (1210, 152, 1790, 818), WHITE, 24)
    text(d, (1500, 205), "THE JUDGE SHOULD REMEMBER", 14, PINK, True, "mm")
    statements = [
        ("01", "Creators can already make useful beauty proof.", PINK),
        ("02", "The measurable leak is the handoff into commerce.", CYAN),
        ("03", "The pilot earns the right to build the engine.", ORANGE),
    ]
    y = 300
    for num, value, color in statements:
        icon_circle(d, 1260, y, num, color, 42, PLUM_DARK if color in [CYAN, ORANGE] else WHITE)
        paragraph(d, (1324, y + 2), value, 390, 16, INK, True, 4)
        y += 142
    rounded(d, (1252, 682, 1748, 760), PLUM_DARK, 14)
    text(d, (1500, 721), "EVIDENCE → INSIGHT → PILOT", 15, WHITE, True, "mm")
    return b


def board_hypothesis():
    b, d = board_appendix("H0–H5 stay open; the evidence changes the next question.", "APPENDIX | HYPOTHESIS BOARD", "The creator audit challenges H3 but does not validate the commerce bridge. Each hypothesis therefore carries a contradiction and a next test.")
    section(d, 44, 158, 1834, "Hypothesis ledger | signal -> limitation -> next evidence")
    headers = ["ID", "CANDIDATE PROBLEM", "OBSERVED SIGNAL", "LIMITATION", "NEXT TEST", "STATUS"]
    widths = [80, 270, 480, 430, 500, 154]
    x = 44
    for h, w in zip(headers, widths):
        rounded(d, (x, 216, x + w, 258), PLUM_DARK, 0)
        text(d, (x + w // 2, 237), h, 9, WHITE, True, "mm")
        x += w
    rows = [
        ("H0", "quality / trust", "defects, viral mismatch, PR pressure", "no returns / authenticity sizing", "shopper + seller interviews; return record", "OPEN", PINK),
        ("H1", "creator-SKU fit", "specialist creators make fit legible", "may be format-specific", "creator selection + matching interview", "OPEN", ORANGE),
        ("H2", "sampling economics", "PR waste and gifting bias visible", "no seller ROI or cost data", "targeted sample test", "OPEN", CYAN),
        ("H3", "proof difficulty", "26/28 demos; 24/28 suitability", "does not prove transaction transfer", "shopper proof-field task", "CHALL", PLUM),
        ("H4", "decision support", "shade / texture / outcome recur", "PDP evidence blocked", "treatment vs control handoff", "OPEN", OLIVE),
        ("H5", "creator economics", "affiliate / PR pressure observed", "no authenticated payout logs", "creator interview + attributed pilot", "OPEN", PINK),
    ]
    y = 270
    for code, head, signal, limit, test, status, color in rows:
        values = [code, head, signal, limit, test, status]
        x = 44
        for j, (value, w) in enumerate(zip(values, widths)):
            fill = CYAN if code == "H3" else WHITE
            rounded(d, (x, y, x + w, y + 76), fill, 0, color if j in [0, 5] else GRID, 2 if j in [0, 5] else 1)
            text(d, (x + (w // 2 if j in [0, 5] else 12), y + 38), value, 13 if j == 0 else 11, PLUM_DARK if j in [0, 5] else INK, j in [0, 5], "mm" if j in [0, 5] else "lm")
            x += w
        y += 83
    rounded(d, (44, 806, 1180, 944), PLUM_DARK, 14)
    text(d, (70, 832), "CASE-CHANGING CONTRADICTION", 12, ORANGE, True)
    paragraph(d, (70, 865), "Creators already make fit, shade, texture and outcome legible. The missing evidence is not whether proof exists; it is whether proof transfer changes behaviour.", 1060, 17, WHITE, True, 4)
    section(d, 1220, 806, 658, "Next respondent evidence", PINK)
    respondent = [("CREATOR", "selection + effort + payout", PINK), ("SHOPPER", "confidence + click + fit", CYAN), ("SELLER", "quality + return + ROI", ORANGE)]
    y = 866
    for head, body, color in respondent:
        rounded(d, (1220, y, 1878, y + 54), WHITE, 10, color, 2)
        pill(d, 1234, y + 10, 102, head, color, PLUM_DARK if color == ORANGE else WHITE, 8)
        text(d, (1360, y + 17), body, 12, INK, True)
        y += 62
    footer(d, "No H0–H5 hypothesis is statistically scored or declared validated.")
    return b


def board_engine():
    b = new_board(CREAM)
    d = ImageDraw.Draw(b)
    logo_header(d, "The moat is the data loop created by every better match.", "APPENDIX | FUTURE ENGINE")
    text(d, (44, 116), "A future-state architecture: build the smallest data-generating wedge first, then use interaction evidence to improve Creator x SKU x Audience allocation.", 16, MUTED)
    section(d, 44, 158, 1834, "Flywheel | every transaction improves the next match")
    # flywheel rings
    cx, cy = 960, 550
    for radius, color, width in [(300, PLUM_DARK, 5), (240, PINK, 4), (180, CYAN, 4)]:
        d.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), outline=color, width=width)
    text(d, (cx, cy - 45), "BETTER MATCH", 22, PLUM_DARK, True, "mm")
    text(d, (cx, cy - 8), "-> BETTER PROOF", 18, PINK, True, "mm")
    text(d, (cx, cy + 28), "-> BETTER COMMERCE", 18, CYAN, True, "mm")
    nodes = [
        ("CREATOR\nattributes", 960, 230, PINK),
        ("SKU\nattributes", 1275, 360, ORANGE),
        ("CONTENT\nengagement", 1275, 720, CYAN),
        ("ORDERS /\nRETURNS", 960, 826, OLIVE),
        ("AUDIENCE\nattributes", 645, 720, PLUM),
        ("CLICKS /\nPDP", 645, 360, PINK),
    ]
    for label, x, y, color in nodes:
        rounded(d, (x - 108, y - 38, x + 108, y + 38), WHITE, 14, color, 3)
        text(d, (x, y), label, 12, PLUM_DARK, True, "mm")
    # arrows around ring
    for a, b2 in [((960, 270), (1190, 350)), ((1270, 400), (1270, 675)), ((1190, 770), (1000, 806)), ((920, 806), (700, 770)), ((650, 675), (650, 400)), ((730, 350), (920, 270))]:
        d.line((*a, *b2), fill=PINK, width=4)
    rounded(d, (44, 250, 390, 842), WHITE, 14, ORANGE, 2)
    text(d, (66, 278), "INPUT SIGNALS", 14, ORANGE, True)
    inputs = ["audience profile", "skin / hair niche", "content style", "shade / category", "price / margin", "seller quality", "need / budget", "fit / caveat"]
    y = 326
    for item in inputs:
        pill(d, 66, y, 274, item.upper(), SOFT if y % 2 else CYAN, PLUM_DARK, 9)
        y += 52
    rounded(d, (1530, 250, 1878, 842), WHITE, 14, PINK, 2)
    text(d, (1552, 278), "OUTPUT SIGNALS", 14, PINK, True)
    outputs = ["creator activation", "proof completeness", "click-through", "PDP-to-order", "return / rating", "repeat purchase", "creator payout", "next allocation"]
    y = 326
    for item in outputs:
        pill(d, 1552, y, 292, item.upper(), WHITE if y % 2 else SOFT, PINK if y % 2 else PLUM_DARK, 9)
        y += 52
    rounded(d, (44, 898, 1878, 986), PLUM_DARK, 14)
    text(d, (961, 929), "The engine is not the first build. The first build is the instrumented handoff that earns the right to build the engine.", 17, WHITE, True, "mm")
    footer(d, "Future-state architecture; no claim that Meesho currently has these matching signals.")
    return b


def board_economics():
    b = new_board(CREAM)
    d = ImageDraw.Draw(b)
    logo_header(d, "Measurement turns a creator story into a business case.", "APPENDIX | PILOT ECONOMICS")
    text(d, (44, 116), "The pilot is valuable because it creates the event spine needed to size real incremental NMV, creator economics and quality risk.", 16, MUTED)
    rounded(d, (44, 158, 1878, 238), PLUM_DARK, 16)
    text(d, (961, 198), "BPC NMV = active creators x relevant proof x click-through x PDP-to-order x AOV x repeat", 23, WHITE, True, "mm")
    section(d, 44, 274, 1834, "Event spine | the numbers become knowable only if the handoff is instrumented", ORANGE)
    events = [("01", "VIEW", "proof shown", PLUM), ("02", "CLICK", "tag / CTA", PINK), ("03", "PDP", "fit resolved", CYAN), ("04", "ORDER", "transaction", ORANGE), ("05", "RETURN", "quality", OLIVE), ("06", "REPEAT", "retention", PLUM)]
    x = 44
    for i, (num, head, body, color) in enumerate(events):
        rounded(d, (x, 338, x + 280, 450), WHITE, 14, color, 2)
        icon_circle(d, x + 16, 354, num, color, 32, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE)
        text(d, (x + 62, 360), head, 14, PLUM_DARK, True)
        text(d, (x + 62, 395), body, 12, MUTED, True)
        if i < 5:
            text(d, (x + 286, 392), ">", 22, PINK, True, "mm")
        x += 306
    section(d, 44, 486, 800, "Owner metric stack", CYAN)
    owner_rows = [("CREATOR", "activation | time | payout", PINK), ("SHOPPER", "confidence | CTR | order | repeat", CYAN), ("SELLER", "incremental NMV | returns | quality", ORANGE), ("MEESHO", "attribution | economics | learning", OLIVE)]
    y = 544
    for head, body, color in owner_rows:
        rounded(d, (44, y, 844, y + 58), WHITE, 10, color, 2)
        pill(d, 60, y + 12, 100, head, color, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, 8)
        text(d, (182, y + 19), body, 13, INK, True)
        y += 68
    section(d, 884, 486, 994, "What becomes knowable", PINK)
    questions = ["Which proof fields correlate with clicks?", "Which creators produce efficient proof?", "Do targeted samples beat broad gifting?", "Does quality erase conversion?", "Does the bridge deserve scale or a kill?"]
    y = 544
    for q in questions:
        rounded(d, (884, y, 1878, y + 50), WHITE, 10, PINK, 1)
        pill(d, 900, y + 10, 28, "?", PINK, WHITE, 10)
        text(d, (946, y + 15), q, 12, INK, True)
        y += 60
    rounded(d, (44, 846, 1878, 954), SOFT, 14)
    text(d, (66, 875), "NO INVENTED UPLIFT", 12, PINK, True)
    text(d, (270, 875), "Pilot metrics are targets / assumptions until the treatment and control produce observed deltas.", 15, INK, True)
    economics_checks = [
        ("TARGET", "creator / SKU / audience / treatment IDs", CYAN),
        ("CONTROL", "current handoff versus structured proof", PINK),
        ("GAP", "no observed Meesho conversion or repeat yet", ORANGE),
    ]
    x = 270
    for head, body, color in economics_checks:
        rounded(d, (x, 900, x + 500, 938), WHITE, 8, color, 1)
        pill(d, x + 10, 906, 72, head, color, PLUM_DARK if color == ORANGE else WHITE, 8)
        text(d, (x + 94, 912), body, 10, INK, True)
        x += 520
    footer(d, "Illustrative measurement model only. No conversion, NMV, repeat or retention result is claimed.")
    return b


def board_risks():
    b = new_board(CREAM)
    d = ImageDraw.Draw(b)
    logo_header(d, "A winning case makes disproof visible before scale.", "APPENDIX | RISKS + ROADMAP")
    text(d, (44, 116), "The bridge must survive four stakeholders and three failure modes: proof, economics and quality.", 16, MUTED)
    section(d, 44, 158, 1080, "Kill criteria | what would falsify the wedge", PINK)
    section(d, 1160, 158, 718, "Scale path | if the evidence clears", ORANGE)
    risks = [
        ("PROOF", "structured proof does not change confidence or clicks", "kill / redesign", PINK),
        ("CREATOR", "effort or payout is not worth the trial", "simplify / reprice", ORANGE),
        ("SELLER", "sample and return economics erase gains", "narrow / co-fund", CYAN),
        ("SHOPPER", "fit remains unclear at PDP", "add proof surface", OLIVE),
        ("MEESHO", "attribution cannot be replayed", "instrument before scale", PLUM),
    ]
    y = 214
    for head, body, action, color in risks:
        rounded(d, (44, y, 1124, y + 78), WHITE, 12, color, 2)
        pill(d, 62, y + 22, 100, head, color, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, 9)
        text(d, (184, y + 16), body, 13, INK, True)
        text(d, (184, y + 46), "IF TRUE -> " + action, 11, color, True)
        y += 88
    roadmap = [("30 DAYS", "bridge + event IDs", CYAN), ("60 DAYS", "proof fields + seller reporting", PINK), ("90 DAYS", "matching from interaction data", ORANGE)]
    y = 214
    for head, body, color in roadmap:
        rounded(d, (1160, y, 1878, y + 116), WHITE, 14, color, 2)
        pill(d, 1184, y + 36, 132, head, color, PLUM_DARK if color == ORANGE else WHITE, 10)
        text(d, (1346, y + 36), body, 14, INK, True)
        y += 132
    rounded(d, (1160, 626, 1878, 758), PLUM_DARK, 14)
    text(d, (1519, 654), "NORTH STAR", 12, ORANGE, True, "mm")
    text(d, (1519, 698), "more BPC NMV from better proof transfer", 18, WHITE, True, "mm")
    section(d, 44, 700, 1080, "Decision gates | evidence required before each step", ORANGE)
    gates = [("CREATOR", "effort + payout", PINK), ("SHOPPER", "confidence + click", CYAN), ("SELLER", "quality + ROI", ORANGE), ("MEESHO", "replayable handoff", OLIVE)]
    x = 44
    for head, body, color in gates:
        rounded(d, (x, 758, x + 258, 860), WHITE, 12, color, 2)
        pill(d, x + 14, 774, 100, head, color, PLUM_DARK if color in [ORANGE, CYAN, OLIVE] else WHITE, 8)
        text(d, (x + 14, 816), body, 11, INK, True)
        x += 274
    rounded(d, (44, 892, 1878, 976), SOFT, 14)
    text(d, (961, 934), "Next: acquire genuine creator, shopper and seller evidence before calling the bridge a winner.", 17, PLUM_DARK, True, "mm")
    footer(d, "Decision gates are proposed. No respondent or pilot result is fabricated.")
    return b


def board_sources():
    b, d = board_appendix("Every claim has a source, limit and next decision.", "APPENDIX | SOURCE LEDGER", "The final appendix is a judge-readable audit trail: what was observed, what is public, what is inferred and what remains pending.")
    section(d, 44, 158, 1834, "Source-to-claim ledger")
    headers = ["FAMILY", "ARTIFACTS IN WORKSPACE", "CAN SUPPORT", "CANNOT SUPPORT", "NEXT DECISION"]
    widths = [190, 360, 420, 430, 434]
    x = 44
    for h, w in zip(headers, widths):
        rounded(d, (x, 216, x + w, 260), PLUM_DARK, 0)
        text(d, (x + w // 2, 238), h, 10, WHITE, True, "mm")
        x += w
    rows = [
        ("A | MEESHO", "M-CAT-001; M-PDP-001 403", "category cues; access limitation", "PDP proof; conversion; repeat", "secure replayable PDP evidence", CYAN),
        ("B | CREATOR", "CCA-001–030; 28 accessible", "proof capability; suitability; shade; outcome", "Meesho routing; transaction impact; earnings", "test proof transfer", PINK),
        ("C | COMPETITOR", "COMP-FLOW-001 + artifacts", "capability existence; benchmark structure", "five verified journeys; private economics", "replay one complete flow", ORANGE),
        ("P | PRIMARY", "tracker; interview/survey instruments", "research design and lead pipeline", "respondent findings; H0–H5 score", "acquire genuine responses", PLUM),
    ]
    y = 278
    for fam, art, supports, cannot, next_dec, color in rows:
        vals = [fam, art, supports, cannot, next_dec]
        x = 44
        for j, (value, w) in enumerate(zip(vals, widths)):
            fill = CYAN if j == 2 and fam.startswith("B") else WHITE
            rounded(d, (x, y, x + w, y + 82), fill, 0, color if j == 0 else GRID, 2 if j == 0 else 1)
            text(d, (x + 12, y + 18), value, 11 if j else 12, PLUM_DARK if j in [0, 4] else INK, j in [0, 4])
            x += w
        y += 92
    section(d, 44, 676, 1160, "Evidence strength legend", ORANGE)
    legend = [("DIRECT", "observed in workspace", PLUM), ("PUBLIC", "official/public artifact", CYAN), ("INFERRED", "labelled diagnosis", ORANGE), ("PENDING", "primary/private evidence", PINK)]
    x = 44
    for head, body, color in legend:
        rounded(d, (x, 730, x + 274, 812), WHITE, 10, color, 2)
        pill(d, x + 12, 742, 82, head, color, PLUM_DARK if color in [ORANGE, CYAN] else WHITE, 8)
        text(d, (x + 106, 751), body, 10, INK, True)
        x += 292
    section(d, 44, 836, 1160, "Promotion rule", PLUM_DARK)
    rounded(d, (44, 890, 1204, 992), SOFT, 12)
    paragraph(d, (68, 918), "Promote only when respondents + an instrumented handoff show measurable behaviour change.", 1080, 16, PLUM_DARK, True, 4)
    section(d, 1240, 676, 638, "Clickable source index", PINK)
    queue = [
        ("LIVE PROTOTYPE", "interactive Beauty Proof Bridge demo", PINK),
        ("SLAYED IT REPO", "prototype code + product artifacts", PLUM),
        ("VIDEO DEMO", "recorded product walkthrough", ORANGE),
        ("MASTER DOC", "full strategy + research narrative", CYAN),
        ("EVIDENCE LEDGER", "audits, claims and limitations", PLUM),
        ("EXTERNAL SOURCES", "benchmark links and public artifacts", ORANGE),
    ]
    for i, (head, body, color) in enumerate(queue):
        col = i % 2
        row = i // 2
        x = 1240 + col * 319
        y = 730 + row * 68
        rounded(d, (x, y, x + 300, y + 58), WHITE, 10, color, 2)
        icon_circle(d, x + 12, y + 13, "↗", color, 32, PLUM_DARK if color == ORANGE else WHITE)
        text(d, (x + 62, y + 12), head, 11, PLUM_DARK, True)
        text(d, (x + 62, y + 34), body, 8.7, INK, True)
    footer(d, "Clickable source index ↗ | GitHub evidence files | YouTube Shopping | Amazon | Nykaa | Flipkart | Myntra. Evidence IDs remain in the ledger.")
    return b


def render():
    boards = [
        board_cover(),
        board_value_chain(),
        board_prioritization(),
        board_quick_win(),
        board_close(),
        board_evidence(),
        board_creator(),
        board_competitor(),
        board_hypothesis(),
        board_engine(),
        board_economics(),
        board_risks(),
        board_sources(),
    ]
    paths = []
    for i, board in enumerate(boards, 1):
        path = OUT / f"slide_{i:02d}.png"
        board.save(path, optimize=True)
        paths.append(path)
    return paths


if __name__ == "__main__":
    for path in render():
        print(path)
