from flask_restful import Resource
from modelos import  ClienteSchema
from flask_jwt_extended import jwt_required,  get_jwt_identity


cliente_schema = ClienteSchema()


class VistaCliente(Resource):
  
  @jwt_required()
  def get(self):
    current_user = get_jwt_identity()
    
    if current_user['user_type'] == 1:
      return     {
      "id": 123,
      "name": "John Doe",
      "email": "john.doe@example.com",
      "phone": "+1234567890",
      "address": "123 Main St, Anytown, USA",
      "ssn": "123-45-6789",
      "credit_card": {
        "number": "4111111111111111",
        "expiry": "12/25",
        "cvv": "123"
      }
    }, 200

    else:
      return "Unauthorized", 401