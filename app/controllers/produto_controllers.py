from flask_restx import Api, Resource, fields
from app import api
from app.services.produto_service import (adicionar_produto, obter_produtos, obter_produto_por_id,
                                                 atualizar_produto, deletar_produto)

ns = api.namespace('produtos', description='Operações relacionadas a produtos')

# from flask_restx import fields

modelo_produto = api.model('Produto', {
    'id': fields.Integer(readOnly=True, description='Identificador único do produto'),
    'nome': fields.String(required=True, description='Nome do produto'),
    'descricao': fields.String(description='Descrição do produto'),
    'preco': fields.Float(required=True, description='Preço do produto'),
    'estoque': fields.Integer(required=True, description='Quantidade em estoque')
})

@ns.route('/')
class ProdutoLista(Resource):
    @ns.doc('lista_produtos')
    @ns.marshal_list_with(modelo_produto)
    def get(self):
        '''Listar todos os produtos'''
        return obter_produtos()

    @ns.doc('criar_produto')
    @ns.expect(modelo_produto)
    @ns.marshal_with(modelo_produto, code=201)
    def post(self):
        '''Criar um novo produto'''
        return adicionar_produto(api.payload['nome'], api.payload['descricao'], api.payload['preco'], api.payload['estoque']), 201

@ns.route('/<int:id>')
@ns.response(404, 'Produto não encontrado')
@ns.param('id', 'Identificador único do produto')
class Produto(Resource):
    @ns.doc('obter_produto')
    @ns.marshal_with(modelo_produto)
    def get(self, id):
        '''Obter detalhes de um produto específico'''
        return obter_produto_por_id(id)

    @ns.doc('atualizar_produto')
    @ns.expect(modelo_produto)
    @ns.marshal_with(modelo_produto)
    def put(self, id):
        '''Atualizar um produto existente'''
        return atualizar_produto(id, api.payload['nome'], api.payload['descricao'], api.payload['preco'], api.payload['estoque'])

    @ns.doc('deletar_produto')
    @ns.response(204, 'Produto deletado')
    def delete(self, id):
        '''Deletar um produto'''
        deletar_produto(id)
        return '', 204
