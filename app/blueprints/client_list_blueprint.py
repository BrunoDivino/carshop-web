from flask import Blueprint, render_template
from app.models import Client

client_list = Blueprint("client_list", __name__)


@client_list.route("/")
def index():
    clients = Client.query.all()
    return render_template("client_list/index.html", title='Client List', clients=clients)
