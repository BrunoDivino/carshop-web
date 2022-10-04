from app.extensions import db


class Client(db.Model):
    cpf = db.Column(db.String(11), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    is_opportunity = db.Column(db.Boolean, default=True)
    cars = db.relationship("Car", backref="client", lazy=True)

    def __repr__(self) -> str:
        return self.name


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    owner_cpf = db.Column(db.String(11), db.ForeignKey("client.cpf"), nullable=False)
    color = db.Column(db.String(6), nullable=False)
    model = db.Column(db.String(11), nullable=False)

    def __repr__(self) -> str:
        return self.name
