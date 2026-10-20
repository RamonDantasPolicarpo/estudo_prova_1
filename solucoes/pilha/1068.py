# 1068 - Balanço de Parênteses I   (PILHA)
#
# IDEIA: cada "(" fica esperando um ")". Empilha o "(" e, quando vier ")", desempilha.
#   - ")" com pilha vazia  -> fechou sem abrir      -> incorrect
#   - sobrou "(" no fim    -> abriu e não fechou    -> incorrect
#
# PYTHON p/ quem vem do Java:
#   - list vira pilha:  pilha.append(x) = push   |   pilha.pop() = pop
#   - "if pilha" é verdadeiro quando NÃO está vazia (como !pilha.isEmpty())
#   - entrada sem N (termina no fim do arquivo) -> "for linha in sys.stdin"
import sys

for linha in sys.stdin:
    pilha = []
    ok = True
    for c in linha:
        if c == "(":
            pilha.append(c)
        elif c == ")":
            if not pilha:          # pilha vazia: ")" sem "(" correspondente
                ok = False
                break
            pilha.pop()
    if pilha:                      # sobrou "(" sem par
        ok = False
    print("correct" if ok else "incorrect")
