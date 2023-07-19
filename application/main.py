from domain.entities.contract import Contract
from domain.services.ner import NERService
from infrastructure.adapters.pdf_to_text import PDFToTextAdapter

def main():
    # Inicialize o adaptador com o caminho para o arquivo PDF
    pdf_adapter = PDFToTextAdapter('example.pdf')
    # Extraia o texto do PDF
    text = pdf_adapter.extract_text()

    # Inicialize o serviço NER com o caminho para o modelo pré-treinado
    ner_service = NERService('ner_model')
    # Identifique os campos no texto
    fields = ner_service.identify_fields(text)

    # Crie uma nova entidade Contrato com os campos identificados
    contract = Contract(**fields)

    # Aqui você pode fazer algo com a entidade Contrato, como salvar em um banco de dados
