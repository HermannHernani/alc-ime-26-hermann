import numpy as np


def substituicao_regressiva(U, b):

    U = np.asarray(U, dtype=float)
    b = np.asarray(b, dtype=float)

    if U.ndim != 2 or U.shape[0] != U.shape[1]:
        raise ValueError(
            "U deve ser uma matriz quadrada."
        )

    n = U.shape[0]

    if b.ndim == 2 and b.shape == (n, 1):
        b = b[:, 0]

    elif b.ndim == 1 and b.shape[0] == n:
        pass

    else:
        raise ValueError(
            "b deve possuir dimensao correspondente a U."
        )

    if not np.allclose(U, np.triu(U)):
        raise ValueError(
            "U deve ser uma matriz triangular superior."
        )

    if np.any(np.isclose(np.diag(U), 0.0)):
        raise ZeroDivisionError(
            "Elemento nulo encontrado na diagonal de U."
        )

    x = np.zeros(n)

    for i in range(n - 1, -1, -1):

        soma = np.dot(
            U[i, i + 1:],
            x[i + 1:]
        )

        x[i] = (
            b[i] - soma
        ) / U[i, i]

    return x.reshape(-1, 1)


# Teste

U = np.array([
    [2, -1, 3],
    [0,  4, 2],
    [0,  0, 5]
], dtype=float)

b = np.array([
    [-3],
    [ 6],
    [-5]
], dtype=float)

x = substituicao_regressiva(U, b)

print("Solucao:")
print(x)

# Verificacao com NumPy

x_numpy = np.linalg.solve(U, b)

print(
    "Resultado validado:",
    np.allclose(x, x_numpy)
)


# Teste com elemento nulo na diagonal

U_zero = np.array([
    [2, -1, 3],
    [0,  0, 2],
    [0,  0, 5]
], dtype=float)

try:
    substituicao_regressiva(U_zero, b)

except ZeroDivisionError as erro:
    print("Erro:", erro)