from flask import Flask, render_template, Blueprint, redirect, request

from models.animal import Animal
from models.vet import Vet

import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/")
def animals():
    animals = animal_repository.select_all()
    return render_template("index.html", animals = animals)