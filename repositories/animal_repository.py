from db.run_sql import run_sql

from models.vet import Vet
from models.animal import Animal
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

#CREATE
def save(animal):
    sql = "INSERT INTO animals( name, type, dob, age, notes, owner, owner_tel, owner_email, vet_id ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s ) RETURNING id"
    values = [animal.name, animal.type, animal.dob, animal.age, animal.notes, animal.owner, animal.owner_tel, animal.owner_email, animal.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    animal.id = id
    return animal

#READ
def select_all():
    animals = []

    sql = "SELECT * FROM animals"
    results = run_sql(sql)

    for row in results:
        animal = Animal(row['name'], row['type'], row['dob'], row['age'], row['notes'], row['owner'], row['owner_tel'], row['owner_email'], row['vet_id'], row['id'])
        animals.append(animal)
    return animals

def select(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        animal = Animal(result['name'], result['type'], result['dob'], result['age'], result['notes'], result['owner'], result['owner_tel'], result['owner_email'], result['vet_id'], result['id'])
    return animal

#DELETE
def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#UPDATE
def update(animal):
    sql = "UPDATE animals SET (name, type, dob, age, notes, owner, owner_tel, owner_email, vet_id) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.type, animal.dob, animal.age, animal.notes, animal.owner, animal.owner_tel, animal.owner_email, animal.vet_id]
    run_sql(sql, values)