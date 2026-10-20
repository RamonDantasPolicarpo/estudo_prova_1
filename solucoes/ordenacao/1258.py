# 1258 - Camisetas   (ORDENAÇÃO com VÁRIOS critérios)
#
# IDEIA: ordenar por cor (asc), tamanho (DESC), nome (asc).
#   Truque: o sorted() é estável, então ordena do critério MENOS importante
#   para o MAIS importante:  1º nome, 2º tamanho (reverse), 3º cor.
#   (Tamanho em ordem alfabética decrescente dá P, M, G - o que o enunciado quer.)
#
# PYTHON: lambda x: x[1]  = função anônima ("pega o item 1 da tupla"), como no Java 8.
primeiro = True
while True:
    n = int(input())
    if n == 0:
        break
    if not primeiro:
        print()                                # linha em branco ENTRE os casos
    primeiro = False

    lista = []
    for _ in range(n):
        nome = input()
        cor, tam = input().split()
        lista.append((cor, tam, nome))

    lista.sort(key=lambda x: x[2])                   # nome  (asc)
    lista.sort(key=lambda x: x[1], reverse=True)     # tam   (desc)
    lista.sort(key=lambda x: x[0])                   # cor   (asc)

    for cor, tam, nome in lista:
        print(cor, tam, nome)
