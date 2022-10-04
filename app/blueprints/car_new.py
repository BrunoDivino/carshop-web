from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Car, Client
from app.forms import FormCar
from app.extensions import db

car_new = Blueprint("car_new", __name__)

  
@car_new.route('/new-car')
def index():
    form = FormCar()
    return render_template('car_new/index.html', title='New Car', form=form)

@car_new.route('/create', methods=['POST',])
def create():
    form = FormCar(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('car_new.index'))

    id = form.id.data
    name = form.name.data
    owner_cpf = form.owner_cpf.data
    color = form.color.data
    model = form.model.data

    car = Car.query.filter_by(id=id).first()

    if car:
        flash('This car already exists.')
        return redirect(url_for('car_new.index'))

    client = Client.query.filter_by(cpf=owner_cpf).first()
    if client:
        client.is_opportunity = False
        db.session.add(client)
        db.session.commit()

    new_car = Car(id=id, name=name, owner_cpf=owner_cpf, color=color, model=model)
    db.session.add(new_car)
    db.session.commit()

    return redirect(url_for('car_list.index'))