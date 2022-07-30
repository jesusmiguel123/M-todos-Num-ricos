import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

def norma(x):
    n = 0
    for i, a in enumerate(x):
        n = x[i]*x[i] + n
    return n**(1/2)

def Jacobiano(var, fun):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    J = sym.zeros(len(f), len(vars))
    for i, fi in enumerate(f):
        for j, s in enumerate(vars):
            if(i == j):
                J[i, j] = sym.diff(fi, s)
    return J

def diagonalJacobiano(var, fun, x):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    J = sym.zeros(len(f), len(vars))
    for i, fi in enumerate(f):
        for j, s in enumerate(vars):
            if(i == j):
                J[i, j] = sym.diff(fi, s)
                for k, muda in enumerate(x):
                    J[i, j] = J[i, j].subs(vars[k], x[k])
                J[i, j] = J[i, j].evalf()
    return J

def evaluar(var, fun, x):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    ev = sym.zeros(len(f), 1)
    for i, fi in enumerate(f):
        ev[i] = fi
        for k, muda in enumerate(x):
            ev[i] = ev[i].subs(vars[k], x[k])
        ev[i] = ev[i].evalf()
    return ev

def Jacobi(var, fun, x, k):
    lx, le = [], []
    for i in range(k):
        inJac = diagonalJacobiano(var, fun, x)**-1
        evf = evaluar(var, fun, x)
        x1 = x - inJac*evf
        lx.append(x), le.append(norma(x - x1))
        x = x1
    return lx, le

def JacobiParada(var, fun, x, tol):
    n, i = 1000000000, 0
    while(n > tol and i < 1000):
        inJac = diagonalJacobiano(var, fun, x)**-1
        evf = evaluar(var, fun, x)
        x1 = x - inJac*evf
        n = norma(x - x1)
        x = x1
        print(f"{i + 1}: x = {x.T} - ea = {n}")
        i = i + 1
    return i

def main():
    x0 = sym.Matrix([1, 
                     1, 
                     1])
    var = 'x y z'
    fun = sym.Matrix(['3*x - cos(y*z) - 1/2', 
                      'x**2 - 81*(y + 1/10)**2 + sin(z) + 1.06',
                      'exp(-x*y) + 20*z + (10*pi - 3)/3'])
    iter = 12

    jacobiano = Jacobiano(var, fun)

    print("Funciones:")
    sym.pprint(fun)
    print("Diagonal del Jacobiano del sístema:")
    sym.pprint(jacobiano)

    itera = np.arange(1, iter + 1, 1)

    lx, error = Jacobi(var, fun, x0, iter)

    for i in range(iter):
        print(f"{i + 1}: x = {lx[i].T} - ea = {error[i]}")

    fig, ax = plt.subplots()
    ax.plot(itera, error)

    ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
    ax.grid()

    plt.show()

if __name__ == "__main__":
    main()