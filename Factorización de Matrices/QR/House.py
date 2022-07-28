import numpy as np
import scipy.linalg as la

a = np.array([[1.0, 2, 3],[3, 1, 2],[1, 3, 1]])

print("Matriz A:")
print(a)

Q, R = np.linalg.qr(a)

print("\nFactorización de Hoseholswe de A:\n")
print("Matriz Q:")
print(Q)
print("Matriz R:")
print(R)
