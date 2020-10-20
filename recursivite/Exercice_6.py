"""
Problème:
    Créer une fonction récursive qui permet de calculer les sommes sous forme de triangle d'une liste donnée.
    
Exemple:
    Paramètre donné: [1, 2, 3, 4, 5]
    Résultats:
        [
            [48], -> (20+28)
            [20, 28], -> (8+12, 12+16)
            [8, 12, 16], -> (3+5, 5+7, 7+9)
            [3, 5, 7, 9], -> (1+2, 2+3, 3+4, 4+5)
            [1, 2, 3, 4, 5]
        ]


Contraintes:
    Il est interdit d'utiliser des boucles.
    Vous avez par contre le droit d'utiliser les fonctions déjà créées lors des précédents exercices.
    Pour importer une fonction depuis un autre fichier: from monFichier.py import maFonction (pycharm souligne cela en rouge, mais ça fonctionne !)
"""

# Votre solution
from recursivite.Exercice_5 import sum_array_pair


# ou : from Exercice_5 import sum_array_pair


def triangle_sum(array: list) -> list:
    if len(array) == 1:  # Condition d'arrêt
        # Si jamais je n'ai plus qu'un seul élément dans mon tableau,
        # c'est que je suis en haut du triangle. Je ne peux plus faire de somme avec et le retourne donc directement
        return [array]

    # Si ce n'est pas le cas, j'appelle ma fonction récursive en lui donnant en paramètre
    # le tableau des sommes du tableau actuel
    result = triangle_sum(sum_array_pair(array))
    # Comme je veux que le tableau actuel soit en dessous du tableau de ces sommes, je l'ajoute à la fin
    result.append(array)
    return result


print(triangle_sum([1, 2, 3, 4, 5]))
