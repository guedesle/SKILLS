---
name: skill-distribution
description: "Distribua uma skill canônica já validada para ChatGPT, Codex ou repositórios consumidores. Use para bundles individuais, instalação pessoal, mirrors e plugins skills-only; não confunda pacote gerado com instalação efetivamente observada."
---

# skill-distribution

Levar skills validadas aos hosts sem criar fontes de verdade divergentes.

## Workflow

1. Confirme que a skill está registrada, validada e `GLOBAL_READY` ou possui adaptador explícito.
2. Para bundle individual do ChatGPT, gere ZIP determinístico com `SKILL.md` na raiz.
3. Para Codex USER, use `$HOME/.agents/skills/<nome>` por diretório ou symlink conforme o host.
4. Para consumidores, aplique somente mirrors declarados no registry, preferindo pull.
5. Para distribuição reutilizável em ChatGPT/Codex, construa plugin skills-only a partir do catálogo canônico; nunca mantenha uma segunda cópia editável como fonte de verdade.
6. Gere marketplace local derivado quando a superfície suportar teste local.
7. Reporte separadamente `DISTRIBUTION_READY`, `INSTALLED`, `VERIFIED` e `PUBLISHED`; não promova um estado sem evidência correspondente.

## Plugin skills-only

O pacote mínimo possui:

```text
<plugin>/
  .codex-plugin/
    plugin.json
  skills/
    <skill>/
      SKILL.md
      ...
```

Regras:

- `.codex-plugin/plugin.json` é o entry point do plugin;
- `skills` no manifest aponta para `./skills/`;
- paths do manifest permanecem relativos e dentro da raiz do plugin;
- não inclua MCP quando o plugin precisar somente de workflows/instruções;
- para marketplace local, gere `.agents/plugins/marketplace.json` apontando para a pasta materializada do plugin;
- local marketplace é artefato de teste/distribuição privada, não publicação universal;
- publicação universal exige submissão e revisão próprias da superfície.

No catálogo central, use:

```bash
python scripts/package_plugins.py --check
python scripts/package_plugins.py
```

O build copia as versões canônicas para `dist/` apenas como artefato derivado. Mudanças de comportamento continuam nascendo em `skills/<nome>/`.

## Estados de distribuição

- `DISTRIBUTION_READY` — pacote e manifest foram gerados e validados;
- `INSTALLED` — instalação foi observada no host;
- `VERIFIED` — ao menos um caso representativo confirmou descoberta/uso após instalação;
- `PUBLISHED` — publicação universal/workspace foi efetivamente confirmada.

Nunca trate `DISTRIBUTION_READY` como sinônimo de qualquer estado posterior.

## Stop e escalation

- Host não permite confirmar instalação solicitada.
- Destino exigiria credencial/permissão não autorizada.
- Skill não passou gate canônico.
- Publicação exige identidade, política, URLs legais ou aprovação ainda ausentes.

## Saída esperada

- artefatos por host;
- plugin/marketplace gerado quando aplicável;
- estado de distribuição observado;
- mirrors afetados;
- limitações verificáveis.
