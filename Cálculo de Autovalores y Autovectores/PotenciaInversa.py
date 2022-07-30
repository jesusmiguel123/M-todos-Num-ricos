import numpy as np

def PotenciaInversa(A, x, k):
    B = np.linalg.inv(A)
    print(f"Matriz inversa de A:\n{B}")
    for it in range(k):
        x = np.dot(B, x)
        n, m = x.shape
        max = 0
        for i in range(n):
            (d, s) = (x[i], 1) if x[i] > 0 else (-x[i], 0)
            (max, s0) = (d, s) if d > max else (max, s0)
        max = -max if s0 == 0 else max
        x = x/max
        print(f"{it + 1}: Autovalor dominante de la inversa de A: {max[0]} - Autovector asociado: [", end="")
        for e in x[:-1]:
            print(e[0], end=" ")
        print(f"{x[-1][0]}]")
    print(f"Autovalor de módulo mínimo: {1/max[0]}")


def main():
    A = np.array([[-18., 40.],
                  [-12., 26.]])
    print(f"Matriz A:\n{A}")
    x = np.array([[1.],
                  [1.]])
    print(f"Vector ínicial:\n{x}")

    PotenciaInversa(A, x, 10)

if __name__ == "__main__":
    main()