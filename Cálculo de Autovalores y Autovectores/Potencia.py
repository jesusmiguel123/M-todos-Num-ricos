import numpy as np

def Potencia(A, x, k):
    for it in range(k):
        x = np.dot(A, x)
        n, m = x.shape
        max = 0
        for i in range(n):
            (d, s) = (x[i], 1) if x[i] > 0 else (-x[i], 0)
            (max, s0) = (d, s) if d > max else (max, s0)
        max = -max if s0 == 0 else max
        x = x/max
        print(f"{it + 1}: Autovalor dominante: {max[0]} - Autovector asociado: [", end="")
        for e in x[:-1]:
            print(e[0], end=" ")
        print(f"{x[-1][0]}]")

def main():
    A = np.array([[ 3., -1.,  0.],
                  [-1.,  2., -1.],
                  [ 0., -1.,  3.]])
    print(f"Matriz A:\n{A}")
    x = np.array([[1.],
                  [1.],
                  [1.]])
    print(f"Vector ínicial:\n{x}")

    Potencia(A, x, 10)

if __name__ == "__main__":
    main()