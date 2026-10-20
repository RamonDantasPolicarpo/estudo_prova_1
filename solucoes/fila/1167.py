# 1167 - Grupo de Festa (Josephus com ficha)   (LISTA CIRCULAR)
#
# IDEIA: a lista guarda os alunos no sentido ANTI-horário, então:
#   ficha PAR   -> conta no sentido horário      -> índice DIMINUI
#   ficha ÍMPAR -> conta no sentido anti-horário -> índice AUMENTA
#   "%" faz o círculo dar a volta.
#   Quem sai define a direção da próxima contagem (pela ficha dele).
#
# PYTHON: lista de tuplas [(nome, ficha), ...];  nome, ficha = tupla  "desempacota".
while True:
    n = int(input())
    if n == 0:
        break
    criancas = []
    for _ in range(n):
        nome, ficha = input().split()
        criancas.append((nome, int(ficha)))

    # 1ª contagem: parte da 1ª criança (índice 0), usando a ficha dela
    ficha = criancas[0][1]
    pos = (0 - ficha) % n if ficha % 2 == 0 else ficha % n
    while True:
        nome, ficha = criancas.pop(pos)       # elimina e guarda a ficha dela
        if not criancas:
            break
        t = len(criancas)
        # depois do pop, o índice "pos" já aponta pro vizinho anti-horário
        # (o vizinho horário é pos-1), por isso o "-1" no caso ímpar
        pos = (pos - ficha) % t if ficha % 2 == 0 else (pos + ficha - 1) % t
        if len(criancas) == 1:
            nome = criancas[0][0]
            break
    print(f"Vencedor(a): {nome}")
