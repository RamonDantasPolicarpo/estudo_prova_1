n = int(input())

for i in range(n):
    linha = input()

    pilha = []
    diamantes = 0

    for c in linha:
        if c == "<":
            pilha.append(1)
        elif c == ">":
            if not pilha:
                pass
            else:
                pilha.pop()
                diamantes += 1
    
    print(diamantes)
        