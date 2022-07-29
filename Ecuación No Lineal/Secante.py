import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

def evaluar(var, fun, x):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    f = f.subs(vars, x)
    f = f.evalf()
    return f

def Secante(var, fun, x0, x1, k):
    la, lb, lx2, lev, le = [], [], [], [], []
    for i in range(k):
        a, x0, x2 = x0, x1, x1 - evaluar(var, fun, x1)*(x1 -x0)/(evaluar(var, fun, x1) - evaluar(var, fun, x0))
        e = x2 - x1 if (x2 - x1) > 0 else -(x2 - x1)
        b, x1 = x1, x2
        if(e == 0):
            break
        la.append(a), lb.append(b), lx2.append(x2), lev.append(evaluar(var, fun, x2)), le.append(e)
    return la, lb, lx2, lev, le

def SecanteParada(var, fun, x0, x1, tol):
    e, i = 100000000000000, 0
    while(e > tol and i < 1000):
        a, x0, x2 = x0, x1, x1 - evaluar(var, fun, x1)*(x1 -x0)/(evaluar(var, fun, x1) - evaluar(var, fun, x0))
        e = x2 - x1 if (x2 - x1) > 0 else -(x2 - x1)
        b, x1 = x1, x2
        print(f"{i + 1}: x0 = {a} - x1 = {b} - x2 = {x2} - f(x2)= {evaluar(var, fun, x2)} - ea = {e}")
        i = i + 1
    return i

def main():
    var = 'x'
    fun = 'x**3 - sin(x)'
    x0, x1 = 1.1, 1.0
    iter = 7

    print("Función: ")
    sym.pprint(sym.sympify(fun))

    lxa, lxb, lxc, lfxc, error = Secante(var, fun, x0, x1, iter)

    itera = np.arange(1, len(error) + 1, 1)

    for i in range(len(error)):
        print(f"{i + 1}: x0 = {lxa[i]} - x1 = {lxb[i]} - x2 = {lxc[i]} - f(x2)= {lfxc[i]} - ea = {error[i]}")

    fig, ax = plt.subplots()
    ax.plot(itera, error)

    ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
    ax.grid()

    plt.show()

if __name__ == "__main__":
    main()