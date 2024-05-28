# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        message = "Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans. "
        majmin = "Je suis mineure"

        if self.EstMajeur():
            majmin = "Je suis majeure"
        print(message + majmin)
        if self.genre:
            print("Genre : Masculin")
        else:
            print("Genre : Feminin")

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne(nom="Jean", age=25, genre=True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17, genre=False)
personne2.SePresenter()

