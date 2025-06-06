from animaux.animal import Animal, Chien, Oiseau

def main():

    # Création d'un chien et d'un oiseau avec leurs attributs spécifiques
    chien = Chien("Rex", 5, "Berger Allemand")
    oiseau = Oiseau("Tweety", 2, "Jaune")

    # Affichage des informations
    print(f"{chien.nom}, un {chien.race}, a {chien.age} ans.")
    print(f"{oiseau.nom}, un oiseau de couleur {oiseau.couleur_plumes}, a {oiseau.age} ans.")

    # Appel des méthodes 'parler'
    print(chien.parler())  # Rex aboie : Woof !
    print(oiseau.parler())  # Tweety chante : Cui cui !

if __name__ == "__main__":
    main()