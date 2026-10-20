# 1063 - Trilhos Novamente   (PILHA)
#
# IDEIA: a estação é uma pilha (só entra e sai pelo mesmo lado).
#   Para cada vagão que chega: empilha (I).
#   Enquanto o TOPO for o próximo vagão desejado na saída: desempilha (R).
#   No fim, se todos saíram na ordem pedida, deu certo; senão "Impossible".
#
# PYTHON: ''.join(linha.split()) tira os espaços entre as letras ("e t d a" -> "etda")
while True:
    n = int(input())
    if n == 0:
        break
    entrada = "".join(input().split())
    saida = "".join(input().split())

    pilha = []
    ops = ""
    j = 0                                  # posição da próxima letra desejada
    for vagao in entrada:
        pilha.append(vagao)
        ops += "I"
        while pilha and j < n and pilha[-1] == saida[j]:
            pilha.pop()
            ops += "R"
            j += 1

    print(ops if j == n else ops + " Impossible")
