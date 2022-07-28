import numpy as np

def Givens(A, i, j):
    i = i - 1
    j = j - 1
    n, m = A.shape
    G = np.eye(n)
    r = (A[j][j]**2 + A[i][j]**2)**0.5
    c = A[j][j]/r
    s = -A[i][j]/r
    G[j][i] = -s
    G[i][j] = s
    G[i][i] = c
    G[j][j] = c
    return G

A = np.array([[1, 2, 3],[3, 1, 2],[1, 3, 1]])
G1 = Givens(A, 2, 1)
print(G1)
A = np.dot(G1, A)
print(A)
G2 = Givens(A, 3, 1)
print(G2)
A = np.dot(G2, A)
print(A)
G3 = Givens(A, 3, 2)
print(G3)
A = np.dot(G3, A)
print(A)
Q = np.dot(np.dot(G1.T, G2.T), G3.T)
print(Q)
print(np.dot(Q, A))
