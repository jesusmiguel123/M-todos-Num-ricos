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
    for i in range(k):
        a = x0
        b = x1
        c = x2
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (evaluar(var, fun, x1) - evaluar(var, fun, x0))/(x1 - x0)
        d1 = (evaluar(var, fun, x2) - evaluar(var, fun, x1))/(x2 - x1)
        a = (d1 - d0)/(h1 + h0)
        b = a*h1 + d1
        c = evaluar(var, fun, x2)
        dis = (b**2 - 4*a*c)**0.5
        if((b + dis) > 0):
            dsum = b + dis
        else:
            dsum = -(b + dis)
        if((b - dis) > 0):
            dres = b - dis
        else:
            dres = -(b - dis)
        if(dsum > dres):
            d = dsum
        else:
            d = dres
        x3 = x2 - 2*c/d
        x0 = x1
        x1 = x2
        if((x3 - x2) > 0):
            e = x3 - x2
        else:
            e = -(x3 - x2)
        x2 = x3
    return a, b, c, x3, evaluar(var, fun, x3), e

def MullerParada(var, fun, x0, x1, x2, tol):
    e = 1000000000000
    i = 0
    while(e > tol and i < 1000):
        a = x0
        b = x1
        c = x2
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (evaluar(var, fun, x1) - evaluar(var, fun, x0))/(x1 - x0)
        d1 = (evaluar(var, fun, x2) - evaluar(var, fun, x1))/(x2 - x1)
        a = (d1 - d0)/(h1 + h0)
        b = a*h1 + d1
        c = evaluar(var, fun, x2)
        dis = (b**2 - 4*a*c)**0.5
        if((b + dis) > 0):
            dsum = b + dis
        else:
            dsum = -(b + dis)
        if((b - dis) > 0):
            dres = b - dis
        else:
            dres = -(b - dis)
        if(dsum > dres):
            d = dsum
        else:
            d = dres
        x3 = x2 - 2*c/d
        x0 = x1
        x1 = x2
        if((x3 - x2) > 0):
            e = x3 - x2
        else:
            e = -(x3 - x2)
        x2 = x3
        print(i + 1, ": x0=", a, "x1=", b, "x2=", c, "x3=", x3, "fx3=", evaluar(var, fun, x3),"ea=", e)
        i = i + 1
    return i

var = 'x'
fun = 'x**3 - sin(x)'
x0 = 1.5
x1 = 1.2
x2 = 1
k = 5

print("Función: ")
sym.pprint(sym.sympify(fun))
print("\n0 : x0=", x0, "x1=", x1, "x2=", x2, "x3= - fx3= - ea= -")

iter = k
itera = np.arange(1, iter + 1, 1)
error = np.zeros(len(itera))

for i in range(iter):
    a, b, c, x3, fx3, error[i] = Muller(var, fun, x0, x1, x2, itera[i])
    print(i + 1, ": x0=", a, "x1=", b, "x2=", c, "x3=", x3, "fx3=", fx3,"ea=", error[i])

fig, ax = plt.subplots()
ax.plot(itera, error)

ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
ax.grid()

plt.show()
