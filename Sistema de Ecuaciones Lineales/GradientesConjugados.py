import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la

def gradConjugados(A, b, x0, k):
    lx, le = [], []
    x, r = x0, b
    ro = la.norm(r, 2)**2
    ro1, p = ro, r
    for i in range(k):
        w = np.dot(A, p)
        alfa = ro1/(np.dot(p.T, w))
        x, r = x + alfa*p, r - alfa*w
        ro1 = la.norm(r, 2)**2
        p = r + (ro1/ro)*p
        ro = ro1
        lx.append(x), le.append(ro)
    return lx, le

def gradConjugadosParada(A, b, x0, tol):
    x, r = x0, b
    ro = la.norm(r, 2)**2
    ro1, k, p = ro, 0, r
    while(ro**0.5 > tol*la.norm(b, 2)):
        w = np.dot(A, p)
        alfa = ro1/(np.dot(p.T, w))
        x, r = x + alfa*p, r - alfa*w
        ro1 = la.norm(r, 2)**2
        p = r + (ro1/ro)*p
        ro = ro1
        print(f"{i + 1}: x = {x.T} - error = {ro}")
        k = k + 1

def main():
    A = np.array([[ 4., -1.,  0., -1.,  0.,  0.],
                  [-1.,  4., -1.,  0., -1.,  0.],
                  [ 0., -1.,  4.,  0.,  0., -1.],
                  [-1.,  0.,  0.,  4., -1.,  0.],
                  [ 0., -1.,  0., -1.,  4., -1.],
                  [ 0.,  0., -1.,  0., -1.,  4.]])
    print(f"Matriz A:\n{A}")
    b = np.array([[ 0.],
                  [ 5.],
                  [ 0.],
                  [ 6.],
                  [-2.],
                  [ 6.]])
    print(f"Vector columna b:\n{b}")
    x0 = np.array([[0.],
                   [0.],
                   [0.],
                   [0.],
                   [0.],
                   [0.]])
    print(f"Solución x0:\n{x0}")
    iter = 10

    itera = np.arange(1, iter + 1, 1)

    lx, error = gradConjugados(A, b, x0, iter)

    for i in range(iter):
        print(f"{i + 1}: x = {lx[i].T} - error = {error[i]}")

    fig, ax = plt.subplots()
    ax.plot(itera, error)

    ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
    ax.grid()

    plt.show()

if __name__ == "__main__":
    main()