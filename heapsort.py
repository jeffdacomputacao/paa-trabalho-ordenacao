def heap_sort(arr):
    """
    Ordenação por HeapSort.
    Primeiro constrói um heap máximo e depois remove sucessivamente
    o maior elemento, colocando-o no final do vetor.

    Recebe:
        arr: lista de elementos inteiros

    Retorna:
        quantidade de comparações realizadas
    """

    comparacoes = [0]
    n = len(arr)

    def heapify(tamanho_heap, i):
        """
        Garante a propriedade de heap máximo a partir do índice i.
        """

        maior = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        # Compara o filho esquerdo com o maior atual
        if esquerda < tamanho_heap:
            comparacoes[0] += 1

            if arr[esquerda] > arr[maior]:
                maior = esquerda

        # Compara o filho direito com o maior atual
        if direita < tamanho_heap:
            comparacoes[0] += 1

            if arr[direita] > arr[maior]:
                maior = direita

        # Se algum filho for maior que o pai, troca e continua ajustando
        if maior != i:
            arr[i], arr[maior] = arr[maior], arr[i]
            heapify(tamanho_heap, maior)

    # Construção do heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extração dos elementos do heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)

    return comparacoes[0]