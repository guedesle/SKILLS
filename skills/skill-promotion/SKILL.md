---
name: skill-promotion
description: "Promova uma capacidade reutilizável de um projeto para o catálogo canônico guedesle/SKILLS. Use após auditoria de portabilidade para extrair a parte transversal, registrar origem, versionar e atualizar catálogo sem copiar dependências locais."
---

# skill-promotion

Converter capacidades locais comprovadamente reutilizáveis em skills gerais governadas.

## Workflow

1. Exija classificação de portabilidade diferente de `PROJECT_ONLY` ou produza-a com `skill-portability-audit`.
2. Extraia invariantes transversais e preserve no projeto somente variante/adaptador quando necessário.
3. Use `skill-authoring` para criar/refatorar a definição geral.
4. Registre `origin`, SemVer, path e mirrors no `registry.json`.
5. Atualize README e `general-skills-status.md` de forma vinculada à mesma versão.
6. Execute `skill-validator` e `skill-evaluator` antes do gate de repositório.

## Stop e escalation

- `PROJECT_ONLY` sem extração transversal segura.
- Promoção exige ampliar autorização operacional ou remover guardrail local obrigatório.
- Conflito de nome/contrato com skill canônica existente exige decisão material.

## Saída esperada

- skill central;
- origin/proveniência;
- versão;
- variante local preservada;
- resultado dos gates.
