---
name: skill-development-lifecycle
description: "Orquestre de ponta a ponta criação, refatoração, validação, avaliação, generalização, promoção e distribuição de skills. Use quando o pedido envolve o ciclo completo de desenvolvimento de uma skill ou a transformação de skill de projeto em global."
---

# skill-development-lifecycle

Executar o lifecycle de skills com baixo HITL e gates especializados, sem concentrar todas as responsabilidades numa mega-skill.

## Workflow

1. Classifique o pedido: nova skill geral, atualização, skill local candidata ou distribuição.
2. Delegue construção para `skill-authoring` e rode `skill-validator` antes de qualquer promoção.
3. Use `skill-evaluator` para triggers/invariantes e `skill-portability-audit` para candidatas locais.
4. Use `skill-promotion` somente quando o contrato transversal estiver definido.
5. Use `skill-distribution` apenas depois dos gates de catálogo e portabilidade.
6. Componha `low-hitl-orchestration`, `batch-quality-gate`, `decision-escalation-control` e `github-branch-pr-lifecycle` para o gate de repositório.
7. FAIL determinístico implica corrigir em lote e revalidar; HITL só em decisão material, autorização, risco ou contrato incompatível.

## Estado low-HITL

```text
AUTO_CONTINUE -> validar -> FAIL determinístico -> corrigir em lote -> revalidar -> PASS -> gate de repositório
                         \-> HUMAN_REVIEW_REQUIRED somente por decisão material/autorização/risco
```

## Stop e escalation

- Decisão material de arquitetura/escopo não aprovada.
- Ação irreversível ou autorização externa não concedida.
- Validação repetidamente falha por causa não determinística.

## Saída esperada

- skills/versões afetadas;
- gates e evals;
- classificação de portabilidade;
- PR/merge/distribuição.
