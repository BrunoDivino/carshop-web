import factory
from faker import Faker

from app.extensions import db
from app.models import Client

faker = Faker()


class ClientFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Client
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    cpf = faker.text()
    name = faker.text()
    is_opportunity = True
