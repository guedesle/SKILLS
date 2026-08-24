---
name: skill-distribution
description: "Distribua uma skill canônica já validada para ChatGPT, Codex ou repositórios consumidores. Use para empacotamento, instalação pessoal, mirrors e plugin skill-only; não confunda pacote gerado com instalação efetivamente observada."
---

# skill-distribution

Levar skills validadas aos hosts sem criar fontes de verdade divergentes.

## Workflow

1. Confirme que a skill está registrada, validada e `GLOBAL_READY` ou possui adaptador explícito.
2. Para ChatGPT, gere bundle individual determinístico com `SKILL.md` na raiz.
3. Para Codex USER, use `$HOME/.agents/skills/<nome>` por diretório ou symlink conforme o host.
4. Para consumidores, aplique somente mirrors declarados no registry, preferindo pull.
5. Para distribuição reutilizável, prepare plugin skill-only quando essa superfície for adotada.
6. Reporte separadamente `DISTRIBUTION_READY`, `INSTALLED` e `VERIFIED`; não promova um estado sem observação.

## Stop e escalation

- Host não permite confirmar instalação solicitada.
- Destino exigiria credencial/permissão não autorizada.
- Skill não passou gate canônico.

## Saída esperada

- artefatos por host;
- estado de distribuição;
- mirrors afetados;
- limitações verificáveis.
