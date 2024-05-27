from unittest import TestCase

from module145.module145 import Personne


class TestPersonne(TestCase):

    def test_est_majeur(self):
        personne = Personne("Toto", 10)
        self.assertEqual(False, personne.est_majeur())
        personne2 = Personne("Tatie", 20)
        self.assertEqual(True, personne2.est_majeur())
