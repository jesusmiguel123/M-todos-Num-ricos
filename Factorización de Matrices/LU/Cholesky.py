from numpy import array
from scipy.linalg import cholesky

a = array([[5, 1, -2, 0],[1, 2, -0, 0],[-2, 0, 4, 1],[0, 0, 1, 3]])

print("Matriz A:")
print(a)

L = cholesky(a, lower = True)
U = cholesky(a, lower = False)

print("\nFactorización de Cholesky de A:\n")
print("Matriz triangular inferior L:")
print(L)
print("Matriz triangular superior L-transpuesta:")
print(U)
