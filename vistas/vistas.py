from datetime import datetime, timedelta
import time
from flask import config
from flask_restful import Resource
from modelos import db, Cliente, ClienteSchema

cliente_schema = ClienteSchema()
#simulate_error_count = config['simulate_error_count']
call_counter=0
last_fail = None
class VistaCliente(Resource):
  
  def get(self, id_cliente):
    global call_counter
    global last_fail
    cliente = cliente_schema.dump(db.get_or_404(Cliente, id_cliente))

    if last_fail is not  None and datetime.now() < last_fail:
      return "Servicio no disponible", 500
    else:
      if call_counter >= 5:
        print(f"Simulando fallo")
        last_fail = datetime.now()+timedelta(seconds=5)
        call_counter = 0
        return "Servicio no disponible", 500
      if cliente is None:
        return "Cliente no encontrado", 404
      else:
        call_counter += 1 
        print(call_counter) 
        return {"cliente": cliente}