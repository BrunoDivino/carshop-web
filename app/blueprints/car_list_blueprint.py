from flask import Blueprint, render_template
from app.models import Car

car_list = Blueprint("car_list", __name__)


@car_list.route("/car-list")
def index():
    cars = Car.query.all()
    return render_template("car_list/index.html", title='Car List', cars=cars)