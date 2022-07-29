import numpy as np

def potenciaInversaDesplazada(A, x, l, k):
    I = np.eye(len(A))
    C = A - l * I
    print(f"Matriz C = A - landa * I:\n{C}")
    B = np.linalg.inv(C)
    print(f"Inversa de C:\n{B}")
    for it in range(k):
        x = np.dot(B, x)
        n, m = x.shape
        max = 0
        for i in range(n):
            (d, s) = (x[i], 1) if x[i] > 0 else (-x[i], 0)
            (max, s0) = (d, s) if d > max else (max, s0)
        max = -max if s0 == 0 else max
        x = x/max
        print(f"{it + 1}: Autovalor dominante de la inversa de C: {max[0]} - Autovector asociado: [", end="")
        for e in x[:-1]:
            print(e[0], end=" ")
        print(f"{x[-1][0]}]")
    print(f"Autovalor asociado a A: {1/max[0] + l}")

def main():
    A = np.array([[ 3., -1.,  0.],
                  [-1.,  2., -1.],
                  [ 0., -1.,  3.]])
    print(f"Matriz A:\n{A}")
    x = np.array([[5.],
                  [1.],
                  [1.]])
    print(f"Vector ínicial:\n{x}")
    l = 2.8
    print(f"Valor propio ínicial: {l}")
    
    potenciaInversaDesplazada(A, x, l, 10)

if __name__ == "__main__":
    main()