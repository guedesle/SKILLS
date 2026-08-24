---
name: skill-portability-audit
description: "Audite uma skill de projeto antes de promovê-la a uso geral. Use para detectar paths, IDs, schemas, URLs e políticas locais e classificar PROJECT_ONLY, GENERALIZABLE, GENERAL_WITH_ADAPTER ou GLOBAL_READY."
---

# skill-portability-audit

Evitar que dependências específicas de um projeto contaminem o catálogo geral.

## Workflow

1. Leia `SKILL.md` e recursos relevantes da candidata.
2. Detecte paths absolutos, endpoints locais, IDs, nomes de projeto, schemas e autorização específica.
3. Separe comportamento transversal de adaptação local.
4. Classifique a candidata em `PROJECT_ONLY`, `GENERALIZABLE`, `GENERAL_WITH_ADAPTER` ou `GLOBAL_READY` e liste blockers/sinais.
5. Para `GENERALIZABLE` ou `GENERAL_WITH_ADAPTER`, descreva o que deve ser extraído e o que deve permanecer local.
6. Entregue `GLOBAL_READY` ou plano de generalização para `skill-promotion`.

## Stop e escalation

- Dependência local é essencial ao valor da skill e não há contrato transversal coerente.
- Remover regra local alteraria obrigação de segurança/autorização.

## Saída esperada

- classification;
- blockers;
- signals;
- plano de extração/adaptador.
