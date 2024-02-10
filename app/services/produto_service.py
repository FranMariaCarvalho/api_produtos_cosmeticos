from app import db
from app.models.models import Produto

def adicionar_produto(nome, descricao, preco, estoque):
    novo_produto = Produto(nome=nome, descricao=descricao, preco=preco, estoque=estoque)
    db.session.add(novo_produto)
    db.session.commit()
    return novo_produto

def obter_produtos():
    return Produto.query.all()

def obter_produto_por_id(produto_id):
    return Produto.query.get(produto_id)

def atualizar_produto(produto_id, nome, descricao, preco, estoque):
    produto = Produto.query.get(produto_id)
    if produto:
        produto.nome = nome
        produto.descricao = descricao
        produto.preco = preco
        produto.estoque = estoque
        db.session.commit()
        return produto
    return None

def deletar_produto(produto_id):
    produto = Produto.query.get(produto_id)
    if produto:
        db.session.delete(produto)
        db.session.commit()
        return True
    return False
