import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

def evaluar(var, fun, x):
    vars = sym.symbols(var)
    f = sym.sympify(fun)
    f = f.subs(vars, x)
    f = f.evalf()
    return f

def puntoFijo(var, fun0, fun1, x, k):
    for i in range(k):
        x1 = evaluar(var, fun1, x)
        if((x1 - x) > 0):
            e = x1 - x
        else:
            e = -(x1 - x)
        x = x1
    return x, evaluar(var, fun0, x), e

def puntoFijoParada(var, fun0, fun1, x, tol):
    e = 100000000000000
    i = 0
    while(e > tol and i < 1000):
        x1 = evaluar(var, fun1, x)
        if((x1 - x) > 0):
            e = x1 - x
        else:
            e = -(x1 - x)
        x = x1
        print(i + 1, ": x=", x, "fx=", evaluar(var, fun0, x),"ea=", e)
        i = i + 1
    return i

var = 'x'
fun0 = 'x**3 - 13*x - 12'
fun1 = '(13*x + 12)**(1/3)'
x0 = 4.5
k = 10

print("Función original: ")
sym.pprint(sym.sympify(fun0))
print("Función para punto fijo: ")
sym.pprint(sym.sympify(fun1))
print("\n0 : x=", x0, "fx=", evaluar(var, fun1, x0),"ea= -")

iter = k
itera = np.arange(1, iter + 1, 1)
error = np.zeros(len(itera))

for i in range(iter):
    x, fx, error[i] = puntoFijo(var, fun0, fun1, x0, itera[i])
    print(i + 1, ": x=", x, "fx=", fx,"ea=", error[i])

fig, ax = plt.subplots()
ax.plot(itera, error)

ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
ax.grid()

plt.show()
