from fpdf import FPDF

class Pdf:

    def gerarPdf(content: str) -> None:
        pdf = FPDF()
        try:
            pdf.add_page()
            pdf.set_font('Arial', size=12)
            pdf.multi_cell(0, 5, txt=content)
            pdf.output("treinoDieta.pdf")
        except Exception as e:
            print(f"Erro em gerar pdf: {e}")