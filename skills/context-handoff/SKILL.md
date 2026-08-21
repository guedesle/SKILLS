---
name: context-handoff
description: Produza handoffs compactos e completos entre agentes, modelos, conversas ou etapas. Use quando um trabalho será continuado por outro executor e é importante preservar estado, decisões, evidências, restrições, débitos, branches/PRs, gates e próximos passos sem reabrir perguntas já respondidas.
---

# Context Handoff

Use esta skill para transferir trabalho entre agentes, modelos, sessões ou etapas com perda mínima de contexto e sem repetir decisões já tomadas.

## Regra principal

Um handoff deve permitir que o próximo executor **continue**, não que reinicie a descoberta.

## Conteúdo mínimo

Inclua somente fatos úteis à continuação:

1. **objetivo atual** — qual resultado está sendo perseguido;
2. **estado observado** — branch, PR, artefatos, versão, dados ou ambiente relevantes;
3. **decisões tomadas** — escolhas já aprovadas e alternativas descartadas;
4. **restrições** — o que não pode ser alterado ou repetido;
5. **evidências** — testes, resultados, fontes, logs e fatos que sustentam o estado;
6. **trabalho concluído** — o que já entrega valor e não deve ser refeito;
7. **débitos abertos** — somente pendências reais;
8. **gates restantes** — técnicos e humanos;
9. **próxima ação recomendada** — ação concreta e verificável;
10. **não perguntar novamente** — informações já fornecidas que devem ser preservadas.

## Compressão sem perda

Prefira estado verificável a narrativa cronológica. Remova conversas intermediárias que não alteraram a decisão final.

Exemplo:

```text
Estado: PR #5 draft; local gate PASS.
Decisão: usar merge commit para preservar ancestry.
Pendente: elevated review final.
Não repetir: escolha da estratégia de merge já foi aprovada.
Próximo passo: revisar boundaries de maior risco e promover PR se não houver bloqueios.
```

## Handoff por responsabilidade

Quando houver roteamento entre modelos/agentes, registre também:

- papel do executor anterior;
- papel esperado do próximo;
- quais conclusões o próximo pode promover;
- quando deve escalar para um executor de maior autoridade/capacidade;
- quais ações continuam dependentes de autorização humana.

## Handoff técnico

Para repositórios, inclua quando aplicável:

- repo;
- branch atual;
- base;
- PR;
- HEAD relevante;
- working tree/status conhecido;
- comandos já executados;
- resultados dos gates;
- arquivos críticos alterados.

## Handoff de longa duração

Em trabalhos de várias rodadas, mantenha um resumo vivo e atualize somente o delta material. Não acumule fatos obsoletos como se ainda fossem pendências.

## Anti-padrões

Não:

- repetir toda a conversa;
- esconder incerteza;
- transformar hipótese em decisão;
- pedir novamente algo já decidido;
- omitir um bloqueio conhecido;
- afirmar `PASS` sem evidência do gate correspondente.

## Saída esperada

Entregue um bloco curto e operacional com: objetivo, estado, decisões, evidências, débitos, gates, próxima ação e itens que não devem ser reabertos.

## Origem

Generalizada dos handoffs usados nas rodadas do `guedesle/cyber-skills-framework`, onde mudanças de modelo, branch, PR e gate preservam contexto sem multiplicar HITL.
