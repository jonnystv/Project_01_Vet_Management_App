import pdb

from models.animal import Animal
import repositories.animal_repository as animal_repository

from models.vet import Vet
import repositories.vet_repository as vet_repository

vet_1 = Vet("Dr Doolittle")
vet_repository.save(vet_1)

vet_2 = Vet("Dr Herriot")
vet_repository.save(vet_2)

vet_3 = Vet("Dr Hamster")
vet_repository.save(vet_3)

vet_4 = Vet("Dr Greene")
vet_repository.save(vet_4)