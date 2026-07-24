# @Program: Imports in Python
# @Author: Saloni Malhotra
# @Date: 24-07-2026


# 1st Program of import
# dir print all the methods that are present inside math module
# Output => ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
# ---------------------------------------------------------------------

import math
print(dir(math))

# 2nd Program of import
# ---------------------------------------------------------------------

import math
print(math) # Error -> <module 'math' (built-in)>
print(math.sqrt(2)) # 1.4142135623730951

# 3rd Program of import
# ---------------------------------------------------------------------

import math as m 
print(m.sqrt(2)) # 1.4142135623730951
print(m.factorial(3)) # 6

# 4th Program of import
# Not Recomended approach as Python copies every public name from math into your current program.
# There is no math object available.
# ---------------------------------------------------------------------

from math import *
print(sqrt(2)) # 1.4142135623730951
print(factorial(3)) # 6

# 5th Program of import
# ---------------------------------------------------------------------

from math import sqrt, factorial
print(sqrt(2)) # 1.4142135623730951
print(factorial(3)) # 6

# 6th Program of import
# ---------------------------------------------------------------------

from math import sqrt, factorial as fct
print(sqrt(2)) # 1.4142135623730951
print(fct(3)) # 6
