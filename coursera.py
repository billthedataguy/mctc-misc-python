import sympy as sym
import numpy as np

x, y = sym.symbols("x y")
eq = np.cosh(y)+x-2

print(sym.diff(eq, y))