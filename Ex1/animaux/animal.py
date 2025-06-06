class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parler(self):
        raise NotImplementedError("Chaque animal doit implémenter sa propre méthode 'parler'.")
