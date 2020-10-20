"""
Problème:
    Créer une fonction recursive qui prend en paramètre une liste l.
    Celle-ci retourne une liste qui comprend la somme de l'ensemble des pairs d'éléments n / n+1 de la liste l.

Exemple:
    l = [1, 2, 3] -> [3, 5]
    l = [1, 2, 3, 4, 5] -> [3, 5, 7, 9]

Contraintes:
    Il est interdit d'utiliser des boucles.

"""


def sum_array_pair(array: list) -> list:
    if len(array) == 2:  # Condition d'arrêt
        # Si jamais je n'ai que 2 éléments dans ma liste, je peux juste retourner
        # un tableau contenant la somme de ces deux éléments
        return [array[0] + array[1]]

    # Si ce n'est pas le cas, je dois créer un tableau contenant la somme du 1er
    # et du 2ème élément puis y concaténer le tableau de sommes
    # trouvé pour le reste du tableau (en enlevant le premier élément)
    return [array[0] + array[1]] + sum_array_pair(array[1:])


print(sum_array_pair([1, 2, 3, 4, 5]))
