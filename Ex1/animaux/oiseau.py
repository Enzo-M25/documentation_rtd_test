from .animal import Animal

class Oiseau(Animal):
    def parler(self):
        return f"{self.nom} chante : Cui cui !"
