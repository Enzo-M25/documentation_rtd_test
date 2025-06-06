class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        return f"{self.nom} fait un bruit générique."  # Implémentation par défaut

# Classe Chien qui surcharge parler
class Chien(Animal):
    def parler(self):
        return f"{self.nom} aboie : Woof !"

# Classe Oiseau qui surcharge parler
class Oiseau(Animal):
    def parler(self):
        return f"{self.nom} chante : Cui cui !"
