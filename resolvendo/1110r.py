from collections import deque

n = int(input())
fila = deque()
descarte = []

for i in range(n):
    fila.append(i+1)

while len(fila) >= 2:
    descarte.append(fila.popleft())
    fila.append(fila.popleft())

texto = ", ".join(str(x) for x in descarte)

print(f"cartas descartadas: {texto}")
print(f"cartas restante: {fila[0]}")