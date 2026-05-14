# ---------------------------------------------------------------
# UNIVERSIDADE FEDERAL DO PIAUÍ - UFPI
# DISCIPLINA: PROJETO E ANÁLISE DE ALGORITMOS
# TRABALHO PRÁTICO - PARTE I
#
# Implementação e comparação de algoritmos de ordenação:
# BubbleSort, InsertionSort, MergeSort, HeapSort e QuickSort.
# ---------------------------------------------------------------

import time
import random
import sys

from bubblesort import bubble_sort
from insertionsort import insertion_sort
from mergesort import merge_sort
from heapsort import heap_sort
from quicksort import quick_sort


# Aumenta o limite de recursão para reduzir risco de erro no QuickSort
sys.setrecursionlimit(300000)


def gerar_vetores(tamanho):
    """
    Gera os três tipos de entrada exigidos no trabalho:
    1. vetor crescente;
    2. vetor decrescente;
    3. vetor aleatório.
    """

    crescente = list(range(tamanho))
    decrescente = list(range(tamanho, 0, -1))
    aleatorio = random.sample(range(tamanho * 2), tamanho)

    return {
        "Crescente": crescente,
        "Decrescente": decrescente,
        "Aleatório": aleatorio
    }


def testar_algoritmo(nome_algoritmo, funcao_algoritmo, vetor, condicao, tamanho):
    """
    Executa um algoritmo de ordenação três vezes sobre uma cópia do vetor.
    Calcula a média do tempo de execução e a média das comparações.
    """

    tempos = []
    comparacoes_lista = []

    for execucao in range(1, 4):

        # Usa cópia para garantir que cada execução receba o vetor original
        arr = vetor.copy()

        inicio = time.perf_counter()
        comparacoes = funcao_algoritmo(arr)
        fim = time.perf_counter()

        tempo = fim - inicio

        # Verificação de segurança: garante que o vetor foi ordenado corretamente
        if arr != sorted(vetor):
            raise Exception(f"Erro: {nome_algoritmo} não ordenou corretamente.")

        tempos.append(tempo)
        comparacoes_lista.append(comparacoes)

    tempo_medio = sum(tempos) / len(tempos)
    comparacoes_media = sum(comparacoes_lista) / len(comparacoes_lista)

    print(
        f"{nome_algoritmo:15} | "
        f"Condição: {condicao:11} | "
        f"Tamanho: {tamanho:6} | "
        f"Tempo médio: {tempo_medio:.6f}s | "
        f"Comparações médias: {comparacoes_media:.0f}"
    )


if __name__ == "__main__":

    # Para a primeira entrega, o cronograma pede teste com tamanho pequeno.
    # O próprio enunciado informa que tamanho 500 é suficiente.
    tamanho = 500

    vetores = gerar_vetores(tamanho)

    algoritmos = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Heap Sort": heap_sort,
        "Quick Sort": quick_sort
    }

    print("\nRESULTADOS DOS TESTES - PARTE I\n")

    for condicao, vetor in vetores.items():
        print(f"\nEntrada: {condicao}")
        print("-" * 100)

        for nome, funcao in algoritmos.items():
            testar_algoritmo(nome, funcao, vetor, condicao, tamanho)