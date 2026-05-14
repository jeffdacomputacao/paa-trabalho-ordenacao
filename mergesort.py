def merge_sort(arr):
    """
    Ordenação por intercalação.
    Divide o vetor em partes menores, ordena recursivamente
    e depois intercala os resultados.

    Recebe:
        arr: lista de elementos inteiros

    Retorna:
        quantidade de comparações realizadas
    """

    comparacoes = [0]

    def merge_sort_rec(vetor):
        if len(vetor) > 1:

            meio = len(vetor) // 2

            esquerda = vetor[:meio]
            direita = vetor[meio:]

            merge_sort_rec(esquerda)
            merge_sort_rec(direita)

            i = 0
            j = 0
            k = 0

            # Intercala os dois subvetores ordenados
            while i < len(esquerda) and j < len(direita):

                comparacoes[0] += 1

                if esquerda[i] <= direita[j]:
                    vetor[k] = esquerda[i]
                    i += 1
                else:
                    vetor[k] = direita[j]
                    j += 1

                k += 1

            # Copia o restante da esquerda, se houver
            while i < len(esquerda):
                vetor[k] = esquerda[i]
                i += 1
                k += 1

            # Copia o restante da direita, se houver
            while j < len(direita):
                vetor[k] = direita[j]
                j += 1
                k += 1

    merge_sort_rec(arr)

    return comparacoes[0]