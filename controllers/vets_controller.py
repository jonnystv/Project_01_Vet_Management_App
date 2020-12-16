from flask import Flask, render_template, Blueprint, redirect, request

from models.vet import Vet
from models.animal import Animal

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets/")
def vets():
    vets = vet_repository.select_all()
    return render_template("/vets/index.html", vets = vets)

@vets_blueprint.route("/vets/new")
def new_vet():
    return render_template("/vets/new.html")

@vets_blueprint.route("/vets", methods=["POST"])
def add_vet():
    name = request.form["name"]
    new_vet = Vet(name)
    vet_repository.save(new_vet)
    return redirect("/vets")

@vets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect("/vets/")
