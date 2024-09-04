from flask_restful import Resource

from modelos import db, Cliente, ClienteSchema

cliente_schema = ClienteSchema()

class VistaCliente(Resource):
  def get(self, id_cliente):
    cliente = cliente_schema.dump(db.get_or_404(Cliente, id_cliente))

    if cliente is None:
      return "Cliente no encontrado", 404
    else: 
      return {"cliente": cliente}