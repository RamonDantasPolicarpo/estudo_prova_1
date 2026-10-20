# Ramon resolve pilha e fila em Python, mas tropeça na sintaxe vinda do Java

Na véspera da prova prática, Ramon montou sozinho a lógica do 1068 (parênteses) e do 1069 (diamantes), com pilha. Acertou as regras de "incorrect" por raciocínio próprio. Os erros foram de sintaxe e de fluxo, não de lógica.

## Evidence
- Escreveu `pilha.len()` e `pilha.len > 0` (Java) em vez de `len(pilha)`
- No 1069, deixou um `break` solto dentro do `for`, que encerrava o laço na 1ª volta, e usou `break` onde devia ignorar o caractere
- Perguntou como montar o laço de entrada (`int(input())` + `for`), o que mostra que o molde de leitura ainda não é automático
- Ficou confuso com `fila.append(fila.popleft())` (ler de dentro pra fora) e com tirar os `[ ]` do print (`join` exige `str()`)
- Corrigido o `break`, o 1069 deu 3 e 1 no exemplo do enunciado

## Implications
- Antes de praticar mais problemas, reforçar: `len(x)`, `break`, `int(input())`, `join` com `str()`
- Ele raciocina bem sobre o problema, então vale gastar tempo na sintaxe e não na lógica
- Falta praticar: ordenação (1259, 1244, 1162), `heapq` e `bisect` em código, e leitura até EOF
- Restrição nova: só pode usar o que foi visto nos Kahoots. Confirmar com a turma o que a prova permite
- Material de consulta criado: `reference/consulta-python-prova.html`
