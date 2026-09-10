from __future__ import annotations

from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

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


def add_hyperlink_hotspot(slide, x, y, w, h, url):
    shape = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, x, y, w, h)
    fill_shape(shape, WHITE, transparency=1.0)
    shape.line.fill.background()
    shape.click_action.hyperlink.address = url
    return shape


def add_source_hotspots(slide, slide_number):
    sources = {
        2: [
            (Inches(0.45), Inches(10.50), Inches(7.0), Inches(0.45), "https://support.google.com/youtube/answer/13376398"),
        ],
        3: [
            (Inches(14.10), Inches(2.65), Inches(4.70), Inches(0.55), "https://support.google.com/youtube/answer/13376398"),
            (Inches(14.10), Inches(8.25), Inches(4.70), Inches(0.70), "https://affiliate-program.amazon.in/"),
        ],
        4: [
            (Inches(0.45), Inches(10.50), Inches(8.0), Inches(0.45), "https://github.com/Samik123Mit/abc"),
            (Inches(15.20), Inches(9.75), Inches(4.20), Inches(0.55), "https://samik123mit.github.io/Slayed-it/"),
        ],
        6: [
            (Inches(0.45), Inches(10.50), Inches(10.0), Inches(0.45), "https://github.com/Samik123Mit/abc/blob/main/DICE_EVIDENCE_DATABASE.md"),
            (Inches(0.45), Inches(4.10), Inches(12.5), Inches(0.75), "https://www.meesho.com/beauty-products/pl/9on"),
        ],
        7: [
            (Inches(0.45), Inches(10.50), Inches(10.0), Inches(0.45), "https://github.com/Samik123Mit/abc/blob/main/DICE_GATE1_AUDIT_WORKBOOK.md"),
        ],
        8: [
            (Inches(0.45), Inches(2.65), Inches(4.0), Inches(0.78), "https://support.google.com/youtube/answer/13376398"),
            (Inches(0.45), Inches(3.47), Inches(4.0), Inches(0.78), "https://affiliate-program.amazon.in/"),
            (Inches(0.45), Inches(4.29), Inches(4.0), Inches(0.78), "https://affiliate.nykaa.com/"),
            (Inches(0.45), Inches(5.11), Inches(4.0), Inches(0.78), "https://affiliate.flipkart.com/"),
            (Inches(0.45), Inches(5.93), Inches(4.0), Inches(0.78), "https://www.myntra.com/"),
            (Inches(0.45), Inches(10.50), Inches(8.0), Inches(0.45), "https://github.com/Samik123Mit/abc/blob/main/DICE_EVIDENCE_DATABASE.md"),
        ],
        9: [
            (Inches(0.45), Inches(10.50), Inches(8.0), Inches(0.45), "https://github.com/Samik123Mit/abc/blob/main/DICE_GATE1_AUDIT_WORKBOOK.md"),
        ],
        10: [
            (Inches(0.45), Inches(10.50), Inches(8.0), Inches(0.45), "https://github.com/Samik123Mit/abc/blob/main/DICE_MASTER_DOC.md"),
        ],
        11: [
            (Inches(0.45), Inches(10.50), Inches(8.0), Inches(0.45), "https://github.com/Samik123Mit/abc/blob/main/DICE_PRIMARY_RESEARCH_TRACKER.md"),
        ],
        12: [
            (Inches(0.45), Inches(10.50), Inches(8.0), Inches(0.45), "https://github.com/Samik123Mit/abc/blob/main/DICE_PRIMARY_RESEARCH_TRACKER.md"),
        ],
        13: [
            (Inches(0.45), Inches(10.50), Inches(19.0), Inches(0.45), "https://github.com/Samik123Mit/abc"),
            (Inches(12.85), Inches(7.53), Inches(2.8), Inches(0.55), "https://samik123mit.github.io/Slayed-it/"),
            (Inches(16.17), Inches(7.53), Inches(2.8), Inches(0.55), "https://github.com/Samik123Mit/Slayed-it"),
            (Inches(12.85), Inches(8.24), Inches(2.8), Inches(0.55), "https://drive.google.com/drive/folders/1G0R-wYdUQVaQYODfuxXvG6kIceHaBhwK?usp=sharing"),
            (Inches(16.17), Inches(8.24), Inches(2.8), Inches(0.55), "https://github.com/Samik123Mit/Slayed-it/blob/main/DICE_MASTER_DOC.md"),
            (Inches(12.85), Inches(8.95), Inches(2.8), Inches(0.55), "https://github.com/Samik123Mit/abc/blob/main/DICE_EVIDENCE_DATABASE.md"),
            (Inches(16.17), Inches(8.95), Inches(2.8), Inches(0.55), "https://support.google.com/youtube/answer/13376398"),
        ],
    }
    for x, y, w, h, url in sources.get(slide_number, []):
        add_hyperlink_hotspot(slide, x, y, w, h, url)


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


def _asset(name: str) -> bytes:
    with ZipFile(TEMPLATE) as archive:
        return archive.read("ppt/media/" + name)


def _wipe(slide) -> None:
    for shape in list(slide.shapes):
        slide.shapes._spTree.remove(shape._element)


def _pic(slide, name: str, x, y, w=None, h=None):
    stream = BytesIO(_asset(name))
    return slide.shapes.add_picture(stream, x, y, width=w, height=h)


def _line(slide, x, y, w, color=GRID, width=1.2):
    shape = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.RECTANGLE, x, y, w, Pt(width))
    fill_shape(shape, color)
    return shape


def _brand_header(slide, section: str, kicker: str = "DICE CHALLENGE | SEASON 3"):
    _pic(slide, "image5.png", Inches(0.45), Inches(0.19), w=Inches(1.48))
    box(slide, Inches(18.68), Inches(0.15), Inches(0.86), Inches(0.60), PLUM_DARK, radius=True)
    text(slide, Inches(18.77), Inches(0.20), Inches(0.68), Inches(0.25), "m", size=26, color=ORANGE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    text(slide, Inches(18.72), Inches(0.49), Inches(0.76), Inches(0.14), "meesho", size=7.5, color=WHITE, bold=True, align=PP_ALIGN.CENTER, margin=0.0)
    text(slide, Inches(2.08), Inches(0.26), Inches(12.8), Inches(0.18), kicker, size=8.5, color=ROSE, bold=True, margin=0.0)
    text(slide, Inches(2.08), Inches(0.48), Inches(15.9), Inches(0.52), section, size=24, color=PLUM_DARK, bold=True, font=FONT_HEAD, margin=0.0)
    _line(slide, Inches(0.45), Inches(1.16), Inches(19.1), GRID, 1.3)


def _section_bar(slide, x, y, w, label, color=PLUM_DARK):
    box(slide, x, y, w, Inches(0.34), color, radius=True)
    text(slide, x + Inches(0.12), y + Inches(0.06), w - Inches(0.24), Inches(0.21), label.upper(), size=9.5, color=WHITE, bold=True, margin=0.0)


def _chevron(slide, x, y, w, label, sub, color, active=False):
    shape = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.CHEVRON, x, y, w, Inches(0.64))
    fill_shape(shape, color if active else PLUM_DARK, line=WHITE, line_width=1.0)
    text(slide, x + Inches(0.12), y + Inches(0.10), w - Inches(0.28), Inches(0.19), label, size=10.5, color=WHITE, bold=True, align=PP_ALIGN.CENTER, margin=0.0)
    text(slide, x + Inches(0.11), y + Inches(0.34), w - Inches(0.24), Inches(0.16), sub, size=7.9, color=CREAM, align=PP_ALIGN.CENTER, margin=0.0)


def _status_chip(slide, x, y, label, color, w=Inches(1.08)):
    box(slide, x, y, w, Inches(0.28), color, radius=True)
    text(slide, x, y + Inches(0.04), w, Inches(0.16), label.upper(), size=7.4, color=WHITE, bold=True, align=PP_ALIGN.CENTER, margin=0.0)


def _evidence_tag(slide, x, y, label, color=ORANGE):
    box(slide, x, y, Inches(0.86), Inches(0.25), color, radius=True)
    text(slide, x, y + Inches(0.04), Inches(0.86), Inches(0.15), label, size=7.2, color=WHITE, bold=True, align=PP_ALIGN.CENTER, margin=0.0)


def _mini_icon(slide, x, y, label, color=ORANGE):
    shape = slide.shapes.add_shape(MSO_AUTO_SHAPE_TYPE.OVAL, x, y, Inches(0.33), Inches(0.33))
    fill_shape(shape, color, line=PLUM_DARK, line_width=0.7)
    text(slide, x, y + Inches(0.04), Inches(0.33), Inches(0.20), label, size=9.5, color=PLUM_DARK, bold=True, align=PP_ALIGN.CENTER, margin=0.0)


def _dense_card(slide, x, y, w, h, title, body, accent=PLUM_DARK, tag=None):
    box(slide, x, y, w, h, WHITE, radius=True, line=GRID, line_width=0.8)
    box(slide, x, y, Inches(0.08), h, accent, radius=False)
    text(slide, x + Inches(0.18), y + Inches(0.13), w - Inches(0.3), Inches(0.22), title, size=11.5, color=PLUM_DARK, bold=True, margin=0.0)
    text(slide, x + Inches(0.18), y + Inches(0.40), w - Inches(0.3), h - Inches(0.48), body, size=9.3, color=INK, margin=0.0)
    if tag:
        _evidence_tag(slide, x + w - Inches(0.98), y + Inches(0.11), tag, accent)


def _metric_ribbon(slide, x, y, w, value, label, accent):
    box(slide, x, y, w, Inches(0.63), accent, radius=True)
    text(slide, x + Inches(0.12), y + Inches(0.10), Inches(0.72), Inches(0.35), value, size=21, color=WHITE, bold=True, font=FONT_HEAD, margin=0.0)
    text(slide, x + Inches(0.92), y + Inches(0.15), w - Inches(1.05), Inches(0.25), label, size=9.0, color=WHITE, bold=True, margin=0.0)


def _new_cover(slide):
    _wipe(slide)
    set_slide_bg(slide, PLUM_DARK)
    _pic(slide, "image3.png", 0, 0, w=W, h=H)
    overlay = box(slide, 0, 0, Inches(11.8), H, PLUM_DARK, radius=False, transparency=14)
    box(slide, Inches(0.78), Inches(0.67), Inches(2.55), Inches(0.32), ORANGE, radius=True)
    text(slide, Inches(0.91), Inches(0.74), Inches(2.28), Inches(0.16), "MEESHO DICE CHALLENGE | S3", size=8.8, color=PLUM_DARK, bold=True, margin=0.0)
    text(slide, Inches(0.82), Inches(2.05), Inches(10.2), Inches(1.05), "Beauty proof is abundant.\nCommerce handoff is not.", size=34, color=WHITE, bold=True, font=FONT_HEAD, margin=0.0)
    text(slide, Inches(0.86), Inches(3.50), Inches(8.6), Inches(0.48), "A measured bridge from creator evidence to confident Meesho purchase.", size=18, color=CREAM, bold=True, font=FONT_HEAD, margin=0.0)
    box(slide, Inches(0.85), Inches(4.45), Inches(6.9), Inches(1.28), SOFT, radius=True)
    text(slide, Inches(1.12), Inches(4.70), Inches(6.35), Inches(0.18), "PROPOSED 30-DAY WEDGE", size=9.2, color=ROSE, bold=True, margin=0.0)
    text(slide, Inches(1.12), Inches(5.03), Inches(6.35), Inches(0.36), "Beauty Proof Bridge", size=23, color=PLUM_DARK, bold=True, font=FONT_HEAD, margin=0.0)
    text(slide, Inches(0.86), Inches(8.75), Inches(5.8), Inches(0.25), "Team Slayed it", size=14, color=WHITE, bold=True, font=FONT_HEAD, margin=0.0)
    text(slide, Inches(0.86), Inches(9.12), Inches(6.2), Inches(0.25), "Samiksha Mitra | IIT Guwahati", size=11.5, color=CREAM, margin=0.0)
    text(slide, Inches(0.86), Inches(10.35), Inches(6.2), Inches(0.22), "Evidence cut: 09 September 2026 | Appendix included", size=8.7, color=CREAM, margin=0.0)


def _new_slide_1(slide):
    _wipe(slide)
    set_slide_bg(slide, CREAM)
    _brand_header(slide, "The leak is not beauty proof. It is the proof handoff.", "ROUND 1 | VALUE CHAIN")
    text(slide, Inches(0.55), Inches(1.38), Inches(18.2), Inches(0.32), "Creators already explain fit, shade, texture and outcomes. The unresolved value leak begins when useful proof leaves the video and enters a generic transaction surface.", size=12.5, color=MUTED, margin=0.0)
    _section_bar(slide, Inches(0.55), Inches(1.92), Inches(18.9), "The creator → SKU → audience → commerce chain")
    stages = [
        ("BRAND / SKU", "claim + cohort", ORANGE),
        ("CREATOR MATCH", "credibility + fit", PINK),
        ("TRIAL", "access + use", PLUM),
        ("PROOF", "shade + result", ROSE),
        ("DISTRIBUTION", "reach + context", CYAN),
        ("MEESHO SURFACE", "decision support", OLIVE),
        ("PURCHASE", "order + return", PLUM),
        ("REPEAT / PAYOUT", "learning loop", ORANGE),
    ]
    x = Inches(0.55)
    for i, (label, sub, color) in enumerate(stages):
        _chevron(slide, x, Inches(2.38), Inches(2.36), label, sub, color, active=(label == "MEESHO SURFACE"))
        x += Inches(2.37)
    _status_chip(slide, Inches(13.73), Inches(3.14), "leak to test", PINK, Inches(1.22))
    _line(slide, Inches(13.50), Inches(3.46), Inches(2.8), PINK, 2.0)
    text(slide, Inches(13.60), Inches(3.56), Inches(2.5), Inches(0.20), "proof → click → order", size=9.0, color=PINK, bold=True, align=PP_ALIGN.CENTER, margin=0.0)

    _section_bar(slide, Inches(0.55), Inches(3.92), Inches(12.18), "What the evidence makes visible")
    cards = [
        ("CREATOR", "26/28 audited videos demonstrate products; 24/28 discuss suitability.", "CCA", PLUM),
        ("SHOPPER", "Shade, skin type, texture and outcome are decision variables, not just views.", "CCA", PINK),
        ("BRAND", "PR volume and product defects create a need for better fit, quality and attribution.", "CCA", ORANGE),
        ("MEESHO", "The public audit does not yet prove the PDP can carry this context into conversion.", "M-PDP", ROSE),
    ]
    x_positions = [Inches(0.55), Inches(3.62), Inches(6.69), Inches(9.76)]
    for (title, body, tag, color), xx in zip(cards, x_positions):
        _dense_card(slide, xx, Inches(4.37), Inches(2.83), Inches(1.43), title, body, color, tag)

    box(slide, Inches(0.55), Inches(6.18), Inches(12.18), Inches(1.44), PLUM_DARK, radius=True)
    text(slide, Inches(0.84), Inches(6.42), Inches(2.10), Inches(0.18), "DIAGNOSIS", size=9.5, color=ORANGE, bold=True, margin=0.0)
    text(slide, Inches(0.84), Inches(6.70), Inches(11.48), Inches(0.54), "The strongest defensible problem is not “creators lack proof.” It is that Meesho has not yet shown a measurable, reusable handoff for proof that already exists.", size=16.2, color=WHITE, bold=True, font=FONT_HEAD, margin=0.0)

    _section_bar(slide, Inches(13.15), Inches(3.92), Inches(6.30), "Reality check")
    facts = [
        ("28", "accessible creator audits", PLUM),
        ("0/28", "routed to Meesho in sample", PINK),
        ("1", "public-source flow capability verified", CYAN),
        ("0", "primary respondents in tracker", ROSE),
    ]
    yy = Inches(4.37)
    for value, label, color in facts:
        _metric_ribbon(slide, Inches(13.15), yy, Inches(6.30), value, label, color)
        yy += Inches(0.77)
    footer(slide, "Evidence: CCA-001–030 audit layer; M-CAT-001; M-PDP-001; COMP-FLOW-001. Proposed diagnosis, not a validated H0–H5 score.")


def _new_slide_2(slide):
    _wipe(slide)
    set_slide_bg(slide, CREAM)
    _brand_header(slide, "Prioritize the bridge before the engine.", "ROUND 1 | PRIORITIZATION")
    text(slide, Inches(0.55), Inches(1.38), Inches(18.2), Inches(0.30), "Decision rule: pick the smallest lever that serves creators, shoppers and sellers while producing the missing transaction evidence.", size=12.5, color=MUTED, margin=0.0)
    _section_bar(slide, Inches(0.55), Inches(1.92), Inches(13.85), "Strategic prioritization under evidence constraints")
    _section_bar(slide, Inches(14.62), Inches(1.92), Inches(4.83), "Why this wins now", ORANGE)
    headers = ["LEVER", "WHAT IT DOES", "3-SIDED VALUE", "EVIDENCE", "30-DAY FIT", "LEARNING", "DECISION"]
    widths = [2.10, 2.75, 1.52, 1.35, 1.25, 1.25, 1.55]
    x0, y0 = Inches(0.55), Inches(2.37)
    xx = x0
    for h, w in zip(headers, widths):
        box(slide, xx, y0, Inches(w), Inches(0.40), PLUM_DARK, radius=False)
        text(slide, xx + Inches(0.04), y0 + Inches(0.10), Inches(w - 0.08), Inches(0.18), h, size=7.8, color=WHITE, bold=True, align=PP_ALIGN.CENTER, margin=0.0)
        xx += Inches(w)
    rows = [
        ("Creator acquisition", "More supply", "C / B", "MED", "HIGH", "LOW", "DEFER", ROSE),
        ("Commission uplift", "Change effort", "C", "LOW", "HIGH", "LOW", "DEFER", PINK),
        ("Broad sampling", "Create volume", "C / B", "MED", "MED", "MED", "NARROW", ORANGE),
        ("Beauty Proof Bridge", "Carry proof into Meesho", "C / S / B", "HIGH*", "HIGH", "HIGH", "PILOT", CYAN),
        ("PDP suitability layer", "Make fit legible", "S / B", "LOW*", "MED", "HIGH", "PAIR", OLIVE),
        ("Full matching engine", "Allocate creator x SKU", "C / S / B", "LOW", "LOW", "VERY HIGH", "LATER", PLUM),
        ("Quality / authenticity", "Reduce bad orders", "S / B", "LOW", "MED", "HIGH", "PARALLEL", ROSE),
    ]
    y = Inches(2.82)
    for name, desc, value, conf, fit, learn, decision, color in rows:
        fill = PALE_CYAN if name == "Beauty Proof Bridge" else WHITE
        border = color if name == "Beauty Proof Bridge" else GRID
        xx = x0
        vals = [name, desc, value, conf, fit, learn, decision]
        for idx, (val, w) in enumerate(zip(vals, widths)):
            box(slide, xx, y, Inches(w), Inches(0.61), fill, radius=False, line=border, line_width=1.0)
            text(slide, xx + Inches(0.07), y + Inches(0.12), Inches(w - 0.14), Inches(0.34), val, size=8.5 if idx != 0 else 9.2, color=PLUM_DARK if name == "Beauty Proof Bridge" else INK, bold=(idx == 0 or (name == "Beauty Proof Bridge" and idx == 6)), align=PP_ALIGN.CENTER if idx >= 2 else PP_ALIGN.LEFT, valign=MSO_ANCHOR.MIDDLE, margin=0.0)
            xx += Inches(w)
        y += Inches(0.65)
    box(slide, Inches(0.55), Inches(7.52), Inches(13.85), Inches(0.87), PLUM_DARK, radius=True)
    text(slide, Inches(0.82), Inches(7.73), Inches(13.3), Inches(0.42), "WINNING MOVE  →  Pilot Beauty Proof Bridge first; use observed click, order, return and creator-effort data to earn the right to build the matching engine.", size=13.5, color=WHITE, bold=True, font=FONT_HEAD, margin=0.0)
    side = [
        ("01", "Uses proof creators already produce", PINK),
        ("02", "Tests the actual commerce leak", CYAN),
        ("03", "Creates the data moat", ORANGE),
        ("04", "Can be killed without platform-scale build", OLIVE),
    ]
    yy = Inches(2.42)
    for num, label, color in side:
        _mini_icon(slide, Inches(14.84), yy + Inches(0.07), num, color)
        text(slide, Inches(15.30), yy + Inches(0.07), Inches(3.70), Inches(0.35), label, size=10.8, color=INK, bold=True, margin=0.0)
        yy += Inches(0.76)
    box(slide, Inches(14.72), Inches(5.72), Inches(4.55), Inches(1.60), SOFT, radius=True, line=ORANGE, line_width=1.1)
    text(slide, Inches(14.96), Inches(5.95), Inches(4.05), Inches(0.18), "CONSTRAINT", size=9.2, color=ORANGE, bold=True, margin=0.0)
    text(slide, Inches(14.96), Inches(6.24), Inches(4.00), Inches(0.72), "No invented uplift. No H0–H5 score. The pilot is the mechanism that creates the missing evidence.", size=13.3, color=PLUM_DARK, bold=True, font=FONT_HEAD, margin=0.0)
    footer(slide, "C = creator | S = shopper | B = brand/seller. *Evidence confidence is based on audit coverage, not Meesho conversion proof.")


def _new_slide_3(slide):
    _wipe(slide)
    set_slide_bg(slide, CREAM)
    _brand_header(slide, "30 days to prove whether proof transfer moves BPC commerce.", "ROUND 1 | QUICK WIN")
    box(slide, Inches(0.55), Inches(1.38), Inches(18.9), Inches(0.66), PLUM_DARK, radius=True)
    text(slide, Inches(0.78), Inches(1.57), Inches(18.4), Inches(0.26), "BEAUTY PROOF BRIDGE  =  structured creator proof + attributable Meesho handoff + a killable experiment", size=14.6, color=WHITE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    _section_bar(slide, Inches(0.55), Inches(2.31), Inches(18.9), "Operating model | one small cohort, one measurable handoff")
    weeks = [
        ("WEEK 1", "Select", "10–20 hero SKUs\n10 sellers\nfit criteria", ORANGE),
        ("WEEK 2", "Match + sample", "25–50 creators\nrelevant audience\nlogged cost", PINK),
        ("WEEK 3", "Structure + surface", "proof fields\ncreator disclosure\nMeesho decision asset", CYAN),
        ("WEEK 4", "Measure + decide", "click → order\nreturn → repeat\ncreator payout", OLIVE),
    ]
    x = Inches(0.55)
    for week, head, body, color in weeks:
        box(slide, x, Inches(2.78), Inches(4.56), Inches(1.42), WHITE, radius=True, line=color, line_width=1.7)
        box(slide, x, Inches(2.78), Inches(4.56), Inches(0.28), color, radius=False)
        text(slide, x + Inches(0.13), Inches(2.84), Inches(1.0), Inches(0.16), week, size=8.3, color=PLUM_DARK, bold=True, margin=0.0)
        text(slide, x + Inches(1.22), Inches(2.83), Inches(3.10), Inches(0.18), head, size=11.3, color=WHITE, bold=True, margin=0.0)
        text(slide, x + Inches(0.18), Inches(3.23), Inches(4.15), Inches(0.67), body, size=12.2, color=INK, bold=True, align=PP_ALIGN.CENTER, margin=0.0)
        x += Inches(4.78)

    _section_bar(slide, Inches(0.55), Inches(4.47), Inches(12.15), "Three-sided workflow")
    lanes = [
        ("CREATOR", "Receive relevant SKU → publish structured proof → tag/link → see attributed outcomes", PINK),
        ("SELLER / BRAND", "Nominate fit-ready SKUs → fund or approve trial → see quality + demand signals", ORANGE),
        ("SHOPPER", "Discover proof → resolve fit/shade/texture → click → buy → rate/reorder", CYAN),
    ]
    y = Inches(4.91)
    for head, body, color in lanes:
        box(slide, Inches(0.55), y, Inches(12.15), Inches(0.72), WHITE, radius=True, line=GRID, line_width=0.8)
        pill(slide, Inches(0.76), y + Inches(0.20), Inches(1.55), head, color, size=8.0)
        text(slide, Inches(2.55), y + Inches(0.17), Inches(9.78), Inches(0.34), body, size=11.0, color=INK, bold=True, margin=0.0)
        y += Inches(0.83)
    _section_bar(slide, Inches(13.05), Inches(4.47), Inches(6.4), "Instrumentation + kill rule", ORANGE)
    instruments = [
        ("IDs", "creator / SKU / audience / treatment"),
        ("Events", "view → click → PDP → order → return"),
        ("Effort", "sample cost + creator time + payout"),
        ("Quality", "rating + defect + repeat signal"),
    ]
    y = Inches(4.92)
    for head, body in instruments:
        _mini_icon(slide, Inches(13.22), y + Inches(0.04), "•", ORANGE)
        text(slide, Inches(13.68), y + Inches(0.03), Inches(5.45), Inches(0.17), head, size=10.1, color=PLUM_DARK, bold=True, margin=0.0)
        text(slide, Inches(13.68), y + Inches(0.24), Inches(5.30), Inches(0.27), body, size=8.8, color=INK, margin=0.0)
        y += Inches(0.66)
    box(slide, Inches(13.16), Inches(7.57), Inches(6.13), Inches(1.05), PLUM_DARK, radius=True)
    text(slide, Inches(13.42), Inches(7.79), Inches(5.62), Inches(0.20), "KILL / SCALE", size=9.3, color=ORANGE, bold=True, margin=0.0)
    text(slide, Inches(13.42), Inches(8.10), Inches(5.56), Inches(0.31), "Scale only if treatment beats control on the handoff without uneconomic creator effort or sample cost.", size=10.8, color=WHITE, bold=True, margin=0.0)
    box(slide, Inches(0.55), Inches(7.72), Inches(12.15), Inches(0.90), SOFT, radius=True)
    text(slide, Inches(0.83), Inches(7.94), Inches(11.60), Inches(0.35), "PILOT  →  MEASURED HANDOFF  →  LEARN  →  SCALE OR KILL", size=16, color=PLUM_DARK, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    footer(slide, "All cohort sizes and metrics are proposed operating parameters. The pilot exists to generate Meesho-specific evidence.")


def _new_slide_4(slide):
    _wipe(slide)
    set_slide_bg(slide, CREAM)
    _brand_header(slide, "Evidence architecture: every claim has a status.", "APPENDIX | RESEARCH QUALITY")
    text(slide, Inches(0.55), Inches(1.38), Inches(18.2), Inches(0.30), "We separate what was seen, what is public, what is inferred and what is still missing so the case stays defensible under challenge.", size=12.5, color=MUTED, margin=0.0)
    _section_bar(slide, Inches(0.55), Inches(1.92), Inches(12.10), "Research status board")
    _section_bar(slide, Inches(13.02), Inches(1.92), Inches(6.43), "Submission guardrails", ORANGE)
    tiers = [
        ("DIRECT OBSERVATION", "CCA manual-quality content audit: 28 accessible records.", "May support capability claims", PLUM),
        ("PUBLIC ARTIFACT", "Official program / platform documentation and public pages.", "May support capability existence", CYAN),
        ("INFERENCE", "Proof handoff is a plausible addressable leak.", "Must be labelled diagnosis", ORANGE),
        ("PENDING", "Meesho conversion, repeat, earnings, respondent evidence.", "Cannot be called validated", ROSE),
    ]
    y = Inches(2.38)
    for head, body, rule, color in tiers:
        box(slide, Inches(0.55), y, Inches(2.42), Inches(0.84), color, radius=True)
        text(slide, Inches(0.71), y + Inches(0.20), Inches(2.10), Inches(0.20), head, size=9.2, color=WHITE, bold=True, margin=0.0)
        box(slide, Inches(3.15), y, Inches(4.38), Inches(0.84), WHITE, radius=True, line=GRID, line_width=0.7)
        text(slide, Inches(3.34), y + Inches(0.19), Inches(4.0), Inches(0.35), body, size=9.4, color=INK, margin=0.0)
        box(slide, Inches(7.70), y, Inches(4.95), Inches(0.84), PALE_PLUM if color == PLUM else SOFT, radius=True)
        text(slide, Inches(7.92), y + Inches(0.19), Inches(4.54), Inches(0.35), rule, size=9.4, color=PLUM_DARK, bold=True, margin=0.0)
        y += Inches(1.02)
    guardrails = [
        ("NO FABRICATED TIMESTAMPS", "Sequential transcript logs are not line-level timecodes."),
        ("NO FABRICATED RESPONDENTS", "Primary tracker count remains 0 unless independently recorded."),
        ("NO INVENTED UPLIFT", "Pilot metrics are proposed, not observed results."),
        ("NO H0–H5 SCORE", "Hypotheses remain open until primary research and transaction evidence."),
    ]
    y = Inches(2.42)
    for head, body in guardrails:
        box(slide, Inches(13.02), y, Inches(6.43), Inches(0.80), WHITE, radius=True, line=ORANGE, line_width=1.0)
        _mini_icon(slide, Inches(13.25), y + Inches(0.23), "!", ORANGE)
        text(slide, Inches(13.72), y + Inches(0.12), Inches(5.40), Inches(0.18), head, size=9.1, color=PLUM_DARK, bold=True, margin=0.0)
        text(slide, Inches(13.72), y + Inches(0.37), Inches(5.35), Inches(0.23), body, size=8.9, color=INK, margin=0.0)
        y += Inches(0.95)
    box(slide, Inches(13.02), Inches(6.44), Inches(6.43), Inches(1.28), PLUM_DARK, radius=True)
    text(slide, Inches(13.30), Inches(6.68), Inches(5.88), Inches(0.60), "Research position today:\nstrong creator-proof evidence, weak Meesho handoff evidence.", size=15, color=WHITE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    footer(slide, "Source files: DICE_GATE1_AUDIT_WORKBOOK.md, DICE_EVIDENCE_DATABASE.md, DICE_PRIMARY_RESEARCH_TRACKER.md.")


def _new_slide_5(slide):
    _wipe(slide)
    set_slide_bg(slide, CREAM)
    _brand_header(slide, "Creator proof is already decision-grade in many cases.", "APPENDIX | STREAM B")
    text(slide, Inches(0.55), Inches(1.38), Inches(18.2), Inches(0.30), "The audit weakens a generic “content difficulty” diagnosis. It strengthens the question: where does useful proof leak before purchase?", size=12.5, color=MUTED, margin=0.0)
    _metric_ribbon(slide, Inches(0.55), Inches(1.92), Inches(3.15), "26/28", "live product demonstrations", PLUM)
    _metric_ribbon(slide, Inches(3.88), Inches(1.92), Inches(3.15), "24/28", "suitability discussions", PINK)
    _metric_ribbon(slide, Inches(7.21), Inches(1.92), Inches(3.15), "22/28", "shade / colour fit", ORANGE)
    _metric_ribbon(slide, Inches(10.54), Inches(1.92), Inches(3.15), "23/28", "visible outcomes", CYAN)
    _metric_ribbon(slide, Inches(13.87), Inches(1.92), Inches(5.58), "0/28", "routed to Meesho in the public lead sample", ROSE)
    _section_bar(slide, Inches(0.55), Inches(2.87), Inches(12.45), "Evidence cards | observed content capability")
    examples = [
        ("CCA-006", "Shade warning", "Lakme Nude Twist washed out without base.", ORANGE),
        ("CCA-007", "Viral reality check", "Pillow Talk / cult products failed on Indian-skin fit or comfort.", PINK),
        ("CCA-010", "Budget quality split", "Zudio eyeliner worked; bullet lipsticks were grainy and dry.", OLIVE),
        ("CCA-023", "Suitability matching", "Dry-skin kit explains cream-vs-powder mechanics and oxidation.", CYAN),
        ("CCA-024", "Undertone proof", "Professional swatching across 15 shades makes fit legible.", PLUM),
        ("CCA-028", "Trust economics", "Fake virality and paid scripts expose review constraints.", ROSE),
    ]
    y = Inches(3.30)
    for eid, title, body, color in examples:
        _evidence_tag(slide, Inches(0.70), y + Inches(0.14), eid, color)
        box(slide, Inches(1.76), y, Inches(4.96), Inches(0.74), WHITE, radius=True, line=GRID, line_width=0.7)
        text(slide, Inches(1.96), y + Inches(0.12), Inches(4.55), Inches(0.18), title, size=10.4, color=PLUM_DARK, bold=True, margin=0.0)
        text(slide, Inches(1.96), y + Inches(0.36), Inches(4.50), Inches(0.22), body, size=8.7, color=INK, margin=0.0)
        y += Inches(0.83)
    _section_bar(slide, Inches(13.30), Inches(2.87), Inches(6.15), "What the audit does not prove", ROSE)
    gaps = [
        "No Meesho-specific conversion or attribution.",
        "No repeat purchase or creator earnings.",
        "No longitudinal skin outcome tracking.",
        "No line-level timestamps where caption stream lacked them.",
        "No evidence that proof is portable into a PDP.",
    ]
    y = Inches(3.33)
    for gap in gaps:
        _mini_icon(slide, Inches(13.46), y + Inches(0.02), "!", ROSE)
        text(slide, Inches(13.92), y, Inches(5.15), Inches(0.34), gap, size=10.0, color=INK, bold=True, margin=0.0)
        y += Inches(0.65)
    box(slide, Inches(13.34), Inches(6.84), Inches(6.02), Inches(1.07), PLUM_DARK, radius=True)
    text(slide, Inches(13.58), Inches(7.08), Inches(5.52), Inches(0.55), "The evidence changes the problem statement:\nnot content creation — proof transfer.", size=15.2, color=WHITE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    footer(slide, "Evidence tier: user-supplied manual audit layer. Counts are descriptive and do not establish transaction impact.")


def _new_slide_6(slide):
    _wipe(slide)
    set_slide_bg(slide, CREAM)
    _brand_header(slide, "Competitor benchmark: separate capability from verified journey.", "APPENDIX | STREAM C")
    text(slide, Inches(0.55), Inches(1.38), Inches(18.2), Inches(0.30), "The corrected record is more credible: one public-source capability, public artifacts, and pending flows—not five independently verified journeys.", size=12.5, color=MUTED, margin=0.0)
    _section_bar(slide, Inches(0.55), Inches(1.92), Inches(18.9), "Seven-stage flow audit")
    stages = ["DISCOVERY", "SELECTION", "INFO", "PROOF", "SHOPPING", "ATTRIBUTION", "EARNINGS"]
    x = Inches(0.55)
    for i, stage in enumerate(stages):
        _chevron(slide, x, Inches(2.38), Inches(2.69), stage, "stage " + str(i + 1), [PLUM, ORANGE, PINK, ROSE, CYAN, OLIVE, PLUM][i], active=(stage == "SHOPPING"))
        x += Inches(2.70)
    records = [
        ("COMP-FLOW-001", "YouTube Shopping", "PUBLIC-SOURCE EVIDENCED", "Official documentation supports a capability map; authenticated dashboards and replayed creator journey are not in workspace.", PLUM),
        ("COMP-001", "Myntra / creator program", "PUBLIC PROGRAM ARTIFACT", "Program existence is evidenced; full stage-by-stage conversion and earnings flow is not.", ORANGE),
        ("COMP-002 / 003", "Google partner announcement", "PUBLIC PARTNER ARTIFACT", "Partner access is evidenced; SKU selection, attribution and payout details remain unverified.", CYAN),
        ("COMP-004 / 005", "Amazon / Meta", "PENDING", "No complete workspace source record supporting all seven stages.", ROSE),
    ]
    y = Inches(3.25)
    for eid, name, status, limitation, color in records:
        _evidence_tag(slide, Inches(0.68), y + Inches(0.15), eid, color)
        box(slide, Inches(1.75), y, Inches(3.18), Inches(0.78), WHITE, radius=True, line=GRID, line_width=0.8)
        text(slide, Inches(1.94), y + Inches(0.18), Inches(2.80), Inches(0.30), name, size=10.3, color=PLUM_DARK, bold=True, margin=0.0)
        box(slide, Inches(5.12), y, Inches(3.10), Inches(0.78), PALE_CYAN if status != "PENDING" else SOFT, radius=True)
        text(slide, Inches(5.30), y + Inches(0.18), Inches(2.74), Inches(0.30), status, size=8.5, color=PLUM_DARK, bold=True, align=PP_ALIGN.CENTER, margin=0.0)
        box(slide, Inches(8.42), y, Inches(10.90), Inches(0.78), WHITE, radius=True, line=GRID, line_width=0.8)
        text(slide, Inches(8.64), y + Inches(0.15), Inches(10.45), Inches(0.38), limitation, size=9.4, color=INK, margin=0.0)
        y += Inches(0.91)
    box(slide, Inches(0.55), Inches(7.17), Inches(18.9), Inches(1.05), PLUM_DARK, radius=True)
    text(slide, Inches(0.85), Inches(7.42), Inches(18.3), Inches(0.48), "Benchmark implication  →  Meesho does not need to copy every competitor feature. It needs a measurable proof-to-commerce bridge, then the interaction data to decide what to build next.", size=14.3, color=WHITE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    footer(slide, "Stream C status: 1 public-source capability record; 3 public artifacts; 2 pending. Authenticated/private claims are not independently verifiable here.")


def _new_slide_7(slide):
    _wipe(slide)
    set_slide_bg(slide, CREAM)
    _brand_header(slide, "H0–H5 remain open; the research now tells us what to test.", "APPENDIX | HYPOTHESIS STATUS")
    text(slide, Inches(0.55), Inches(1.38), Inches(18.2), Inches(0.30), "We do not score hypotheses from descriptive creator content alone. We preserve the contradictions and define the next evidence needed.", size=12.5, color=MUTED, margin=0.0)
    _section_bar(slide, Inches(0.55), Inches(1.92), Inches(18.9), "Evidence / contradiction / next test")
    headers = ["HYPOTHESIS", "SUPPORTING SIGNAL", "CONTRADICTION / LIMIT", "NEXT TEST", "STATUS"]
    widths = [2.05, 4.38, 4.35, 5.35, 2.42]
    x0, y0 = Inches(0.55), Inches(2.38)
    xx = x0
    for h, w in zip(headers, widths):
        box(slide, xx, y0, Inches(w), Inches(0.42), PLUM_DARK, radius=False)
        text(slide, xx + Inches(0.05), y0 + Inches(0.10), Inches(w - 0.10), Inches(0.20), h, size=8.1, color=WHITE, bold=True, align=PP_ALIGN.CENTER, margin=0.0)
        xx += Inches(w)
    rows = [
        ("H0 | quality / trust", "Defects, viral mismatch and PR pressure appear in creator audits.", "Public content cannot size return or authenticity impact.", "Seller + shopper interviews; returns / ratings pilot.", "OPEN", ROSE),
        ("H1 | creator-SKU fit", "Professional creators can make undertone and suitability legible.", "This may be true only for specialist formats.", "Creator interview: matching, selection and effort.", "OPEN", PINK),
        ("H2 | sampling", "PR volume and waste are directly visible.", "Gifting may create bias and uneconomic effort.", "Seller economics + targeted sample test.", "OPEN", ORANGE),
        ("H3 | proof difficulty", "26/28 demos; 24/28 suitability discussions.", "Proof quality does not prove transaction transfer.", "Shopper test: which fields change confidence/click.", "CHALLENGED", CYAN),
        ("H4 | decision support", "Shade, texture and outcome proof recur across audits.", "No Meesho PDP / conversion evidence.", "Treatment vs control proof handoff.", "OPEN", OLIVE),
        ("H5 | creator economics", "Affiliate codes, PR pressure and platform commissions observed.", "Earnings and conversion logs are absent.", "Creator interviews + attributed pilot earnings.", "OPEN", PLUM),
    ]
    y = Inches(2.85)
    for hyp, support, contra, test, status, color in rows:
        xx = x0
        vals = [hyp, support, contra, test, status]
        for idx, (val, w) in enumerate(zip(vals, widths)):
            fill = PALE_CYAN if status == "CHALLENGED" else WHITE
            box(slide, xx, y, Inches(w), Inches(0.74), fill, radius=False, line=GRID, line_width=0.8)
            text(slide, xx + Inches(0.08), y + Inches(0.12), Inches(w - 0.16), Inches(0.48), val, size=8.6 if idx else 9.2, color=PLUM_DARK if idx == 0 else INK, bold=(idx == 0 or idx == 4), align=PP_ALIGN.CENTER if idx == 4 else PP_ALIGN.LEFT, valign=MSO_ANCHOR.MIDDLE, margin=0.0)
            xx += Inches(w)
        y += Inches(0.78)
    box(slide, Inches(0.55), Inches(7.72), Inches(18.9), Inches(0.68), SOFT, radius=True)
    text(slide, Inches(0.82), Inches(7.91), Inches(18.35), Inches(0.30), "Important: H3 is challenged by creator evidence; the winning case must now locate the leak after proof, not assume proof is absent.", size=13.6, color=PLUM_DARK, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    footer(slide, "No hypothesis has been statistically scored or declared validated.")


def _new_slide_8(slide):
    _wipe(slide)
    set_slide_bg(slide, CREAM)
    _brand_header(slide, "The long-term moat is a learning loop, not a sample box.", "APPENDIX | FUTURE ENGINE")
    text(slide, Inches(0.55), Inches(1.38), Inches(18.2), Inches(0.30), "The wedge is intentionally small. Its output is the interaction data required for Creator x SKU x Audience allocation.", size=12.5, color=MUTED, margin=0.0)
    _section_bar(slide, Inches(0.55), Inches(1.92), Inches(18.9), "Decision engine wireframe")
    # Left: inputs
    _section_bar(slide, Inches(0.72), Inches(2.36), Inches(4.20), "Inputs", ORANGE)
    inputs = [
        ("CREATOR", "audience / credibility / effort"),
        ("SKU", "category / margin / authenticity"),
        ("AUDIENCE", "concern / budget / context"),
        ("PROOF", "shade / texture / outcome / caveat"),
    ]
    y = Inches(2.82)
    for head, body in inputs:
        _dense_card(slide, Inches(0.72), y, Inches(4.20), Inches(0.68), head, body, ORANGE)
        y += Inches(0.78)
    # Center: bridge
    box(slide, Inches(5.42), Inches(2.36), Inches(8.42), Inches(4.36), PLUM_DARK, radius=True)
    text(slide, Inches(5.78), Inches(2.69), Inches(7.75), Inches(0.23), "BEAUTY PROOF BRIDGE", size=14, color=ORANGE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    nodes = [
        ("MATCH", "relevant creator ↔ SKU"),
        ("CAPTURE", "structured proof fields"),
        ("SURFACE", "contextual Meesho decision point"),
        ("ATTRIBUTE", "creator / SKU / audience IDs"),
        ("LEARN", "click, order, return, repeat, payout"),
    ]
    y = Inches(3.25)
    for i, (head, body) in enumerate(nodes):
        color = [PINK, CYAN, ORANGE, OLIVE, ROSE][i]
        box(slide, Inches(6.20), y, Inches(6.85), Inches(0.55), color, radius=True)
        text(slide, Inches(6.38), y + Inches(0.10), Inches(1.15), Inches(0.18), head, size=9.0, color=PLUM_DARK if color in [ORANGE, OLIVE] else WHITE, bold=True, margin=0.0)
        text(slide, Inches(7.58), y + Inches(0.10), Inches(5.20), Inches(0.18), body, size=9.2, color=PLUM_DARK if color in [ORANGE, OLIVE] else WHITE, bold=True, margin=0.0)
        if i < len(nodes) - 1:
            arrow(slide, Inches(9.62), y + Inches(0.55), Inches(9.62), y + Inches(0.75), ORANGE, 1.2)
        y += Inches(0.70)
    # Right: outputs
    _section_bar(slide, Inches(14.18), Inches(2.36), Inches(5.10), "Outputs", CYAN)
    outputs = [
        ("SHOPPER", "faster fit decision"),
        ("SELLER", "better SKU demand signal"),
        ("CREATOR", "clearer attribution + payout"),
        ("MEESHO", "better allocation data"),
    ]
    y = Inches(2.82)
    for head, body in outputs:
        _dense_card(slide, Inches(14.18), y, Inches(5.10), Inches(0.78), head, body, CYAN)
        y += Inches(0.88)
    box(slide, Inches(0.72), Inches(7.18), Inches(18.56), Inches(0.87), SOFT, radius=True)
    text(slide, Inches(1.00), Inches(7.43), Inches(18.0), Inches(0.30), "Do not build the engine first. Build the first data-generating wedge that earns the right to build it.", size=15.0, color=PLUM_DARK, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    footer(slide, "Future-state architecture; not a claim that Meesho currently has these matching signals.")


def _new_slide_9(slide):
    _wipe(slide)
    set_slide_bg(slide, CREAM)
    _brand_header(slide, "Measurement turns the idea into a business case.", "APPENDIX | PILOT ECONOMICS")
    text(slide, Inches(0.55), Inches(1.38), Inches(18.2), Inches(0.30), "We will size the opportunity from observed pilot deltas—not invented market-response percentages.", size=12.5, color=MUTED, margin=0.0)
    box(slide, Inches(0.55), Inches(1.92), Inches(18.9), Inches(0.76), PLUM_DARK, radius=True)
    text(slide, Inches(0.83), Inches(2.16), Inches(18.35), Inches(0.27), "BPC NMV = active creators × relevant proof × click-through × PDP-to-order × AOV × repeat", size=18, color=WHITE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    _section_bar(slide, Inches(0.55), Inches(3.05), Inches(9.15), "Measurement stack")
    _section_bar(slide, Inches(10.05), Inches(3.05), Inches(9.40), "What becomes knowable")
    drivers = [
        ("ACTIVE CREATORS", "sample-to-post\nretention"),
        ("RELEVANT PROOF", "completeness\nusefulness"),
        ("CLICK-THROUGH", "placement\nCTA quality"),
        ("CONVERSION", "fit confidence\nPDP support"),
        ("REPEAT", "quality\nreturns / reorder"),
    ]
    x = Inches(0.55)
    for head, body in drivers:
        box(slide, x, Inches(3.51), Inches(1.75), Inches(1.18), WHITE, radius=True, line=PLUM, line_width=1.1)
        text(slide, x + Inches(0.10), Inches(3.68), Inches(1.55), Inches(0.25), head, size=7.2, color=PLUM_DARK, bold=True, align=PP_ALIGN.CENTER, margin=0.0)
        text(slide, x + Inches(0.16), Inches(4.10), Inches(1.42), Inches(0.43), body, size=10.5, color=INK, bold=True, align=PP_ALIGN.CENTER, margin=0.0)
        x += Inches(1.82)
    bullets(slide, Inches(0.72), Inches(5.05), Inches(8.6), Inches(2.0), [
        "Unique creator / SKU / audience / treatment IDs.",
        "Tagged click, PDP, order and return events.",
        "Sample cost, creator time and payout.",
        "Rating, defect and repeat cohort.",
    ], size=12)
    know = [
        ("Which proof fields correlate with clicks and orders?", CYAN),
        ("Which creators produce efficient, credible proof?", PINK),
        ("Do targeted samples beat broad gifting?", ORANGE),
        ("Does the bridge deserve scale or a kill?", OLIVE),
    ]
    y = Inches(3.58)
    for label, color in know:
        box(slide, Inches(10.05), y, Inches(9.40), Inches(0.66), WHITE, radius=True, line=color, line_width=1.0)
        _mini_icon(slide, Inches(10.28), y + Inches(0.17), "→", color)
        text(slide, Inches(10.78), y + Inches(0.16), Inches(8.25), Inches(0.26), label, size=10.6, color=INK, bold=True, margin=0.0)
        y += Inches(0.80)
    box(slide, Inches(10.05), Inches(6.88), Inches(9.40), Inches(0.88), PLUM_DARK, radius=True)
    text(slide, Inches(10.28), Inches(7.11), Inches(8.95), Inches(0.33), "No uplift is claimed. The pilot is the mechanism for generating defensible uplift.", size=13.2, color=WHITE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    footer(slide, "Illustrative measurement model only. No conversion, NMV, repeat or retention result is claimed.")


def _new_slide_10(slide):
    _wipe(slide)
    set_slide_bg(slide, CREAM)
    _brand_header(slide, "A credible case makes disproof visible.", "APPENDIX | RISKS + ROADMAP")
    text(slide, Inches(0.55), Inches(1.38), Inches(18.2), Inches(0.30), "The bridge is only a winner if it survives creator, shopper, seller and economics reality.", size=12.5, color=MUTED, margin=0.0)
    _section_bar(slide, Inches(0.55), Inches(1.92), Inches(10.05), "Kill criteria")
    risks = [
        ("Proof does not move orders", "Kill or redesign; investigate price, quality, delivery and PDP UX.", ROSE),
        ("Creators reject effort", "Shift toward economics, lighter formats or better matching.", PINK),
        ("Sampling is uneconomic", "Narrow SKU set; require seller co-funding or repeat potential.", ORANGE),
        ("PDP cannot carry proof", "Use a landing/storefront surface while integration is built.", CYAN),
        ("Quality dominates returns", "Move trust / authenticity to the front of the roadmap.", OLIVE),
    ]
    y = Inches(2.39)
    for head, body, color in risks:
        box(slide, Inches(0.55), y, Inches(10.05), Inches(0.70), WHITE, radius=True, line=color, line_width=1.0)
        pill(slide, Inches(0.76), y + Inches(0.18), Inches(2.42), head.upper(), color, size=7.7)
        text(slide, Inches(3.45), y + Inches(0.17), Inches(6.75), Inches(0.27), body, size=10.1, color=INK, bold=True, margin=0.0)
        y += Inches(0.80)
    _section_bar(slide, Inches(10.95), Inches(1.92), Inches(8.50), "Scale path", PLUM_DARK)
    roadmap = [
        ("30 DAYS", "Pilot bridge; instrument the full handoff.", CYAN),
        ("60 DAYS", "Add reusable proof fields and seller reporting.", PINK),
        ("90 DAYS", "Use interaction data to rank creator–SKU–audience matches.", ORANGE),
    ]
    y = Inches(2.42)
    for head, body, color in roadmap:
        box(slide, Inches(11.12), y, Inches(8.16), Inches(1.06), WHITE, radius=True, line=color, line_width=1.2)
        pill(slide, Inches(11.36), y + Inches(0.33), Inches(1.42), head, color, size=8.0)
        text(slide, Inches(13.05), y + Inches(0.26), Inches(5.95), Inches(0.38), body, size=11.0, color=INK, bold=True, margin=0.0)
        y += Inches(1.20)
    box(slide, Inches(11.12), Inches(6.38), Inches(8.16), Inches(1.06), PLUM_DARK, radius=True)
    text(slide, Inches(11.40), Inches(6.64), Inches(7.60), Inches(0.50), "North star:\nmore BPC NMV from better proof transfer.", size=15.1, color=WHITE, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    box(slide, Inches(0.55), Inches(7.73), Inches(10.05), Inches(0.70), SOFT, radius=True)
    text(slide, Inches(0.80), Inches(7.95), Inches(9.55), Inches(0.28), "Research next: creators + shoppers + sellers before scale.", size=13.4, color=PLUM_DARK, bold=True, font=FONT_HEAD, align=PP_ALIGN.CENTER, margin=0.0)
    footer(slide, "Team: Samiksha Mitra | Slayed it | IIT Guwahati | Full source ledger remains in the workspace.")


def build_deck() -> None:
    prs = Presentation(str(TEMPLATE))
    slides = list(prs.slides)
    from render_dice_visual_boards import render as render_visual_boards

    board_paths = render_visual_boards()
    for index, (path, slide) in enumerate(zip(board_paths[:5], slides), 1):
        _wipe(slide)
        slide.shapes.add_picture(str(path), 0, 0, width=W, height=H)
        add_source_hotspots(slide, index)
    blank_layout = prs.slide_layouts[6]
    for index, path in enumerate(board_paths[5:], 6):
        slide = prs.slides.add_slide(blank_layout)
        _wipe(slide)
        slide.shapes.add_picture(str(path), 0, 0, width=W, height=H)
        add_source_hotspots(slide, index)
    prs.save(str(OUTPUT))


if __name__ == "__main__":
    build_deck()
