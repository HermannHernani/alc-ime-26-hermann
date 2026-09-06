import numpy as np

u = np.array([1.0, 1.0, 1.0])
v = np.array([1.0, -1.0, -1.0])

# Vetor que satisfaz y = z
w = np.array([7.0, 2.0, 2.0])

x, y, z = w

if np.isclose(y - z, 0.0):

    alpha = (x + y) / 2
    beta = (x - y) / 2

    w_reconstruido = alpha * u + beta * v

    print("alpha =", alpha)
    print("beta =", beta)

    print("w =", w)
    print("w reconstruido =", w_reconstruido)

    assert np.allclose(w, w_reconstruido)

    print("w pertence ao subespaco F.")

else:
    print("w nao pertence a F.")
