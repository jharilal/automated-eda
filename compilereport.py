from fpdf import FPDF

pdf = FPDF('P', 'mm' ,'A4')

pdf.add_page()
pdf.set_font('times', '', 12)
pdf.cell(40, 10, 'Automate EDA', ln=True)
pdf.cell(50, 10, 'Jordan Harilal')
pdf.output('reports/test.pdf')