# tests/test_products.py

import pytest
from flask import Flask
from app import app
from factory import create_app

@pytest.fixture(scope='module')
def test_client():
    # Cria uma instância do app usando a configuração de teste
    flask_app = create_app(config_class='config.TestConfig')

    # Cria um cliente de teste para esta instância do app
    testing_client = flask_app.test_client()

    # Cria um contexto de aplicação
    ctx = flask_app.app_context()
    ctx.push()

    # 'yield' o cliente de teste para ser usado pelo teste
    yield testing_client

    # Limpa o contexto após o teste ser concluído
    ctx.pop()

def test_criar_produto(test_client):
    response = test_client.post('/criar_produto', json={'chave': 'valor'})
    assert response.status_code == 201
