import numpy as np

u = np.array([1.0, 1.0, 1.0])
v = np.array([1.0, -1.0, -1.0])

# Coeficientes arbitrarios da combinacao linear
alpha = 3.0
beta = -2.0

# Vetor pertencente a F
w = alpha * u + beta * v

x, y, z = w

print("w =", w)
print("y - z =", y - z)

assert np.isclose(y - z, 0.0)

print("O vetor pertence a F e satisfaz y - z = 0.")
