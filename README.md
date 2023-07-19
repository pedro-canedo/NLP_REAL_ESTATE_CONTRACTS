# Contract Extraction System (Sistema de Extração de Contratos)

This project is an application for extracting contract information from PDF documents using a Named Entity Recognition (NER) model.
(Este projeto é um aplicativo para extração de informações de contratos em documentos PDF, utilizando um modelo de Reconhecimento de Entidades Nomeadas (NER).)

## Requirements (Requisitos)

- Python 3.8+
- Pip (Python package manager)
  (Pip (gerenciador de pacotes Python))

## Installation (Instalação)

1. Clone the repository: (Clone o repositório:)
   ```
   https://github.com/pedro-canedo/NLP_REAL_ESTATE_CONTRACTS.git
   ```
2. Create and activate a virtual environment (recommended): (Crie e ative um ambiente virtual (recomendado):)

   ```
   python -m venv venv
   venv\Scripts\activate (Windows)
   source venv/bin/activate (Linux)
   ```

3. Install the dependencies: (Instale as dependências:)
   ```
   pip install -r requirements.txt
   ```

## Model Preparation (Preparação do Modelo)

The system relies on a pre-trained NER model to extract the contract fields from the text. This model should be trained to recognize the specific contract fields you're interested in.
(O sistema depende de um modelo NER pré-treinado para extrair os campos do contrato do texto. Este modelo deve ser treinado para reconhecer os campos específicos do contrato que lhe interessam.)

Once you have a trained model, place it in the project directory and update the model path in the `application/main.py` file.
(Uma vez que você tenha um modelo treinado, coloque-o no diretório do projeto e atualize o caminho do modelo no arquivo `application/main.py`.)

## Running the Project (Executando o Projeto)

With the environment set up and the dependencies installed, you can run the project with the following command:
(Com o ambiente preparado e as dependências instaladas, você pode rodar o projeto com o seguinte comando:)

```
python application/main.py
```

This will execute the main script that coordinates the extraction of the text from the PDF, the identification of the contract fields, and the creation of the Contract object.
(Isso executará o script principal que coordena a extração do texto do PDF, a identificação dos campos do contrato e a criação do objeto Contrato.)

## Testing (Testes)

The `/tests` directory contains unit and integration tests for the project. You can run them with the following command:
(O diretório `/tests` contém testes unitários e de integração para o projeto. Você pode executá-los com o seguinte comando:)

```
python -m unittest discover -s tests
```

## License (Licença)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
(Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.)
