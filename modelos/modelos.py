from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class Cliente(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(128))
   

class ClienteSchema(SQLAlchemyAutoSchema):
  class Meta:
    model = Cliente
    load_instance = True