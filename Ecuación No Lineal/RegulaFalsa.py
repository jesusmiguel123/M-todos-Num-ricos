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
    c = 0
    for i in range(k):
        c1 = (b*evaluar(var, fun, a)-a*evaluar(var, fun, b))/(evaluar(var, fun, a) - evaluar(var, fun, b))
        a1 = a
        b1 = b
        if(evaluar(var, fun, c1) == 0):
            return a, b, c1, 0, 0
        if(evaluar(var, fun, a)*evaluar(var, fun, c1) < 0):
            b = c1
        else:
            a = c1
        if((c1 - c) > 0):
            e = c1 - c
        else:
            e = -(c1 - c)
        c = c1
    return a1, b1, c, evaluar(var, fun, c), e

def regulaFalsaParada(var, fun, a, b, tol):
    e = 100000000000
    i = 0
    c = 0
    while(e > tol and i < 1000):
        c1 = (b*evaluar(var, fun, a)-a*evaluar(var, fun, b))/(evaluar(var, fun, a) - evaluar(var, fun, b))
        a1 = a
        b1 = b
        if(evaluar(var, fun, c1) == 0):
            return a, b, c1, 0, 0
        if(evaluar(var, fun, a)*evaluar(var, fun, c1) < 0):
            b = c1
        else:
            a = c1
        if((c1 - c) > 0):
            e = c1 - c
        else:
            e = -(c1 - c)
        c = c1
        print(i + 1, ": x1=", a1, "xu=", b1, "xr=", c, "fr=", evaluar(var, fun, c),"ea=", e)
        i = i + 1
    return i

var = 'x'
fun = 'x**3 + x - 1'
x0 = 0
x1 = 1
k = 8

print("Función: ")
sym.pprint(sym.sympify(fun))
print("\n0 : x1=", x0, "xu=", x1, "xr= - fr= - ea= -")

iter = k
itera = np.arange(1, iter + 1, 1)
error = np.zeros(len(itera))

for i in range(iter):
    x, xu, xr, fr, error[i] = regulaFalsa(var, fun, x0, x1, itera[i])
    print(i + 1, ": x1=", x, "xu=", xu, "xr=", xr, "fr=", fr,"ea=", error[i])

fig, ax = plt.subplots()
ax.plot(itera, error)

ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
ax.grid()

plt.show()
