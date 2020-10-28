def f(n: list) -> int:
    a: int = 0  # C2
    i: int = len(n)  # C3
    while i > 0:  # C4 * (log(n) + 1)
        a += 1  # C5 * log(n)
        i /= 2  # C6 * log(n)
    return a  # C7


## 1. Création de l'équation
# C1 + C2 + C3 + C4 * (log(n) + 1) + C5 * log(n) + C6 * log(n) + C7
## 2. Mettre toutes les constantes multiplicatives à 1
# C1 + C2 + C3 + 1 * (log(n) + 1) + 1 * log(n) + 1 * log(n) + C7
## 3. Supprimer toutes les constantes additives
# 1 * (log(n) + 1) + 1 * log(n) + 1 * log(n)
## 4. Réduire / simplifier de manière mathématique
# log(n) + 1 + log(n) + log(n)
# 3log(n) + 1
## 5. Lorsque l'on ne peut plus simplifier de manière mathématique, il faut à nouveau simplifier de manière informatique
# log(n) + 1
# log(n)


# Complexité réelle de l'algorithme : T(n) = 3log(n) + 1
# Complexité asymptotique de l'algorithme : T(n) = O(log(n))


if __name__ == '__main__':
    # Vos tests ici
    print(f([1]*1000000000))  # C1
    print(f([1]))  # C1
    pass
