import numpy as np

A = np.array([
    [1, 2, 6],
    [2, 1, 6],
    [1, 1, 4]
], dtype=float)

try:
    A_inv = np.linalg.inv(A)
    print(A_inv)

except np.linalg.LinAlgError:
    print("Nao foi possivel calcular a inversa: a matriz e singular.")
