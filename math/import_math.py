import math
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


m = math
print("Value of pi",m.pi)
print("Value of e",m.e)
print("Value of tan",m.tan)
print("Value of cube", m.cbrt(27))
print("Value of sqr", m.sqrt(144)) 

x = 20
y = 30
get = (x + y)/ m.pi
print(int(get))
print(m.ceil(10.01))
print(m.floor(10.99))

radius = float(input("Enter the radius number of a circle: "))
circumfernce = 2 * m.pi * radius
print(f"Your circle radius number is : {round(circumfernce)}")


areaRadius = float(input("Enter the radius of circle : "))
area = m.pi *pow(radius, 2)
print(f"The area of the circle is : {round(area)}cm^2")
