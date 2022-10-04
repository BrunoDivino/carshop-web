from app.blueprints.client_list_blueprint import client_list
from app.blueprints.car_list_blueprint import car_list
from app.blueprints.client_new import client_new
from app.blueprints.car_new import car_new


def init_app(app):
    app.register_blueprint(client_list)
    app.register_blueprint(car_list)
    app.register_blueprint(client_new)
    app.register_blueprint(car_new)
