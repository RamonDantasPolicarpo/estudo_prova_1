# 1022 - TDA Racional   (frações + MDC)
#
# IDEIA: lê "N1 / D1 op N2 / D2", aplica a fórmula da operação e simplifica
#   dividindo numerador e denominador pelo MDC (máximo divisor comum).
#
# PYTHON: math.gcd(a, b) já calcula o MDC. split() separa a linha em pedaços.
from math import gcd

n = int(input())
for _ in range(n):
    n1, _b1, d1, op, n2, _b2, d2 = input().split()   # os "/" viram variáveis ignoradas
    n1, d1, n2, d2 = int(n1), int(d1), int(n2), int(d2)

    if op == "+":
        num, den = n1 * d2 + n2 * d1, d1 * d2
    elif op == "-":
        num, den = n1 * d2 - n2 * d1, d1 * d2
    elif op == "*":
        num, den = n1 * n2, d1 * d2
    else:                                            # "/"
        num, den = n1 * d2, n2 * d1

    g = gcd(num, den)                                # gcd aceita negativo e devolve positivo
    print(f"{num}/{den} = {num // g}/{den // g}")
