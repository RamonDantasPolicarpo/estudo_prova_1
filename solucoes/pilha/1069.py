# 1069 - Diamantes e Areia   (PILHA)
#
# IDEIA: é o MESMO algoritmo do 1068. "<" é o "(" e ">" é o ")".
#   Cada ">" que encontra um "<" esperando forma um diamante -> conta +1.
#   A areia "." é ignorada.
#
# PYTHON: for _ in range(n)  = repetir n vezes (o "_" diz que não usamos o contador)
n = int(input())

for _ in range(n):
    linha = input()
    pilha = []
    diamantes = 0
    for c in linha:
        if c == "<":
            pilha.append(c)
        elif c == ">" and pilha:   # só forma diamante se houver "<" esperando
            pilha.pop()
            diamantes += 1
    print(diamantes)
