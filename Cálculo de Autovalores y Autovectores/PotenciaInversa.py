import numpy as np

def potenciaInversa(A, x, k):
    print("Matriz inversa de A:")
    B = np.linalg.inv(A)
    print(B)
    for it in range(k):
        x = np.dot(B, x)
        n, m = x.shape
        max = 0
        for i in range(n):
            if(x[i] > 0):
                d = x[i]
                s = 1
            else:
                d = -x[i]
                s = 0
            if(d > max):
                max = d
                s0 = s
        if(s0 == 0):
            max = -max
        x = x/max
        print(it + 1, ": Autovalor dominante de la inversa de A", max, "Autovector asociado", x[0],x[1])
    print("Autovalor de módulo mínimo:", 1/max)

print("Matriz A:")
A = np.array([[-18.0, 40],[-12, 26]])
print(A)
print("Vector ínicial:")
x = np.array([[1.0],[1]])
print(x)

potenciaInversa(A, x, 10)
