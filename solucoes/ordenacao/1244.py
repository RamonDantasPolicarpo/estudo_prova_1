# 1244 - Ordenação por Tamanho   (ORDENAÇÃO ESTÁVEL)
#
# IDEIA: ordena as palavras pelo tamanho, do maior pro menor.
#   Empate -> mantém a ordem original. Isso é ESTABILIDADE, e o sorted() do
#   Python já é estável (mesmo com reverse=True).
#
# PYTHON: key=len  -> "ordene usando len(palavra) como critério"
#         (parecido com um Comparator do Java).
n = int(input())
for _ in range(n):
    palavras = input().split()
    print(" ".join(sorted(palavras, key=len, reverse=True)))
