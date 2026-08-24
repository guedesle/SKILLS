---
name: chatgpt-governed-workflow
description: "Aplique a governança operacional low-HITL do catálogo a trabalhos complexos de repositório e skills. Use como entry point quando for preciso decompor, executar, validar, corrigir e concluir um workflow; delegue desenvolvimento de skills para skill-development-lifecycle."
---

# chatgpt-governed-workflow

Selecionar e compor o workflow governado adequado sem exigir invocação manual de cada skill de processo.

## Workflow

1. Entenda intenção, restrições, autorização e critério de conclusão.
2. Se o objeto principal for uma skill, delegue para `skill-development-lifecycle`.
3. Caso contrário, decomponha em lote coerente e componha `low-hitl-orchestration`, `batch-quality-gate` e `decision-escalation-control`.
4. Para GitHub, use `github-branch-pr-lifecycle`; para mudança de executor use `context-handoff`.
5. Corrija falhas determinísticas em lote, revalide e não peça aprovação intermediária sem materialidade.
6. Use `contract-governed-execution` quando risco/autorização exigir fail-closed.
7. Conclua com estado verificável e escale somente o menor conjunto de decisões materiais.

## Estado low-HITL

```text
AUTO_CONTINUE -> validar -> FAIL determinístico -> corrigir em lote -> revalidar -> PASS -> gate de repositório
                         \-> HUMAN_REVIEW_REQUIRED somente por decisão material/autorização/risco
```

## Stop e escalation

- Falta autorização necessária.
- Há decisão material não inferível com segurança.
- Stop condition de contrato foi atingida.

## Saída esperada

- estado final;
- gates executados;
- ações automáticas;
- HITL evitado/necessário;
- handoff quando aplicável.
