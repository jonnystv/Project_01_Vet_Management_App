from db.run_sql import run_sql

from models.vet import Vet
from models.animal import Animal

import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository


def save(vet):
    sql = "INSERT INTO vets( name ) VALUES ( %s ) RETURNING id"
    values = [vet.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)