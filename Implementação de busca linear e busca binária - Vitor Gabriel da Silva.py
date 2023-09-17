def busca_linear(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  # Retorna o índice onde o valor foi encontrado
    return -1  # Retorna -1 se o valor não estiver na lista

def busca_binaria(lista, valor):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return meio  # Retorna o índice onde o valor foi encontrado
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1  # Retorna -1 se o valor não estiver na lista

minha_lista = [1, 3, 5, 7, 9, 11, 13, 15]
valor_a_buscar = 3

# Para a busca linear
resultado_linear = busca_linear(minha_lista, valor_a_buscar)
if resultado_linear != -1:
    print(f"Busca Linear: Valor {valor_a_buscar} encontrado no índice {resultado_linear}")
else:
    print(f"Busca Linear: Valor {valor_a_buscar} não encontrado na lista")

# Para a busca binária (a lista deve estar ordenada)
minha_lista_ordenada = sorted(minha_lista)
resultado_binario = busca_binaria(minha_lista_ordenada, valor_a_buscar)
if resultado_binario != -1:
    print(f"Busca Binária: Valor {valor_a_buscar} encontrado no índice {resultado_binario}")
else:
    print(f"Busca Binária: Valor {valor_a_buscar} não encontrado na lista")