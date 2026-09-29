# Ramon compreende Fila (FIFO) e distingue de Pilha

Ramon demonstrou entendimento imediato de FIFO — identificou corretamente que `popleft()` remove o primeiro elemento e articulou a regra com suas palavras ("o primeiro que entrou vai ser o primeiro a sair"). A transição LIFO→FIFO foi suave, a base de Java ajudou.

## Evidence
- Respondeu corretamente que `deque(["A","B","C"]).popleft()` retorna "A"
- Identificou como comportamento de Fila sem hesitação

## Implications
- Distinção Pilha vs Fila está sólida — pode avançar para Busca
- Conceito de `deque` e `popleft` internalizado
- Pronto para entender por que ordenação habilita busca binária
