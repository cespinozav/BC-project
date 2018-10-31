from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
#creando base de datos
engine = create_engine('sqlite:///mosquitos.db', echo=True) #devuelve una conexion a la base de datos, acceso al motor
Base = declarative_base()


class Especie(Base):
    __tablename__ = "especies"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "<Especie: {}>".format(self.name)


class Info(Base):
    """"""
    __tablename__ = "infos"

    id = Column(Integer, primary_key=True)
    nombre_cadena = Column(String) 
    cadena = Column(String)  
    accesion = Column(String)
    cadena_type = Column(String)

    especie_id = Column(Integer, ForeignKey("especies.id"))
    especie = relationship("Especie", backref=backref(
        "infos", order_by=id))


# crea tablas
Base.metadata.create_all(engine)