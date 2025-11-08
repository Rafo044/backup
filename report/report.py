import os
from datetime import datetime

from dotenv import load_dotenv
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

load_dotenv()

pdfmetrics.registerFont(
    TTFont("DejaVuSans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
)


doc = SimpleDocTemplate("DReport.pdf", pagesize=A4)
elements = []
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    "TitleStyle",
    parent=styles["Heading1"],
    fontName="DejaVuSans",
    fontSize=20,
    leading=24,
    alignment=1,
    textColor=colors.darkblue,
    spaceAfter=20,
)
subtitle_style = ParagraphStyle(
    "SubtitleStyle",
    parent=styles["Heading2"],
    fontName="DejaVuSans",
    textColor=colors.darkred,
    spaceAfter=10,
)
body_style = ParagraphStyle(
    "BodyStyle",
    parent=styles["BodyText"],
    fontName="DejaVuSans",
    fontSize=11,
    leading=15,
    spaceAfter=6,
)

report_date = datetime.now().strftime("%Y-%m-%d %H:%M")
rto = os.getenv("RTO")
rpo = os.getenv("RPO")
incident = os.getenv("INCIDENT")
impact = os.getenv("IMPACT")
recovery_steps = [
    "Zəmanətli ehtiyat nüsxə bərpası başladı",
    "Database cluster yenidən işə salındı",
    "Məlumatların integrasiyası yoxlanıldı",
    "Monitorinq sistemi ilə nəticə təsdiqləndi",
]

elements.append(Paragraph("Disaster Recovery Report", title_style))
elements.append(Paragraph(f"Hesabat tarixi: {report_date}", body_style))
elements.append(Spacer(1, 12))

data = [
    ["Hadisə", incident],
    ["Təsir səviyyəsi", impact],
    ["RTO", rto],
    ["RPO", rpo],
]

table = Table(data, colWidths=[120, 360])
table.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("FONTNAME", (0, 0), (-1, -1), "DejaVuSans"),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("FONTNAME", (0, 0), (-1, 0), "DejaVuSans"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
        ]
    )
)
elements.append(table)
elements.append(Spacer(1, 20))

# === Bərpa addımları ===
elements.append(Paragraph("Bərpa Addımları", subtitle_style))
for step in recovery_steps:
    elements.append(Paragraph(f"• {step}", body_style))
elements.append(Spacer(1, 20))

# === Qeyd ===
elements.append(
    Paragraph(
        "Bu hesabat avtomatik olaraq sistem tərəfindən yaradılmışdır.", body_style
    )
)

# === PDF faylı yaradılır ===
doc.build(elements)
print(" 'DRecovery.pdf' faylı uğurla yaradıldı.")
