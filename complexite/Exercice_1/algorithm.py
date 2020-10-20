def f(n: list, m: list) -> (int, int):
    a, b = 0, 0  # C2, C3
    for i in range(0, len(n)):  # C4 * (n + 1)
        a = a + i  # C5 * n
    for j in range(0, len(m)):  # C6 * (m + 1)
        b = b + j * 2  # C7 * m
    return a, b  # C8


## 1. Création de l'équation
# C1 + C2 + C3 + C4 * (n + 1) + C5 * n + C6 * (m + 1) + C7 * m + C8
## 2. Mettre toutes les constantes multiplicatives à 1
# C1 + C2 + C3 + 1 * (n + 1) + 1 * n + 1 * (m + 1) + 1 * m + C8
## 3. Supprimer toutes les constantes additives
# 1 * (n + 1) + 1 * n + 1 * (m + 1) + 1 * m
## 4. Réduire / simplifier de manière mathématique
# n + 1 + n + m + 1 + m
# 2n + 1 +  2m + 1
## 5. Lorsque l'on ne peut plus simplifier de manière mathématique, il faut à nouveau simplifier de manière informatique
# 2n + 2m + 2
# n + m

# Complexité réelle de l'algorithme : T(n, m) = 2n + 2m + 2
# Complexité asymptotique de l'algorithme : T(n,m) =O(n+m)

if __name__ == '__main__':
    # Vos tests ici
    print(f([1, 2], [1]))  # C1
    pass
