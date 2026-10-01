from fpdf import FPDF

name = input("Name:")
pdf = FPDF()
pdf.add_page()
pdf.set_margins(0,0)
pdf.set_font("helvetica", "B", size = 30)
pdf.cell(w = 0, h = 60, txt = "CS50 Shirtificate", border = 0, align = "C")
pdf.image("shirtificate.png", x = 15, y = 75, w = 180)
pdf.ln(100)
pdf.set_text_color(255,255,255)
pdf.set_font("helvetica", "U", size = 30)
pdf.cell(w = 210, h = 45, txt = f"{name} took CS50", align = "C")
pdf.output("shirtificate.pdf")


