from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Client
from app.forms import FormClient
from app.extensions import db

client_new = Blueprint("client_new", __name__)

  
@client_new.route('/new-client')
def index():
    form = FormClient()
    return render_template('client_new/index.html', title='New Client', form=form)

@client_new.route('/create', methods=['POST',])
def create():
    form = FormClient(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('client_new.index'))

    cpf = form.cpf.data
    name = form.name.data
    is_opportunity = form.is_opportunity.data

    client = Client.query.filter_by(cpf=cpf).first()

    if client:
        flash('This client already exists.')
        return redirect(url_for('client_new.index'))

    new_client = Client(cpf=cpf, name=name, is_opportunity=is_opportunity)
    db.session.add(new_client)
    db.session.commit()

    return redirect(url_for('client_list.index'))