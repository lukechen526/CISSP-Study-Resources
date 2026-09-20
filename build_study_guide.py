from pathlib import Path
import html
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    Table, TableStyle, HRFlowable
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output" / "pdf" / "CISSP-Study-Guide-2024.pdf"
FILES = sorted(ROOT.glob("CISSP-Domain-*-2024+Objectives.md"), key=lambda p: int(re.search(r"Domain-(\d+)", p.name).group(1)))

NAVY = colors.HexColor("#17324D")
BLUE = colors.HexColor("#2F6F9F")
TEAL = colors.HexColor("#2F8F9D")
INK = colors.HexColor("#263238")
MUTED = colors.HexColor("#667781")
PALE = colors.HexColor("#F1F6F9")
LINE = colors.HexColor("#D9E3EA")


def clean_text(text):
    replacements = {
        "\u2011": "-", "\u2013": "-", "\u2014": "-", "\u2212": "-",
        "\u00a0": " ", "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
        "\u2026": "...", "\u2192": "->", "\u2260": "!=", "\u2265": ">=", "\u2264": "<=",
    }
    for a, b in replacements.items():
        text = text.replace(a, b)
    return text


def inline_markup(text):
    text = clean_text(text.strip())
    # Remove markdown image syntax, preserving alt text.
    text = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", text)
    # Render links as readable linked text.
    text = re.sub(r"\[([^]]+)\]\(([^)]+)\)", r'<link href="\2" color="#2F6F9F">\1</link>', text)
    text = re.sub(r"<((?:https?://)[^>]+)>", r'<link href="\1" color="#2F6F9F">\1</link>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"__([^_]+)__", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", text)
    text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)
    return text


def parse_file(path):
    lines = [clean_text(x.rstrip()) for x in path.read_text(encoding="utf-8").splitlines()]
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("# "):
            blocks.append(("h1", line[2:].strip()))
            i += 1
            continue
        if line.startswith("## "):
            blocks.append(("h2", line[3:].strip()))
            i += 1
            continue
        if line.startswith("### "):
            blocks.append(("h3", line[4:].strip()))
            i += 1
            continue
        if re.match(r"^\s*[-*] ", line):
            items = []
            while i < len(lines) and (re.match(r"^\s*[-*] ", lines[i]) or re.match(r"^\s+[-*] ", lines[i])):
                m = re.match(r"^(\s*)[-*] (.*)$", lines[i])
                if not m:
                    break
                items.append((len(m.group(1)) // 2, m.group(2)))
                i += 1
            blocks.append(("list", items))
            continue
        # A numbered list is common in the source notes.
        if re.match(r"^\s*\d+[.)] ", line):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+[.)] ", lines[i]):
                m = re.match(r"^(\s*)\d+[.)] (.*)$", lines[i])
                items.append((len(m.group(1)) // 2, m.group(2)))
                i += 1
            blocks.append(("olist", items))
            continue
        # Join wrapped prose lines into one paragraph, stopping at a structural line.
        para = [line.strip()]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,3}) |^\s*[-*] |^\s*\d+[.)] ", lines[i]):
            para.append(lines[i].strip())
            i += 1
        blocks.append(("p", " ".join(para)))
    return blocks


class GuideDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        super().__init__(filename, **kwargs)
        self._content_started = False
        self._bookmark_counter = 0
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="normal")
        self.addPageTemplates([PageTemplate(id="guide", frames=frame, onPage=draw_page)])

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        style = flowable.style.name
        if style == "DomainTitle":
            self._content_started = True
            level = 0
        elif self._content_started and style == "SectionHeading":
            level = 1
        elif self._content_started and style == "Subheading":
            level = 2
        else:
            return
        self._bookmark_counter += 1
        title = flowable.getPlainText()
        key = f"guide-heading-{self._bookmark_counter}"
        self.canv.bookmarkPage(key)
        self.canv.addOutlineEntry(title, key, level=level, closed=False)
        self.notify("TOCEntry", (level, title, self.page))


def draw_page(canvas, doc):
    canvas.saveState()
    w, h = letter
    if doc.page > 1:
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(doc.leftMargin, h - 0.52 * inch, w - doc.rightMargin, h - 0.52 * inch)
        canvas.setFont("Helvetica-Bold", 8)
        canvas.setFillColor(NAVY)
        canvas.drawString(doc.leftMargin, h - 0.38 * inch, "CISSP STUDY GUIDE")
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(MUTED)
        canvas.drawRightString(w - doc.rightMargin, h - 0.38 * inch, "2024 Exam Objectives")
        canvas.line(doc.leftMargin, 0.47 * inch, w - doc.rightMargin, 0.47 * inch)
        canvas.setFont("Helvetica", 8)
        canvas.drawString(doc.leftMargin, 0.29 * inch, "Study notes compiled from the current domain files")
        canvas.drawRightString(w - doc.rightMargin, 0.29 * inch, f"{doc.page}")
    canvas.restoreState()


def bullet_flow(items, styles, ordered=False):
    flow = []
    for idx, (level, text) in enumerate(items, 1):
        level = min(level, 3)
        prefix = f"{idx}." if ordered and level == 0 else "•"
        style = styles["GuideBullet"] if level == 0 else styles["GuideBulletNested"]
        flow.append(Paragraph(f'<font color="#2F8F9D">{prefix}</font> {inline_markup(text)}', style))
    return flow


def build():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=29, leading=34, textColor=NAVY, alignment=TA_LEFT, spaceAfter=14))
    styles.add(ParagraphStyle(name="CoverSub", parent=styles["Normal"], fontName="Helvetica", fontSize=13, leading=18, textColor=MUTED, spaceAfter=8))
    styles.add(ParagraphStyle(name="CoverSection", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=BLUE, spaceBefore=14, spaceAfter=6, keepWithNext=True))
    styles.add(ParagraphStyle(name="DomainTitle", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=22, leading=27, textColor=NAVY, spaceBefore=5, spaceAfter=12, keepWithNext=True))
    styles.add(ParagraphStyle(name="SectionHeading", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=BLUE, spaceBefore=14, spaceAfter=6, keepWithNext=True))
    styles.add(ParagraphStyle(name="Subheading", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=11.5, leading=15, textColor=TEAL, spaceBefore=9, spaceAfter=4, keepWithNext=True))
    styles.add(ParagraphStyle(name="BodyGuide", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.2, leading=13.2, textColor=INK, spaceAfter=6, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name="GuideBullet", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.0, leading=12.8, leftIndent=14, firstLineIndent=-10, textColor=INK, spaceAfter=2))
    styles.add(ParagraphStyle(name="GuideBulletNested", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.7, leading=12.2, leftIndent=29, firstLineIndent=-10, textColor=INK, spaceAfter=1))
    styles.add(ParagraphStyle(name="TOCHeading", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=20, textColor=NAVY, spaceAfter=12))
    styles.add(ParagraphStyle(name="TOC0", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=11, leading=17, leftIndent=0, rightIndent=28, textColor=NAVY))
    styles.add(ParagraphStyle(name="TOC1", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5, leading=15, leftIndent=16, rightIndent=28, textColor=INK))
    styles.add(ParagraphStyle(name="TOC2", parent=styles["Normal"], fontName="Helvetica", fontSize=8.5, leading=13, leftIndent=32, rightIndent=28, textColor=MUTED))

    doc = GuideDocTemplate(str(OUT), pagesize=letter, leftMargin=0.72*inch, rightMargin=0.72*inch, topMargin=0.72*inch, bottomMargin=0.68*inch, title="CISSP Study Guide 2024", author="OpenAI")
    story = []
    story += [Spacer(1, 0.9*inch), Paragraph("CISSP Study Guide", styles["CoverTitle"]), Paragraph("2024 Exam Objectives", styles["CoverSub"]), Spacer(1, 0.18*inch), HRFlowable(width="100%", thickness=2, color=TEAL), Spacer(1, 0.24*inch)]
    story += [Paragraph("A coherent, reader-friendly compilation of the eight CISSP domains.", styles["CoverSub"]), Spacer(1, 0.15*inch)]
    story += [Paragraph("How to use this guide", styles["CoverSection"]), Paragraph("Read each domain from start to finish, then return to the bold definitions and objective headings for rapid review. Links in the source notes are preserved where useful.", styles["BodyGuide"]), Spacer(1, 0.3*inch)]
    domain_rows = [[Paragraph("Domain", styles["TOC0"]), Paragraph("Focus", styles["TOC0"]), Paragraph("Weight", styles["TOC0"])]]
    for p in FILES:
        blocks = parse_file(p)
        first = next((b[1] for b in blocks if b[0] == "h1"), p.stem)
        focus = re.sub(r"^\[Domain-\d+\]\(#.*?\)\s*", "", first)
        m = re.search(r"(\d+)%", " ".join(str(b[1]) for b in blocks)[:1200])
        domain_rows.append([Paragraph(f"Domain {re.search(r'Domain-(\d+)', p.name).group(1)}", styles["BodyGuide"]), Paragraph(inline_markup(focus), styles["BodyGuide"]), Paragraph((m.group(1)+"%") if m else "-", styles["BodyGuide"])])
    t = Table(domain_rows, colWidths=[0.95*inch, 4.55*inch, 0.75*inch], repeatRows=1)
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,0), PALE), ("TEXTCOLOR", (0,0), (-1,0), NAVY), ("GRID", (0,0), (-1,-1), 0.4, LINE), ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7), ("TOPPADDING", (0,0), (-1,-1), 6), ("BOTTOMPADDING", (0,0), (-1,-1), 6)]))
    toc = TableOfContents()
    toc.levelStyles = [styles["TOC0"], styles["TOC1"], styles["TOC2"]]
    toc.dotsMinLevel = 0
    story += [t, PageBreak(), Paragraph("Contents", styles["TOCHeading"]), Spacer(1, 0.05*inch), toc]
    story.append(PageBreak())

    for file_index, p in enumerate(FILES):
        blocks = parse_file(p)
        for kind, value in blocks:
            if kind == "h1":
                title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
                story.append(Paragraph(inline_markup(title), styles["DomainTitle"]))
                story.append(HRFlowable(width="100%", thickness=1.5, color=TEAL, spaceAfter=10))
            elif kind == "h2":
                title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
                story.append(Paragraph(inline_markup(title), styles["SectionHeading"]))
            elif kind == "h3":
                title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
                story.append(Paragraph(inline_markup(title), styles["Subheading"]))
            elif kind == "p":
                story.append(Paragraph(inline_markup(value), styles["BodyGuide"]))
            elif kind == "list":
                story.extend(bullet_flow(value, styles, ordered=False))
            elif kind == "olist":
                story.extend(bullet_flow(value, styles, ordered=True))
        if file_index < len(FILES) - 1:
            story.append(PageBreak())
    doc.multiBuild(story)
    print(OUT)


if __name__ == "__main__":
    build()
