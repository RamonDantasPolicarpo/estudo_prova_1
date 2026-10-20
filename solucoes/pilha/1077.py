# 1077 - Infixa para Posfixa   (PILHA - algoritmo "shunting yard")
#
# IDEIA: operandos (letras/números) vão direto pra saída.
#   Operadores ficam numa pilha. Antes de empilhar um operador, tira da pilha
#   (e joga na saída) os que têm precedência MAIOR ou IGUAL.
#   "(" empilha; ")" desempilha tudo até achar o "(".
#   Exceção: "^" é associativo à direita, então só tira os de precedência MAIOR.
#
# PYTHON: dicionário  { chave: valor }  = HashMap do Java.
PREC = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

n = int(input())
for _ in range(n):
    expr = input().strip()
    saida = ""
    pilha = []
    for c in expr:
        if c == "(":
            pilha.append(c)
        elif c == ")":
            while pilha[-1] != "(":
                saida += pilha.pop()
            pilha.pop()                     # descarta o "("
        elif c in PREC:
            while pilha and pilha[-1] != "(" and (
                PREC[pilha[-1]] > PREC[c]
                or (PREC[pilha[-1]] == PREC[c] and c != "^")
            ):
                saida += pilha.pop()
            pilha.append(c)
        else:                               # operando
            saida += c
    while pilha:                            # esvazia o que sobrou
        saida += pilha.pop()
    print(saida)
