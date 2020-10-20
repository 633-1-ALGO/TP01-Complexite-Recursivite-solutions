def f(n: list) -> int:
    a: int = 0  # C2
    i: int = 0  # C3
    while i < len(n):  # C4 * infini
        a += 1  # C5 * infini
    return a  # C6


## 1. Création de l'équation
# C1 + C2 + C3 + C4 * infini + C5 * infini + C6
## 2. Mettre toutes les constantes multiplicatives à 1
# C1 + C2 + C3 + 1 * infini + 1 * infini + C6
## 3. Supprimer toutes les constantes additives
# 1 * infini + 1 * infini
## 4. Réduire / simplifier de manière mathématique
# infini + infini
# 2infini
## 5. Lorsque l'on ne peut plus simplifier de manière mathématique, il faut à nouveau simplifier de manière informatique
# infini


# Complexité réelle de l'algorithme : T(n) = infini
# Complexité asymptotique de l'algorithme : T(n) = O(infini)


if __name__ == '__main__':
    # Vos tests ici
    print(f([1, 2]))  # C1
    pass
