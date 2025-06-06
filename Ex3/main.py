from animaux.animal import Animal
from animaux.animal import Chien
from animaux.animal import Oiseau

def main():

    chien = Chien("Médor")
    oiseau = Oiseau("Bip")
    animal_generique = Animal("Animal inconnu")

    print(chien.parler())
    print(oiseau.parler())
    print(animal_generique.parler())

if __name__ == "__main__":
    main()