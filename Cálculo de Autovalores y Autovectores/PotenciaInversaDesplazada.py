import numpy as np

def potenciaInversaDesplazada(A, x, l, k):
    I = np.eye(len(A))
    print("Matriz C = A - landa * I:")
    C = A - l * I
    print(C)
    print("Inversa de C:")
    B = np.linalg.inv(C)
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
        print(it + 1, ": Autovalor dominante de la inversa de C", max, "Autovector asociado", x[0],x[1], x[2])
    print("Autovalor asociado a A:", 1/max + l)

print("Matriz A:")
A = np.array([[3, -1, 0],[-1, 2, -1],[0, -1, 3]])
print(A)
print("Vector ínicial:")
x = np.array([[5.0],[1],[1]])
print(x)
l = 2.8
print("Valor propio ínicial:", l)
potenciaInversaDesplazada(A, x, l, 10)
