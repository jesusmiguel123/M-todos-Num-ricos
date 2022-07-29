import numpy as np
from scipy.linalg import qr

def main():
    A = np.array([[1., 2., 3.],
                  [3., 1., 2.],
                  [1., 3., 1.]])
    print(f"Matriz A:\n{A}")

    Q, R = qr(A)

    print("\nFactorización QR de A:\n")
    print(f"Matriz ortogonal Q:\n{Q}")
    print(f"\nMatriz triangular superior R:\n{R}")

if __name__ == "__main__":
    main()