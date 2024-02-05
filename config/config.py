# config/config.py

import os

class Config:
    """Configurações base do aplicativo."""
    # Caminho para o diretório raiz do projeto. Isso assume que sua estrutura de diretórios segue a recomendada.
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Configuração do banco de dados
    # SQLITE
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'meu_projeto.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
