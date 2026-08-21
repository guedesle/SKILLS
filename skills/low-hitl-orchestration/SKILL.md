---
name: low-hitl-orchestration
description: Orquestre trabalhos longos com mínimo Human-in-the-Loop. Use quando houver múltiplas etapas, validações, correções determinísticas, handoffs e um gate humano final. Agrupe falhas corrigíveis, evite aprovações intermediárias desnecessárias e interrompa apenas para decisões materiais, irreversíveis ou não inferíveis com segurança.
---

# Low-HITL Orchestration

Use esta skill para conduzir trabalhos multi-etapas com alta autonomia sem enfraquecer gates humanos realmente necessários.

## Princípio

**Falha determinística não gera HITL.**

Se um erro puder ser corrigido sem mudar intenção, escopo, risco, autorização ou decisão de negócio, acumule os bloqueios, corrija-os em lote e revalide antes de chamar o usuário.

## Estados de execução

- `AUTO_CONTINUE` — prossiga sem intervenção humana;
- `HUMAN_REVIEW_RECOMMENDED` — prossiga tecnicamente e registre o ponto para a revisão final;
- `HUMAN_REVIEW_REQUIRED` — pare antes de ação que depende de julgamento, autorização, escopo ou irreversibilidade;
- `BLOCKED_UNTIL_REVIEW` — não há caminho seguro ou válido sem informação/decisão humana.

## Fluxo padrão

1. decompor o objetivo em um lote coerente;
2. identificar dependências, riscos e gates;
3. executar etapas determinísticas sem pedir confirmação intermediária;
4. usar validações rápidas opcionais durante o trabalho;
5. executar um gate consolidado ao fechar o lote;
6. corrigir todas as falhas determinísticas em conjunto;
7. repetir o gate até `PASS` ou até surgir uma decisão realmente humana;
8. solicitar **um único HITL final** para revisão, aceite, merge ou publicação quando necessário.

## Não solicitar HITL para

- erro sintático ou estrutural;
- metadata ou registro inconsistente;
- divergência determinística de arquivos/estado;
- teste/autoteste falhando por causa identificável;
- relatório incompleto que possa ser regenerado;
- branch/base/remoto resolvível sem ambiguidade;
- correção segura que preserve o contrato e o escopo aprovados;
- reexecução de validação após correção determinística.

## Solicitar HITL quando

- houver mudança material de objetivo, escopo ou prioridade;
- alternativas arquiteturais não equivalentes exigirem escolha;
- ação for destrutiva, irreversível ou em produção;
- autorização, credencial, responsabilidade ou decisão legal/organizacional dependerem do usuário;
- evidência nova alterar substancialmente risco, custo, impacto ou compromisso assumido;
- informação indispensável não puder ser inferida com segurança.

## Revisão elevada

`elevated review` aumenta a profundidade do único gate final; **não cria uma sequência de approvals**.

Use revisão elevada quando o lote altera fronteiras de segurança, autorização, dados sensíveis, infraestrutura, políticas, modelos de capacidade, contratos de execução ou outros componentes de alto impacto.

## Lotes

Prefira lotes funcionalmente coerentes. Evite micro-HITLs por arquivo, commit ou subetapa.

Um lote deve ser pequeno o suficiente para ser revisável e grande o suficiente para produzir valor completo.

## Handoff

Ao transferir o trabalho para outra etapa ou agente, forneça estado observado, decisões já tomadas, evidências, débitos, próximos gates e o que **não deve ser perguntado novamente**.

## Saída esperada

Informe:

- objetivo do lote;
- estado atual;
- gates executados;
- falhas corrigidas automaticamente;
- decisões humanas ainda necessárias;
- próximo checkpoint;
- nível de revisão final: normal ou elevated.

## Origem

Generalizada do workflow de desenvolvimento do `guedesle/cyber-skills-framework`, especialmente do padrão `FAIL → corrigir em lote → revalidar → um único gate humano final`.
