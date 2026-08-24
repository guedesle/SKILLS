# Estado das skills gerais

Atualizado em 24 de agosto de 2026.

## Fonte canônica

`guedesle/SKILLS` é a fonte de verdade das skills gerais/reutilizáveis. O inventário machine-readable vive em [`registry.json`](registry.json), o catálogo navegável em [`README.md`](README.md), a política transversal em [`AGENTS.md`](AGENTS.md) e as composições de plugin em [`plugin-catalog.json`](plugin-catalog.json).

Skills de projeto não são promovidas automaticamente: passam por auditoria de portabilidade, extração da parte transversal, validação, evals e registro central.

## Catálogo atual

| Skill | Categoria | Versão | Estado |
|---|---|---:|---|
| `plan-content` | Editorial | 1.0.0 | Canônica |
| `architect-text` | Editorial | 1.2.0 | Canônica |
| `design-paragraphs` | Editorial | 1.2.0 | Canônica |
| `write-with-evidence` | Editorial | 1.0.0 | Canônica |
| `write-technical-content` | Editorial/Técnica | 1.0.0 | Canônica + mirror |
| `calibrate-rhetoric` | Editorial | 1.0.0 | Canônica |
| `review-editorial-quality` | QA | 1.0.0 | Canônica + mirror |
| `improve-accessible-writing` | Acessibilidade | 1.0.0 | Canônica |
| `assess-editorial-alignment` | Governança editorial | 1.0.0 | Canônica |
| `writing-workflow` | Orquestração editorial | 1.0.0 | Canônica + meta-skill + evals |
| `prompt-generator` | Prompt engineering | 1.0.0 | Canônica + evals |
| `graphify` | Engenharia de software | 1.0.0 | Canônica |
| `github-project-repo-sync` | GitHub automation | 1.0.0 | Canônica |
| `github-project-drift-audit` | GitHub/QA | 1.0.0 | Canônica |
| `skills-central-governance` | Gestão de skills | 1.3.0 | Canônica + policy/delegação |
| `skill-development-lifecycle` | Gestão de skills | 1.0.0 | Canônica + meta-skill |
| `skill-authoring` | Gestão de skills | 1.0.0 | Canônica + evals |
| `skill-validator` | Gestão de skills | 1.0.0 | Canônica + evals |
| `skill-evaluator` | Gestão de skills | 1.0.0 | Canônica + evals |
| `skill-portability-audit` | Gestão de skills | 1.0.0 | Canônica + evals |
| `skill-promotion` | Gestão de skills | 1.0.0 | Canônica + evals |
| `skill-distribution` | Gestão de skills | 1.1.0 | Canônica + evals + plugin skills-only |
| `chatgpt-governed-workflow` | Workflow | 1.0.0 | Canônica + meta-skill |
| `low-hitl-orchestration` | Orquestração | 1.0.0 | Canônica |
| `batch-quality-gate` | QA automation | 1.0.0 | Canônica |
| `context-handoff` | Context engineering | 1.0.0 | Canônica |
| `github-branch-pr-lifecycle` | GitHub automation | 1.0.0 | Canônica |
| `adaptive-model-routing` | Model routing | 1.1.1 | Canônica + adaptador Codex |
| `decision-escalation-control` | Governança de workflow | 1.0.0 | Canônica |
| `contract-governed-execution` | Governança de execução | 1.0.0 | Canônica |
| `knowledge-source-governance` | Governança de conhecimento | 1.0.0 | Canônica |

**Total: 31 skills canônicas.**

## Fábrica governada de skills

Em 24/08/2026 foi materializado o lifecycle:

```text
chatgpt-governed-workflow
        │
        └─ skill-development-lifecycle
             ├─ skill-authoring
             ├─ skill-validator
             ├─ skill-evaluator
             ├─ skill-portability-audit
             ├─ skill-promotion
             └─ skill-distribution
```

A governança central (`skills-central-governance` 1.3.0) mantém policy e fonte de verdade; a meta-skill `skill-development-lifecycle` executa o ciclo especializado.

## Workflow editorial

`writing-workflow` 1.0.0 é o entry point do plugin Writing. O roteamento é proporcional: uma tarefa pontual vai diretamente para a skill especializada; tarefas multi-etapas podem compor planejamento, arquitetura, parágrafos, evidência, redação técnica, retórica, acessibilidade, QA e alinhamento editorial.

O contrato principal não exige filesystem, CLI nem modelo específico. Isso o torna candidato direto a uso em plugin skills-only no ChatGPT Work web, além do marketplace local.

## Gates implementados

O catálogo diferencia:

- **estrutura** — YAML real, kebab-case, SemVer, paths e registry;
- **integridade** — versão da mesma skill em registry/README/status e recursos canônicos;
- **evals** — schema declarativo de trigger positivo, trigger negativo e comportamento;
- **portabilidade** — `PROJECT_ONLY`, `GENERALIZABLE`, `GENERAL_WITH_ADAPTER`, `GLOBAL_READY`;
- **distribuição** — bundle, plugin, manifest, mirrors e estados `DISTRIBUTION_READY`, `INSTALLED`, `VERIFIED`, `PUBLISHED`;
- **repositório** — testes, CI, diff, review, mergeability e verificação pós-merge.

O gate canônico é:

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/sync_skills.py --check
python scripts/validate_skill_evals.py
python scripts/package_chatgpt_skills.py --check
python scripts/package_plugins.py --check
python -m py_compile scripts/*.py
```

O parser manual de frontmatter foi substituído por YAML real. A validação documental exige que a versão pertença à mesma skill.

## Low-HITL

```text
AUTO_CONTINUE
  ↓
validar
  ↓
FAIL determinístico → corrigir em lote → revalidar
  ↓ PASS
gate final
```

Falhas mecânicas/determinísticas não geram HITL. Escalonar somente decisão material, mudança de escopo/contrato, autorização, risco ou ação irreversível.

## Promoção project → global

1. auditar portabilidade;
2. separar comportamento transversal de dependência local;
3. manter adaptador no projeto quando necessário;
4. criar/refatorar a skill geral;
5. registrar `origin` e SemVer;
6. executar validação + evals;
7. merge no catálogo central;
8. distribuir a partir da fonte canônica.

Capacidades previamente promovidas continuam registrando suas origens: `editor-agent`, `SieDOE`, PFC IBMEC e `cyber-skills-framework`.

## Distribuição

- **Codex USER**: `$HOME/.agents/skills/<nome>` apontando para a fonte canônica.
- **ChatGPT Personal Skill**: ZIP determinístico por skill quando a superfície permitir upload.
- **Marketplace local skills-only**: `guedesle-skills-local`, gerado em `dist/plugins/marketplace`.
- **Plugins locais**:
  - `guedesle-governed-workflow` 1.0.0 — 17 skills;
  - `guedesle-skill-creator` 1.0.0 — 12 skills;
  - `guedesle-writing` 1.0.0 — 10 skills.
- **Consumers**: mirrors declarados em `registry.json`, preferindo pull.

Preparar bundle/plugin equivale apenas a `DISTRIBUTION_READY`. O catálogo não declara `INSTALLED`, `VERIFIED` ou `PUBLISHED` sem evidência da superfície de destino.

### Política de publicação e Work web

A distribuição corrente permanece `local-only` e `universal_publication: false`.

O alvo futuro registrado é `chatgpt-work-workspace-private`: compartilhar os plugins dentro de um workspace compatível, sem publicação no diretório universal.

Estado de portabilidade estrutural:

| Plugin | Local | Work web estrutural | Observação |
|---|---|---|---|
| `guedesle-governed-workflow` | READY | GENERAL_WITH_ADAPTER | Operações de repositório dependem das capabilities/apps disponíveis no host |
| `guedesle-skill-creator` | READY | GENERAL_WITH_ADAPTER | Authoring/evals são portáveis; empacotamento e writes dependem das capabilities do host |
| `guedesle-writing` | READY | WORK_WEB_PORTABLE | Função editorial principal é skills-only e host-agnostic |

Nenhum desses estados equivale a instalação real no ChatGPT Work. A validação de runtime web será uma etapa posterior em workspace compatível.

## Roteamento Codex

O contrato funcional das skills permanece agnóstico de modelo. O adaptador transversal mantém:

```text
leaf / bounded        → gpt-5.6-luna  + reasoning high
orchestration/handoff → gpt-5.6-terra + reasoning medium
high complexity       → gpt-5.6-sol   + reasoning high
```

A política concreta vive em `AGENTS.md` e `adaptive-model-routing`, evitando duplicação por skill.

## Mirrors ativos

Consumidor homologado: `guedesle/download-edicoes-doe`, branch `main`.

- `write-technical-content` → `.agents/skills/write-technical-content`;
- `review-editorial-quality` → `.agents/skills/review-editorial-quality`.

Demais skills canônicas podem ser consumidas globalmente por hosts que apontem para o catálogo central; mirrors específicos só são criados quando declarados.

## Próximas métricas de maturidade

- instalar e executar os três plugins no marketplace local e registrar evals observados;
- validar `guedesle-writing` no ChatGPT Work web quando o workspace permitir import/share de plugin privado;
- criar adapters de capability para Governed Workflow e Skill Creator até ambos atingirem `WORK_WEB_PORTABLE`;
- medir colisão de gatilhos, regressões e taxa de sucesso;
- medir HITLs evitados versus reversões materiais;
- ampliar fixtures negativas sem transformar validação determinística em julgamento LLM implícito.
