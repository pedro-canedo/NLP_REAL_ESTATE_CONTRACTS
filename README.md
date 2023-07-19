# Sistema de Extração de Contratos

Este projeto é um aplicativo de extração de informações de contrato de documentos PDF usando um modelo de reconhecimento de entidades nomeadas (NER).

## Requisitos

- Python 3.8+
- Pip (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório:
   ```
   git clone 'repository'
   cd contract_extraction
   ```
2. Crie e ative um ambiente virtual (recomendado):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

## Preparação do Modelo

O sistema depende de um modelo NER pré-treinado para extrair os campos do contrato do texto. Esse modelo deve ser treinado para reconhecer os campos específicos do contrato que você está interessado.

Uma vez que você tem um modelo treinado, coloque-o no diretório do projeto e atualize o caminho do modelo no arquivo `application/main.py`.

## Executando o Projeto

Com o ambiente preparado e as dependências instaladas, você pode rodar o projeto com o seguinte comando:

    ```
    python -m application.main
    ```

Isso irá executar o script principal que coordena a extração do texto do PDF, a identificação dos campos do contrato e a criação do objeto Contrato.

## Testando

O diretório `/tests` contém testes unitários e de integração para o projeto. Você pode executá-los com o seguinte comando:

```
python -m unittest discover -s tests
```

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
