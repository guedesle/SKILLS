---
name: skills-central-governance
description: "Governe o catálogo central guedesle/SKILLS como fonte canônica de skills gerais. Use para política de criação, promoção, versionamento, registro, documentação e distribuição; delegue a execução ponta a ponta para skill-development-lifecycle e preserve low-HITL por padrão."
---

# Central Skills Governance

`guedesle/SKILLS` é a fonte canônica das skills gerais e reutilizáveis. Esta skill governa **política e estado do catálogo**; não reimplementa authoring, evals, portabilidade ou distribuição.

## Regra principal

Toda skill geral deve:

1. existir em `skills/<nome>/SKILL.md`;
2. possuir versão SemVer em `registry.json`;
3. possuir entrada vinculada à mesma versão no README e em `general-skills-status.md`;
4. registrar origem/proveniência e mirrors quando aplicável;
5. receber primeiro aqui qualquer mudança de comportamento geral;
6. passar o gate canônico antes de merge/distribuição.

## Delegação do lifecycle

Quando o trabalho envolver criação, refatoração, promoção ou distribuição de uma skill, componha `skill-development-lifecycle`, que delega para:

- `skill-authoring` — contrato e pacote Agent Skills;
- `skill-validator` — checks determinísticos;
- `skill-evaluator` — should-trigger, should-not-trigger e invariantes;
- `skill-portability-audit` — classificação project/global;
- `skill-promotion` — extração e registro da parte transversal;
- `skill-distribution` — ChatGPT, Codex e consumidores.

Para trabalhos complexos que não sejam primariamente lifecycle de skill, `chatgpt-governed-workflow` é o entry point geral da governança operacional.

## Low-HITL

Componha `low-hitl-orchestration`, `batch-quality-gate` e `decision-escalation-control`:

```text
lote coerente -> validar -> FAIL determinístico -> corrigir em lote -> revalidar -> PASS -> gate final
```

Não solicite HITL para lint, YAML, SemVer, drift documental, eval schema, testes, empacotamento, conflitos mecânicos ou reexecução de gate quando a correção não altera intenção, escopo, risco, autorização ou contrato.

`elevated review` aumenta profundidade do mesmo gate; não multiplica approvals.

## Gate canônico

Para mudança no catálogo, execute conforme aplicável:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/sync_skills.py --check
python scripts/validate_skill_evals.py
python scripts/package_chatgpt_skills.py --check
python -m py_compile scripts/*.py
```

Falha em qualquer check determinístico impede merge até correção e revalidação.

## Geral versus específica

Use `skill-portability-audit` antes de promover uma skill local relevante:

- `PROJECT_ONLY` — permanece no projeto;
- `GENERALIZABLE` — extrair contrato transversal;
- `GENERAL_WITH_ADAPTER` — promover núcleo geral e manter adaptador local;
- `GLOBAL_READY` — pode seguir para registro/gates centrais.

Nunca copie literalmente para o catálogo paths absolutos, IDs, endpoints internos, schemas ou regras institucionais que só façam sentido no projeto de origem.

## Versionamento

- PATCH: correção/esclarecimento sem mudança de contrato;
- MINOR: nova capacidade compatível;
- MAJOR: mudança incompatível de gatilho, contrato ou saída.

Alteração geral nasce na cópia canônica; mirror não é fonte de verdade.

## Distribuição

`skill-distribution` deve separar estados:

- `DISTRIBUTION_READY` — artefato/configuração preparado;
- `INSTALLED` — instalação observada no host;
- `VERIFIED` — host confirmou descoberta/uso.

Bundle gerado não é prova de instalação. Para Codex USER, a referência geral é `$HOME/.agents/skills/<nome>`; para ChatGPT, use bundle individual quando a superfície permitir; consumers seguem mirrors declarados no registry.

O roteamento de modelos permanece definido transversalmente por `AGENTS.md` e `adaptive-model-routing`; esta skill não duplica a tabela concreta.

## Merge e publicação

Antes do merge:

- diff restrito ao lote;
- branch reconciliada com a base;
- registry, README, status e arquivos canônicos concordam;
- testes, eval schema, package check e CI passam;
- PR está mergeável;
- não há bloqueador material não resolvido.

Depois do merge, verifique `main`, CI e estados de distribuição solicitados.

## Saída esperada

Informe skills/versões afetadas, origem, arquivos centrais, gates, evals, portabilidade, mirrors/distribuição, PR/merge e HITL solicitado ou evitado.
