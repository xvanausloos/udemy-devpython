# -- definition
class Personne:
    # default constructor
    def __init__(self, nom):
        self.nom = nom
        print(f"Bonjour mon nom est {nom}")


if __name__ == '__main__':
    # implementation
    personne1 = Personne("jean")
    print(id(personne1))
    personne2 = Personne("xav")
    print(id(personne2))