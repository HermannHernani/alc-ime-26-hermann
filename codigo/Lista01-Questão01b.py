import numpy as np

A = np.array([
    [1, 2, 6],
    [2, 1, 6],
    [1, 1, 4]
], dtype=float)

# Determinante
det_A = np.linalg.det(A)

print(f"det(A) = {det_A:.10f}")

# Posto da matriz
rank_A = np.linalg.matrix_rank(A)

print(f"posto(A) = {rank_A}")

# Verificacao de inversibilidade
if np.isclose(det_A, 0.0):
    print("A matriz A nao e inversivel.")
else:
    A_inv = np.linalg.inv(A)

    print("A^-1 =")
    print(A_inv)