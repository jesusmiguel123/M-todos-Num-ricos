import sympy as sym

def Lagrange(p, n, val):
    n = n + 1
    x = sym.symbols('x')
    f = sym.sympify('x')
    P = 0
    for i in range(n):
        num = 1
        den = 1
        for k in range(n):
            if(i != k):
                a = f - p.row(k)[0]
                num = num*a
            if((p.row(i)[0] - p.row(k)[0]) != 0):
                b = p.row(i)[0] - p.row(k)[0]
                den = den*b
        l = num/den
        P = P + p.row(i)[1]*l
    res = P.subs(x, val)
    res = res.evalf()
    return P, res

p = sym.Matrix([[1,3],[2,1],[3,4]])
val = 2.5
gr = 2

print("Puntos:")
sym.pprint(p)
P, res = Lagrange(p, gr, val)
print("Polinomio de lagrange de grado", gr, ":")
sym.pprint(P)
print("Polinomio de Lagrange simplificado:")
P = sym.simplify(P)
sym.pprint(P)
print("Valor a evaluar:", val)
print("Valor obtenido:", res)
