# -- definition
class Personne:
    # default constructor
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
        print(f"Bonjour mon nom est {nom} j'ai {age}")

    def sepresenter(self):
        print(f"Bonjour je m'appelle {self.nom}")

if __name__ == '__main__':
    # implementation
    personne1 = Personne("jean", 10)
    print(id(personne1))
    personne2 = Personne("xav", 50)
    print(id(personne2))
    personne1.sepresenter()
    personne2.sepresenter()