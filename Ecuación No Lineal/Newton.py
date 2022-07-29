import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

def evaluar(var, fun, x):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    f = f.subs(vars, x)
    f = f.evalf()
    return f

def Dx(var, fun):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    k = sym.diff(f, vars)
    return k

def Diferenciar(var, fun, x):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    k = sym.diff(f, vars)
    k = k.subs(vars, x)
    k = k.evalf()
    return k

def Newton(var, fun, x, k):
    lx, lev, le = [], [], []
    for i in range(k):
        x1 = x - evaluar(var, fun, x)/Diferenciar(var, fun, x)
        e = x1 - x if (x1 - x) > 0 else -(x1 - x)
        x = x1
        lx.append(x), lev.append(evaluar(var, fun, x)), le.append(e)
    return lx, lev, le

def NewtonParada(var, fun, x, tol):
    e, i = 10000000000000, 0
    while(e > tol and i < 1000):
        x1 = x - evaluar(var, fun, x)/Diferenciar(var, fun, x)
        e = x1 - x if (x1 - x) > 0 else -(x1 - x)
        x = x1
        print(f"{i + 1}: x = {x} - f(x) = {evaluar(var, fun, x)} - ea = {e}")
        i = i + 1
    return i

def main():
    var = 'x'
    fun = 'x**7 - 13*x - 12'
    x0 = 4.5
    iter = 10

    dx = Dx(var, fun)

    print("Función: ")
    sym.pprint(sym.sympify(fun))
    print("Derivada: ")
    sym.pprint(dx)

    itera = np.arange(1, iter + 1, 1)

    lx, lfx, error = Newton(var, fun, x0, iter)

    for i in range(iter):
        print(f"{i + 1}: x = {lx[i]} - f(x) = {lfx[i]} - ea = {error[i]}")

    fig, ax = plt.subplots()
    ax.plot(itera, error)

    ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
    ax.grid()

    plt.show()

if __name__ == "__main__":
    main()