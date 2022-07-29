import numpy as np

def Doolittle(A):
    n, m = A.shape
    L = np.eye(n)
    U = np.diag(np.diag(A))
    for k in range(n):
        for i in range(k, n):
            z = 0
            for p in range(k):
                z = z + L[k][p]*U[p][i]
            U[k][i] = A[k][i] - z
        for i in range(k + 1, n):
            z = 0
            for q in range(k):
                z = z + L[i][q]*U[q][k]
            L[i][k] = (A[i][k] - z)/U[k][k]
    return L, U

def main():
    A = np.array([[1.,  2., 5.],
                  [8.,  4., 2.],
                  [2., 10., 6.]])
    print(f"Matriz A:\n{A}")

    L, U = Doolittle(A)

    print("\nFactorización LU de A:\n")
    print(f"Matriz triangular inferior L:\n{L}")
    print(f"\nMatriz triangular superior U:\n{U}")

if __name__ == "__main__":
    main()