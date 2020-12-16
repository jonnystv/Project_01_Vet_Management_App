from db.run_sql import run_sql

from models.animal import Animal
from models.vet import Vet
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

#CREATE
def save(vet):
    sql = "INSERT INTO vets( name, animal_ide ) VALUES ( %s ) RETURNING id"
    values = [vet.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

#READ
def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['name'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = Vet(result['name'], result['id'] )
    return vet

#DELETE
def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#UPDATE
def update(vet):
    sql = "UPDATE vets SET (name) = (%s) WHERE id = %s"
    values = [vet.name, vet.id]
    run_sql(sql, values)