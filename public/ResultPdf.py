import csv
import datetime
from reportlab.lib.units import cm, inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
def sendPdf(data,info,prn):
    elements = []

    # PDF Text
    # PDF Text - Styles
    styles = getSampleStyleSheet()
    styleNormal = styles['Normal']

    # PDF Text - Content
    line1 = 'Name : '+str(info[0][0])
    line3 = 'Prn Number : '+str(prn)
    line4 = 'College Name : '+str(info[0][2])
    line5 = 'Branch : '+str(info[0][1])
    line6 = 'Semester : '+str(info[0][3])

    elements.append(Paragraph(line1, styleNormal))
    elements.append(Paragraph(line3, styleNormal))
    elements.append(Paragraph(line4, styleNormal))
    elements.append(Paragraph(line5, styleNormal))
    elements.append(Paragraph(line6, styleNormal))
    elements.append(Spacer(inch, .25 * inch))

    # PDF Table
    # PDF Table - Styles
    # [(start_column, start_row), (end_column, end_row)]
    all_cells = [(0, 0), (-1, -1)]
    header = [(0, 0), (-1, 0)]
    column0 = [(0, 0), (0, -1)]
    column1 = [(1, 0), (1, -1)]
    column2 = [(2, 0), (2, -1)]
    column3 = [(3, 0), (3, -1)]
    column4 = [(4, 0), (4, -1)]
    column5 = [(5, 0), (5, -1)]
    column6 = [(6, 0), (6, -1)]
    table_style = TableStyle([
        ('VALIGN', all_cells[0], all_cells[1], 'TOP'),
        ('LINEBELOW', header[0], header[1], 1, colors.black),
        ('ALIGN', column0[0], column0[1], 'LEFT'),
        ('ALIGN', column1[0], column1[1], 'LEFT'),
        ('ALIGN', column2[0], column2[1], 'LEFT'),
        ('ALIGN', column3[0], column3[1], 'RIGHT'),
        ('ALIGN', column4[0], column4[1], 'RIGHT'),
        ('ALIGN', column5[0], column5[1], 'LEFT'),
        ('ALIGN', column6[0], column6[1], 'RIGHT'),
    ])

    # PDF Table - Column Widths
    colWidths = [
        2.5 * cm,  # Column 0
        2.5 * cm,  # Column 1
        2.5 * cm,  # Column 2
        2.5 * cm,  # Column 3
        5.5 * cm,  # Column 4
        2.5 * cm,  # Column 5
        2.5 * cm,  # Column 6
    ]

    # PDF Table - Strip '[]() and add word wrap to column 5
    for index, row in enumerate(data):
        for col, val in enumerate(row):
            # print(val,type(val))
            val = str(val)
            if col != 5 or index == 0:
                data[index][col] = val
            else:
                data[index][col] = Paragraph(val, styles['Normal'])

    # Add table to elements
    t = Table(data, colWidths=colWidths)
    t.setStyle(table_style)
    elements.append(t)

    # Generate PDF
    archivo_pdf = SimpleDocTemplate(
        'Report Card.pdf',
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=28)
    archivo_pdf.build(elements)
    print('Report Card Generated!')
    import os
    return os.path.join('','Report Card.pdf')
if __name__ == '__main__':
    with open('smsInfo.csv', "r") as csvfile:
        data = list(csv.reader(csvfile))
    print(sendPdf(data))