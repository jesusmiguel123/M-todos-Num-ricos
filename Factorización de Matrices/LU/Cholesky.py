from numpy import array
from scipy.linalg import cholesky

def main():
    A = array([[ 5., 1., -2., 0.],
               [ 1., 2., -0., 0.],
               [-2., 0.,  4., 1.],
               [ 0., 0.,  1., 3.]])
    print(f"Matriz A:\n{A}")

    L = cholesky(A, lower = True)
    U = cholesky(A, lower = False)

    print("\nFactorización LU de A:\n")
    print(f"Matriz triangular inferior L:\n{L}")
    print(f"\nMatriz triangular superior L-transpuesta:\n{U}")

if __name__ == "__main__":
    main()