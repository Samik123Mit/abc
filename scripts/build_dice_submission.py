from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_AUTO_SHAPE_TYPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


ROOT = Path("/workspaces/abc")
TEMPLATE = ROOT / "DICE Challenge S3  Template for Case studies submission  (Presentation).pptx"
OUTPUT = ROOT / "DICE Challenge S3 - Slayed it Winning Submission.pptx"

PLUM = RGBColor(84, 12, 74)
PLUM_DARK = RGBColor(55, 7, 48)
ORANGE = RGBColor(245, 158, 11)
PINK = RGBColor(242, 74, 120)
ROSE = RGBColor(224, 85, 121)
CREAM = RGBColor(255, 247, 224)
INK = RGBColor(34, 22, 40)
MUTED = RGBColor(103, 87, 97)
OLIVE = RGBColor(164, 171, 67)
CYAN = RGBColor(54, 172, 196)
SOFT = RGBColor(255, 239, 214)
GRID = RGBColor(222, 206, 192)
WHITE = RGBColor(255, 255, 255)
PALE_PLUM = RGBColor(246, 232, 243)
PALE_CYAN = RGBColor(229, 247, 249)

FONT_HEAD = "Aptos Display"
FONT_BODY = "Aptos"
W = Inches(20)
H = Inches(11.25)


def remove_all_slides(prs: Presentation) -> None:
    slide_ids = list(prs.slides._sldIdLst)
    for slide_id in slide_ids:
        prs.slides._sldIdLst.remove(slide_id)


def set_slide_bg(slide, color=CREAM) -> None:
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def fill_shape(shape, color, transparency=0.0, line=None, line_width=0.0) -> None:
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.fill.transparency = transparency
    if line is None:
        shape.line.fill.background()
    else:
        shape.line.color.rgb = line
        shape.line.width = Pt(line_width)


def box(slide, x, y, w, h, color=WHITE, radius=True, transparency=0.0, line=None, line_width=0.0):
    shape_type = MSO_AUTO_SHAPE_TYPE.ROUNDED_RECTANGLE if radius else MSO_AUTO_SHAPE_TYPE.RECTANGLE
    shape = slide.shapes.add_shape(shape_type, x, y, w, h)
    fill_shape(shape, color, transparency, line, line_width)
    return shape


def text(
    slide,
    x,
    y,
    w,
    h,
    value,
    size=16,
    color=INK,
    bold=False,
    font=FONT_BODY,
    align=PP_ALIGN.LEFT,
    valign=MSO_ANCHOR.TOP,
    margin=0.06,
    italic=False,
):
    shape = slide.shapes.add_textbox(x, y, w, h)
    frame = shape.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = Inches(margin)
    frame.margin_right = Inches(margin)
    frame.margin_top = Inches(margin * 0.65)
    frame.margin_bottom = Inches(margin * 0.35)
    frame.vertical_anchor = valign
    paragraph = frame.paragraphs[0]
    paragraph.alignment = align
    run = paragraph.add_run()
    run.text = value
    run.font.name = font
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    return shape


def bullets(slide, x, y, w, h, items, size=13, color=INK, spacing=1.02):
    shape = slide.shapes.add_textbox(x, y, w, h)
    frame = shape.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = Inches(0.08)
    frame.margin_right = Inches(0.04)
    frame.margin_top = Inches(0.04)
    frame.margin_bottom = Inches(0.02)
    for i, item in enumerate(items):
        paragraph = frame.paragraphs[0] if i == 0 else frame.add_paragraph()
        paragraph.space_after = Pt(3)
        paragraph.line_spacing = spacing
        run = paragraph.add_run()
        run.text = "• " + item
        run.font.name = FONT_BODY
        run.font.size = Pt(size)
        run.font.color.rgb = color
    return shape


def pill(slide, x, y, w, label, color=PLUM, size=9):
    box(slide, x, y, w, Inches(0.34), color, radius=True)
    text(slide, x, y + Inches(0.01), w, Inches(0.28), label, size=size, color=WHITE, bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, margin=0.0)


def title_bar(slide, title, section):
    pill(slide, Inches(0.62), Inches(0.52), Inches(2.55), "SLAYED IT | IIT GUWAHATI", PLUM)
    pill(slide, Inches(15.75), Inches(0.52), Inches(3.45), section, ORANGE)
    text(slide, Inches(0.62), Inches(0.98), Inches(18.1), Inches(0.7), title, size=27, color=PLUM_DARK, bold=True, font=FONT_HEAD)


def footer(slide, value):
    text(slide, Inches(0.62), Inches(10.78), Inches(18.7), Inches(0.22), value, size=8.2, color=MUTED, margin=0.0)


def card(slide, x, y, w, h, heading, body, color=PLUM, body_size=11.5):
    item = box(slide, x, y, w, h, WHITE, radius=True, line=color, line_width=1.2)
    band = box(slide, x, y, w, Inches(0.27), color, radius=False)
    text(slide, x + Inches(0.09), y + Inches(0.04), w - Inches(0.18), Inches(0.2), heading, size=10.5, color=WHITE, bold=True, margin=0.0)
    text(slide, x + Inches(0.11), y + Inches(0.36), w - Inches(0.22), h - Inches(0.43), body, size=body_size, color=INK)
    return item


def metric(slide, x, y, w, label, value, color):
    box(slide, x, y, w, Inches(0.92), color, radius=True)
    text(slide, x + Inches(0.08), y + Inches(0.09), w - Inches(0.16), Inches(0.22), label, size=9.5, color=WHITE, bold=True, margin=0.0)
    text(slide, x + Inches(0.08), y + Inches(0.34), w - Inches(0.16), Inches(0.42), value, size=16, color=WHITE, bold=True, font=FONT_HEAD, margin=0.0)


def arrow(slide, x1, y1, x2, y2, color=PINK, width=1.4):
    connector = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, x1, y1, x2, y2)
    connector.line.color.rgb = color
    connector.line.width = Pt(width)
    connector.line.end_arrowhead = True
    return connector


def flow_node(slide, x, y, w, heading, sub, color, highlight=False):
    fill = PALE_PLUM if highlight else WHITE
    box(slide, x, y, w, Inches(0.95), fill, radius=True, line=color, line_width=1.4)
    box(slide, x, y, w, Inches(0.24), color, radius=False)
    text(slide, x + Inches(0.07), y + Inches(0.035), w - Inches(0.14), Inches(0.18), heading, size=10.5, color=WHITE, bold=True, margin=0.0)
    text(slide, x + Inches(0.08), y + Inches(0.31), w - Inches(0.16), Inches(0.52), sub, size=10.2, color=INK, margin=0.0)


def build_cover(slide):
    set_slide_bg(slide)
    pill(slide, Inches(1.00), Inches(1.05), Inches(2.70), "DICE CHALLENGE | SEASON 2", ORANGE)
    text(slide, Inches(1.00), Inches(2.05), Inches(11.2), Inches(1.0), "Growing Beauty & Personal Care through Influencers", size=34, color=PLUM_DARK, bold=True, font=FONT_HEAD)
    text(slide, Inches(1.02), Inches(3.28), Inches(9.5), Inches(0.7), "From creator proof to confident Meesho commerce", size=22, color=PLUM, bold=True, font=FONT_HEAD)
    box(slide, Inches(1.02), Inches(4.35), Inches(8.7), Inches(1.35), SOFT, radius=True)
    text(slide, Inches(1.32), Inches(4.68), Inches(8.1), Inches(0.28), "PROPOSED STRATEGIC CAPABILITY", size=11, color=PLUM, bold=True, margin=0.0)
    text(slide, Inches(1.32), Inches(5.02), Inches(8.1), Inches(0.42), "Creator x SKU x Audience Decision Engine", size=19, color=INK, bold=True, font=FONT_HEAD, margin=0.0)
    text(slide, Inches(1.02), Inches(7.55), Inches(8.5), Inches(0.3), "Team Slayed it", size=15, color=PLUM_DARK, bold=True, font=FONT_HEAD)
    text(slide, Inches(1.02), Inches(7.93), Inches(8.5), Inches(0.3), "Samiksha Mitra | IIT Guwahati", size=13, color=MUTED)
    text(slide, Inches(1.02), Inches(9.50), Inches(9.2), Inches(0.32), "Research cut: 09 September 2026", size=10.5, color=MUTED)
    text(slide, Inches(1.02), Inches(9.88), Inches(9.2), Inches(0.42), "Round 1 submission with evidence appendix", size=12, color=PLUM, bold=True)


def build_slide_1(slide):
    set_slide_bg(slide)
    title_bar(slide, "The leak is not beauty proof. It is the proof handoff.", "ROUND 1 | VALUE CHAIN")
    text(
        slide,
        Inches(0.68),
        Inches(1.76),
        Inches(18.0),
        Inches(0.5),
        "Creators already demonstrate fit, shade, texture and outcomes. The unanswered question is whether that context travels into a measurable Meesho purchase journey.",
        size=15,
        color=MUTED,
    )

    metric(slide, Inches(0.72), Inches(2.38), Inches(2.75), "CASE FACT", "BPC under-indexes in affiliate NMV", PLUM)
    metric(slide, Inches(3.68), Inches(2.38), Inches(2.75), "TEAM AUDIT", "15 manual-quality records", PINK)
    metric(slide, Inches(6.64), Inches(2.38), Inches(2.75), "MEESHO SURFACE", "10,000+ BPC listings", ORANGE)
    metric(slide, Inches(9.60), Inches(2.38), Inches(2.75), "COMPETITOR", "1 public flow documented", CYAN)

    text(slide, Inches(0.72), Inches(3.62), Inches(5.0), Inches(0.3), "Creator-led BPC value chain", size=16, color=PLUM_DARK, bold=True, font=FONT_HEAD)
    nodes = [
        ("1. SKU", "Brand defines product, claim and target cohort.", ORANGE, False),
        ("2. MATCH", "Creator decides: will this work for my audience?", PINK, False),
        ("3. TRIAL", "Product access enables credible use, not just unboxing.", PLUM, False),
        ("4. PROOF", "Demo, shade, texture, suitability and result.", ROSE, False),
        ("5. HANDOFF", "Proof must survive the click into commerce.", CYAN, True),
        ("6. DECISION", "Shopper resolves fit, trust, value and risk.", OLIVE, False),
        ("7. LEARN", "Order, return, repeat and creator earnings.", PLUM, False),
    ]
    x = Inches(0.72)
    y = Inches(4.02)
    node_w = Inches(2.34)
    gap = Inches(0.18)
    for i, (head, sub, color, highlight) in enumerate(nodes):
        current_x = x + i * (node_w + gap)
        flow_node(slide, current_x, y, node_w, head, sub, color, highlight)
        if i < len(nodes) - 1:
            arrow(slide, current_x + node_w, y + Inches(0.47), current_x + node_w + gap, y + Inches(0.47))

    box(slide, Inches(0.72), Inches(5.38), Inches(12.55), Inches(1.62), SOFT, radius=True)
    text(slide, Inches(0.98), Inches(5.60), Inches(2.4), Inches(0.24), "WHAT THE AUDIT SAYS", size=10.5, color=PLUM, bold=True, margin=0.0)
    bullets(
        slide,
        Inches(0.95),
        Inches(5.90),
        Inches(11.95),
        Inches(0.86),
        [
            "Manual creator audits show decision-grade proof is already possible: shade/undertone, skin fit, texture, comparisons and outcomes.",
            "The audit does not show Meesho conversion, attribution, repeat or creator earnings; those are still the critical handoff unknowns.",
        ],
        size=12.2,
    )

    panel = box(slide, Inches(13.55), Inches(3.62), Inches(5.04), Inches(3.38), PLUM_DARK, radius=True)
    text(slide, Inches(13.86), Inches(3.92), Inches(4.45), Inches(0.3), "Evidence-backed diagnosis", size=17, color=WHITE, bold=True, font=FONT_HEAD)
    text(
        slide,
        Inches(13.86),
        Inches(4.42),
        Inches(4.32),
        Inches(1.45),
        "Do not create more generic creator content first. Build the smallest bridge that carries useful beauty proof into Meesho's measurable commerce surface.",
        size=17,
        color=WHITE,
        bold=True,
        font=FONT_HEAD,
    )
    box(slide, Inches(13.86), Inches(6.10), Inches(4.22), Inches(0.55), CYAN, radius=True)
    text(slide, Inches(14.02), Inches(6.22), Inches(3.9), Inches(0.25), "Test the handoff before scaling the engine.", size=12.5, color=WHITE, bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, margin=0.0)
    footer(slide, "Evidence: S-001, M-CAT-001, COMP-FLOW-001, CCA manual-audit layer | Research cut: 09 Sep 2026 | Diagnosis remains a pilot hypothesis.")


def build_slide_2(slide):
    set_slide_bg(slide)
    title_bar(slide, "Prioritize the bridge before the engine.", "ROUND 1 | PRIORITIZATION")
    text(
        slide,
        Inches(0.68),
        Inches(1.73),
        Inches(18.0),
        Inches(0.52),
        "Decision rule: choose the smallest lever that improves the creator, shopper and brand loop while generating the data required for the long-term capability.",
        size=14.5,
        color=MUTED,
    )

    table_x, table_y = Inches(0.72), Inches(2.50)
    widths = [Inches(4.05), Inches(2.0), Inches(2.0), Inches(2.05), Inches(3.45)]
    headers = ["Lever", "30-day fit", "Learning", "Three-sided value", "Evidence-led read"]
    x = table_x
    for w, h in zip(widths, headers):
        box(slide, x, table_y, w, Inches(0.45), PLUM, radius=False)
        text(slide, x + Inches(0.06), table_y + Inches(0.07), w - Inches(0.12), Inches(0.27), h, size=10.3, color=WHITE, bold=True, margin=0.0, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE)
        x += w

    rows = [
        ("Acquire more creators", "High", "Low", "Medium", "Supply is not the only unknown; does not test proof handoff.", MUTED),
        ("Increase commission", "High", "Low", "Creator-led", "Can change behavior, but does not explain product or shopper uncertainty.", ROSE),
        ("Broad free sampling", "Medium", "Medium", "Medium", "May create content, but can create waste without fit or measurement.", ORANGE),
        ("Beauty Proof Bridge", "High", "High", "High", "Tests the live question: does structured proof improve the click-to-order handoff?", PINK),
        ("Full matching engine", "Low", "Very high", "Very high", "Strategic destination, but needs interaction data first.", PLUM),
    ]
    y = table_y + Inches(0.49)
    row_h = Inches(0.82)
    for lever, fit, learning, value, read, color in rows:
        x = table_x
        values = [lever, fit, learning, value, read]
        for idx, (w, value_text) in enumerate(zip(widths, values)):
            fill = PALE_PLUM if lever == "Beauty Proof Bridge" else WHITE
            border = color if lever == "Beauty Proof Bridge" else GRID
            box(slide, x, y, w, row_h, fill, radius=False, line=border, line_width=1.2)
            text(slide, x + Inches(0.08), y + Inches(0.11), w - Inches(0.16), row_h - Inches(0.17), value_text, size=11.3 if idx != 4 else 10.6, color=PLUM_DARK if lever == "Beauty Proof Bridge" else INK, bold=(idx == 0 or lever == "Beauty Proof Bridge"), valign=MSO_ANCHOR.MIDDLE)
            x += w
        y += row_h

    panel = box(slide, Inches(0.72), Inches(7.42), Inches(12.1), Inches(1.74), PLUM_DARK, radius=True)
    text(slide, Inches(1.00), Inches(7.68), Inches(4.5), Inches(0.3), "30-day wedge", size=18, color=WHITE, bold=True, font=FONT_HEAD)
    text(
        slide,
        Inches(1.00),
        Inches(8.08),
        Inches(11.25),
        Inches(0.75),
        "Beauty Proof Bridge: convert an existing creator review into a structured, attributable Meesho decision asset - without pretending the full matching engine already exists.",
        size=17,
        color=WHITE,
        bold=True,
        font=FONT_HEAD,
    )

    box(slide, Inches(13.15), Inches(2.50), Inches(5.45), Inches(6.66), SOFT, radius=True)
    text(slide, Inches(13.45), Inches(2.83), Inches(4.7), Inches(0.32), "Why this wins the first sprint", size=18, color=PLUM_DARK, bold=True, font=FONT_HEAD)
    bullets(
        slide,
        Inches(13.40),
        Inches(3.35),
        Inches(4.72),
        Inches(2.55),
        [
            "Builds on proof creators already know how to produce.",
            "Makes the handoff measurable instead of relying on views or vague influence.",
            "Serves brands with better product context, shoppers with faster fit decisions, and creators with clearer attribution.",
            "Generates the interaction data needed for future Creator x SKU x Audience matching.",
        ],
        size=13,
    )
    box(slide, Inches(13.45), Inches(6.35), Inches(4.66), Inches(1.28), WHITE, radius=True, line=ORANGE, line_width=1.3)
    text(slide, Inches(13.66), Inches(6.56), Inches(4.2), Inches(0.22), "Important constraint", size=10.5, color=ORANGE, bold=True, margin=0.0)
    text(slide, Inches(13.66), Inches(6.83), Inches(4.17), Inches(0.58), "The pilot must be allowed to kill the wedge if proof does not move transaction behavior.", size=13, color=INK, bold=True, margin=0.0)
    footer(slide, "Prioritization is a strategic decision under evidence constraints, not a completed H0-H5 statistical score.")


def build_slide_3(slide):
    set_slide_bg(slide)
    title_bar(slide, "30 days to prove whether proof transfer moves BPC commerce.", "ROUND 1 | QUICK WIN")
    box(slide, Inches(0.72), Inches(1.72), Inches(18.56), Inches(0.77), PLUM, radius=True)
    text(
        slide,
        Inches(0.98),
        Inches(1.92),
        Inches(18.0),
        Inches(0.34),
        "Beauty Proof Bridge = sample a small, relevant SKU set, structure the creator proof, surface it at the decision point, and measure the complete handoff.",
        size=15,
        color=WHITE,
        bold=True,
        align=PP_ALIGN.CENTER,
        valign=MSO_ANCHOR.MIDDLE,
        margin=0.0,
    )

    steps = [
        ("1. Select", "10-20 hero BPC SKUs with clear audience/use-case signals.", ORANGE),
        ("2. Match", "Invite a small creator cohort based on audience and category fit.", PINK),
        ("3. Sample", "Provide targeted product access; log cost and trial completion.", PLUM),
        ("4. Structure", "Capture fit, shade, texture, result, caveat and disclosure.", ROSE),
        ("5. Surface", "Attach proof to the Meesho commerce decision point.", CYAN),
        ("6. Measure", "Click -> order -> return -> repeat -> creator earnings.", OLIVE),
    ]
    x = Inches(0.78)
    y = Inches(3.00)
    w = Inches(2.85)
    gap = Inches(0.20)
    for i, (head, body, color) in enumerate(steps):
        flow_node(slide, x + i * (w + gap), y, w, head, body, color, i == 4)
        if i < len(steps) - 1:
            arrow(slide, x + i * (w + gap) + w, y + Inches(0.47), x + i * (w + gap) + w + gap, y + Inches(0.47))

    box(slide, Inches(0.78), Inches(4.48), Inches(8.75), Inches(3.48), WHITE, radius=True, line=PLUM, line_width=1.3)
    text(slide, Inches(1.05), Inches(4.78), Inches(4.4), Inches(0.3), "Pilot design", size=18, color=PLUM_DARK, bold=True, font=FONT_HEAD)
    bullets(
        slide,
        Inches(1.02),
        Inches(5.25),
        Inches(8.05),
        Inches(2.2),
        [
            "Proposed cohort: 10 sellers, 10-20 SKUs, 25-50 creators, four weeks.",
            "Treatment: structured proof plus tagged commerce surface.",
            "Control: comparable creator-led SKUs using the existing link/PDP journey.",
            "No scale decision until the pilot records the full funnel and creator effort.",
        ],
        size=13.2,
    )

    box(slide, Inches(9.80), Inches(4.48), Inches(9.50), Inches(3.48), PLUM_DARK, radius=True)
    text(slide, Inches(10.10), Inches(4.78), Inches(4.8), Inches(0.3), "Pre-registered decision metrics", size=18, color=WHITE, bold=True, font=FONT_HEAD)
    metrics = [
        ("Creator", "sample-to-post, effort/hour, earnings"),
        ("Content", "proof completeness, audience questions"),
        ("Commerce", "click-through, PDP-to-order, AOV"),
        ("Quality", "returns, ratings, repeat signal"),
    ]
    yy = Inches(5.28)
    for label, value in metrics:
        pill(slide, Inches(10.10), yy, Inches(1.35), label.upper(), CYAN if label == "Commerce" else PINK, size=8.5)
        text(slide, Inches(11.62), yy + Inches(0.01), Inches(6.85), Inches(0.30), value, size=13.1, color=WHITE, bold=True, valign=MSO_ANCHOR.MIDDLE, margin=0.0)
        yy += Inches(0.56)

    box(slide, Inches(0.78), Inches(8.38), Inches(18.52), Inches(1.02), SOFT, radius=True)
    text(slide, Inches(1.05), Inches(8.59), Inches(2.25), Inches(0.23), "KILL / SCALE RULE", size=10.5, color=PLUM, bold=True, margin=0.0)
    text(slide, Inches(3.35), Inches(8.55), Inches(15.45), Inches(0.40), "Scale only if the treatment improves the measurable handoff without making creator effort or sample cost uneconomic. Otherwise redirect to the winning leakage point.", size=14.5, color=INK, bold=True, font=FONT_HEAD, margin=0.0)
    footer(slide, "Pilot numbers are proposed operating parameters, not observed results. The experiment is designed to generate the missing Meesho-specific evidence.")


def build_slide_4(slide):
    set_slide_bg(slide)
    title_bar(slide, "Research architecture: separate observation, inference and model.", "APPENDIX | METHOD")
    text(slide, Inches(0.68), Inches(1.74), Inches(18.0), Inches(0.45), "The deck only promotes a claim when the artifact, source, limitation and funnel node are visible.", size=14.5, color=MUTED)
    tiers = [
        ("OBSERVED", "Case brief, category page, supplied manual audit notes, official YouTube documentation.", PLUM, "Can support a slide claim with a source ID."),
        ("INFERENCE", "The proof handoff may be the highest-addressability gap.", ORANGE, "Must be labeled as a diagnosis or hypothesis."),
        ("ILLUSTRATIVE MODEL", "Pilot cohort, measurement design and scenario economics.", CYAN, "Shows how Meesho will learn; not a reported result."),
        ("PENDING", "PDP decision support, conversion, repeat, creator earnings and primary respondent evidence.", ROSE, "Cannot be presented as established fact."),
    ]
    y = Inches(2.50)
    for head, body, color, rule in tiers:
        box(slide, Inches(0.82), y, Inches(3.0), Inches(1.15), color, radius=True)
        text(slide, Inches(1.03), y + Inches(0.21), Inches(2.55), Inches(0.25), head, size=14, color=WHITE, bold=True, font=FONT_HEAD, margin=0.0)
        box(slide, Inches(4.05), y, Inches(7.25), Inches(1.15), WHITE, radius=True, line=color, line_width=1.2)
        text(slide, Inches(4.27), y + Inches(0.16), Inches(6.82), Inches(0.75), body, size=13, color=INK, margin=0.0)
        box(slide, Inches(11.65), y, Inches(7.62), Inches(1.15), PALE_PLUM if color == PLUM else SOFT, radius=True)
        text(slide, Inches(11.90), y + Inches(0.17), Inches(7.1), Inches(0.7), rule, size=12.8, color=PLUM_DARK, bold=True, margin=0.0)
        y += Inches(1.42)
    box(slide, Inches(0.82), Inches(8.35), Inches(18.45), Inches(1.10), PLUM_DARK, radius=True)
    text(slide, Inches(1.10), Inches(8.62), Inches(17.9), Inches(0.45), "Research cut: 09 Sep 2026 | Primary respondents: 0 in the committed tracker | H0-H5 scores intentionally blank | PPT claims must remain traceable to evidence IDs.", size=15, color=WHITE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, margin=0.0)
    footer(slide, "Source files: DICE_GATE1_AUDIT_WORKBOOK.md, DICE_EVIDENCE_DATABASE.md, DICE_PRIMARY_RESEARCH_TRACKER.md.")


def build_slide_5(slide):
    set_slide_bg(slide)
    title_bar(slide, "What the creator audit changes: proof capability is real.", "APPENDIX | CREATOR EVIDENCE")
    text(slide, Inches(0.68), Inches(1.74), Inches(18.0), Inches(0.45), "The opportunity is not to teach creators how to review beauty products. It is to make their useful proof portable, attributable and decision-ready.", size=14.5, color=MUTED)
    examples = [
        ("CCA-006", "Shade and skin-fit warning", "Lakme Nude Twist was reported to wash out without a base.", "Direct team-supplied manual observation", H0_COLOR := ORANGE),
        ("CCA-007", "Viral product reality check", "Cult products were tested against Indian-skin shade and formula experience.", "Direct team-supplied manual observation", PINK),
        ("CCA-010", "Budget quality is uneven", "Zudio products showed strong and weak performers in the same ultra-budget line.", "Direct team-supplied manual observation", OLIVE),
        ("CCA-012", "Proof includes reliability", "Foundation white cast and a failed pump were both visible quality risks.", "Direct team-supplied manual observation", ROSE),
        ("CCA-013", "Business context matters", "Founder review connected product performance with commission and marketing claims.", "Financial figures require separate verification", PLUM),
        ("CCA-023/024", "Structured suitability is possible", "Dry-skin curation and professional undertone swatching make fit legible.", "Contradicts a generic content-difficulty claim", CYAN),
    ]
    y = Inches(2.48)
    for eid, head, body, note, color in examples:
        pill(slide, Inches(0.82), y + Inches(0.14), Inches(1.25), eid, color, size=8.5)
        box(slide, Inches(2.25), y, Inches(4.45), Inches(0.88), WHITE, radius=True, line=color, line_width=1.1)
        text(slide, Inches(2.45), y + Inches(0.13), Inches(4.0), Inches(0.23), head, size=12.2, color=PLUM_DARK, bold=True, margin=0.0)
        text(slide, Inches(2.45), y + Inches(0.40), Inches(4.0), Inches(0.32), body, size=10.8, color=INK, margin=0.0)
        box(slide, Inches(6.95), y, Inches(5.1), Inches(0.88), PALE_CYAN, radius=True)
        text(slide, Inches(7.16), y + Inches(0.20), Inches(4.65), Inches(0.40), note, size=11, color=INK, bold=True, margin=0.0)
        y += Inches(1.08)
    box(slide, Inches(12.55), Inches(2.48), Inches(6.72), Inches(5.98), PLUM_DARK, radius=True)
    text(slide, Inches(12.88), Inches(2.83), Inches(5.95), Inches(0.35), "What this does not prove", size=18, color=WHITE, bold=True, font=FONT_HEAD)
    bullets(
        slide,
        Inches(12.83),
        Inches(3.38),
        Inches(5.85),
        Inches(2.5),
        [
            "The videos are not Meesho-specific creator evidence.",
            "Content quality does not establish click-through, conversion, repeat or earnings.",
            "No exact line-level timestamps or screenshots are attached in the current workbook.",
            "A creator proof gap at the Meesho PDP remains unverified because the PDP audit was blocked.",
        ],
        size=13,
        color=WHITE,
    )
    box(slide, Inches(12.88), Inches(6.45), Inches(5.88), Inches(1.35), SOFT, radius=True)
    text(slide, Inches(13.10), Inches(6.70), Inches(5.45), Inches(0.65), "Therefore: preserve the proof, test the handoff, and let the pilot decide whether the bridge is the winner.", size=15, color=INK, bold=True, font=FONT_HEAD, margin=0.0)
    footer(slide, "Evidence tier: user-supplied manual audit layer; no independent replay claimed.")


def build_slide_6(slide):
    set_slide_bg(slide)
    title_bar(slide, "Competitive benchmark: the missing pattern is measurable handoff.", "APPENDIX | COMPETITOR EVIDENCE")
    text(slide, Inches(0.68), Inches(1.74), Inches(18.0), Inches(0.45), "The workspace verifies one public-source flow capability, not five end-to-end platform journeys.", size=14.5, color=MUTED)
    stages = ["Discovery", "Selection", "Info", "Proof", "Shopping", "Attribution", "Earnings"]
    x0 = Inches(0.82)
    stage_w = Inches(2.45)
    gap = Inches(0.13)
    y = Inches(2.45)
    for i, stage in enumerate(stages):
        color = [PLUM, ORANGE, PINK, ROSE, CYAN, OLIVE, PLUM][i]
        box(slide, x0 + i * (stage_w + gap), y, stage_w, Inches(0.45), color, radius=False)
        text(slide, x0 + i * (stage_w + gap), y + Inches(0.08), stage_w, Inches(0.24), stage, size=10.3, color=WHITE, bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, margin=0.0)
    statuses = [
        ("COMP-FLOW-001", "YouTube Shopping official documentation", "Public-source evidenced capability", "No replayed creator account or dashboard"),
        ("COMP-001", "Myntra Ultimate Glam Clan post", "Public program artifact", "Scale message, not conversion flow"),
        ("COMP-002/003", "Google India partner announcement", "Public partner artifact", "Nykaa/Purplle/Flipkart access, not full journeys"),
        ("COMP-004/005", "Amazon / Instagram-Meta", "Pending", "No workspace source record"),
    ]
    y = Inches(3.15)
    for eid, source, status, limitation in statuses:
        pill(slide, Inches(0.82), y + Inches(0.15), Inches(1.55), eid, PLUM if "FLOW" in eid else ORANGE, size=8.5)
        box(slide, Inches(2.55), y, Inches(5.1), Inches(0.78), WHITE, radius=True, line=GRID, line_width=1.0)
        text(slide, Inches(2.73), y + Inches(0.16), Inches(4.75), Inches(0.35), source, size=11.8, color=INK, bold=True, margin=0.0)
        box(slide, Inches(7.92), y, Inches(4.1), Inches(0.78), PALE_CYAN if status != "Pending" else SOFT, radius=True)
        text(slide, Inches(8.12), y + Inches(0.16), Inches(3.72), Inches(0.35), status, size=11.2, color=PLUM_DARK, bold=True, margin=0.0)
        box(slide, Inches(12.28), y, Inches(6.98), Inches(0.78), WHITE, radius=True, line=GRID, line_width=1.0)
        text(slide, Inches(12.48), y + Inches(0.16), Inches(6.55), Inches(0.35), limitation, size=11.2, color=INK, margin=0.0)
        y += Inches(1.03)
    box(slide, Inches(0.82), Inches(7.62), Inches(18.45), Inches(1.34), PALE_PLUM, radius=True)
    text(slide, Inches(1.08), Inches(7.92), Inches(17.9), Inches(0.65), "Strategic implication: Meesho does not need to copy every competitor feature. It needs one measurable bridge from creator proof to commerce, then the interaction data to build better matching.", size=16, color=PLUM_DARK, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, margin=0.0)
    footer(slide, "Evidence: COMP-FLOW-001, COMP-001, COMP-002, COMP-003. The workbook explicitly keeps COMP-004 and COMP-005 pending.")


def build_slide_7(slide):
    set_slide_bg(slide)
    title_bar(slide, "The long-term moat is a learning loop, not a sample box.", "APPENDIX | FUTURE ENGINE")
    text(slide, Inches(0.68), Inches(1.74), Inches(18.0), Inches(0.45), "The 30-day bridge is deliberately small. Its output is the interaction data required for Creator x SKU x Audience matching.", size=14.5, color=MUTED)
    cols = [
        ("BRAND -> SKU", "Which products have a clear use case, margin, authenticity and repeat potential?", ORANGE),
        ("CREATOR -> SKU", "Which creator can credibly demonstrate this product and invest the effort?", PINK),
        ("SKU -> AUDIENCE", "Which audience cohort has the right concern, budget and context?", CYAN),
        ("PROOF -> DECISION", "Which evidence reduces uncertainty enough to click, buy and reorder?", OLIVE),
    ]
    x = Inches(0.82)
    for head, body, color in cols:
        card(slide, x, Inches(2.50), Inches(4.35), Inches(2.08), head, body, color, body_size=13)
        x += Inches(4.58)
    loop = [
        ("Match", "Creator, SKU and audience signals"),
        ("Access", "Targeted sample or product trial"),
        ("Create", "Structured proof asset"),
        ("Surface", "Contextual Meesho decision point"),
        ("Measure", "Click, order, return, repeat, earnings"),
        ("Learn", "Improve future allocation"),
    ]
    x = Inches(1.05)
    y = Inches(5.35)
    node_w = Inches(2.70)
    for i, (head, body) in enumerate(loop):
        color = [PLUM, PINK, ORANGE, CYAN, OLIVE, ROSE][i]
        box(slide, x + (i % 3) * Inches(6.0), y + (i // 3) * Inches(1.45), node_w, Inches(0.90), color, radius=True)
        text(slide, x + (i % 3) * Inches(6.0) + Inches(0.08), y + (i // 3) * Inches(1.45) + Inches(0.12), node_w - Inches(0.16), Inches(0.22), head, size=12.2, color=WHITE, bold=True, margin=0.0)
        text(slide, x + (i % 3) * Inches(6.0) + Inches(0.08), y + (i // 3) * Inches(1.45) + Inches(0.39), node_w - Inches(0.16), Inches(0.34), body, size=10.5, color=WHITE, margin=0.0)
    box(slide, Inches(0.82), Inches(8.60), Inches(18.45), Inches(0.86), SOFT, radius=True)
    text(slide, Inches(1.05), Inches(8.82), Inches(17.95), Inches(0.35), "Do not build the engine first. Build the first data-generating wedge that earns the right to build it.", size=16, color=PLUM_DARK, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, margin=0.0)
    footer(slide, "Future-state architecture; not a claim that Meesho currently has these matching signals.")


def build_slide_8(slide):
    set_slide_bg(slide)
    title_bar(slide, "Measurement turns the idea into a business case.", "APPENDIX | ECONOMICS")
    text(slide, Inches(0.68), Inches(1.74), Inches(18.0), Inches(0.45), "We will size the opportunity from observed pilot deltas, not invented market-response percentages.", size=14.5, color=MUTED)
    box(slide, Inches(0.82), Inches(2.45), Inches(18.45), Inches(1.02), PLUM_DARK, radius=True)
    text(slide, Inches(1.05), Inches(2.76), Inches(17.9), Inches(0.38), "BPC creator NMV = active creators x relevant posts x click-through x PDP-to-order conversion x AOV x repeat", size=20, color=WHITE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, margin=0.0)
    drivers = [
        ("ACTIVE CREATORS", "sample-to-post\ncreator retention", PLUM),
        ("RELEVANT POSTS", "proof completeness\ncontent usefulness", PINK),
        ("CLICK-THROUGH", "tag/CTA quality\nproof placement", ORANGE),
        ("CONVERSION", "fit confidence\nPDP decision support", CYAN),
        ("REPEAT", "quality\nreturns\nreorder", OLIVE),
    ]
    x = Inches(0.82)
    for head, body, color in drivers:
        box(slide, x, Inches(4.05), Inches(3.47), Inches(1.38), WHITE, radius=True, line=color, line_width=1.3)
        box(slide, x, Inches(4.05), Inches(3.47), Inches(0.25), color, radius=False)
        text(slide, x + Inches(0.11), Inches(4.12), Inches(3.25), Inches(0.18), head, size=10.2, color=WHITE, bold=True, align=PP_ALIGN.CENTER, margin=0.0)
        text(slide, x + Inches(0.20), Inches(4.48), Inches(3.05), Inches(0.75), body, size=13, color=INK, bold=True, align=PP_ALIGN.CENTER, margin=0.0)
        x += Inches(3.67)
    box(slide, Inches(0.82), Inches(5.90), Inches(8.95), Inches(2.55), PALE_CYAN, radius=True)
    text(slide, Inches(1.10), Inches(6.20), Inches(8.3), Inches(0.28), "Pilot instrumentation", size=17, color=PLUM_DARK, bold=True, font=FONT_HEAD)
    bullets(slide, Inches(1.08), Inches(6.66), Inches(8.25), Inches(1.35), [
        "Unique creator/SKU/audience IDs.",
        "Tagged click and order events.",
        "Sample cost, creator time and payout.",
        "Returns, rating and repeat cohort.",
    ], size=13)
    box(slide, Inches(10.12), Inches(5.90), Inches(9.15), Inches(2.55), SOFT, radius=True)
    text(slide, Inches(10.42), Inches(6.20), Inches(8.5), Inches(0.28), "What we can say after the pilot", size=17, color=PLUM_DARK, bold=True, font=FONT_HEAD)
    bullets(slide, Inches(10.40), Inches(6.66), Inches(8.3), Inches(1.35), [
        "Which proof fields correlate with clicks and orders.",
        "Which creators produce efficient, credible proof.",
        "Whether targeted samples beat broad gifting.",
        "Whether the bridge deserves scale or should be killed.",
    ], size=13)
    footer(slide, "No uplift is claimed in this deck. The pilot is the mechanism for generating defensible NMV and retention estimates.")


def build_slide_9(slide):
    set_slide_bg(slide)
    title_bar(slide, "Risks, kill criteria and the path to scale.", "APPENDIX | EXECUTION")
    text(slide, Inches(0.68), Inches(1.74), Inches(18.0), Inches(0.45), "A credible case does not hide what could disprove it. It pre-commits to learning and stopping rules.", size=14.5, color=MUTED)
    risks = [
        ("Proof does not move orders", "Kill or redesign the bridge; investigate price, quality, delivery and PDP UX.", ROSE),
        ("Creators reject the effort", "Shift toward economics, sampling design or lighter proof formats.", ORANGE),
        ("Sample cost is uneconomic", "Narrow SKU set and require seller co-funding or higher repeat potential.", PINK),
        ("PDP cannot carry proof", "Start with storefront/landing surfaces while product integration is built.", CYAN),
        ("Quality/returns dominate", "Move H0 to the front; solve assortment/authenticity before creator scale.", OLIVE),
    ]
    y = Inches(2.42)
    for head, body, color in risks:
        box(slide, Inches(0.82), y, Inches(8.75), Inches(0.82), WHITE, radius=True, line=color, line_width=1.2)
        pill(slide, Inches(1.02), y + Inches(0.22), Inches(2.25), head.upper(), color, size=8.2)
        text(slide, Inches(3.48), y + Inches(0.18), Inches(5.75), Inches(0.42), body, size=11.8, color=INK, bold=True, margin=0.0)
        y += Inches(0.99)
    box(slide, Inches(10.05), Inches(2.42), Inches(9.22), Inches(4.85), PLUM_DARK, radius=True)
    text(slide, Inches(10.38), Inches(2.78), Inches(8.55), Inches(0.3), "30 / 60 / 90", size=20, color=WHITE, bold=True, font=FONT_HEAD)
    roadmap = [
        ("30 days", "Pilot the Beauty Proof Bridge on a controlled SKU and creator cohort."),
        ("60 days", "Add reusable proof fields, creator attribution and seller reporting."),
        ("90 days", "Use observed interaction data to allocate samples and rank creator-SKU-audience matches."),
    ]
    yy = Inches(3.35)
    for head, body in roadmap:
        pill(slide, Inches(10.38), yy, Inches(1.35), head.upper(), CYAN if head == "30 days" else PINK if head == "60 days" else ORANGE, size=8.5)
        text(slide, Inches(11.98), yy + Inches(0.02), Inches(6.75), Inches(0.52), body, size=12.2, color=WHITE, bold=True, margin=0.0)
        yy += Inches(1.05)
    box(slide, Inches(10.38), Inches(6.37), Inches(8.42), Inches(0.55), SOFT, radius=True)
    text(slide, Inches(10.58), Inches(6.50), Inches(8.0), Inches(0.25), "Scale only after treatment beats control on the pre-registered handoff metrics.", size=11.5, color=INK, bold=True, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, margin=0.0)
    box(slide, Inches(0.82), Inches(7.64), Inches(18.45), Inches(1.02), PALE_PLUM, radius=True)
    text(slide, Inches(1.10), Inches(7.93), Inches(17.9), Inches(0.40), "North-star outcome: more BPC NMV and stronger creator retention by making credible proof measurable, reusable and increasingly better matched.", size=15.5, color=PLUM_DARK, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, valign=MSO_ANCHOR.MIDDLE, margin=0.0)
    footer(slide, "Team: Samiksha Mitra | Slayed it | IIT Guwahati | Sources and limitations documented in the research workspace.")


def build_deck() -> None:
    prs = Presentation(str(TEMPLATE))
    # Preserve the required template cover and content-slide structure.
    # Slides 2-4 are Round 1; slide 5 starts the appendix. New slides are
    # appended after the existing template slides to avoid duplicate parts.
    builders = [
        build_slide_1,
        build_slide_2,
        build_slide_3,
    ]
    appendix_builders = [
        build_slide_5,
        build_slide_6,
        build_slide_7,
        build_slide_8,
        build_slide_9,
    ]
    slides = list(prs.slides)
    build_cover(slides[0])
    for builder, slide in zip(builders, slides[1:4]):
        builder(slide)
    build_slide_4(slides[4])

    blank_layout = prs.slide_layouts[6]
    for builder in appendix_builders:
        slide = prs.slides.add_slide(blank_layout)
        builder(slide)
    prs.save(str(OUTPUT))


if __name__ == "__main__":
    build_deck()
