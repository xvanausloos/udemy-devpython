# -- definition
class Personne:
    # default constructor
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom
        if self.nom == "":
            name = input("Quel est le nom de l'utilisateur ? ")
            self.nom = name
        self.age = age

    def se_presenter(self):
        info_personne =   f"Bonjour je m'appelle {self.nom}"
        if self.age != 0:
            info_personne += ", jai " + str(str(self.age) + " ans")
        print(info_personne)

        if self.age != 0:
            if self.est_majeur():
                print(f"Je suis majeure")
            else:
                print(f"Je suis mineur")

    def est_majeur(self) -> bool:
        return self.age >= 18

    def demander_lenom(self):
        pass

if __name__ == '__main__':
    # implementation
    personne1 = Personne("jean", 30)
    print(id(personne1))
    personne2 = Personne("Paul", 15)
    print(id(personne2))
    personne1.se_presenter()
    personne2.se_presenter()
    personne3 = Personne()
    personne3.se_presenter()

