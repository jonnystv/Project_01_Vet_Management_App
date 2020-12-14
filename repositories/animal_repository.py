from db.run_sql import run_sql

from models.vet import Vet
from models.animal import Animal

import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

def save(animal):
    sql = "INSERT INTO animals( name, type, dob, age, notes, owner, owner_tel, owner_email, vet_id ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [animal.name, animal.type, animal.dob, animal.age, animal.notes, animal.owner,animal.owner_tel, animal.owner_email, animal.vet.id]
    results = run_sql(sql, values)
    animal.id = results[0]['id']
    return animal

    