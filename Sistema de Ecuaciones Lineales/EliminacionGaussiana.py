import numpy as np

def EliminacionGaussiana(A):
    n, m = A.shape
    x = np.zeros(n)
    for k in range(n - 1):
        max, l = 0, 0
        for i in range(k, n):
            t = A[i][k] if A[i][k] > 0 else -A[i][k]
            (max, l) = (t, i) if t > max else (max, l)  
        if(l != 0):
            for j in range(n + 1):
                A[k][j], A[l][j] = A[l][j], A[k][j]
        for j in range(k + 1, n):
            t = A[j][k]/A[k][k]
            for w in range(k, n + 1):
                A[j][w] = A[j][w] - t*A[k][w]
            
    x[n-1] = A[n-1][n]/A[n-1][n-1]
    for i in range(n):
        s = n - 1 - i
        c = A[s][n]
        for j in range(s + 1, n):
            c = c - A[s][j]*x[j]
        x[s] = c/A[s][s]
    return A, x

def main():
    A = np.array([[1.,  2., 5.,  1.],
                  [8.,  4., 2.,  3.],
                  [2., 10., 6., -1.]])
    print(f"Matriz A:\n{A}")

    A, x = EliminacionGaussiana(A)

    print(f"Matriz resultante:\n{A}")
    print(f"Vector solución: {x}")

if __name__ == "__main__":
    main()