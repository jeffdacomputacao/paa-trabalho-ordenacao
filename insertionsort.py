def insertion_sort(arr):
    """
    Ordenação por inserção.
    Implementação baseada na ideia apresentada no Cormen.

    Recebe:
        arr: lista de elementos inteiros

    Retorna:
        quantidade de comparações realizadas
    """

    comparacoes = 0

    # Começa no segundo elemento, pois o primeiro já é considerado ordenado
    for j in range(1, len(arr)):

        chave = arr[j]
        i = j - 1

        # Move os elementos maiores que a chave uma posição à frente
        while i >= 0:

            comparacoes += 1

            if arr[i] > chave:
                arr[i + 1] = arr[i]
                i -= 1
            else:
                break

        arr[i + 1] = chave

    return comparacoes