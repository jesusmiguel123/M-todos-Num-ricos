import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la

def Gauss(A, b, x0, k):
    D = np.diag(np.diag(A))
    L = -(np.tril(A) - D)
    U = -(np.triu(A) - D)
    x = x0
    for i in range(k):
        T = np.dot(la.inv(D - L), U)
        c = np.dot(la.inv(D - L), b)
        x = np.dot(T, x) + c
        r = b - np.dot(A, x)
        e = la.norm(r, 2)
    return x, e

def GaussParada(A, b, x0, tau):
    print("\n0 : x=", x0[0], ",", x0[1], ",", x0[2], "error= -")
    D = np.diag(np.diag(A))
    L = -(np.tril(A) - D)
    U = -(np.triu(A) - D)
    r = b - np.dot(A, x0)
    e = la.norm(r, 2)
    x = x0
    i = 0
    while(tau > e and i <= 100):
        T = np.dot(la.inv(D - L), U)
        c = np.dot(la.inv(D - L), b)
        x = np.dot(T, x) + c
        r = b - np.dot(A, x)
        e = la.norm(r, 2)
        print(i + 1, ": x=", x[0], ",", x[1], ",", x[2], "error=", e)
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
print("\n0 : x=", x0[0], ",", x0[1], ",", x0[2], "error= -")

iter = k
itera = np.arange(1, iter + 1, 1)
error = np.zeros(len(itera))

for i in range(iter):
    x, error[i] = Gauss(A, b, x0, itera[i])
    print(i + 1, ": x=", x[0], ",", x[1], ",", x[2], "error=", error[i])

fig, ax = plt.subplots()
ax.plot(itera, error)

ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
ax.grid()

plt.show()
