from db import db


class Coordenada(db.Model):
    
    __tablename__="Coordenada"
    
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.column(db.String(50))
    latitud=db.column(db.String(20))
    longitud=db.column(db.String(20))
    
    
    def __init__(self,nombre,latitud,longitud):
        self.nombre=nombre
        self.latitud=latitud
        self.longitud=longitud