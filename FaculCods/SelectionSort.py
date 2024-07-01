# Lista inicial não ordenada
arr = [64, 25, 12, 22, 11]
n = len(arr)

# Passo a passo do Selection Sort
for i in range(n):
    # Encontrar o índice do menor elemento restante na lista não ordenada
    min_index = i
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Trocar o elemento mínimo com o primeiro elemento não ordenado
    arr[i], arr[min_index] = arr[min_index], arr[i]

    # Mostrar a lista após cada passo
    print(f"Passo {i + 1}: {arr}")

# Resultado final
print("Lista ordenada:", arr)
