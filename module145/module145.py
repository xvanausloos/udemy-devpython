# -- definition
class Personne:
    # default constructor
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        print(f"Bonjour je m'appelle {self.nom}, j'ai {self.age}")
        if self.est_majeur():
            print(f"Je suis majeure")
        else:
            print(f"Je suis mineur")

    def est_majeur(self) -> bool:
        return self.age >= 18


if __name__ == '__main__':
    # implementation
    personne1 = Personne("jean", 30)
    print(id(personne1))
    personne2 = Personne("Paul", 15)
    print(id(personne2))
    personne1.se_presenter()
    personne2.se_presenter()

