import numpy as np

# integers

i = 10
print(type(i))

a_i = np.zeros(i, dtype=int)
print(type(a_i))        # ndarray
print(type(a_i[0]))     # int64

#floats

x = 119.0
print(type(x))          # floating point num

y = 1.19e2
print(type(y))          # 119 in scientific notation

z = np.zeros(i, dtype=float)
print(type(z))          # ndarray
print(type(z[0]))       # float64

