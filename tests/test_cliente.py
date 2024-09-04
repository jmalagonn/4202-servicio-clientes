from unittest import TestCase

from app import app

class TestCLiente(TestCase):

  def setUp(self):
    self.client = app.test_client()

  def test_obtener_cliente(self):
    self.id_usuario = 1
    endpoint_obtener_cliente = "cliente/{}".format(str(self.id_usuario))
    headers = {'Content-Type': 'application/json'}

    solicitud_consultar_cliente = self.client.get(endpoint_obtener_cliente, headers=headers)
    respuesta = solicitud_consultar_cliente.get_json()

    cliente = respuesta["cliente"]

    self.assertEqual(cliente["nombre"], "Claro")