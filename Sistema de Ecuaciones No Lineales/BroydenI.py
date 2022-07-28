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

def completoJacobiano(var, fun, x):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    J = sym.zeros(len(f), len(vars))
    for i, fi in enumerate(f):
        for j, s in enumerate(vars):
            J[i, j] = sym.diff(fi, s)
            for k, muda in enumerate(x):
                J[i, j] = J[i, j].subs(vars[k], x[k])
            J[i, j] = J[i, j].evalf()
    return J

def inferiorJacobiano(var, fun, x):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    J = sym.zeros(len(f), len(vars))
    for i, fi in enumerate(f):
        for j, s in enumerate(vars):
            if(i >= j):
                J[i, j] = sym.diff(fi, s)
                for k, muda in enumerate(x):
                    J[i, j] = J[i, j].subs(vars[k], x[k])
                J[i, j] = J[i, j].evalf()
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

def metBroydenI(var, fun, x, k):
    A = sym.eye(len(x))
    A = completoJacobiano(var, fun, x)
    for i in range(k):
        inA = A**-1
        evf = evaluar(var, fun, x)
        x1 = x - inA*evf
        delta = x1 - x
        dif = evaluar(var, fun, x1) - evaluar(var, fun, x)
        m = delta.T*delta
        A = A + (dif - A*delta)*delta.T/m[0]
        n = norma(x - x1)
        x = x1
    return x, n

def metBroydenIParada(var, fun, x, tol):
    n = 10000000000000
    i = 0
    A = sym.eye(len(x))
    A = completoJacobiano(var, fun, x)
    while(n > tol and i < 1000):
        inA = A**-1
        evf = evaluar(var, fun, x)
        x1 = x - inA*evf
        delta = x1 - x
        dif = evaluar(var, fun, x1) - evaluar(var, fun, x)
        m = delta.T*delta
        A = A + (dif - A*delta)*delta.T/m[0]
        n = norma(x - x1)
        x = x1
        print(i + 1, ": x=", x[0], ",", x[1], ",", x[2], "ea=", n)
        i = i + 1
    return i

x0 = sym.Matrix([1, 1, 1])
var = 'x y z'
fun = sym.Matrix(['3*x - cos(y*z)- 1/2', 'x**2 - 81*(y + 1/10)**2 + sin(z) + 1.06','exp(-x*y) + 20*z + (10*pi - 3)/3'])
k = 12

jacobiano = Jacobiano(var, fun)

print("Funciones:")
sym.pprint(fun)
print("Diagonal del Jacobiano del sístema: ")
sym.pprint(jacobiano)
print("\n0 : x=", x0[0], ",", x0[1], ",", x0[2], "ea= -")

iter = k
itera = np.arange(1, iter + 1, 1)
error = np.zeros(len(itera))

for i in range(iter):
    x, error[i] = metBroydenI(var, fun, x0, itera[i])
    print(i + 1, ": x=", x[0], ",", x[1], ",", x[2], "ea=", error[i])

fig, ax = plt.subplots()
ax.plot(itera, error)

ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
ax.grid()

plt.show()
