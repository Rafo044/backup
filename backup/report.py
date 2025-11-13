"""This module contains functions for generating disaster recovery reports."""

import json
import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

with open("pgbackrest_info.json", "r") as f:
    data_list = json.load(f)


data = data_list[0]


stanza_name = data["name"]
pg_version = data["db"][0]["version"] if data["db"] else None
system_id = data["db"][0]["system-id"] if data["db"] else None

if data["backup"]:
    last_backup = data["backup"][-1]  # son backup
    last_backup_label = last_backup["label"]
    backup_type = last_backup["type"]
    backup_start_ts = last_backup["timestamp"]["start"]
    backup_stop_ts = last_backup["timestamp"]["stop"]
    backup_size = last_backup["info"]["size"]
else:
    last_backup_label = backup_type = backup_start_ts = backup_stop_ts = backup_size = (
        None
    )
backup_duration = (backup_stop_ts - backup_start_ts).total_seconds() / 60
now = datetime.now()
rpo = (now - backup_stop_ts).total_seconds() / 60

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
