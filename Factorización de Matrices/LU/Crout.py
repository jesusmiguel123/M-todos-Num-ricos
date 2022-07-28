import numpy as np
import scipy.linalg as la

a = np.array([[1.0, 2, 5],[8, 4, 2],[2, 10, 6]])
print("Matriz A:")
print(a)

n, m = a.shape
L = np.eye(n)
U = np.eye(n)

for k in range(n):
    for i in range(k, n):
        z = 0
        for p in range(k):
            z = z + L[i][p]*U[p][k]
        L[i][k] = a[i][k] - z
    for i in range(k + 1, n):
        z = 0
        for q in range(k):
            z = z + L[k][q]*U[q][i]
        U[k][i] = (a[k][i] - z)/L[k][k]

print("\nFactorización de Doolittle de A:\n")
print("Matriz triangular inferior L:")
print(L)
print("Matriz triangular superior U:")
print(U)
