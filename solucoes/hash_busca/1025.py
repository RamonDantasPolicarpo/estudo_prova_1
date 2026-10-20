# 1025 - Onde está o Mármore?   (ORDENAR + BUSCA BINÁRIA)
#
# IDEIA: ordena os mármores e usa bisect_left, que faz BUSCA BINÁRIA e devolve
#   a posição da PRIMEIRA ocorrência (ou onde o valor entraria, se não existir).
#   Se naquela posição o valor for igual a x -> found at (posição+1); senão not found.
#
# PYTHON: biblioteca  bisect  (de "bisection" = dividir ao meio).
#   bisect_left(lista_ordenada, x) -> índice da 1ª ocorrência de x.
import sys
from bisect import bisect_left

dados = sys.stdin.read().split()
p = 0
caso = 0
saida = []
while True:
    n, q = int(dados[p]), int(dados[p + 1]); p += 2
    if n == 0 and q == 0:
        break
    caso += 1
    marmores = sorted(int(x) for x in dados[p:p + n]); p += n
    saida.append(f"CASE# {caso}:")
    for _ in range(q):
        x = int(dados[p]); p += 1
        i = bisect_left(marmores, x)
        if i < n and marmores[i] == x:
            saida.append(f"{x} found at {i + 1}")    # +1: posições começam em 1
        else:
            saida.append(f"{x} not found")
print("\n".join(saida))
