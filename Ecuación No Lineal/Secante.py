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
    for i in range(k):
        x2 = x1 - evaluar(var, fun, x1)*(x1 -x0)/(evaluar(var, fun, x1) - evaluar(var, fun, x0))
        a = x0
        x0 = x1
        if((x2 - x1) > 0):
            e = x2 - x1
        else:
            e = -(x2 - x1)
        b = x1
        x1 = x2
    return a, b, x2, evaluar(var, fun, x2), e

def SecanteParada(var, fun, x0, x1, tol):
    e = 100000000000000
    i = 0
    while(e > tol and i < 1000):
        x2 = x1 - evaluar(var, fun, x1)*(x1 -x0)/(evaluar(var, fun, x1) - evaluar(var, fun, x0))
        a = x0
        x0 = x1
        if((x2 - x1) > 0):
            e = x2 - x1
        else:
            e = -(x2 - x1)
        b = x1
        x1 = x2
        print(i + 1, ": x0=", a, ": x1=", b, ": x2=", x2, "fx2=", evaluar(var, fun, x2),"ea=", e)
        i = i + 1
    return i

var = 'x'
fun = 'x**3 - sin(x)'
x0 = 1.1
x1 = 1.0
k = 8

print("Función: ")
sym.pprint(sym.sympify(fun))
print("\n0 : x0=", x0, ": x1=", x1, ": x2= - fx2= - ea= -")

iter = k
itera = np.arange(1, iter + 1, 1)
error = np.zeros(len(itera))

for i in range(iter):
    xa, xb, xc, fxc, error[i] = Secante(var, fun, x0, x1, itera[i])
    print(i + 1, ": x0=", xa, ": x1=", xb, ": x2=", xc, "fx2=", fxc,"ea=", error[i])

fig, ax = plt.subplots()
ax.plot(itera, error)

ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
ax.grid()

plt.show()
