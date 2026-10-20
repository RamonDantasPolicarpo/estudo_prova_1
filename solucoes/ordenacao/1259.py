# 1259 - Pares e Ímpares   (ORDENAÇÃO)
#
# IDEIA: separa em duas listas. Pares em ordem crescente, ímpares em decrescente.
#
# PYTHON:
#   - x % 2 == 0 testa par (igual ao Java).
#   - sorted(lista) = crescente;  sorted(lista, reverse=True) = decrescente.
#   - "pares + impares" CONCATENA listas.
n = int(input())
pares, impares = [], []
for _ in range(n):
    x = int(input())
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

resultado = sorted(pares) + sorted(impares, reverse=True)
print("\n".join(map(str, resultado)))
