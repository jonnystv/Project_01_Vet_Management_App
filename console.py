from models.vet import Vet
from models.animal import Animal
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository

animal_repository.delete_all()
vet_repository.delete_all()

vet_1 = Vet("Dr Doolittle")
vet_repository.save(vet_1)

vet_2 = Vet("Dr Herriot")
vet_repository.save(vet_2)

vet_3 = Vet("Dr Hamster")
vet_repository.save(vet_3)

vet_4 = Vet("Dr Greene")
vet_repository.save(vet_4)

animal_1 = Animal("Spot", "Cat", "15-06-2005", "15", "Deep gash on nose to be treated", "Commander Data", "07922175003", "star@trek.com", vet_1)
animal_repository.save(animal_1)

animal_2 = Animal("Twiggy", "Stick Insect", "10-10-2019", "1", "Leg pulled off by spider. Replacement leg needed", "David Bellamy", "07922175003", "cdavid@bellamy.com", vet_1)
animal_repository.save(animal_2)

animal_3 = Animal("Zeus", "Silverback", "17-10-1990", "30", "Ingrowing toenail, left pinky toe", "Jo Mobutu", "07922175003", "big@thief.com", vet_3)
animal_repository.save(animal_3)

animal_4 = Animal("Cornelius", "Chimpanzee", "12-11-1995", "25", "Nasty bruise to forehead. Possible X-Ray", "George Taylor", "07922175003", "dirty@ape.com", vet_4)
animal_repository.save(animal_4)