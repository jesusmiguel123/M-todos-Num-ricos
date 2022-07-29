import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la

def GaussSeidel(A, b, x0, k):
    lx, le = [], []
    D = np.diag(np.diag(A))
    L, U = np.tril(A), np.triu(A) - D
    x = x0
    for i in range(k):
        T, c = -np.dot(la.inv(L), U), np.dot(la.inv(L), b)
        x = np.dot(T, x) + c
        r = b - np.dot(A, x)
        e = la.norm(r, 2)
        lx.append(x), le.append(e)
    return lx, le

def GaussSeidelParada(A, b, x0, tau):
    D = np.diag(np.diag(A))
    L, U = np.tril(A), np.triu(A) - D
    r = b - np.dot(A, x0)
    e, x, i = la.norm(r, 2), x0, 0
    while(tau > e and i <= 100):
        T, c = -np.dot(la.inv(L), U), np.dot(la.inv(L), b)
        x = np.dot(T, x) + c
        r = b - np.dot(A, x)
        e = la.norm(r, 2)
        print(f"{i + 1}: x = {x} - error = {e}")
        i = i + 1
    return x, i

def main():
    A = np.array([[16.,   3.],
                  [ 7., -11.]])
    print(f"Matriz A:\n{A}")
    b = np.array([[11.],
                  [13.]])
    print(f"Vector columna b:\n{b}")
    x0 = np.array([[1.],
                   [1.]])
    print(f"Solución x0:\n{x0}")
    iter = 10

    itera = np.arange(1, iter + 1, 1)

    lx, error = GaussSeidel(A, b, x0, iter)

    for i in range(iter):
        print(f"{i + 1}: x = {lx[i].T} - error = {error[i]}")

    fig, ax = plt.subplots()
    ax.plot(itera, error)

    ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
    ax.grid()

    plt.show()

if __name__ == "__main__":
    main()