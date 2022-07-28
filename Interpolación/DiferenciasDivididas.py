import sympy as sym
import numpy as np

def Diferencias(p, n, val):
    n = n + 1
    c = np.zeros(n)
    a = np.zeros(n)
    b = np.zeros(n)
    x = sym.symbols('x')
    f = sym.sympify('x')
    P = 0
    for i in range(n):
        c[i] = p.row(i)[1]
    for w in range(n):
        a[w] = p.row(w)[1]
    for z in range(n):
        b[z] = p.row(z)[0]
    for j in range(1, n):
        for k in range(n - j):
            num = a[k + 1] - a[k]
            den = b[j + k] - b[k]
            a[k] = num/den
            if(k == 0):
                c[j] = a[k]
    for l in range(n):
        ter = 1
        for m in range(l):
            dif = f - b[m]
            ter = ter*dif
        P = P + c[l]*ter
    res = P.subs(x, val)
    res = res.evalf()
    return P, res

p = sym.Matrix([[1,3],[2,1],[3,4]])
val = 2.5
gr = 2

print("Puntos:")
sym.pprint(p)
P, res = Diferencias(p, gr, val)
print("Polinomio de lagrange de grado", gr, ":")
sym.pprint(P)
print("Polinomio de Lagrange simplificado:")
P = sym.simplify(P)
sym.pprint(P)
print("Valor a evaluar:", val)
print("Valor obtenido:", res)
