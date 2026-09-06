import numpy as np


def posicao_efetuador(theta1, theta2, arredondar=True):
    """
    Calcula a posicao do efetuador final de um robo planar
    de dois elos.

    Parametros
    ----------
    theta1 : float
        Angulo da primeira junta, em radianos.

    theta2 : float
        Angulo da segunda junta em relacao ao primeiro elo,
        em radianos.

    arredondar : bool
        Se True, retorna as coordenadas com uma casa decimal.

    Retorna
    -------
    tuple
        Coordenadas (X_U, Y_U) do efetuador final, em cm.
    """

    L1 = 20.0
    L2 = 15.0

    # Orientacao absoluta do segundo elo
    phi = theta1 + theta2

    x_u = (
        L1 * np.cos(theta1)
        + L2 * np.cos(phi)
    )

    y_u = (
        L1 * np.sin(theta1)
        + L2 * np.sin(phi)
    )

    if arredondar:
        return round(float(x_u), 1), round(float(y_u), 1)

    return float(x_u), float(y_u)


def transformacao_efetuador(theta1, theta2):
    """
    Calcula a matriz de transformacao homogenea do
    referencial do efetuador final E para o referencial U.

    Parametros
    ----------
    theta1 : float
        Angulo da primeira junta, em radianos.

    theta2 : float
        Angulo da segunda junta em relacao ao primeiro elo,
        em radianos.

    Retorna
    -------
    numpy.ndarray
        Matriz homogenea 3x3 que representa a pose do
        efetuador final em relacao ao referencial U.
    """

    # Posicao sem arredondamento para preservar a precisao
    x_u, y_u = posicao_efetuador(
        theta1,
        theta2,
        arredondar=False
    )

    # Orientacao absoluta do efetuador
    phi = theta1 + theta2

    T_UE = np.array([
        [
            np.cos(phi),
            -np.sin(phi),
            x_u
        ],
        [
            np.sin(phi),
            np.cos(phi),
            y_u
        ],
        [
            0.0,
            0.0,
            1.0
        ]
    ])

    return T_UE


# ============================================================
# TESTE 1
# theta1 = 0 graus
# theta2 = 0 graus
# ============================================================

theta1 = np.deg2rad(0.0)
theta2 = np.deg2rad(0.0)

posicao = posicao_efetuador(theta1, theta2)
T = transformacao_efetuador(theta1, theta2)

print("Teste 1")
print("Posicao do efetuador:")
print(posicao)

print("\nMatriz de transformacao:")
print(np.round(T, 10))


# Resultado esperado:
# posicao = (35.0, 0.0)

assert posicao == (35.0, 0.0)

T_esperada_1 = np.array([
    [1.0, 0.0, 35.0],
    [0.0, 1.0,  0.0],
    [0.0, 0.0,  1.0]
])

assert np.allclose(T, T_esperada_1)


# ============================================================
# TESTE 2
# theta1 = 0 graus
# theta2 = 90 graus
# ============================================================

theta1 = np.deg2rad(0.0)
theta2 = np.deg2rad(90.0)

posicao = posicao_efetuador(theta1, theta2)
T = transformacao_efetuador(theta1, theta2)

print("\nTeste 2")
print("Posicao do efetuador:")
print(posicao)

print("\nMatriz de transformacao:")
print(np.round(T, 10))


# Resultado esperado:
# posicao = (20.0, 15.0)

assert posicao == (20.0, 15.0)

T_esperada_2 = np.array([
    [0.0, -1.0, 20.0],
    [1.0,  0.0, 15.0],
    [0.0,  0.0,  1.0]
])

assert np.allclose(T, T_esperada_2)

print("\nTodos os testes foram concluidos com sucesso.")
