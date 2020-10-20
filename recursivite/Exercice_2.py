"""
Problème:
  Créer une fonction récursive qui permet de connaitre le plus petit multiple commun entre 2 nombres entiers positifs.
  Le retour de la fonction doit être un nombre entier positif.
  Rappel: Le plus petit multiple commun (PPMC ou PPCM) est l'entier positif le plus petit qui soit un multiple du premier nombre comme du deuxième.

Signature de la méthode:
  sum_array(array: list) -> float

Exemple:
  4 et 6 -> 12 (4*3 et 6*2)
  24 et 36 -> 72 (24*3 et 36*2)
  3 et 89 -> 267 (3*89 et 89*3)

Contraintes:
  Il est interdit d'utiliser des boucles !
"""


# Votre solution
def ppcm(nb1, nb2, m=None) -> float:
    # Comme j'ai un 3ème paramètre par défaut,
    # je dois l'initialiser si jamais je suis dans le premier appel de la fonction
    if m is None:
        # On pourrait mettre 1 ici. Définir m à nb2 (ou nb1) permet juste de réduire le nombre de récursivités
        m = nb2
    # Si jamais la division du nombre que je teste avec nb1 et nb2
    # ne retourne pas une valeur entière, c'est que ce n'est pas un ppmc
    # Exemple:
    # m = 1, nb1 = 4, nb2 = 6 => 1%4 != 0, 1%6 != 0 => false
    # m = 2, nb1 = 4, nb2 = 6 => 2%4 != 0, 2%6 != 0 => false
    # ...
    # m = 8, nb1 = 4, nb2 = 6 => 8%4 == 0, 8%6 != 0 => false
    # ...
    # m = 11, nb1 = 4, nb2 = 6 => 11%4 != 0, 11%6 != 0 => false
    # m = 12, nb1 = 4, nb2 = 6 => 2%4 == 0, 3%6 == 0 => true
    if m % nb1 == 0 and m % nb2 == 0:
        # Je retourne le ppmc trouvé
        return m
    else:
        # Si m n'est pas le ppmc, je recherche en augmentant m
        return ppcm(nb1, nb2, m + 1)


print(ppcm(24, 36))
