from pdfminer.high_level import extract_text

class PDFToTextAdapter:
    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path

    def extract_text(self):
        # Extrai o texto do PDF
        text = extract_text(self.pdf_file_path)
        return text
