def f(n: list) -> int:
    a: int = 0  # C2
    i: int = int(len(n) / 2)  # C3
    while i <= len(n):  # C4 * (n/2 + 1)
        j: int = 2  # C5 * n/2
        while j <= len(n):  # C6 * n/2 * (log(n-2) + 1)
            a += 1  # C7 * n/2 * log(n-2)
            j *= 2  # C8 * n/2 * log(n-2)
        i += 1  # C9 * n/2
    return a  # C10

## 1. Création de l'équation
# C1 + C2 + C3 + C4 * (n/2 + 1) + C5 * n/2 + C6 * n/2 * (log(n-2) + 1) + C7 * n/2 * log(n-2) + C8 * n/2 * log(n-2) + C9 * n/2 + C10
## 2. Mettre toutes les constantes multiplicatives à 1
# C1 + C2 + C3 + 1 * (n/2 + 1) + 1 * n/2 + 1 * n/2 * (log(n-2) + 1) + 1 * n/2 * log(n-2) + 1 * n/2 * log(n-2) + 1 * n/2 + C10
# 1 * (n/2 + 1) + 1 * n/2 + 1 * n/2 * (log(n-2) + 1) + 1 * n/2 * log(n-2) + 1 * n/2 * log(n-2) + 1 * n/2
## 3. Supprimer toutes les constantes additives
# n/2 + 1 + n/2 + n/2 * (log(n-2) + 1) + n/2 * log(n-2) + n/2 * log(n-2) + n/2
## 4. Réduire / simplifier de manière mathématique
# n/2 + 1 + n/2 + n/2 * log(n-2) + n/2 + n/2 * log(n-2) + n/2 * log(n-2) + n/2
# 3n/2 + 3(n/2 * log(n-2)) + 1
## 5. Lorsque l'on ne peut plus simplifier de manière mathématique, il faut à nouveau simplifier de manière informatique
# n/2 + n/2 * log(n-2)
# n + n * log(n-2)
# n + n * log(n)
## 6. Quand on a simplifié au maximum et qu'il reste plusieurs polynômes séparés par des additions, on ne garde que le plus important
# n * log(n)

# Complexité réelle de l'algorithme : T(n) = 3n/2 + 3(n/2 * log(n-2)) + 1
# Complexité asymptotique de l'algorithme : T(n) = O(n * log(n))


if __name__ == '__main__':
    # Vos tests ici
    print(f([1, 2]))  # C1
    pass
