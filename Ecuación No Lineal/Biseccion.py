import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

def evaluar(var, fun, x):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    f = f.subs(vars, x)
    f = f.evalf()
    return f

def Biseccion(var, fun, a, b, k):
    lx, lxu, lxr, lfr, le = [], [], [], [], []
    c = 0
    for i in range(k):
        a1, b1, c1 = a, b, (a + b)/2
        if(evaluar(var, fun, c) == 0):
            return a, b, c, 0, 0
        if(evaluar(var, fun, a)*evaluar(var, fun, c1) < 0):
            b = c1
        else:
            a = c1
        e = c1 - c if (c1 - c) > 0 else -(c1 - c)
        c = c1
        lx.append(a1), lxu.append(b1), lxr.append(c), lfr.append(evaluar(var, fun, c)), le.append(e)
    return lx, lxu, lxr, lfr, le

def BiseccionParada(var, fun, a, b, tol):
    e, i, c = 10000000000000, 0, 0
    while(e > tol and i < 1000):
        a1, b1, c1 = a, b, (a + b)/2
        if(evaluar(var, fun, c) == 0):
            return a, b, c, 0, 0
        if(evaluar(var, fun, a)*evaluar(var, fun, c1) < 0):
            b = c1
        else:
            a = c1
        e = c1 - c if (c1 - c) > 0 else -(c1 - c)
        c = c1
        print(f"{i + 1}: x1 = {x} - xu = {xu} - xr = {xr} - f(r) = {fr} - {evaluar(var, fun, c)} - ea = {e}")
        i = i + 1
    return i

def main():
    var = 'x'
    fun1 = 'sin(2*x) - 2*cos(x/3)'
    x0, x1 = 4, 5
    iter = 10

    print("Función: ")
    sym.pprint(sym.sympify(fun1))

    itera = np.arange(1, iter + 1, 1)

    lx, lxu, lxr, lfr, error = Biseccion(var, fun1, x0, x1, iter)

    for i in range(iter):
        print(f"{i + 1}: x1 = {lx[i]} - xu = {lxu[i]} - xr = {lxr[i]} - f(r) = {lfr[i]} - ea = {error[i]}")

    fig, ax = plt.subplots()
    ax.plot(itera, error)

    ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
    ax.grid()

    plt.show()

if __name__ == "__main__":
    main()