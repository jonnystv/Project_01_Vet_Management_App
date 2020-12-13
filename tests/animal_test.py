import unittest
from models.animal import Animal

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal = Animal("Fido", "Labrador", "12-12-2015", "5", "Ankle X-Ray required. Potential fracture", "Jim Smith", "07922175003", "jim@smith.com")


    def test_animal_has_name(self):
        self.assertEqual("Fido", self.animal.name)
    
    def test_animal_has_type(self):
        self.assertEqual("Labrador", self.animal.type)

    def test_animal_has_dob(self):
        self.assertEqual("12-12-2015", self.animal.dob)

    def test_animal_has_age(self):
        self.assertEqual("5", self.animal.age)

    def test_animal_has_notes(self):
        self.assertEqual("Ankle X-Ray required. Potential fracture", self.animal.notes)

    def test_animal_has_owner(self):
        self.assertEqual("Jim Smith", self.animal.owner)

    def test_animal_has_owner_tel(self):
        self.assertEqual("07922175003", self.animal.owner_tel)

    def test_animal_has_owner_email(self):
        self.assertEqual("jim@smith.com", self.animal.owner_email)