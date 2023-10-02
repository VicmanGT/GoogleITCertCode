#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSamplesStylesSheet

def generate_report(filename,paragraph, title):
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_paragragh = Paragraph(paragraph, styles["h2"])
  report.build([report_title, report_paragragh])
