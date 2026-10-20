# 1340 - Eu Posso Adivinhar a Estrutura   (PILHA + FILA + HEAP)
#
# IDEIA: simula as TRÊS estruturas ao mesmo tempo. Em cada comando "2 x" vê
#   quais delas retornariam x. Se nenhuma -> impossible; se alguma para de
#   bater, ela é marcada como "descartada" pro resto do caso.
#
# PYTHON:
#   - heapq é MIN-heap. Para ter MAX-heap (fila de prioridade que tira o maior),
#     guarda-se o valor NEGATIVO:  heappush(h, -x)  e  -heappop(h).
#   - Entrada termina no fim do arquivo: try/except EOFError.
import sys
from collections import deque
from heapq import heappush, heappop

dados = sys.stdin.read().split()
p = 0
while p < len(dados):
    n = int(dados[p]); p += 1
    pilha, fila, heap = [], deque(), []
    e_pilha = e_fila = e_heap = True
    for _ in range(n):
        cmd, x = int(dados[p]), int(dados[p + 1]); p += 2
        if cmd == 1:
            pilha.append(x)
            fila.append(x)
            heappush(heap, -x)
        else:
            # só tira da estrutura que ainda é candidata (e que não esvaziou)
            if e_pilha:
                e_pilha = bool(pilha) and pilha.pop() == x
            if e_fila:
                e_fila = bool(fila) and fila.popleft() == x
            if e_heap:
                e_heap = bool(heap) and -heappop(heap) == x
    candidatas = [nome for nome, ok in
                  (("stack", e_pilha), ("queue", e_fila), ("priority queue", e_heap)) if ok]
    if len(candidatas) == 0:
        print("impossible")
    elif len(candidatas) == 1:
        print(candidatas[0])
    else:
        print("not sure")
