import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

def evaluar(var, fun, x):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    f = f.subs(vars, x)
    f = f.evalf()
    return f

def regulaFalsa(var, fun, a, b, k):
    la, lb, lc, lev, le = [], [], [], [], []
    c = 0
    for i in range(k):
        a1, b1, c1 = a, b, (b*evaluar(var, fun, a)-a*evaluar(var, fun, b))/(evaluar(var, fun, a) - evaluar(var, fun, b))
        if(evaluar(var, fun, c1) == 0):
            return a, b, c1, 0, 0
        if(evaluar(var, fun, a)*evaluar(var, fun, c1) < 0):
            b = c1
        else:
            a = c1
        e = c1 - c if (c1 - c) > 0 else -(c1 - c)
        c = c1
        la.append(a1), lb.append(b1), lc.append(c), lev.append(evaluar(var, fun, c)), le.append(e)
    return la, lb, lc, lev, le

def regulaFalsaParada(var, fun, a, b, tol):
    e, i, c = 100000000000, 0, 0
    while(e > tol and i < 1000):
        a1, b1, c1 = a, b, (b*evaluar(var, fun, a)-a*evaluar(var, fun, b))/(evaluar(var, fun, a) - evaluar(var, fun, b))
        if(evaluar(var, fun, c1) == 0):
            return a, b, c1, 0, 0
        if(evaluar(var, fun, a)*evaluar(var, fun, c1) < 0):
            b = c1
        else:
            a = c1
        e = c1 - c if (c1 - c) > 0 else -(c1 - c)
        c = c1
        print(f"{i + 1}: x1 = {a1} - xu = {b1} - xr = {c} - f(xr) = {evaluar(var, fun, c)} - ea = {e}")
        i = i + 1
    return i

def main():
    var = 'x'
    fun = 'x**3 + x - 1'
    x0, x1 = 0, 1
    iter = 10

    print("Función: ")
    sym.pprint(sym.sympify(fun))

    itera = np.arange(1, iter + 1, 1)

    lx, lxu, lxr, lfxr, error = regulaFalsa(var, fun, x0, x1, iter)

    for i in range(iter):
        print(f"{i + 1}: x1 = {lx[i]} - xu = {lxu[i]} - xr = {lxr[i]} - f(xr) = {lfxr[i]} - ea = {error[i]}")

    fig, ax = plt.subplots()
    ax.plot(itera, error)

    ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
    ax.grid()

    plt.show()

if __name__ == "__main__":
    main()