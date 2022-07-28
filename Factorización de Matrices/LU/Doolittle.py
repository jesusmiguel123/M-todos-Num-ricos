import numpy as np
import scipy.linalg as la

a = np.array([[1.0, 2, 5],[8, 4, 2],[2, 10, 6]])

print("Matriz A:")
print(a)

n, m = a.shape
L = np.eye(n)
U = np.diag(np.diag(a))

for k in range(n):
    for i in range(k, n):
        z = 0
        for p in range(k):
            z = z + L[k][p]*U[p][i]
        U[k][i] = a[k][i] - z
    for i in range(k + 1, n):
        z = 0
        for q in range(k):
            z = z + L[i][q]*U[q][k]
        L[i][k] = (a[i][k] - z)/U[k][k]

print("\nFactorización de Doolittle de A:\n")
print("Matriz triangular inferior L:")
print(L)
print("Matriz triangular superior U:")
print(U)
b = np.array([[1],[3],[-1]])
b = np.dot(np.linalg.inv(L),b)
b = np.dot(np.linalg.inv(U),b)
print(b)
