import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

def evaluar(var, fun, x):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    f = f.subs(vars, x)
    f = f.evalf()
    return f

def Muller(var, fun, x0, x1, x2, k):
    la, lb, lc, lx3, lev, le = [], [], [], [], [], []
    for i in range(k):
        a, b, c = x0, x1, x2
        h0, h1 = x1 - x0, x2 - x1
        d0 = (evaluar(var, fun, x1) - evaluar(var, fun, x0))/(x1 - x0)
        d1 = (evaluar(var, fun, x2) - evaluar(var, fun, x1))/(x2 - x1)
        a, b, c = (d1 - d0)/(h1 + h0), a*h1 + d1, evaluar(var, fun, x2)
        dis = (b**2 - 4*a*c)**0.5
        dsum = b + dis if (b + dis) > 0 else -(b + dis)
        dres = b - dis if (b - dis) > 0 else -(b - dis)
        d = dsum if dsum > dres else dres
        x3 = x2 - 2*c/d
        x0, x1 = x1, x2
        e = x3 - x2 if (x3 - x2) > 0 else -(x3 - x2)
        x2 = x3
        la.append(a), lb.append(b), lc.append(c), lx3.append(x3), lev.append(evaluar(var, fun, x3)), le.append(e)
        if(e == 0):
            break
    return la, lb, lc, lx3, lev, le

def MullerParada(var, fun, x0, x1, x2, tol):
    e, i = 1000000000000, 0
    while(e > tol and i < 1000):
        a, b, c = x0, x1, x2
        h0, h1 = x1 - x0, x2 - x1
        d0 = (evaluar(var, fun, x1) - evaluar(var, fun, x0))/(x1 - x0)
        d1 = (evaluar(var, fun, x2) - evaluar(var, fun, x1))/(x2 - x1)
        a, b, c = (d1 - d0)/(h1 + h0), a*h1 + d1, evaluar(var, fun, x2)
        dis = (b**2 - 4*a*c)**0.5
        dsum = b + dis if (b + dis) > 0 else -(b + dis)
        dres = b - dis if (b - dis) > 0 else -(b - dis)
        d = dsum if dsum > dres else dres
        x3 = x2 - 2*c/d
        x0, x1 = x1, x2
        e = x3 - x2 if (x3 - x2) > 0 else -(x3 - x2)
        x2 = x3
        print(f"{i + 1}: x0 = {a}, x1 = {b}, x2 = {c}, x3 = {x3}, f(x3) = {evaluar(var, fun, x3)}, ea = {e}")
        i = i + 1
    return i

def main():
    var = 'x'
    fun = 'x**3 - sin(x)'
    x0, x1, x2 = 1.5, 1.2, 1
    iter = 7

    print("Función: ")
    sym.pprint(sym.sympify(fun))

    la, lb, lc, lx3, lfx3, error  = Muller(var, fun, x0, x1, x2, iter)

    itera = np.arange(1, len(error) + 1, 1)

    for i in range(len(error)):
        print(f"{i + 1}: x0 = {la[i]} - x1 = {lb[i]} - x2 = {lc[i]} - x3 = {lx3[i]} - f(x3) = {lfx3[i]} - ea = {error[i]}")

    fig, ax = plt.subplots()
    ax.plot(itera, error)

    ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
    ax.grid()

    plt.show()

if __name__ == "__main__":
    main()