import unittest
from models.vet import Vet

class TestVet(unittest.TestCase):

    def setUp(self):
        self.vet = Vet("Dr Doolittle")


    def test_vet_has_name(self):
        self.assertEqual("Dr Doolittle", self.vet.name)