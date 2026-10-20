# 1256 - Tabelas Hash   (HASH com encadeamento exterior)
#
# IDEIA: tabela = M "gavetas" (listas). A chave x vai na gaveta  x % M.
#   Se duas chaves caem na mesma gaveta (colisão), ficam encadeadas, na ordem de chegada.
#
# PYTHON: [[] for _ in range(M)] cria M listas independentes.
#         (CUIDADO: [[]] * M criaria M referências à MESMA lista!)
n = int(input())
for caso in range(n):
    m, c = map(int, input().split())
    chaves = list(map(int, input().split()))

    tabela = [[] for _ in range(m)]
    for x in chaves:
        tabela[x % m].append(x)

    if caso > 0:
        print()                                    # linha em branco entre os casos
    for i in range(m):
        linha = f"{i} -> "
        for x in tabela[i]:
            linha += f"{x} -> "
        print(linha + "\\")
