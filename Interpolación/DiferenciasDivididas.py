import sympy as sym

def Diferencias(p, n, val):
    n = n + 1
    a, b, c = p[:, 1], p[:, 0], p[:, 1]
    x = sym.symbols('x')
    f = sym.sympify('x')
    P = 0
    for j in range(1, n):
        for k in range(n - j):
            a[k] = (a[k+1] - a[k])/(b[j+k] - b[k])
            c[j] = a[k] if k == 0 else c[j]
    for l in range(n):
        ter = 1
        for m in range(l):
            ter = ter*(f - b[m])
        P = P + c[l]*ter
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
    P, res = Diferencias(p, gr, val)
    print(f"Polinomio de lagrange de grado {gr}:")
    sym.pprint(P)
    print("Polinomio de Lagrange simplificado:")
    P = sym.simplify(P)
    sym.pprint(P)
    print(f"Valor a evaluar: {val}")
    print(f"Valor obtenido: {res}")

if __name__ == "__main__":
    main()