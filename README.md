# API de Gerenciamento de Produtos

Esta é uma API RESTful para gerenciamento de produtos em estoque. Ela permite operações CRUD (Criar, Ler, Atualizar, Deletar) em um banco de dados de produtos. Este projeto foi construído utilizando Python com o framework Flask e segue a arquitetura MVC. A documentação da API é gerada automaticamente via Swagger.

## Características

- **Linguagem**: Python 3.8+
- **Framework**: Flask
- **Arquitetura**: MVC
- **Documentação da API**: Swagger (flask-restx)
- **Banco de Dados**: SQLite
- **ORM**: SQLAlchemy (Flask-SQLAlchemy)

## Instalação

Antes de iniciar, certifique-se de que você tem Python 3.8 ou superior instalado na sua máquina. Recomenda-se a utilização de um ambiente virtual.

1. Clone o repositório para sua máquina local:

git clone https://github.com/FranMariaCarvalho/api_produtos_cosmeticos
cd caminho-para-o-repositorio
Crie um ambiente virtual e ative-o:

# Para sistemas baseados em Unix ou MacOS
python3 -m venv venv
source venv/bin/activate

# Para sistemas Windows
python -m venv venv
venv\Scripts\activate
Instale as dependências:
bash
Copy code
pip install -r requirements.txt
Configuração
As configurações do banco de dados e outras podem ser encontradas e modificadas em config/config.py.

Execução
Para rodar a aplicação, execute:

python main.py
Isso iniciará um servidor de desenvolvimento na porta 5000 por padrão.

Testes
Para executar os testes, use:

python -m unittest
Documentação da API
Com a aplicação rodando, acesse http://127.0.0.1:5000 para visualizar a documentação da API e testar os endpoints.

Contribuindo
Contribuições são bem-vindas!
