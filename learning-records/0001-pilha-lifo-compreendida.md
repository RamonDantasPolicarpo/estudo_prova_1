# Ramon compreende Pilha (LIFO) e o mecanismo de inversão

Ramon demonstrou entendimento genuíno de LIFO — não apenas que pilha "remove o último", mas *por que* isso causa inversão quando se transfere elementos entre duas estruturas. Explicou com suas palavras ("os últimos serão os primeiros") sem consultar material. Já programa em Java, então o conceito de Stack não é novo — a barreira era apenas a sintaxe Python (`append`/`pop` vs `push`/`pop`).

## Evidence
- Respondeu corretamente que `[1,2,3,4,5]` invertido via pop+append gera `[5,4,3,2,1]`
- Explicou o mecanismo: "cada um de cima vai sendo colocado no resultado invertendo a ordem"

## Implications
- Pode avançar para Fila (FIFO) — o contraste LIFO vs FIFO vai se ancorar bem
- Sintaxe Python básica (`while lista:`, `append`, `pop`) já está internalizada
- Provavelmente captará rápido por que `pop(0)` é problemático em listas (gargalo)
