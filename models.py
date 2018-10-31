from app import db


class Especie(db.Model):
    __tablename__ = "especies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "{}".format(self.name)


class Info(db.Model):
    """"""
    __tablename__ = "infos"

    id = db.Column(db.Integer, primary_key=True)
    nombre_cadena = db.Column(db.String)
    cadena = db.Column(db.String)
    accesion = db.Column(db.String)
    cadena_type = db.Column(db.String)

    especie_id = db.Column(db.Integer, db.ForeignKey("especies.id"))
    especie = db.relationship("Especie", backref=db.backref(
        "infos", order_by=id), lazy=True)
