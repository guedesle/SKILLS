# SKILLS — catálogo central

Repositório canônico de **skills gerais e reutilizáveis**. A fonte de verdade é `guedesle/SKILLS`; skills específicas de projeto permanecem locais até que sua parte transversal seja auditada e promovida.

## Índice de skills

| Skill | Versão | Categoria | Função |
|---|---:|---|---|
| [`plan-content`](skills/plan-content/SKILL.md) | **1.0.0** | Editorial | Briefing, tese, escopo, outline e riscos |
| [`architect-text`](skills/architect-text/SKILL.md) | **1.2.0** | Editorial | Finalidade → seções → plano de parágrafos → arquitetura |
| [`design-paragraphs`](skills/design-paragraphs/SKILL.md) | **1.2.0** | Editorial | 18 funções, contratos de refatoração e exemplos estruturais |
| [`write-with-evidence`](skills/write-with-evidence/SKILL.md) | **1.0.0** | Editorial | Evidência, inferência, causalidade e incerteza |
| [`write-technical-content`](skills/write-technical-content/SKILL.md) | **1.0.0** | Técnica | Requisitos, procedimentos e documentação |
| [`calibrate-rhetoric`](skills/calibrate-rhetoric/SKILL.md) | **1.0.0** | Editorial | Tom e força argumentativa |
| [`review-editorial-quality`](skills/review-editorial-quality/SKILL.md) | **1.0.0** | QA | Achados, bloqueios e prontidão |
| [`improve-accessible-writing`](skills/improve-accessible-writing/SKILL.md) | **1.0.0** | Acessibilidade | Clareza e leitura em tela |
| [`assess-editorial-alignment`](skills/assess-editorial-alignment/SKILL.md) | **1.0.0** | Governança | Aderência a princípios editoriais |
| [`writing-workflow`](skills/writing-workflow/SKILL.md) | **1.0.0** | Orquestração editorial | Entry point proporcional para planejamento → redação → QA |
| [`prompt-generator`](skills/prompt-generator/SKILL.md) | **1.0.0** | Prompt engineering | Prompts testáveis, padrões e evals |
| [`graphify`](skills/graphify/SKILL.md) | **1.0.0** | Engenharia | Navegação de código orientada por grafo |
| [`github-project-repo-sync`](skills/github-project-repo-sync/SKILL.md) | **1.0.0** | GitHub | Reconciliação Project v2 ↔ repositório |
| [`github-project-drift-audit`](skills/github-project-drift-audit/SKILL.md) | **1.0.0** | GitHub/QA | Auditoria desired/observed/live |
| [`skills-central-governance`](skills/skills-central-governance/SKILL.md) | **1.3.0** | Gestão de skills | Política e estado do catálogo canônico |
| [`skill-development-lifecycle`](skills/skill-development-lifecycle/SKILL.md) | **1.0.0** | Gestão de skills | Lifecycle ponta a ponta de skills |
| [`skill-authoring`](skills/skill-authoring/SKILL.md) | **1.0.0** | Gestão de skills | Construção/refatoração do pacote Agent Skills |
| [`skill-validator`](skills/skill-validator/SKILL.md) | **1.0.0** | Gestão de skills | YAML, registry, docs, recursos e gates determinísticos |
| [`skill-evaluator`](skills/skill-evaluator/SKILL.md) | **1.0.0** | Gestão de skills | Should-trigger, should-not-trigger e behavior evals |
| [`skill-portability-audit`](skills/skill-portability-audit/SKILL.md) | **1.0.0** | Gestão de skills | PROJECT_ONLY → GLOBAL_READY |
| [`skill-promotion`](skills/skill-promotion/SKILL.md) | **1.0.0** | Gestão de skills | Promoção project → catálogo geral |
| [`skill-distribution`](skills/skill-distribution/SKILL.md) | **1.1.0** | Gestão de skills | ChatGPT, Codex, mirrors e plugins skills-only |
| [`chatgpt-governed-workflow`](skills/chatgpt-governed-workflow/SKILL.md) | **1.0.0** | Workflow | Entry point low-HITL para trabalho complexo |
| [`low-hitl-orchestration`](skills/low-hitl-orchestration/SKILL.md) | **1.0.0** | Workflow | Lotes autônomos + gate humano por materialidade |
| [`batch-quality-gate`](skills/batch-quality-gate/SKILL.md) | **1.0.0** | QA automation | Fast/batch/CI e relatório consolidado |
| [`context-handoff`](skills/context-handoff/SKILL.md) | **1.0.0** | Context engineering | Continuidade entre agentes/modelos/sessões |
| [`github-branch-pr-lifecycle`](skills/github-branch-pr-lifecycle/SKILL.md) | **1.0.0** | GitHub | Branches, PRs, divergência e merges seguros |
| [`adaptive-model-routing`](skills/adaptive-model-routing/SKILL.md) | **1.1.1** | Model routing | Roteamento por papel no Codex |
| [`decision-escalation-control`](skills/decision-escalation-control/SKILL.md) | **1.0.0** | Governança | AUTO_CONTINUE e revisão por materialidade |
| [`contract-governed-execution`](skills/contract-governed-execution/SKILL.md) | **1.0.0** | Governança | Contratos fail-closed e ledger |
| [`knowledge-source-governance`](skills/knowledge-source-governance/SKILL.md) | **1.0.0** | Conhecimento | Proveniência, freshness e evidence ceilings |

## Fábrica governada de skills

A partir de **24/08/2026**, o catálogo possui um lifecycle explícito para construir e promover skills:

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

### `skill-development-lifecycle`

Orquestra nova skill, atualização, candidata de projeto ou distribuição. Compõe as seis capacidades especializadas e os gates low-HITL sem duplicar seus contratos.

### `skill-authoring`

Transforma comportamento desejado em `SKILL.md` + recursos auxiliares. Exige fronteira clara de responsabilidade e evals para novas skills deste lifecycle.

### `skill-validator`

Executa checks determinísticos de YAML real, nome/path, SemVer, registro, documentação vinculada à mesma skill, eval schema, recursos e bundles.

### `skill-evaluator`

Mantém casos `trigger_positive`, `trigger_negative` e `behavior`. Schema validado não é tratado como prova de acurácia do modelo; execução LLM só é declarada quando realmente observada no host.

### `skill-portability-audit`

Classifica candidatas:

- `PROJECT_ONLY` — permanece local;
- `GENERALIZABLE` — exige extração da parte transversal;
- `GENERAL_WITH_ADAPTER` — núcleo geral + adaptador local;
- `GLOBAL_READY` — apta a seguir para promoção/gates.

### `skill-promotion`

Promove somente a parte reutilizável, registra `origin`, SemVer e mirrors e preserva adaptações locais quando necessárias.

### `skill-distribution`

Separa `DISTRIBUTION_READY`, `INSTALLED`, `VERIFIED` e `PUBLISHED`. A versão 1.1.0 adiciona empacotamento de **plugins skills-only** a partir da fonte canônica, sem criar uma segunda cópia editável das skills.

### `chatgpt-governed-workflow`

Entry point geral para trabalhos complexos. Quando o objeto principal é uma skill, delega ao `skill-development-lifecycle`; nos demais casos compõe as skills transversais de low-HITL, QA, GitHub e handoff.

## Workflow editorial

`writing-workflow` é o entry point editorial. Ele escolhe somente as etapas necessárias entre `plan-content`, `architect-text`, `design-paragraphs`, `write-with-evidence`, `write-technical-content`, `calibrate-rhetoric`, `improve-accessible-writing`, `review-editorial-quality` e `assess-editorial-alignment`.

O contrato é host-agnostic: a função editorial principal não exige filesystem, CLI ou modelo específico. Isso permite testar localmente agora e manter portabilidade estrutural para um plugin privado no ChatGPT Work web depois.

## Low-HITL por padrão

```text
lote coerente
  ↓
validação
  ↓
FAIL determinístico → corrigir em lote → revalidar
  ↓ PASS
gate final somente por materialidade
```

Falhas de YAML, SemVer, lint, testes, documentação, eval schema, package check, conflitos mecânicos ou reexecução de gate não exigem aprovação humana quando a correção não altera intenção, escopo, risco, autorização ou contrato.

## Validação local

Pré-requisito Python:

```bash
python -m pip install -r requirements-dev.txt
```

Gate canônico:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/sync_skills.py --check
python scripts/validate_skill_evals.py
python scripts/package_chatgpt_skills.py --check
python scripts/package_plugins.py --check
python -m py_compile scripts/*.py
```

`sync_skills.py` usa parser YAML real e vincula a versão do `registry.json` à linha da **mesma skill** no README e em `general-skills-status.md`.

Skills que declaram `evals/` devem conter no mínimo:

```text
evals/
  trigger-positive.yaml
  trigger-negative.yaml
  behavior.yaml
```

## Como usar

Exemplos:

```text
Use $chatgpt-governed-workflow para conduzir este desenvolvimento até o merge com low-HITL.
Use $skill-development-lifecycle para criar, validar, promover e distribuir esta skill.
Use $writing-workflow para transformar estas notas e fontes em um texto estruturado e revisado.
Use $skill-portability-audit para decidir se esta skill local pode virar global.
Use $skill-validator para rodar o gate determinístico do catálogo.
Use $skill-evaluator para criar should-trigger e should-not-trigger.
Use $skill-distribution para gerar bundles e um plugin skills-only a partir das skills canônicas.
```

## Instalação global

Clone a fonte canônica:

```bash
git clone https://github.com/guedesle/SKILLS.git "$HOME/SKILLS"
cd "$HOME/SKILLS"
python -m pip install -r requirements-dev.txt
python scripts/sync_skills.py --check
```

### Codex

Diretório USER recomendado:

```text
$HOME/.agents/skills/<nome>/SKILL.md
```

macOS/Linux/WSL:

```bash
mkdir -p "$HOME/.agents/skills"
for skill in "$HOME/SKILLS"/skills/*; do
  [ -d "$skill" ] || continue
  ln -sfn "$skill" "$HOME/.agents/skills/$(basename "$skill")"
done
```

Windows / PowerShell:

```powershell
$Repo = Join-Path $HOME "SKILLS\skills"
$Target = Join-Path $HOME ".agents\skills"
New-Item -ItemType Directory -Force -Path $Target | Out-Null
Get-ChildItem $Repo -Directory | ForEach-Object {
  $Link = Join-Path $Target $_.Name
  if (-not (Test-Path $Link)) {
    New-Item -ItemType Junction -Path $Link -Target $_.FullName | Out-Null
  }
}
```

No Codex, o roteamento por papel é herdado de `AGENTS.md` + `adaptive-model-routing`. O contrato funcional das skills não depende do nome do modelo.

### OpenCode

Diretório global:

```text
~/.config/opencode/skills/<nome>/SKILL.md
```

Aponte cada diretório para a pasta canônica em `$HOME/SKILLS/skills` por symlink/junction.

### Claude Code

Diretório global:

```text
~/.claude/skills/<nome>/SKILL.md
```

Aponte cada diretório para a pasta canônica em `$HOME/SKILLS/skills` por symlink/junction.

### ChatGPT

Consulte [`CHATGPT.md`](CHATGPT.md). O repositório oferece duas rotas derivadas da mesma fonte canônica:

1. ZIP individual por skill, quando a superfície de Personal Skills permitir upload;
2. plugin **skills-only** para o Plugins Directory/marketplace quando essa superfície estiver disponível ao plano/host.

Não existe suposição de sincronização automática GitHub → ChatGPT.

## Empacotamento ChatGPT por skill

```bash
python scripts/package_chatgpt_skills.py --check
python scripts/package_chatgpt_skills.py
```

Saída:

```text
dist/chatgpt/
  manifest.json
  <skill>-v<semver>.zip
```

Cada ZIP mantém `SKILL.md` na raiz e inclui os recursos auxiliares da mesma pasta canônica.

## Plugins skills-only para ChatGPT e Codex

O catálogo de plugins vive em [`plugin-catalog.json`](plugin-catalog.json). A distribuição atual é **local-only** e possui três composições derivadas da mesma fonte canônica:

- `guedesle-governed-workflow` — governança low-HITL e workflow complexo;
- `guedesle-skill-creator` — fábrica e lifecycle de skills;
- `guedesle-writing` — planejamento, arquitetura, redação e QA editorial.

Valide e gere:

```bash
python scripts/package_plugins.py --check
python scripts/package_plugins.py
```

Saída:

```text
dist/plugins/
  manifest.json
  guedesle-governed-workflow-v1.0.0.zip
  guedesle-skill-creator-v1.0.0.zip
  guedesle-writing-v1.0.0.zip
  marketplace/
    .agents/plugins/marketplace.json
    plugins/
      guedesle-governed-workflow/
      guedesle-skill-creator/
      guedesle-writing/
```

Cada plugin contém seu próprio `.codex-plugin/plugin.json`; `dist/` é artefato derivado e as skills continuam sendo editadas somente em `skills/<nome>/`.

A meta futura é permitir uso privado dos mesmos plugins no **ChatGPT Work web** via compartilhamento/diretório do workspace, sem publicação no diretório universal. Essa meta é registrada como portabilidade futura; não equivale a plugin já instalado ou validado no Work.

## Sincronização e mirrors

O inventário vive em [`registry.json`](registry.json). Mirrors `pull` são preferidos e usam:

- `.github/workflows/mirror-consumer.yml`;
- `scripts/sync_consumer.py`;
- `templates/sync-central-skills.yml`;
- `scripts/bootstrap_consumers.py`.

Fluxo:

```text
skill canônica → registry.json → validação → consumer workflow → path registrado
```

`mode: push` é fallback explícito quando escrita cross-repository for realmente necessária.

## Versionamento

- **PATCH** — correção/esclarecimento compatível;
- **MINOR** — nova capacidade compatível;
- **MAJOR** — mudança incompatível de gatilho, contrato ou saída.

A mudança geral nasce no catálogo central, nunca no mirror.

## Histórico

- **24/08/2026** — adicionado `writing-workflow` 1.0.0 e plugin local `guedesle-writing` 1.0.0, mantendo portabilidade estrutural para compartilhamento privado futuro no ChatGPT Work web.
- **24/08/2026** — adicionado `guedesle-skill-creator` 1.0.0 ao marketplace local e governança explícita de skills compartilhadas entre plugins.
- **24/08/2026** — `skill-distribution` 1.1.0 e primeiro plugin skills-only `guedesle-governed-workflow`, gerado a partir do catálogo canônico com marketplace local derivado.
- **24/08/2026** — `adaptive-model-routing` 1.1.1 após correção de frontmatter YAML legado.
- **24/08/2026** — criada a fábrica governada: `chatgpt-governed-workflow`, `skill-development-lifecycle`, authoring, validator, evaluator, portability, promotion e distribution; `skills-central-governance` 1.3.0; parser YAML real, eval schema e auditoria de portabilidade.
- **24/08/2026** — adicionado empacotamento determinístico para ChatGPT por skill.
- **23/08/2026** — adicionada `prompt-generator` 1.0.0.
- **21/08/2026** — promovidas oito capacidades transversais de low-HITL/governança e definido roteamento Codex por papel.
- **16/08/2026** — `architect-text` e `design-paragraphs` 1.2.0 e documentação de instalação multi-host.
