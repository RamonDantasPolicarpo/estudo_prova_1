# 1211 - Lista Telefônica Econômica   (ORDENAÇÃO + prefixo comum)
#
# IDEIA: depois de ORDENAR os números, os que compartilham prefixo ficam vizinhos.
#   Então basta somar o prefixo comum de cada número com o ANTERIOR.
#
# PYTHON: entrada até EOF -> lê tudo com sys.stdin.read().split() e vai andando
#         por um índice. (Telefones são tratados como texto, pois podem começar com 0.)
import sys

dados = sys.stdin.read().split()
p = 0
while p < len(dados):
    n = int(dados[p]); p += 1
    telefones = sorted(dados[p:p + n]); p += n
    economia = 0
    for i in range(1, n):
        a, b = telefones[i - 1], telefones[i]
        k = 0
        while k < len(a) and a[k] == b[k]:     # conta caracteres iguais no começo
            k += 1
        economia += k
    print(economia)
