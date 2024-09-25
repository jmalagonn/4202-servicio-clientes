from datetime import datetime, timedelta
from flask_restful import Resource
from modelos import db, Cliente, ClienteSchema
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity


cliente_schema = ClienteSchema()


class VistaCliente(Resource):
  
  @jwt_required()
  def get(self):
    current_user = get_jwt_identity()
    
    if current_user['user_type'] == 1:
      return current_user, 200
    else:
      return "Unauthorized", 401