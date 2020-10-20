"""
Problème:
    Créer une fonction récursive qui permet de connaitre la somme de l'ensemble des éléments (nombres réels) d'une liste.
    Le retour de la fonction doit être un nombre réel.


Exemple:
    [1, 1] -> 2
    [1, 2] -> 3
    [2, 4, 6] -> 12

Contrainte:
    Il est interdit d'utiliser des boucles !
"""


# Votre solution
def sum_array(array: list) -> float:
    if len(array) == 1:  # Condition d'arrêt
        # Si jamais je n'ai plus qu'un seul élément dans la liste,
        # je le retourne directement
        return array[0]
    # Je fais la somme de l'élément à la première position
    # avec la somme des autres éléments de la liste
    # La somme des autres éléments de la liste est récupéré via la récursivité
    return array[0] + sum(array[1:])


print(sum_array([1, 1, 3, 4]))
