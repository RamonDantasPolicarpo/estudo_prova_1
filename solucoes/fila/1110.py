# 1110 - Jogando Cartas Fora   (FILA / deque)
#
# IDEIA: enquanto tiver 2+ cartas: descarta a do topo (frente) e manda a próxima
#   para o fim. Frente = popleft(); fim = append(). Isso é uma FILA (FIFO).
#
# PYTHON: deque (de collections) = fila eficiente. NÃO use list.pop(0): é lento.
from collections import deque

while True:
    n = int(input())
    if n == 0:
        break
    cartas = deque(range(1, n + 1))        # 1..n, com 1 no topo
    descartadas = []
    while len(cartas) >= 2:
        descartadas.append(cartas.popleft())     # joga fora a do topo
        cartas.append(cartas.popleft())          # a seguinte vai pra base
    print(f"Discarded cards: {', '.join(map(str, descartadas))}".rstrip())
    print(f"Remaining card: {cartas[0]}")
