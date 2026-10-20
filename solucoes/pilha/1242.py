# 1242 - Ácido Ribonucleico Alienígena   (PILHA)
#
# IDEIA: de novo o molde do 1068. Cada base tenta casar com a do TOPO da pilha.
#   Pares válidos: B-S e C-F (em qualquer ordem).
#   Se casa  -> desempilha e conta 1 ligação.
#   Se não   -> empilha e segue.
#
# PYTHON: "in" funciona em conjunto/tupla; aqui guardamos os pares válidos num set.
import sys

PARES = {("B", "S"), ("S", "B"), ("C", "F"), ("F", "C")}

for linha in sys.stdin:
    fita = linha.strip()
    pilha = []
    ligacoes = 0
    for base in fita:
        if pilha and (pilha[-1], base) in PARES:   # pilha[-1] = topo (peek)
            pilha.pop()
            ligacoes += 1
        else:
            pilha.append(base)
    print(ligacoes)
