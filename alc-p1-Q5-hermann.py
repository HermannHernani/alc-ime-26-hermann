
from numpy import array, eye, zeros


def substituicao_progressiva(L, b):
    """
    Resolve Ly = b por substituicao progressiva.

    L: matriz triangular inferior com diagonal unitaria.
    b: vetor de termos independentes.

    Retorna o vetor y.
    """
    n = len(b)
    y = zeros(n, dtype=float)

    for i in range(n):
        soma = 0.0

        # Utiliza os valores de y ja calculados
        for j in range(i):
            soma += L[i, j] * y[j]

        # A diagonal de L e igual a 1
        y[i] = b[i] - soma

    return y


def substituicao_regressiva(U, y):
    """
    Resolve Ux = y por substituicao regressiva.

    U: matriz triangular superior.
    y: vetor obtido na substituicao progressiva.

    Retorna o vetor x.
    """
    n = len(y)
    x = zeros(n, dtype=float)

    for i in range(n - 1, -1, -1):
        soma = 0.0

        # Utiliza os valores de x ja calculados
        for j in range(i + 1, n):
            soma += U[i, j] * x[j]

        pivo = U[i, i]

        if pivo == 0.0:
            raise Exception(
                f"Pivo nulo na linha {i + 1}. "
                "Utilize um metodo alternativo com pivoteamento."
            )

        x[i] = (y[i] - soma) / pivo

    return x


def resolve_lu(A, b):
    """
    Resolve Ax = b por decomposicao LU sem pivoteamento.

    A: matriz quadrada.
    b: vetor de termos independentes.

    Retorna L, U e x, nesta ordem.
    """
    # Converte as entradas para arrays de ponto flutuante
    A = array(A, dtype=float)
    b = array(b, dtype=float)

    # Verifica se A e quadrada
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("A matriz A deve ser quadrada.")

    n = A.shape[0]

    if n == 0:
        raise ValueError("A matriz A nao pode ser vazia.")

    # Verifica se b possui dimensao compativel
    if b.ndim != 1 or b.shape[0] != n:
        raise ValueError(
            "O vetor b deve ter dimensao compativel com A."
        )

    # Inicializa as matrizes da decomposicao LU
    L = eye(n, dtype=float)
    U = array(A, dtype=float)

    for k in range(n):
        pivo = U[k, k]

        if pivo == 0.0:
            raise Exception(
                f"Pivo nulo na posicao ({k + 1}, {k + 1}). "
                "Utilize um metodo alternativo com pivoteamento."
            )

        # Elimina os elementos abaixo do pivo
        for i in range(k + 1, n):

            # Calcula o multiplicador da eliminacao
            multiplicador = U[i, k] / pivo

            # Armazena o multiplicador em L
            L[i, k] = multiplicador

            # Zera o elemento correspondente em U
            U[i, k] = 0.0

            # Atualiza os demais elementos da linha
            for j in range(k + 1, n):
                U[i, j] -= multiplicador * U[k, j]

    # Resolve Ly = b
    y = substituicao_progressiva(L, b)

    # Resolve Ux = y
    x = substituicao_regressiva(U, y)

    return L, U, x


# Exemplo de uso - Sistema 2x2
A = [[4, 3],
     [6, 3]]

b = [10, 12]

L, U, x = resolve_lu(A, b)

print("\n===== RESULTADO DA DECOMPOSIÇÃO LU (2x2)=====")

print("\nMatriz L:")
print(L)

print("\nMatriz U:")
print(U)

print("\nVetor solução x:")
print(x)

print("\n=======================================")


# Exemplo de uso - Sistema 3x3
A = [[ 2, 1, -1],
     [ 4, 5,  0],
     [-2, 8, 11]]

b = [5, 14, 3]

L, U, x = resolve_lu(A, b)

print("\n===== RESULTADO DA DECOMPOSIÇÃO LU (3x3)=====")

print("\nMatriz L:")
print(L)

print("\nMatriz U:")
print(U)

print("\nVetor solução x:")
print(x)

print("\n=======================================")


# Teste com pivô nulo
A = [[0, 1],
     [1, 1]]

b = [1, 2]

L, U, x = resolve_lu(A, b)