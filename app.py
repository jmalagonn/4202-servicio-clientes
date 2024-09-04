from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from modelos import db
from vistas import VistaCliente

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaCliente, '/cliente/<int:id_cliente>')