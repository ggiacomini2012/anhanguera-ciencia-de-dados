# -*- coding: utf-8 -*-
import time
import random

"""
    Ponto de Partida
    
    Este arquivo Python exemplifica os conceitos abordados na aula sobre eficiência de algoritmos de ordenação e busca binária.
    Ele implementa diversos algoritmos de ordenação (Bubble Sort, Quick Sort, Merge Sort e Insertion Sort) e a busca binária.
    
    O estudo de caso de um e-commerce é utilizado para contextualizar a importância desses algoritmos. O código simula
    o problema de ordenar e buscar produtos, medindo o tempo de execução de cada algoritmo para demonstrar suas
    diferenças de eficiência na prática.
    
    Vamos começar!
"""

# --- Eficiência dos algoritmos de ordenação ---

def bubble_sort(arr):
    """
    Implementação do Bubble Sort.
    Complexidade: O(n^2) - menos eficiente para grandes conjuntos de dados.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def quick_sort(arr):
    """
    Implementação do Quick Sort.
    Complexidade média: O(n log n).
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quick_sort(less) + equal + quick_sort(greater)

def merge_sort(arr):
    """
    Implementação do Merge Sort.
    Complexidade: O(n log n).
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def insertion_sort(arr):
    """
    Implementação do Insertion Sort.
    Complexidade: O(n^2), mas eficiente para dados pequenos ou quase ordenados.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# --- Busca Binária e suas variações ---

def binary_search(arr, target):
    """
    Implementação da busca binária.
    Requer que a lista esteja ordenada.
    Complexidade: O(log n).
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Elemento encontrado, retorna o índice
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Elemento não encontrado

# --- Estudo de Caso: E-commerce ---

def main():
    """
    Função principal que simula o estudo de caso do e-commerce.
    """
    print("Iniciando simulação de e-commerce com algoritmos de ordenação e busca...")

    # Gerando um grande conjunto de dados de produtos (preços simulados)
    # A lista de produtos está desordenada inicialmente.
    num_products = 5000  # Aumente este número para testar a eficiência em maior escala
    unsorted_prices = [random.randint(1, 10000) for _ in range(num_products)]
    target_price = random.choice(unsorted_prices)

    print(f"\nConjunto de dados de {num_products} produtos gerado.")
    print(f"Buscando o preço: {target_price}")

    # Testando a eficiência dos algoritmos de ordenação
    print("\n--- Testando Algoritmos de Ordenação ---")

    # Bubble Sort
    prices_bubble = unsorted_prices[:]
    start_time = time.time()
    bubble_sort(prices_bubble)
    end_time = time.time()
    print(f"Bubble Sort: {end_time - start_time:.6f} segundos")

    # Insertion Sort
    prices_insertion = unsorted_prices[:]
    start_time = time.time()
    insertion_sort(prices_insertion)
    end_time = time.time()
    print(f"Insertion Sort: {end_time - start_time:.6f} segundos")

    # Quick Sort
    prices_quick = unsorted_prices[:]
    start_time = time.time()
    prices_quick = quick_sort(prices_quick)
    end_time = time.time()
    print(f"Quick Sort: {end_time - start_time:.6f} segundos")

    # Merge Sort
    prices_merge = unsorted_prices[:]
    start_time = time.time()
    prices_merge = merge_sort(prices_merge)
    end_time = time.time()
    print(f"Merge Sort: {end_time - start_time:.6f} segundos")

    print("\n--- Análise da Solução ---")
    print("Como observado nos tempos de execução, para grandes volumes de dados,")
    print("algoritmos como Quick Sort e Merge Sort (O(n log n)) são significativamente mais rápidos")
    print("do que Bubble Sort e Insertion Sort (O(n^2)).")
    print("No contexto do e-commerce, utilizar um algoritmo eficiente é crucial para a")
    print("ordenação de produtos, especialmente em listagens com milhares de itens,")
    print("garantindo uma melhor experiência para o usuário.")

    # Implementação da busca binária para otimizar a recuperação de produtos
    print("\n--- Implementando a Busca Binária ---")

    # A busca binária requer que a lista esteja ordenada.
    # Usaremos a lista ordenada pelo Quick Sort.
    sorted_prices = prices_quick

    # Teste de busca binária
    start_time = time.time()
    found_index = binary_search(sorted_prices, target_price)
    end_time = time.time()

    print(f"\nBusca binária por {target_price}:")
    if found_index != -1:
        print(f"Elemento encontrado no índice {found_index} em {end_time - start_time:.10f} segundos.")
    else:
        print("Elemento não encontrado.")

    # Exemplo de busca linear para comparação
    start_time = time.time()
    try:
        linear_index = unsorted_prices.index(target_price)
    except ValueError:
        linear_index = -1
    end_time = time.time()

    print(f"\nBusca linear (para comparação):")
    if linear_index != -1:
        print(f"Elemento encontrado em {end_time - start_time:.10f} segundos.")
    else:
        print("Elemento não encontrado.")

    print("\n--- Otimizações e Conclusão ---")
    print("A busca binária (O(log n)) é incomparavelmente mais rápida que a busca linear (O(n))")
    print("para conjuntos de dados ordenados. Em um sistema de e-commerce, a busca binária")
    print("pode ser aplicada em índices de produtos, permitindo que a busca por um item,")
    print("seja por ID, preço ou nome (após ordenação), seja praticamente instantânea,")
    print("melhorando drasticamente a usabilidade.")
    print("Para um e-commerce, a melhor estratégia seria: ordenar os produtos usando")
    print("Quick Sort ou Merge Sort para grandes listagens e, em seguida, usar busca binária")
    print("para encontrar itens específicos. Essas otimizações são a chave para sistemas")
    print("escaláveis e eficientes.")


if __name__ == "__main__":
    main()