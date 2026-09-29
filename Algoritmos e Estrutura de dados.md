## Matéria 4º semestre

Matéria boa, professor péssimo, linguagem péssima.
A matéria em si é muito importante, porém o professor é péssimo, não explica nada, e faz em Python que é cheio de bibliotecas que substituem nossa abstração dos conceitos por métodos prontos com nomes completamente diferentes de outras linguagens mais estáveis no quesito de sintaxe, eu uso Java, mas acho que o C++ seria perfeito para essa matéria, ele não explica nada só faz as atividades lá no VS Code em Python, e a gente copia o código sem nem entender o que tá fazendo, não explica nada, a única coisa que ele fala é -"Em Python é literalmente isso, se fosse em Java seriam não sei quantas mil linhas". Vai ter prova prática em código dessa matéria então preciso aprender essa bosta de Python, mas isso é para a próxima prova, essa primeira vai ser teórica, então preciso compreender todos em conceitos presentes no Kahoot, inclusive dessas bibliotecas em python.

---
### Kahoot 1

1ª Qual dessas estruturas é LIFO?
R: Pilha

2ª Quando a busca binária é melhor?
R: Vetor ordenado

3ª Por que ordenar antes de buscar?
R: Permite busca binária

4ª Como funciona uma fila em um sistema de impressão?
R: Primeiro que chega, primeiro sai 

5ª Como remover elemento da fila?
R: Deque

6ª Qual vantagem da busca binária sobre a linear?
R: Menos comparações

7ª Como uma fila ajuda em sistemas de atendimento?
R: Organizar ordens 

8ª Porque a busca binária usa meio de intervalo?
R: Divide problema

9ª Quando a busca linear pode ser melhor que a binária?
R: Poucos elementos

10ª Como a pilha é usada em desfazer ações?
R: Ultima ação primeiro

11ª Qual dessas ordenações seria mais estável?
R: Que mantém iguais juntos 

12ª Qual efeito da ordenação em pesquisa de dados?
R: Busca mais rápida

13ª Uma busca binária sempre permite busca binária.
R: Verdadeiro

14ª Quantos vizinhos máximos são checados em uma busca binária?
R: 2

---
### Kahoot 2

1ª Resolva este código:
``` python
pilha = []

pilha.append(10)
pilha.append(20)
pilha.append(30)

print(pilha.pop())
```

R: 30

2ª Resolva este código:
``` python
pilha = [5, 10, 15, 20]

pilha.pop()
pilha.pop()

print(pilha)
```

R: [5, 10]

3ª Resolva este código:
``` python
pilha = []

for i in range(1, 5):
	pilha.append(i)

while pilha:
	print(pilha.pop(), end=" ")
```

R: 4 3 2 1

4ª Resolva este código:
``` python
texto = "DADOS"
pilha = []

for letras in texto:
	pilha.append(letra)
	
invertido = ""

while pilha:
	inverido += pilha.pop()
	
	print(invertido)
```

R:  SODAD

5ª Resolva este código:
``` python
pilha = [1, 2, 3, 4, 5]

resultado = []

while pilha:
	resultado.append(pilha.pop())
	
print(resultado)
```

R: [5, 4, 3, 2, 1]

6ª Resolva este código:
``` python
from collections import deque

fila = deque()

fila.append(10)
fila.append(20)
fila.append(30)

print(fila.popleft())
```

R: 10

7ª Resolva este código:
``` python
from collections import deque

fila = deque([10, 20, 30, 40])

fila.popleft()
fila.append(50)

print(fila)
```

R:  [20, 30, 40, 50]

8ª Resolva este código:
``` python
from collections import deque

fila = deque()

for i in range(1, 6):
	fila.append(i)

print(fila.popleft())
print(fila.popleft())
```

R: 1, 2

9ª Resolva este código:
``` python
estrutura = []

estrutura.append("A")
estrutura.append("B")
estrutura.append("C")

print(estrutura.pop())
```

R: Pilha

10ª Resolva este código:
``` python
from collections import deque

fila = deque(["A", "B", "C"])

print(fila.popleft())
```

R: FIFO

11ª Resolva este código:
``` python
vetor = [2, 4, 6, 8, 10, 12, 14]

inicio = 0
fim = len(vetor) - 1
meio = (inicio + fim) // 2

print(vetor[meio])
```

R:  8

12ª Resolva este código:
``` python
vetor = [10, 20, 30, 40, 50, 60, 70]

inicio = 0
fim = len(vetor) - 1

meio = (inicio + fim) // 2

if vetor[meio] == 40:
	print("Encontrado")
else:
	print("Não encontrado")

```

R: Encontrado

13ª Coloque o código na ordem correta da melhor forma, considerando um exercício de Ordem Binária.
R: 
	1º vetor = [5, 10, 15, 20, 25, 30, 35]
	2º incicio = 0 fim = 6 meio =(inicio + fim) // 2
	3º if vetor[meio] < 25: inicio = meio + 1
	4º print(inicio)

---
### Kahoot 3

1ª por que pilha em vetor pode estourar mais cedo?
R: Limite estático

2ª como contador em pilha ligada ajuda?
R: Check rápido

3ª Como notação pós-fixa usa pilha na prática? (São duas respostas)
R: Empilha operandos + Empilha operadores

4ª como lista circular ajuda escalonamento?
R: Percurso contínuo

5ª em execução recursiva, o que a pilha da máquina guarda?
R: Frames de chamada

6ª como pilha ajuda a verificar parênteses balanceados?
R: Empilha aberturas

7ª qual resultado do código?
``` python
v = [2, 4, 6]
v.append(8)
v.append(10)

print(len(v))
```

R: 5

8ª qual resultado do código?
``` python
v = [7, 2, 9, 4, 1]

v.sort()

print(v[0])
```

R: 1

9ª qual resultado do código?
``` python
v = [7, 2, 9, 4, 1]

v.sort()

print(v[-1])
```

R: 9

10ª quantas trocas surgirá neste código?
``` python
v = [3, 1, 2]

trocas = 0

for i in range(1, len(v)):
	j = i
	
	while j > 0 and v[j] < v[j - 1]:
	v[j], v[j - 1] = v[j - 1], v[j]
	trocas += 1
	j -= 1
	
print(trocas)
```

R: 9

---
### Kahoot 4

1ª Ao implementar uma fila FIFO com list, qual operação se torna gargalo principal em um projeto?
R: pop(0)

2ª você tem muitas remoções no início da fila; qual estratégia para ajustar sua implementação?
R: Usar deque

3ª por que deque é mais indicado que list para operações frequentes nas duas extremidades?
R: Blocos ligados

4ª Qual combinação de métodos de deque implementa corretamente uma fila FIFO clássica?
R: append+popleft

5ª Como você montaria uma fila FIFO clássica usando apenas métodos nativos de deque?
R: append e popleft

6ª Por que usar append e popleft em deque respeita naturalmente a ordem de chegada FIFO?
R: Entrada no fim

7ª Você precisa de acesso LIFO simples; qual estrutura padrão de Python é mais direta?
R: List

8ª você quer uma pilha rápida com push e pop no final; qual método usar?
R: append e pop

9ª por que concatenar strings com "+" em um grande loop pode ser mais trabalhoso em um projeto robusto?
R: cópias repetidas

10ª como você deveria concatenar muitas strings para obter um resultado total de forma linear?
R: ".join(lista)

11ª como o uso de join em vez de mais reduz o custo ao concatenar strings?
R: uma cópia final

12ª Quando foi criada as primeiras estruturas de Dados em Python?
R: 1989

13ª como você simularia uma fila de prioridade máxima usando heapq sem uma nova estrutura?
R: Negar pesos

14ª qual diferença principal entre bisect_left e bisect_right ao inserir duplicatas?
R: Posição em borda

15ª você recebe um gerador; o que sorted faz com ele internamente antes de ordenar?
R: Consome inteiro

16ª Qual estrutura você escolheria para acesso por prioridade com extração frequente em um projeto de Fila de prioridade?
R: heapq

17ª entre list, deque e heapq, qual critério orienta melhor a escolha prática?
R: Operações alvo



