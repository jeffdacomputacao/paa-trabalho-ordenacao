def bubble_sort(arr):
    """
    Ordenação pelo método da bolha.
    Implementação próxima ao algoritmo clássico estudado em sala.

    Recebe:
        arr: lista de elementos inteiros

    Retorna:
        quantidade de comparações realizadas
    """

    n = len(arr)
    comparacoes = 0

    # O laço externo controla a quantidade de passagens pelo vetor
    for i in range(n - 1):

        # O laço interno compara elementos vizinhos
        # A cada passagem, o maior elemento "sobe" para o final
        for j in range(n - 1 - i):

            comparacoes += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return comparacoes