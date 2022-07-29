import sympy as sym

def Lagrange(p, n, val):
    n = n + 1
    x = sym.symbols('x')
    f = sym.sympify('x')
    P = 0
    for i in range(n):
        num, den = 1, 1
        for k in range(n):
            num = num*(f - p.row(k)[0]) if i != k else num
            den = den*(p.row(i)[0] - p.row(k)[0]) if (p.row(i)[0] - p.row(k)[0]) != 0 else den
        l = num/den
        P = P + p.row(i)[1]*l
    res = P.subs(x, val).evalf()
    return P, res

def main():
    p = sym.Matrix([[1, 3],
                    [2, 1],
                    [3, 4]])
    val = 2.5
    gr = 2

    print("Puntos:")
    sym.pprint(p)
    P, res = Lagrange(p, gr, val)
    print(f"Polinomio de lagrange de grado {gr}:")
    sym.pprint(P)
    print("Polinomio de Lagrange simplificado:")
    P = sym.simplify(P)
    sym.pprint(P)
    print(f"Valor a evaluar: {val}")
    print(f"Valor obtenido: {res}")

if __name__ == "__main__":
    main()