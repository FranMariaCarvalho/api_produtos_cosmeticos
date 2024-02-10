from app import app, db, api
from app.models.models import *
from app.controllers.produto_controllers import ns as produtos_ns

# Registra o namespace dos produtos na API
api.add_namespace(produtos_ns)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Produto': Produto}

if __name__ == '__main__':
    app.run(debug=True)
