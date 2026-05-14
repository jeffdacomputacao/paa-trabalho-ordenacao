import random


def quick_sort(arr):
    """
    Ordenação rápida.
    Usa particionamento no estilo Lomuto, mas com escolha aleatória do pivô
    para reduzir a chance de pior caso em vetores já ordenados.

    Recebe:
        arr: lista de elementos inteiros

    Retorna:
        quantidade de comparações realizadas
    """

    comparacoes = [0]

    def partition(low, high):
        """
        Particiona o vetor em torno de um pivô.
        Elementos menores ou iguais ao pivô ficam à esquerda.
        Elementos maiores ficam à direita.
        """

        # Escolha aleatória do pivô para evitar pior caso em vetor crescente/decrescente
        indice_pivo = random.randint(low, high)
        arr[indice_pivo], arr[high] = arr[high], arr[indice_pivo]

        pivo = arr[high]
        i = low - 1

        for j in range(low, high):

            comparacoes[0] += 1

            if arr[j] <= pivo:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    def quicksort_rec(low, high):
        if low < high:
            posicao_pivo = partition(low, high)

            quicksort_rec(low, posicao_pivo - 1)
            quicksort_rec(posicao_pivo + 1, high)

    quicksort_rec(0, len(arr) - 1)

    return comparacoes[0]