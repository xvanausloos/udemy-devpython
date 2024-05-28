# POO EXERCICE DE MISE EN SITUATION 3

# ---
class Chat:
    def __init__(self, nom: str):
        self.nom = nom

    def se_presenter(self):
        print("Bonjour, je suis un chat et je m'appelle " + self.nom)

# ---

class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def se_presenter(self):
        print("Bonjour, je suis une personne et je m'appelle " + self.nom)


chat1 = Chat("inconnu")
chat1.se_presenter()  # Bonjour, je suis un chat egit je m'appelle inconnu

chat2 = Chat("Garfield")
chat2.se_presenter()  # Bonjour, je suis un chat et je m'appelle Garfield

personne = Personne("Jean")
personne.se_presenter()  # Bonjour, je suis une personne et je m'appelle Jean
