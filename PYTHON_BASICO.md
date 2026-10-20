# Python básico — SÓ o que apareceu nos Kahoots

Se o professor limita ao que foi usado em aula, este é o seu vocabulário.
Tudo aqui saiu dos 4 Kahoots (ver `Algoritmos e Estrutura de dados.md`).

## 0. Regras gerais (Java -> Python)

| Java | Python |
|---|---|
| `{ }` para blocos | **indentação** (4 espaços ou Tab) + `:` no fim da linha |
| `;` no fim | não usa |
| `int x = 5;` | `x = 5` (sem tipo) |
| `ArrayList<Integer> v = new ArrayList<>();` | `v = []` |
| `v.add(x)` | `v.append(x)` |
| `v.size()` | `len(v)` |
| `System.out.println(x)` | `print(x)` |
| `for (int i=1; i<5; i++)` | `for i in range(1, 5):` (vai de 1 a **4**, o fim não entra) |
| `&&`, `||`, `!` | `and`, `or`, `not` |
| `else if` | `elif` |
| `//` comentário | `# comentário` |

## 1. Lista = vetor / pilha

```python
v = [5, 10, 15]
v.append(20)        # põe no FIM        -> [5, 10, 15, 20]
v.pop()             # tira do FIM e devolve (20)
v[0]                # primeiro (5)
v[-1]               # ÚLTIMO (10)       <- no Kahoot 3
len(v)              # tamanho
v.sort()            # ordena a própria lista (crescente)
```

## 2. Pilha (LIFO) = lista com `append` + `pop`

```python
pilha = []
pilha.append(10)
pilha.append(20)
print(pilha.pop())          # 20 (último a entrar, primeiro a sair)

while pilha:                # "enquanto a pilha NÃO estiver vazia"
    print(pilha.pop(), end=" ")   # end=" " imprime sem pular linha
```

## 3. Fila (FIFO) = `deque` com `append` + `popleft`

```python
from collections import deque     # precisa importar!

fila = deque()                    # ou deque([10, 20, 30])
fila.append(10)                   # entra no FIM
fila.append(20)
print(fila.popleft())             # 10 (sai pelo INÍCIO)
```
Não use `lista.pop(0)` para fila: é lento (Kahoot 4).

## 4. Laços e condições

```python
for i in range(1, 5):          # 1,2,3,4
    print(i)

for letra in "DADOS":          # percorre texto letra a letra
    print(letra)

while j > 0 and v[j] < v[j-1]:
    j -= 1                     # -=  +=  funcionam como em Java

if x == 40:
    print("Encontrado")
else:
    print("Não encontrado")
```

## 5. Texto (string)

```python
invertido = ""
invertido += letra                  # concatena (ok para poucos)
" ".join(lista_de_textos)           # junta vários textos com separador (Kahoot 4)
```
`join` só junta **textos**. Para números: `" ".join([str(x) for x in lista])` não foi
visto; faça um laço e use `str(x)` se precisar.

## 6. Troca de dois valores (Insertion/Bubble Sort)

```python
v[j], v[j-1] = v[j-1], v[j]         # sem variável temporária
```

## 7. Busca binária (Kahoot 2)

```python
vetor = [5, 10, 15, 20, 25, 30, 35]
inicio = 0
fim = len(vetor) - 1
meio = (inicio + fim) // 2          # // = divisão INTEIRA
if vetor[meio] < 25:
    inicio = meio + 1               # procura na metade da direita
```
Biblioteca pronta (Kahoot 4): `from bisect import bisect_left, bisect_right`.
`bisect_left` e `bisect_right` só diferem com **duplicatas** (posição da borda).

## 8. Fila de prioridade (Kahoot 4)

```python
import heapq
heap = []
heapq.heappush(heap, 5)
heapq.heappop(heap)                 # sai o MENOR (min-heap)
# MAIOR primeiro: guarde o valor NEGADO  ->  heappush(heap, -x)  e  -heappop(heap)
```

## 9. `sorted` x `sort`

- `v.sort()` altera a lista. `sorted(v)` devolve uma nova.
- Ordenação **estável**: itens iguais mantêm a ordem original.

---

## ⚠️ Coisas das minhas soluções que NÃO apareceram nos Kahoots

As soluções em `solucoes/` usam recursos extras. Se o professor realmente restringe,
**evite** estes e prefira o equivalente da coluna da direita:

| Usei | Não visto em aula | Alternativa |
|---|---|---|
| `import sys` / `sys.stdin` | leitura até EOF | `input()` em laço `while True` (confirme com a turma como a prova entrega a entrada) |
| `dict` (`{}`) | dicionários | duas listas paralelas ou lista de listas |
| `lambda`, `key=` | ordenação com critério | `v.sort()` simples; ou implementar Bubble/Insertion Sort na mão (esse **foi** visto!) |
| f-strings `f"..{x}.."` | formatação | `print("texto", x)` |
| `map(int, ...)`, `split()` | conversão em massa | `int(x)` e `.split()` (pergunte se `split` vale) |
| `math.gcd` | MDC | laço com `while b != 0` |
| `ord`, `chr`, `set`, tuplas | — | evitar |

**Veja o que o enunciado pede e use só pilha / fila / Insertion Sort / busca binária.**
Os problemas mais seguros para esse limite: 1068, 1069, 1242, 1063, 1110, 1162, 1259, 1025.
