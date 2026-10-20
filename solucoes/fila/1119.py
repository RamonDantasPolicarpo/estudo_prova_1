# 1119 - A Fila do Desemprego   (LISTA CIRCULAR)
#
# IDEIA: lista com 1..N. Dois "ponteiros" andam em sentidos opostos:
#   a -> horário (soma k), b -> anti-horário (subtrai m).
#   O operador "%" (resto da divisão) faz o círculo "dar a volta".
#   Os dois são removidos ao mesmo tempo (se forem o mesmo, remove um só).
#   Depois, cada um recomeça na pessoa seguinte disponível no seu sentido.
#
# PYTHON: "%" com negativo dá resultado positivo ((-1) % 5 == 4) - diferente do Java!
#         "%3d" formata o número com largura 3 (alinha à direita, com espaços).
while True:
    n, k, m = map(int, input().split())
    if n == 0 and k == 0 and m == 0:
        break
    L = list(range(1, n + 1))
    a, b = 0, n - 1                          # início: 1º (horário) e N-ésimo (anti-horário)
    saida = []
    while L:
        t = len(L)
        a = (a + k - 1) % t
        b = (b - (m - 1)) % t
        if a == b:
            saida.append("%3d" % L[a])
            del L[a]
            if L:
                a = a % len(L)               # próximo no horário
                b = (a - 1) % len(L)         # próximo no anti-horário
        else:
            saida.append("%3d%3d" % (L[a], L[b]))
            for i in sorted((a, b), reverse=True):   # remove o maior índice primeiro
                del L[i]
            if L:
                na = a - (1 if b < a else 0)         # ajusta índices após as remoções
                nb = b - 1 - (1 if a < b else 0)
                a, b = na % len(L), nb % len(L)
    print(",".join(saida))
