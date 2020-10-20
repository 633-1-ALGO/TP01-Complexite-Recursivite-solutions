class Matrix:

    def __init__(self):
        self.matrix = [
            [
                "{}{}".format(j, i) for i in range(0, 10)  # C4 * 10
            ] for j in range(0, 10)  # C3 * 10
        ]  # C2

    def get(self, i, j):
        if i >= len(self.matrix) or j >= len(self.matrix[0]):  # C6
            raise ValueError("Indices out of bound")  # C7
        return self.matrix[i][j]  # C7


## 1. Création de l'équation
# C1 + C2 + C3 * 10 + C4 * 10 + C5 + C6 + C7
## 2. Mettre toutes les constantes multiplicatives à 1
# C1 + C2 + 1 * 10 + 1 * 10 + C5 + C6 + C7
## 3. Supprimer toutes les constantes additives
# 1 * 10 + 1 * 10
## 4. Réduire / simplifier de manière mathématique
# 10 + 10
# 20

# Complexité réelle de l'algorithme : T(n) = 20
# Complexité asymptotique de l'algorithme : T(n) = O(1)

if __name__ == '__main__':
    matrix = Matrix()  # C1
    print(matrix.get(9, 9))  # C5
