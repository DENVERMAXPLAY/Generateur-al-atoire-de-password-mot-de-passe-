#Générateur de mot de passe automatique

#Utilisation de la bibliothèque "string" afin d'obtenir des letrres
#des chiffes et des caractères. Utilisation de random pour la sélection aléatoire

import string
import numpy as np

def mot_de_passe(longueur) :
    lettre = string.ascii_letters
    chiffre = string.digits
    caractere = string.punctuation

    all_caractere = lettre+chiffre+caractere

    password = "".join(np.random.choice(list(all_caractere), longueur))

    return password

#Je veux un mot de passe de longueur 12

print(mot_de_passe(12))

#c'est bon
