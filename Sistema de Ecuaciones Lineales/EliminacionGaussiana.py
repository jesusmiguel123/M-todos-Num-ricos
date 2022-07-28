import numpy as np
import scipy.linalg as la

a = np.array([[1.0, 2, 5, 1],[8, 4, 2, 3],[2, 10, 6, -1]])
print("Matriz A:")
print(a)

n, m = a.shape
x = np.zeros(n)

for k in range(n - 1):
    max = 0
    l = 0
    for i in range(k, n):
        t = a[i][k]
        if(t > 0):
            t = t
        else:
            t = -t
        if(t > max):
            max = t
            l = i
    if(l != 0):
        for j in range(n + 1):
            aux = a[l][j]
            a[l][j] = a[k][j]
            a[k][j] = aux
    for j in range(k + 1, n):
        t = a[j][k]/a[k][k]
        for w in range(k, n + 1):
            a[j][w] = a[j][w] - t*a[k][w]
            
x[n - 1] = a[n - 1][n]/a[n - 1][n - 1]
for i in range(n):
    s = n - 1 - i
    c = a[s][n]
    for j in range(s + 1, n):
        c = c - a[s][j]*x[j]
    x[s] = c/a[s][s]

print("Matriz resultante:")
print(a)
print("Vector solución:")
print(x)
