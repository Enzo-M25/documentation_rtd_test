from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nom):
        self.nom = nom

    @abstractmethod
    def parler(self):
        pass  # Cette méthode doit être implémentée par les sous-classes

from .animal import Animal

class Chien(Animal):
    def parler(self):
        return f"{self.nom} aboie : Woof !"

from .animal import Animal

class Oiseau(Animal):
    def parler(self):
        return f"{self.nom} chante : Cui cui !"
