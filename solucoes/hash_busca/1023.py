# 1023 - Estiagem   (DICIONÁRIO: agrupar + ordenar)
#
# IDEIA: consumo por pessoa = Y // X (divisão inteira, arredonda pra baixo).
#   Agrupa num dict: consumo -> total de pessoas com esse consumo.
#   Imprime por consumo crescente. Média = total_m3 / total_pessoas TRUNCADA
#   (sem arredondar) em 2 casas.
#
# PYTHON: "//" = divisão inteira.  "/" = divisão com decimais (diferente do Java!)
#   Para truncar sem erro de ponto flutuante, usamos só inteiros:
#   v = total*100 // pessoas  ->  parte inteira = v//100 ; decimais = v%100
import sys

dados = sys.stdin.read().split()
p = 0
cidade = 0
while True:
    n = int(dados[p]); p += 1
    if n == 0:
        break
    cidade += 1
    grupos = {}
    total_pessoas = total_m3 = 0
    for _ in range(n):
        x, y = int(dados[p]), int(dados[p + 1]); p += 2
        consumo = y // x
        grupos[consumo] = grupos.get(consumo, 0) + x
        total_pessoas += x
        total_m3 += y

    if cidade > 1:
        print()                                    # linha em branco entre cidades
    print(f"Cidade# {cidade}:")
    print(" ".join(f"{qtd}-{cons}" for cons, qtd in sorted(grupos.items())))
    v = total_m3 * 100 // total_pessoas
    print(f"Consumo medio: {v // 100}.{v % 100:02d} m3.")
