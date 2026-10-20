# 1162 - Organizador de Vagões   (ORDENAÇÃO - Bubble Sort contando trocas)
#
# IDEIA: o número mínimo de trocas entre vizinhos = número de trocas que o
#   Bubble Sort faz. Percorre repetidamente trocando vizinhos fora de ordem.
#
# PYTHON: troca sem variável temporária:  a[i], a[j] = a[j], a[i]
#         (em Java precisaria de um "tmp")
n = int(input())
for _ in range(n):
    tam = int(input())
    vagoes = list(map(int, input().split()))   # "1 3 2" -> [1, 3, 2]
    trocas = 0
    for i in range(tam):
        for j in range(tam - 1 - i):
            if vagoes[j] > vagoes[j + 1]:
                vagoes[j], vagoes[j + 1] = vagoes[j + 1], vagoes[j]
                trocas += 1
    print(f"Optimal train swapping takes {trocas} swaps.")
