# 1251 - Diga-me a Frequência   (DICIONÁRIO + ordenação com 2 critérios)
#
# IDEIA: conta quantas vezes cada caractere aparece (dict), usando o valor ASCII
#   (ord). Ordena por frequência CRESCENTE e, no empate, ASCII DECRESCENTE.
#
# PYTHON:
#   ord("A") = 65  (caractere -> número)      chr(65) = "A"
#   dict.get(k, 0) devolve 0 se a chave não existe (evita o "if k in dict").
#   key=lambda: (freq, -ascii)  -> tupla compara o 1º item, depois o 2º.
import sys

primeiro = True
for linha in sys.stdin:
    linha = linha.rstrip("\n")
    freq = {}
    for c in linha:
        freq[ord(c)] = freq.get(ord(c), 0) + 1

    if not primeiro:
        print()                                    # linha em branco ENTRE conjuntos
    primeiro = False
    for ascii_, qtd in sorted(freq.items(), key=lambda kv: (kv[1], -kv[0])):
        print(ascii_, qtd)
