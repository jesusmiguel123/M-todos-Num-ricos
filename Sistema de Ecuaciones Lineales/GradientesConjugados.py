import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la

def gradConjugados(A, x0, b, tol):
    x = x0
    r = b
    ro = la.norm(r, 2)**2
    ro1 = ro
    k = 0
    while(ro**0.5 > tol*la.norm(b, 2)):
        if(k == 0):
            p = r
        else:
            B = ro1/ro
            p = r + B*p
            ro = ro1
        w = np.dot(A, p)
        alfa = ro1/(np.dot(p.T, w))
        x = x + alfa*p
        r = r - alfa*w
        ro1 = la.norm(r, 2)**2
        k = k + 1
        print("Iteración", k)
        print(x)

print("Matriz A:")
A = np.array([[4.0, -1, 0, -1, 0, 0],[-1, 4, -1, 0, -1, 0],[0, -1, 4, 0, 0, -1],[-1, 0, 0, 4, -1, 0],[0, -1, 0, -1, 4, -1],[0, 0, -1, 0, -1, 4]])
print(A)
print("Vector columna b:")
b = np.array([[0],[5],[0],[6],[-2],[6]])
print(b)
print("Solución x0:")
x0 = np.array([[0],[0],[0],[0],[0],[0]])
print(x0)

gradConjugados(A, x0, b, 0.0000000001)
