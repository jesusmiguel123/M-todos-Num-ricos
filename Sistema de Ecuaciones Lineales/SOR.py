import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la

def SOR(A, b, x0, k):
    D = np.diag(np.diag(A))
    L = -(np.tril(A) - D)
    U = -(np.triu(A) - D)
    x = x0
    for i in range(k):
        T = np.dot(la.inv(D - np.dot(w, L)), (np.dot(1 - w, D) + np.dot(w, U)))
        c = np.dot(np.dot(w, la.inv(D - np.dot(w, L))), b)
        x = np.dot(T, x) + c
        r = b - np.dot(A, x)
        e = la.norm(r, 2)
    return x, e

def SORParada(A, b, x0, w, tau):
    D = np.diag(np.diag(A))
    L = -(np.tril(A) - D)
    U = -(np.triu(A) - D)
    r0 = b - np.dot(A, x0)
    r = b - np.dot(A, x0)
    x = x0
    i = 0
    while(la.norm(r)/la.norm(r0) > tau and i <= 10):
        T = np.dot(la.inv(D - np.dot(w, L)), (np.dot(1 - w, D) + np.dot(w, U)))
        c = np.dot(np.dot(w, la.inv(D - np.dot(w, L))), b)
        x = np.dot(T, x) + c
        r = b - np.dot(A, x)
        e = la.norm(r, 2)
        i = i + 1
    return x, i

print("Matriz A:")
A = np.array([[1, 2, 5],[8, 4, 2],[2, 10, 6]])
print(A)
print("Vector columna b:")
b = np.array([[1],[3],[-1]])
print(b)
print("Solución x0:")
x0 = np.array([[0],[0],[0]])
print(x0)

k = 10
tau = 0.0001

print("\n0 : x=", x0[0], ",", x0[1], ",", x0[2], "error= -")

iter = k
w = np.arange(0.1, 2.0, 0.1)
it = np.zeros(len(w))

for i in range(iter):
    x, it[i] = SORParada(A, b, x0, w[i], tau)
    print(i + 1, ": x=", x[0], ",", x[1], ",", x[2], "error=", it[i], "w=", w[i])

fig, ax = plt.subplots()
ax.plot(w, it)

ax.set(xlabel='w',ylabel='iteraciones',title='w vs Iteraciones')
ax.grid()

plt.show()
