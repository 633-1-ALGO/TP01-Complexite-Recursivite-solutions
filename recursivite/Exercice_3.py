"""
Problème:
    Créer une fonction récursive qui permet de savoir si une liste est un palindrome.
    Le retour de la fonction doit être une valeur booléen.
    Rappel: Un palindrome est un mot, un nombre, une phrase ou une séquence d'éléments qui se lit aussi bien à l'envers qu'à l'endroit.

Exemple:
    [1] est un palindrome
    [1, 1] est un palindrome
    [1, 2] n'est pas un palindrome
    [1, 2, 1] est un palindrome
    [1, 2, 2, 1] est un palindrome
    [3, 3, 3, 3, 1] n'est pas un palindrome

Contraintes:
    Il est interdit d'utiliser des boucles et la fonction reverse.

Résultat attendu:
    Un message affichant: "La liste [xxx] est un palindrome" ou "La liste [xxx] n'est pas un palindrome".
"""


# Votre solution
def is_palindrome(array: list) -> bool:
    length = len(array)  # Comme j'utilise la longueur du tableau à plusieurs endroits, j'initialise une variable
    if length <= 2:  # Condition d'arrêt (le tableau doit avoir une taille de 2 ou moins)
        if length == 2:
            # Si jamais il reste 2 éléments, je vérifie qu'ils soient égaux
            if array[0] == array[1]:
                # Si jamais ils sont égaux, c'est un palindrome
                return True
            else:
                # Sinon ce n'est pas un palindrome
                return False
        else:
            # Si jamais il ne reste qu'un seul élément,
            # il est forcément égal avec lui-même
            return True
    # Je vérifie que le premier et le dernier élément de ma liste soient égaux
    if array[0] == array[length - 1]:
        # Si c'est le cas, je continue la vérification en entrant
        # plus en profondeur dans ma liste
        return is_palindrome(array[1:length - 1])
    # Si ce n'est pas le cas, ce n'est pas un palindrome
    return False


print(is_palindrome([1, 2, 3, 2, 1]))
