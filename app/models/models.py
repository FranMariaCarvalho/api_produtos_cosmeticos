from app import db

class Produto(db.Model):
    __tablename__ = 'produto'  # Define explicitamente o nome da tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128), nullable=False)
    descricao = db.Column(db.String(256))
    preco = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Produto {}>'.format(self.nome)
