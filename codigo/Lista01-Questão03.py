import numpy as np


def matrizes_transformacao(alpha, beta):
    """
    Calcula as matrizes correspondentes a:

    1. escala seguida de rotacao;
    2. rotacao seguida de escala.
    """

    theta = np.deg2rad(30.0)

    S = np.array([
        [alpha, 0.0],
        [0.0, beta]
    ])

    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    # Primeiro escala, depois rotaciona
    A = R @ S

    # Primeiro rotaciona, depois escala
    A_invertida = S @ R

    return A, A_invertida


# Valores utilizados apenas para teste
alpha = 2.0
beta = 3.0

A, A_invertida = matrizes_transformacao(alpha, beta)

print("Escala seguida de rotacao:")
print(A)

print("\nRotacao seguida de escala:")
print(A_invertida)

print("\nAs matrizes sao iguais?")
print(np.allclose(A, A_invertida))
