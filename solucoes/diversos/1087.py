# 1087 - Dama   (LÓGICA, sem estrutura de dados)
#
# IDEIA: dama move em linha, coluna ou diagonal.
#   mesma casa             -> 0 movimentos
#   mesma linha/coluna     -> 1
#   mesma diagonal         -> 1  (|dx| == |dy|)
#   qualquer outra         -> 2  (sempre dá em 2 no tabuleiro 8x8)
#
# PYTHON: abs() = valor absoluto (Math.abs do Java).
while True:
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
    if x1 == x2 and y1 == y2:
        print(0)
    elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        print(1)
    else:
        print(2)
