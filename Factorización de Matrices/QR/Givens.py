import numpy as np

def GivensMatrix(A, i, j):
    n, m = A.shape
    G = np.eye(n)
    r = (A[j][j]**2 + A[i][j]**2)**0.5
    c, s = A[j][j]/r, -A[i][j]/r
    G[i][i], G[i][j] =  c, s
    G[j][i], G[j][j] = -s, c
    return G

def GivensQR(A):
    n, m = A.shape
    G, R = np.eye(n), A
    for i in range(1, n):
        for j in range(0, i):
            Gx = GivensMatrix(R, i, j)
            G = np.dot(Gx, G)
            R = np.dot(Gx, R)
    Q = G.T
    return Q, R

def main():
    A = np.array([[1., 2., 3.],
                  [3., 1., 2.],
                  [1., 3., 1.]])
    print(f"Matriz A:\n{A}")

    Q, R = GivensQR(A)

    print("\nFactorización QR de A:\n")
    print(f"Matriz ortogonal Q:\n{Q}")
    print(f"\nMatriz triangular superior R:\n{R}")

if __name__ == "__main__":
    main()