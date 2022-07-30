import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

def evaluar(var, fun, x):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    f = f.subs(vars, x)
    f = f.evalf()
    return f

def PuntoFijo(var, fun0, fun1, x, k):
    lx, lev, le = [], [], []
    for i in range(k):
        x1 = evaluar(var, fun1, x)
        e = x1 - x if (x1 - x) > 0 else -(x1 - x)
        x = x1
        lx.append(x), lev.append(evaluar(var, fun0, x)), le.append(e)
    return lx, lev, le

def PuntoFijoParada(var, fun0, fun1, x, tol):
    e, i = 100000000000000, 0
    while(e > tol and i < 1000):
        x1 = evaluar(var, fun1, x)
        e = x1 - x if (x1 - x) > 0 else -(x1 - x)
        x = x1
        print(f"{i + 1}: x = {x} - f(x) = {evaluar(var, fun0, x)} - ea = {e}")
        i = i + 1
    return i

def main():
    var = 'x'
    fun0 = 'x**3 - 13*x - 12'
    fun1 = '(13*x + 12)**(1/3)'
    x0 = 4.5
    iter = 10

    print("Función original: ")
    sym.pprint(sym.sympify(fun0))
    print("Función para punto fijo: ")
    sym.pprint(sym.sympify(fun1))

    itera = np.arange(1, iter + 1, 1)
    
    lx, lfx, error = PuntoFijo(var, fun0, fun1, x0, iter)

    for i in range(iter):
        print(f"{i + 1}: x = {lx[i]} - f(x) = {lfx[i]} - ea = {error[i]}")

    fig, ax = plt.subplots()
    ax.plot(itera, error)

    ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
    ax.grid()

    plt.show()

if __name__ == "__main__":
    main()