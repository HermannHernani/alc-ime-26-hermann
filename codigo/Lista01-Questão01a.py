import numpy as np

A = np.array([
    [1, 2],
    [2, 1]
], dtype=float)

det_A = np.linalg.det(A)

print(f"det(A) = {det_A:.10f}")

if np.isclose(det_A, 0.0):
    print("A matriz A nao e inversivel.")
else:
    A_inv = np.linalg.inv(A)

    print("A^-1 =")
    print(A_inv)

    verificacao = A @ A_inv

    print("A @ A^-1 =")
    print(np.round(verificacao, 10))

    assert np.allclose(verificacao, np.eye(2))