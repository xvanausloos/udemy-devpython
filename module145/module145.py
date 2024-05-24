# -- definition
class Personne:
    # default constructor
    def __init__(self, nom):
        self.nom = nom
        print(f"Bonjour mon nom est {nom}")

    def sepresenter(self):
        print(f"Bonjour je m'appelle {self.nom}")

if __name__ == '__main__':
    # implementation
    personne1 = Personne("jean")
    print(id(personne1))
    personne2 = Personne("xav")
    print(id(personne2))
    personne1.sepresenter()
    personne2.sepresenter()