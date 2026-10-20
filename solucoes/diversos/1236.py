# 1236 - Compactação de Arquivos   (STRING: contar repetições)
#
# IDEIA: percorre a linha agrupando sequências do MESMO caractere.
#   - Sequência de "0" ou " " com 3+ repetições -> símbolo + chr(quantidade)
#       "#" para zeros, "$" para espaços.
#   - Se passar de 255, divide em blocos de até 255.
#   - Sequência de 1 ou 2 (ou outros caracteres) -> fica como está.
#
# PYTHON:
#   chr(n) = caractere de código ASCII n.
#   Saída escrita em bytes (latin-1) para o chr(255) e afins saírem certos no Windows.
import sys

def compacta(linha):
    saida = []
    i = 0
    while i < len(linha):
        c = linha[i]
        j = i
        while j < len(linha) and linha[j] == c:    # j avança enquanto repete
            j += 1
        qtd = j - i
        if c in "0 ":
            simbolo = "#" if c == "0" else "$"
            while qtd > 0:
                bloco = min(qtd, 255)
                saida.append(simbolo + chr(bloco) if bloco >= 3 else c * bloco)
                qtd -= bloco
        else:
            saida.append(c * qtd)
        i = j
    return "".join(saida)

n = int(sys.stdin.readline())
for _ in range(n):
    linha = sys.stdin.readline().rstrip("\n")
    sys.stdout.buffer.write((compacta(linha) + "\n").encode("latin-1"))
