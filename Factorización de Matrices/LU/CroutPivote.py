import numpy as np

def Pivotar(A):
    n, m = A.shape
    for k in range(n):
        max, l = 0, 0
        for i in range(k, n):
            t = A[i][k] if A[i][k] > 0 else -A[i][k]
            max, l = t, i if t > max else max, l
        if(l != 0):
            for j in range(n):
                A[k][j], A[l][j] = A[l][j], A[k][j]
    return A

def Crout(A):
    n, m = A.shape
    L, U = np.eye(n), np.eye(n)
    for k in range(n):
        for i in range(k, n):
            z = 0
            for p in range(k):
                z = z + L[i][p]*U[p][k]
            L[i][k] = A[i][k] - z
        for i in range(k + 1, n):
            z = 0
            for q in range(k):
                z = z + L[k][q]*U[q][i]
            U[k][i] = (A[k][i] - z)/L[k][k]
    return L, U

def main():
    A = np.array([[1.,  2., 5.],
                  [8.,  4., 2.],
                  [2., 10., 6.]])
    print(f"Matriz A:\n{A}")

    A = Pivotar(A)

    print(f"Matriz pivotada:\n{A}")

    L, U = Crout(A)

    print("\nFactorización LU de A:\n")
    print(f"Matriz triangular inferior L:\n{L}")
    print(f"\nMatriz triangular superior U:\n{U}")

if __name__ == "__main__":
    main()