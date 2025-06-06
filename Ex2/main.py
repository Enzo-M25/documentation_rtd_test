from animaux.animal import Chien
from animaux.animal import Oiseau

def main():
    animaux = [
        Chien("Benji"),
        Oiseau("Titi")
    ]

    for animal in animaux:
        print(animal.parler())

if __name__ == "__main__":
    main()
