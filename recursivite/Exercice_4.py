"""
Problème:
    Créer une fonction récursive qui prend un entier n en paramètre.
    Celle-ci retourne toutes les combinaisons binaires possibles de taille n.
    Le retour de la fonction doit être une liste comprenant l'ensemble des combinaisons binaires sous forme de chaines de caractères.

Exemple:
    n = 1 -> ['0', '1']
    n = 2 -> ['00', '01', '10', '11']
    n = 3 -> ['000', '001', '010', '011', '100', '101', '110', '111']
"""


# Votre solution
def generate_binaries_combinations(n: int) -> list:
    if n == 1:  # Conditions d'arrêt
        # Si n = 1, je dois juste retourner [0, 1], comme dans l'exemple
        return ["0", "1"]

    # Si jamais n est plus grand que 1, je dois d'abord récupérer toutes
    # les combinaisons possibles pour n-1
    previous_combinations = generate_binaries_combinations(n - 1)

    # Je rajoute un 0 devant toutes les combinaisons trouvées pour n-1
    zeros = ["0" + s for s in previous_combinations]

    # Je fais la même chose mais en rajoutant un 1 devant les combinaisons trouvées pour n-1
    ones = ["1" + s for s in previous_combinations]

    # Je concatène les deux tableaux
    return zeros + ones


print(generate_binaries_combinations(10))
