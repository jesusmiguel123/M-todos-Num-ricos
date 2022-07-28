import numpy as np

def Potencia(A, x, k):
    for it in range(k):
        x = np.dot(A, x)
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
        print(it + 1, ": Autovalor dominante", max, "Autovector asociado", x[0],x[1],x[2])

print("Matriz A:")
A = np.array([[3.0, -1, 0],[-1, 2, -1],[0, -1, 3]])
print(A)
print("Vector ínicial:")
x = np.array([[1.0],[1],[1]])
print(x)

Potencia(A, x, 10)
    
        
