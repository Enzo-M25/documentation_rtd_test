class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age  # Donnée membre commune à tous les animaux

    def parler(self):
        return f"{self.nom} fait un bruit générique."

# Classe Chien avec des données spécifiques en plus de celles héritées
class Chien(Animal):
    def __init__(self, nom, age, race):
        super().__init__(nom, age)  # Appel du constructeur de la classe parente
        self.race = race  # Donnée membre spécifique au Chien

    def parler(self):
        return f"{self.nom} aboie : Woof !"

# Classe Oiseau avec des données spécifiques en plus de celles héritées
class Oiseau(Animal):
    def __init__(self, nom, age, couleur_plumes):
        super().__init__(nom, age)  # Appel du constructeur de la classe parente
        self.couleur_plumes = couleur_plumes  # Donnée membre spécifique à l'Oiseau

    def parler(self):
        return f"{self.nom} chante : Cui cui !"
