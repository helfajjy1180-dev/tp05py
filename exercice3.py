
class CsvException(Exception):
    pass


class FichierIntrouvableException(CsvException):
    pass


class LigneInvalideException(CsvException):
    pass


class PrixNegatifException(CsvException):
    pass


def charger_csv(chemin):
    articles = []

    try:
        fichier = open(chemin, "r", encoding="utf-8")
    except FileNotFoundError:
        raise FichierIntrouvableException(
            f"Fichier introuvable : {chemin}"
        )

    with fichier:
        for numero, ligne in enumerate(fichier, start=1):

            if ligne.strip() == "":
                continue

            colonnes = ligne.strip().split(";")

            if len(colonnes) != 3:
                raise LigneInvalideException(
                    f"Ligne {numero} : nombre de colonnes invalide"
                )

            identifiant, nom, prix = colonnes

            try:
                prix = float(prix)
            except ValueError:
                raise LigneInvalideException(
                    f"Ligne {numero} : prix non numérique"
                )

            if prix < 0:
                raise PrixNegatifException(
                    f"Ligne {numero} : prix négatif"
                )

            if prix == 0:
                raise LigneInvalideException(
                    f"Ligne {numero} : le prix doit être supérieur à 0"
                )

            article = {
                "id": identifiant,
                "nom": nom,
                "prix": prix
            }

            articles.append(article)

    return articles
