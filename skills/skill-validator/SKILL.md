---
name: skill-validator
description: "Valide deterministicamente uma skill ou o catálogo de skills: YAML, nomes, paths, SemVer, registry, documentação, recursos, evals e empacotamento. Use para gates estruturais; não substitui avaliação semântica ou decisão de promoção."
---

# skill-validator

Transformar invariantes estruturais de skills em checks reproduzíveis e fail-closed.

## Workflow

1. Execute primeiro os testes unitários dos validadores.
2. Valide frontmatter com parser YAML real e associe versão documental à mesma skill.
3. Valide registry, paths canônicos, mirrors, recursos locais e presença de evals declarados.
4. Execute `validate_skill_evals.py` e `package_chatgpt_skills.py --check` quando aplicável.
5. Consolide erros determinísticos, corrija em lote e revalide.
6. Encaminhe julgamento de gatilho/comportamento não determinístico para `skill-evaluator`.

## Stop e escalation

- O gate exige julgamento semântico não representável deterministicamente.
- Uma correção mudaria intenção, escopo ou contrato aprovado.

## Saída esperada

- PASS/FAIL;
- erros por arquivo/invariante;
- checks executados;
- próximo gate.
