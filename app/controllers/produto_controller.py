# app/controllers/produto_controller.py

from flask import request, jsonify, Blueprint
from app.database import db
from app.models.produto import Produto

produto_blueprint = Blueprint('produto_blueprint', __name__)

@produto_blueprint.route('/produtos', methods=['POST'])
def criar_produto():
    """
    Cria um novo produto
    ---
    post:
      summary: Cria um novo produto
      description: Adiciona um novo produto ao banco de dados
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                nome:
                  type: string
                  description: O nome do produto
                descricao:
                  type: string
                  description: A descrição do produto
                preco:
                  type: number
                  description: O preço do produto
              required:
                - nome
                - preco
      responses:
        201:
          description: Produto criado com sucesso
          content:
            application/json:
              schema:
                type: object
                properties:
                  mensagem:
                    type: string
                    example: Produto criado com sucesso!
        400:
          description: Entrada inválida
    """
    dados = request.get_json()  # Obtém os dados do corpo da requisição

    # Validação básica dos dados de entrada
    if not dados or not 'nome' in dados or not 'preco' in dados:
        return jsonify({'mensagem': 'Dados inválidos.'}), 400

    # Criação do produto
    try:
        novo_produto = Produto(nome=dados['nome'], descricao=dados.get('descricao', ''), preco=dados['preco'])
        db.session.add(novo_produto)
        db.session.commit()
        return jsonify({'mensagem': 'Produto criado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'mensagem': 'Erro ao criar o produto.', 'error': str(e)}), 500

@produto_blueprint.route('/produtos', methods=['GET'])
def listar_produtos():
    """
    Lista todos os produtos
    ---
    get:
      summary: Lista todos os produtos
      description: Retorna uma lista de todos os produtos no banco de dados
      responses:
        200:
          description: Uma lista de produtos
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    id:
                      type: integer
                      description: O ID único do produto
                    nome:
                      type: string
                      description: O nome do produto
                    descricao:
                      type: string
                      description: A descrição do produto
                    preco:
                      type: number
                      description: O preço do produto
    """
    produtos = Produto.query.all()
    resultado = []

    for produto in produtos:
        objeto_produto = {
            'id': produto.id,
            'nome': produto.nome,
            'descricao': produto.descricao,
            'preco': produto.preco
        }
        resultado.append(objeto_produto)

    return jsonify({'produtos': resultado})

@produto_blueprint.route('/produtos/<int:id>', methods=['GET'])
def obter_produto(id):
    """
    Obtém um produto específico
    ---
    get:
      summary: Obtém um produto por ID
      description: Retorna os detalhes de um único produto com base no ID fornecido
      parameters:
        - in: path
          name: id
          required: true
          description: ID único do produto
          schema:
            type: integer
      responses:
        200:
          description: Detalhes do produto
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    description: O ID único do produto
                  nome:
                    type: string
                    description: O nome do produto
                  descricao:
                    type: string
                    description: A descrição do produto
                  preco:
                    type: number
                    description: O preço do produto
        404:
          description: Produto não encontrado
    """
    produto = Produto.query.get_or_404(id)
    return jsonify({
        'id': produto.id,
        'nome': produto.nome,
        'descricao': produto.descricao,
        'preco': produto.preco
    })

@produto_blueprint.route('/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    """
    Atualiza um produto existente
    ---
    put:
      summary: Atualiza um produto por ID
      description: Atualiza os detalhes de um produto existente no banco de dados
      parameters:
        - in: path
          name: id
          required: true
          description: ID único do produto
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                nome:
                  type: string
                  description: O novo nome do produto
                descricao:
                  type: string
                  description: A nova descrição do produto
                preco:
                  type: number
                  description: O novo preço do produto
      responses:
        200:
          description: Produto atualizado com sucesso
          content:
            application/json:
              schema:
                type: object
                properties:
                  mensagem:
                    type: string
                    example: Produto atualizado com sucesso!
        404:
          description: Produto não encontrado
    """
    produto = Produto.query.get_or_404(id)
    dados = request.get_json()

    produto.nome = dados.get('nome', produto.nome)
    produto.descricao = dados.get('descricao', produto.descricao)
    produto.preco = dados.get('preco', produto.preco)

    db.session.commit()

    return jsonify({'mensagem': 'Produto atualizado com sucesso!'})

@produto_blueprint.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    """
    Deleta um produto específico
    ---
    delete:
      summary: Deleta um produto por ID
      description: Remove um produto do banco de dados com base no ID fornecido
      parameters:
        - in: path
          name: id
          required: true
          description: ID único do produto
          schema:
            type: integer
      responses:
        200:
          description: Produto deletado com sucesso
          content:
            application/json:
              schema:
                type: object
                properties:
                  mensagem:
                    type: string
                    example: Produto deletado com sucesso!
        404:
          description: Produto não encontrado
    """
    produto = Produto.query.get_or_404(id)

    db.session.delete(produto)
    db.session.commit()

    return jsonify({'mensagem': 'Produto deletado com sucesso!'})
