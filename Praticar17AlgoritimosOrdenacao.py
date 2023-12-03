import random
import time
import sys


sys.setrecursionlimit(10**6)

def bubble_sort(arr):
    comparacoes, trocas = 0, 0

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                trocas += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return comparacoes, trocas

def improved_bubble_sort(arr):
    comparacoes, trocas = 0, 0

    n = len(arr)
    trocado = True

    while trocado:
        trocado = False
        for i in range(1, n):
            comparacoes += 1
            if arr[i-1] > arr[i]:
                trocas += 1
                arr[i-1], arr[i] = arr[i], arr[i-1]
                trocado = True

    return comparacoes, trocas

def insertion_sort(arr):
    comparacoes, trocas = 0, 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        comparacoes += 1

        while j >= 0 and key < arr[j]:
            trocas += 1
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return comparacoes, trocas

def selection_sort(arr):
    comparacoes, trocas = 0, 0

    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        trocas += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return comparacoes, trocas

def merge_sort(arr):
    comparacoes, trocas = 0, 0

    if len(arr) > 1:
        meio = len(arr)//2
        L = arr[:meio]
        R = arr[meio:]

        comparacoes_L, trocas_L = merge_sort(L)
        comparacoes_R, trocas_R = merge_sort(R)
        comparacoes += comparacoes_L + comparacoes_R
        trocas += trocas_L + trocas_R

        i = j = k = 0

        while i < len(L) and j < len(R):
            comparacoes += 1
            if L[i] < R[j]:
                trocas += 1
                arr[k] = L[i]
                i += 1
            else:
                trocas += 1
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            trocas += 1
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            trocas += 1
            arr[k] = R[j]
            j += 1
            k += 1

    return comparacoes, trocas

def quick_sort(arr):
    comparacoes, trocas = 0, 0

    def partition(arr, low, high):
        nonlocal comparacoes, trocas
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            comparacoes += 1
            if arr[j] <= pivot:
                trocas += 1
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        trocas += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_util(arr, low, high):
        nonlocal comparacoes, trocas
        if low < high:
            pi = partition(arr, low, high)

            quick_sort_util(arr, low, pi - 1)
            quick_sort_util(arr, pi + 1, high)

    quick_sort_util(arr, 0, len(arr) - 1)
    return comparacoes, trocas

def counting_sort(arr):
    comparacoes, trocas = 0, 0

    max_value = max(arr) + 1
    count = [0] * max_value

    for num in arr:
        count[num] += 1

    index = 0
    for i in range(max_value):
        for j in range(count[i]):
            arr[index] = i
            index += 1

    return comparacoes, trocas

# Adicionar Counting Sort ao menu interativo
def counting_sort_option():
    print("7. Counting Sort")

# Função para executar Counting Sort
def counting_sort_execution(arr):
    comparacoes, trocas = counting_sort(arr)
    return comparacoes, trocas

# Função para ordenar e obter métricas
def ordenar_e_obter_metricas(algoritmo, tamanho, tipo_caso, arr):
    if algoritmo == 1:
        comparacoes, trocas = bubble_sort(arr)
    elif algoritmo == 2:
        comparacoes, trocas = improved_bubble_sort(arr)
    elif algoritmo == 3:
        comparacoes, trocas = insertion_sort(arr)
    elif algoritmo == 4:
        comparacoes, trocas = selection_sort(arr)
    elif algoritmo == 5:
        comparacoes, trocas = merge_sort(arr)
    elif algoritmo == 6:
        comparacoes, trocas = quick_sort(arr)
    elif algoritmo == 7:
        comparacoes, trocas = counting_sort_execution(arr)

    return comparacoes, trocas

# Função para apresentar os resultados
def apresentar_resultados(tempo_execucao, comparacoes, trocas):
    print(f"Tempo de Execução: {tempo_execucao:.6f} segundos")
    print(f"Quantidade de Comparações: {comparacoes}")
    print(f"Quantidade de Trocas: {trocas}")

# Menu interativo
print("Escolha o algoritmo de ordenação:")
print("1. Bubble Sort")
print("2. Improved Bubble Sort")
print("3. Insertion Sort")
print("4. Selection Sort")
print("5. Merge Sort")
print("6. Quick Sort")

# Adicionar Counting Sort ao menu
counting_sort_option()

algoritmo_escolhido = int(input("Digite o número do algoritmo desejado: "))

print("\nEscolha o tamanho:")
print("1. 1.000")
print("2. 10.000")
print("3. 100.000")

tamanho_escolhido = int(input("Digite o número do tamanho desejado: "))
tamanho = [1000, 10000, 100000][tamanho_escolhido - 1]

print("\nEscolha o tipo de caso:")
print("1. Melhor Caso (Valores em ordem crescente)")
print("2. Caso Médio (Valores desordenados com números aleatórios)")
print("3. Pior Caso (Valores em ordem decrescente)")

tipo_caso_escolhido = int(input("Digite o número do tipo de caso desejado: "))
tipos_caso = ["melhor", "medio", "pior"]
tipo_caso = tipos_caso[tipo_caso_escolhido - 1]

# Criar lista com valores conforme tamanho escolhido
arr = random.sample(range(1, tamanho + 1), tamanho) if tipo_caso == "medio" else list(range(1, tamanho + 1))
if tipo_caso == "pior":
    arr.reverse()

# Executar ordenação e obter métricas
inicio = time.time()
comparacoes, trocas = ordenar_e_obter_metricas(algoritmo_escolhido, tamanho, tipo_caso, arr)
fim = time.time()
tempo_execucao = fim - inicio

# Apresentar resultados
print("\nResultados:")
apresentar_resultados(tempo_execucao, comparacoes, trocas)
