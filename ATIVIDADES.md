# Atividades — Prova Prática (Beecrowd)

22 problemas, na ordem em que o professor liberou (= ordem das aulas).

## Visão geral (ordem das aulas)

| # | Problema | Título (Beecrowd) | Estrutura / técnica | Entrada termina com | Dificuldade |
|---|---|---|---|---|---|
| 1 | 1025 | Onde está o Mármore? | Ordenar + busca (binária / `bisect`) | sentinela `0 0` | ⭐⭐ |
| 2 | 1068 | Balanço de Parênteses I | **Pilha** | EOF | ⭐ |
| 3 | 1069 | Diamantes e Areia | **Pilha** (contador) | N casos | ⭐ |
| 4 | 1110 | Jogando Cartas Fora | **Fila** (`deque`) | sentinela `0` | ⭐ |
| 5 | 1119 | A Fila do Desemprego | Lista circular (dois contadores) | sentinela `0 0 0` | ⭐⭐⭐ |
| 6 | 1167 | Grupo de Festa (Josephus) | Lista circular | sentinela `0` | ⭐⭐⭐ |
| 7 | 1162 | Organizador de Vagões | **Ordenação** — Bubble Sort contando trocas | N casos | ⭐ |
| 8 | 1211 | Lista Telefônica Econômica | Ordenação + prefixo comum | EOF | ⭐⭐ |
| 9 | 1259 | Pares e Ímpares | Ordenação (crescente / decrescente) | N valores | ⭐ |
| 10 | 1244 | Ordenação por Tamanho | Ordenação **estável** com `key=len` | N casos | ⭐ |
| 11 | 1251 | Diga-me a Frequência | Contagem (**dicionário**) + ordenação com 2 critérios | EOF | ⭐⭐ |
| 12 | 1256 | Tabelas Hash | **Hash** com encadeamento (lista de listas) | N casos | ⭐⭐ |
| 13 | 1258 | Camisetas | Ordenação com **vários critérios** | sentinela `0` | ⭐⭐ |
| 14 | 1022 | TDA Racional | Frações + MDC (`math.gcd`) | N casos | ⭐⭐ |
| 15 | 1023 | Estiagem | **Dicionário** (agrupar) + ordenação + truncar | sentinela `0` | ⭐⭐⭐ |
| 16 | 1063 | Trilhos Novamente | **Pilha** (simulação I/R) | sentinela `0` | ⭐⭐ |
| 17 | 1077 | Infixa para Posfixa | **Pilha** de operadores (precedência) | N casos | ⭐⭐⭐ |
| 18 | 1236 | Compactação de Arquivos | String / contagem de repetições + `chr()` | N casos | ⭐⭐⭐ |
| 19 | 1242 | Ácido Ribonucleico Alienígena | **Pilha** (casar pares) | EOF | ⭐⭐ |
| 20 | 1340 | Eu Posso Adivinhar a Estrutura | **Pilha + Fila + Heap** ao mesmo tempo | EOF | ⭐⭐ |
| 21 | 1087 | Dama | Lógica / condicionais (sem estrutura) | sentinela `0 0 0 0` | ⭐ |
| 22 | 1112 | Schweisen | Matriz 2D (soma em retângulo — BIT 2D) | sentinela `0 0 0` | ⭐⭐⭐⭐ |

## Agrupado por padrão

### 🥞 Pilha (LIFO) — `list` com `append()` / `pop()`
O bloco mais importante: **6 problemas**.
- **1068** Parênteses → empilha `(`, desempilha em `)`. Pilha vazia na hora errada = incorrect.
- **1069** Diamantes → mesma ideia do 1068 com `<` e `>`, mas conta quantos pares fechou.
- **1242** RNA → mesma ideia, mas o "par" é B–S ou C–F. Se o topo casa com o atual, desempilha e conta.
- **1063** Trilhos → simula: empilha vagão (I), desempilha quando o topo é o próximo esperado (R).
- **1077** Infixa → posfixa → pilha de operadores com precedência (`^` > `*` `/` > `+` `-`).
- **1340** (também usa pilha, ver abaixo)

> 💡 1068, 1069 e 1242 são **o mesmo algoritmo** com outra roupagem. Aprendeu um, aprendeu os três.

### 🚶 Fila (FIFO) / Lista circular — `collections.deque`
- **1110** Cartas → `popleft()` (descarta) + `append(popleft())` (manda pra base). Clássico.
- **1167** Josephus → círculo; remove posição calculada com `%` (resto da divisão).
- **1119** Desemprego → círculo com dois contadores andando em sentidos opostos. O mais chato do grupo.

### 🔀 Pilha + Fila + Heap juntas
- **1340** → simula as três estruturas em paralelo (`list`, `deque`, `heapq` com números negativos para ter max-heap) e vê quais "sobrevivem".

### 🔍 Busca
- **1025** Mármore → ordena e acha a **primeira** ocorrência. `bisect_left` resolve direto.

### 📊 Ordenação — `sorted()` / `.sort()` com `key=`
- **1162** Vagões → implementar **Bubble Sort** na mão e contar as trocas (o único que pede o algoritmo).
- **1259** Pares/ímpares → separa em duas listas, ordena uma crescente e outra decrescente.
- **1244** Por tamanho → `sorted(palavras, key=len, reverse=True)` (o `sorted` do Python é **estável**).
- **1258** Camisetas → `key=` com tupla de vários critérios (cor ↑, tamanho ↓, nome ↑).
- **1211** Lista telefônica → ordena e compara cada número com o anterior (prefixo comum).

### #️⃣ Hash / Dicionário — `dict`
- **1256** Tabela Hash → `tabela = [[] for _ in range(M)]`, endereço = `chave % M`.
- **1251** Frequência → conta com `dict` e ordena com 2 critérios.
- **1023** Estiagem → agrupa consumo por pessoa com `dict` e ordena as chaves.

### 🧩 Diversos (sem estrutura de dados central)
- **1022** Frações → contas + `math.gcd` para simplificar.
- **1087** Dama → só `if`: mesma casa = 0, mesma linha/coluna/diagonal = 1, senão 2.
- **1236** Compactação → percorrer string contando repetições; saída com `chr()`. Detalhista.
- **1112** Schweisen → exige BIT 2D para não estourar o tempo. **Fora do escopo provável.**

## Os 3 jeitos que a entrada termina (aparece em TODOS)

É a parte "montar a função a partir do enunciado" que mais se repete:

| O enunciado diz... | Padrão de leitura |
|---|---|
| "A primeira linha contém N casos de teste" | `for _ in range(int(input())):` |
| "A entrada termina com 0" (sentinela) | `while True:` … `if n == 0: break` |
| "Termina com final de arquivo (EOF)" | `while True:` + `try: linha = input()` / `except EOFError: break` |

## Prioridade sugerida (tempo curto)

1. **Pilha:** 1068 → 1069 → 1242 → 1063 → 1077
2. **Fila:** 1110 → 1340
3. **Ordenação:** 1259 → 1244 → 1162 → 1258
4. **Hash/Busca:** 1256 → 1025 → 1251
5. Se sobrar tempo: 1022, 1087, 1211, 1023, 1167, 1119, 1236
6. Ignorar: 1112
