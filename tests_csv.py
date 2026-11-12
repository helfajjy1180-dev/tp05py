
import unittest
import os

from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)


class TestCSV(unittest.TestCase):

    def setUp(self):
        self.fichier = "test_articles.csv"

    def tearDown(self):
        if os.path.exists(self.fichier):
            os.remove(self.fichier)

    def creer_fichier(self, contenu):
        with open(self.fichier, "w", encoding="utf-8") as f:
            f.write(contenu)

    # Test 1 : CSV valide
    def test_csv_valide(self):
        self.creer_fichier(
            "1;Ordinateur;5500\n"
            "2;Clavier;150\n"
            "3;Souris;80\n"
        )

        resultat = charger_csv(self.fichier)

        self.assertEqual(len(resultat), 3)
        self.assertEqual(resultat[0]["nom"], "Ordinateur")

    # Test 2 : Fichier absent
    def test_fichier_introuvable(self):
        with self.assertRaises(FichierIntrouvableException):
            charger_csv("fichier_inexistant.csv")

    # Test 3 : Prix texte
    def test_prix_non_numerique(self):
        self.creer_fichier("1;Ordinateur;abc\n")

        with self.assertRaises(LigneInvalideException):
            charger_csv(self.fichier)

    # Test 4 : Prix négatif
    def test_prix_negatif(self):
        self.creer_fichier("1;Ordinateur;-100\n")

        with self.assertRaises(PrixNegatifException):
            charger_csv(self.fichier)


if __name__ == "__main__":
    unittest.main()
