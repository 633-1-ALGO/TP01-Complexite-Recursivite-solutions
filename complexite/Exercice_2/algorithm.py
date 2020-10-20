def f(n: list) -> (int, int):
    a, b = 0, 0  # C2, C3
    for i in range(0, len(n)):  # C4 * (n + 1)
        a = a + i  # C5 * n
    for j in range(0, len(n)):  # C6 * (n + 1)
        b = b + j * 2  # C7 * n
    return a, b  # C8

## 1. Création de l'équation
# C1 + C2 + C3 + C4 * (n + 1) + C5 * n + C6 * (n + 1) + C7 * n + C8
## 2. Mettre toutes les constantes multiplicatives à 1
# C1 + C2 + C3 + 1 * (n + 1) + 1 * n + 1 * (n + 1) + 1 * n + C8
## 3. Supprimer toutes les constantes additives
# 1 * (n + 1) + 1 * n + 1 * (n + 1) + 1 * n
## 4. Réduire / simplifier de manière mathématique
# n + 1 + n + n + 1 + n
# 4n + 2
## 5. Lorsque l'on ne peut plus simplifier de manière mathématique, il faut à nouveau simplifier de manière informatique
# n

# Complexité réelle de l'algorithme : T(n) = 4n + 2
# Complexité asymptotique de l'algorithme : T(n) = O(n)

if __name__ == '__main__':
    # Vos tests ici
    print(f([1, 2]))  # C1
    pass
