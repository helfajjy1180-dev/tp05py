
import csv
import os


# Exception principale
class CsvException(Exception):
    pass


# Fichier introuvable
class FichierIntrouvableException(CsvException):
    pass


# Ligne invalide
class LigneInvalideException(CsvException):
    pass


# Prix négatif ou nul
class PrixNegatifException(CsvException):
    pass


def charger_csv(chemin):

    # Vérifier si le fichier existe
    if not os.path.isfile(chemin):
        raise FichierIntrouvableException(
            f"Le fichier {chemin} est introuvable."
        )

    articles = []

    with open(chemin, "r", encoding="utf-8") as fichier:

        lecteur = csv.reader(fichier, delimiter=";")

        for numero, ligne in enumerate(lecteur, start=1):

            # Ignorer les lignes vides
            if not ligne or all(colonne.strip() == "" for colonne in ligne):
                continue

            # Vérifier le nombre de colonnes
            if len(ligne) != 3:
                raise LigneInvalideException(
                    f"Ligne {numero} : exactement 3 colonnes sont attendues."
                )

            identifiant, nom, prix = ligne

            # Vérifier les champs obligatoires
            if not identifiant.strip() or not nom.strip():
                raise LigneInvalideException(
                    f"Ligne {numero} : ID ou nom manquant."
                )

            # Vérifier si le prix est numérique
            try:
                prix = float(prix)
            except ValueError:
                raise LigneInvalideException(
                    f"Ligne {numero} : le prix doit être numérique."
                )

            # Vérifier si le prix est positif
            if prix <= 0:
                raise PrixNegatifException(
                    f"Ligne {numero} : le prix doit être supérieur à 0."
                )

            article = {
                "id": identifiant.strip(),
                "nom": nom.strip(),
                "prix": prix
            }

            articles.append(article)

    return articles
