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
def new_vetl():
    return render_template("/vets/new.html")