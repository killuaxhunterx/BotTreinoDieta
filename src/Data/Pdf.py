from fpdf import FPDF

class Pdf:

    def gerarPdf(content: str) -> None:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size=12)
        pdf.multi_cell(0, 5, txt=content)
        pdf.output("treinoDieta.pdf")