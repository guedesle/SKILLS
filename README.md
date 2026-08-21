# SKILLS — catálogo central

Repositório canônico das **skills gerais e reutilizáveis**. A fonte de verdade é `guedesle/SKILLS`; skills específicas de projeto podem permanecer locais, mas capacidades reutilizáveis devem ser promovidas para este catálogo.

## Navegação

- [Índice](#índice-de-skills)
- [Skills de workflow e baixo HITL](#skills-de-workflow-e-baixo-hitl)
- [Como usar](#como-usar)
- [Instalação em OpenCode, Codex e Claude Code](#instalação-em-opencode-codex-e-claude-code)
- [Sincronização](#sincronização)
- [Mirrors genéricos](#mirrors-genéricos)
- [Homologação](#homologação)
- [Versionamento](#versionamento)
- [Histórico](#histórico)

## Índice de skills

| Skill | Versão | Categoria | Função |
|---|---:|---|---|
| [`plan-content`](#plan-content) | **1.0.0** | Editorial | Briefing, tese, escopo, outline e riscos |
| [`architect-text`](#architect-text) | **1.2.0** | Editorial | Finalidade → seções → plano de parágrafos → arquitetura |
| [`design-paragraphs`](#design-paragraphs) | **1.2.0** | Editorial | 18 funções, contratos de refatoração e exemplos estruturais |
| [`write-with-evidence`](#write-with-evidence) | **1.0.0** | Editorial | Evidência, inferência, causalidade e incerteza |
| [`write-technical-content`](#write-technical-content) | **1.0.0** | Técnica | Requisitos, procedimentos e documentação |
| [`calibrate-rhetoric`](#calibrate-rhetoric) | **1.0.0** | Editorial | Tom e força argumentativa |
| [`review-editorial-quality`](#review-editorial-quality) | **1.0.0** | QA | Achados, bloqueios e prontidão |
| [`improve-accessible-writing`](#improve-accessible-writing) | **1.0.0** | Acessibilidade | Clareza e leitura em tela |
| [`assess-editorial-alignment`](#assess-editorial-alignment) | **1.0.0** | Governança | Aderência a princípios editoriais |
| [`graphify`](#graphify) | **1.0.0** | Engenharia | Navegação de código orientada por grafo |
| [`github-project-repo-sync`](#github-project-repo-sync) | **1.0.0** | GitHub | Reconciliação Project v2 ↔ repositório |
| [`github-project-drift-audit`](#github-project-drift-audit) | **1.0.0** | GitHub/QA | Auditoria desired/observed/live |
| [`skills-central-governance`](#skills-central-governance) | **1.0.0** | Governança | Ciclo de vida do catálogo |
| [`low-hitl-orchestration`](#low-hitl-orchestration) | **1.0.0** | Workflow | Lotes autônomos + um gate humano final |
| [`batch-quality-gate`](#batch-quality-gate) | **1.0.0** | QA automation | Fast/batch/CI, autotestes e relatório consolidado |
| [`context-handoff`](#context-handoff) | **1.0.0** | Context engineering | Transferência de estado sem reiniciar descoberta |
| [`github-branch-pr-lifecycle`](#github-branch-pr-lifecycle) | **1.0.0** | GitHub | Branches, stacked PRs, divergência e merges seguros |
| [`adaptive-model-routing`](#adaptive-model-routing) | **1.0.0** | Model routing | Execução, contexto e frontier reasoning por papel |
| [`decision-escalation-control`](#decision-escalation-control) | **1.0.0** | Governança | AUTO_CONTINUE, review e bloqueios por materialidade |
| [`contract-governed-execution`](#contract-governed-execution) | **1.0.0** | Governança | Contratos machine-readable, fail-closed e ledger |
| [`knowledge-source-governance`](#knowledge-source-governance) | **1.0.0** | Conhecimento | Proveniência, freshness, corroboration e evidence ceilings |

### `plan-content`
Transforma objetivo e contexto em briefing operacional, escopo, outline, evidências necessárias, riscos e critérios. [SKILL.md](skills/plan-content/SKILL.md) · [↑ Índice](#índice-de-skills)

### `architect-text`
Converte a **finalidade do texto** em arquitetura funcional de leitura, com seções, funções de parágrafo, dependências, evidências, transições e instruções para a próxima etapa. [SKILL.md](skills/architect-text/SKILL.md) · [↑ Índice](#índice-de-skills)

### `design-paragraphs`
Projeta e refatora parágrafos com 18 funções estruturais e corpus de exemplos clássicos usado apenas para abstração estrutural. [SKILL.md](skills/design-paragraphs/SKILL.md) · [↑ Índice](#índice-de-skills)

### `write-with-evidence`
Distingue fatos, inferências, estimativas e opiniões e controla causalidade, extrapolação e incerteza. [SKILL.md](skills/write-with-evidence/SKILL.md) · [↑ Índice](#índice-de-skills)

### `write-technical-content`
Estrutura especificações, requisitos, procedimentos, critérios de aceite e rastreabilidade. Mirror homologado em `guedesle/download-edicoes-doe/.agents/skills/write-technical-content`. [SKILL.md](skills/write-technical-content/SKILL.md) · [↑ Índice](#índice-de-skills)

### `calibrate-rhetoric`
Ajusta tom, autoridade, persuasão e força argumentativa à evidência disponível. [SKILL.md](skills/calibrate-rhetoric/SKILL.md) · [↑ Índice](#índice-de-skills)

### `review-editorial-quality`
Executa QA editorial por severidade e declara prontidão somente após critérios críticos. [SKILL.md](skills/review-editorial-quality/SKILL.md) · [↑ Índice](#índice-de-skills)

### `improve-accessible-writing`
Melhora clareza, escaneabilidade e linguagem simples preservando precisão. [SKILL.md](skills/improve-accessible-writing/SKILL.md) · [↑ Índice](#índice-de-skills)

### `assess-editorial-alignment`
Compara conteúdo com princípios editoriais explicitamente fornecidos. [SKILL.md](skills/assess-editorial-alignment/SKILL.md) · [↑ Índice](#índice-de-skills)

### `graphify`
Usa grafo para reduzir o espaço de busca em código e confirma detalhes diretamente nos arquivos antes de editar. [SKILL.md](skills/graphify/SKILL.md) · [↑ Índice](#índice-de-skills)

### `github-project-repo-sync`
Reconcilia GitHub Project v2 com intenção versionada no repositório, preservando itens não gerenciados. [SKILL.md](skills/github-project-repo-sync/SKILL.md) · [↑ Índice](#índice-de-skills)

### `github-project-drift-audit`
Audita sem mutação desired, observed e live e classifica `IN_SYNC`, `DRIFT`, `STALE` ou `UNVERIFIED`. [SKILL.md](skills/github-project-drift-audit/SKILL.md) · [↑ Índice](#índice-de-skills)

### `skills-central-governance`
Governa criação, promoção, versão, documentação e distribuição de skills gerais. [SKILL.md](skills/skills-central-governance/SKILL.md) · [↑ Índice](#índice-de-skills)

## Skills de workflow e baixo HITL

As oito skills abaixo foram generalizadas em 21/08/2026 a partir de estratégias desenvolvidas e homologadas no `guedesle/cyber-skills-framework`. Elas removem dependências exclusivas do domínio de cibersegurança e preservam padrões transversais de execução, QA, handoff, GitHub, roteamento de modelos, contratos, conhecimento e escalonamento.

### `low-hitl-orchestration`
Executa lotes coerentes com o princípio **falha determinística não gera HITL**: `FAIL → corrigir em lote → revalidar → um gate humano final`. [SKILL.md](skills/low-hitl-orchestration/SKILL.md) · [↑ Índice](#índice-de-skills)

### `batch-quality-gate`
Consolida estrutura, contratos, autotestes, sintaxe, secrets, testes e escopo em um gate com modos `fast`, `batch` e `CI`; recomenda o mesmo motor local/remoto. [SKILL.md](skills/batch-quality-gate/SKILL.md) · [↑ Índice](#índice-de-skills)

### `context-handoff`
Entrega estado compacto entre agentes/modelos/sessões: decisões, evidências, débitos, gates, próxima ação e itens que não devem ser perguntados novamente. [SKILL.md](skills/context-handoff/SKILL.md) · [↑ Índice](#índice-de-skills)

### `github-branch-pr-lifecycle`
Gerencia feature branches, stacked PRs, retarget, preservação de ancestralidade, backup antes de alinhamento destrutivo e verificação pós-merge. [SKILL.md](skills/github-branch-pr-lifecycle/SKILL.md) · [↑ Índice](#índice-de-skills)

### `adaptive-model-routing`
Separa `bounded execution`, `context handoff` e `frontier reasoning`; modelos são adaptadores temporários, não dependências das skills. Evidência inesperada pode escalar o papel sem ampliar autorização. [SKILL.md](skills/adaptive-model-routing/SKILL.md) · [↑ Índice](#índice-de-skills)

### `decision-escalation-control`
Classifica eventos em `AUTO_CONTINUE`, `HUMAN_REVIEW_RECOMMENDED`, `HUMAN_REVIEW_REQUIRED` e `BLOCKED_UNTIL_REVIEW`. `elevated review` aumenta profundidade, não número de approvals. [SKILL.md](skills/decision-escalation-control/SKILL.md) · [↑ Índice](#índice-de-skills)

### `contract-governed-execution`
Governa ações de maior risco por contratos estruturados, autorização explícita, limites, stop conditions, fail-closed e ledger de evidências. [SKILL.md](skills/contract-governed-execution/SKILL.md) · [↑ Índice](#índice-de-skills)

### `knowledge-source-governance`
Governa fontes por proveniência, autoridade, freshness, aplicabilidade, corroboration e teto de conclusão, evitando que evidência fraca promova sozinha uma conclusão material. [SKILL.md](skills/knowledge-source-governance/SKILL.md) · [↑ Índice](#índice-de-skills)

## Como usar

Cada definição canônica vive em `skills/<nome>/SKILL.md`; o inventário e os mirrors vivem em [`registry.json`](registry.json).

```text
Use $plan-content para planejar este relatório.
Use $architect-text para transformar a finalidade deste texto em arquitetura.
Use $low-hitl-orchestration para conduzir esta implementação em lotes com mínimo HITL.
Use $batch-quality-gate para consolidar todos os checks antes da revisão final.
Use $context-handoff para preparar a continuação em outro agente ou conversa.
Use $github-branch-pr-lifecycle para organizar esta mudança em stacked PRs.
Use $adaptive-model-routing para distribuir execução, contexto e raciocínio por papel.
Use $decision-escalation-control para decidir se devemos continuar ou pedir aprovação.
Use $contract-governed-execution para executar ações de maior risco sob contrato fail-closed.
Use $knowledge-source-governance para controlar proveniência, freshness e teto de conclusão das fontes.
```

## Instalação em OpenCode, Codex e Claude Code

As skills usam o formato **Agent Skills**: cada capacidade vive em diretório próprio com `SKILL.md` como ponto de entrada e pode incluir `scripts/`, `references/`, `assets/` e outros recursos.

> **Recomendação:** clone este repositório uma vez e faça cada host apontar para `SKILLS/skills`. Assim, `git pull` atualiza a fonte canônica sem criar cópias divergentes.

### 1. Pré-requisitos

Instale Git e pelo menos um host.

#### OpenCode

```bash
npm install -g opencode-ai
opencode --version
```

#### Codex

```bash
npm install -g @openai/codex
codex
```

#### Claude Code

Windows:

```powershell
winget install Anthropic.ClaudeCode
```

ou:

```powershell
irm https://claude.ai/install.ps1 | iex
```

macOS/Linux/WSL:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### 2. Clone a fonte canônica

Windows / PowerShell:

```powershell
cd $HOME
git clone https://github.com/guedesle/SKILLS.git
cd $HOME\SKILLS
python .\scripts\sync_skills.py --check
```

macOS/Linux/WSL:

```bash
cd "$HOME"
git clone https://github.com/guedesle/SKILLS.git
cd "$HOME/SKILLS"
python scripts/sync_skills.py --check
```

Se já existir:

```bash
git -C "$HOME/SKILLS" pull --ff-only
```

### 3. Instalação global no OpenCode

Diretório:

```text
~/.config/opencode/skills/<nome>/SKILL.md
```

Windows / PowerShell:

```powershell
$Repo = Join-Path $HOME "SKILLS"
$Target = Join-Path $HOME ".config\opencode\skills"
New-Item -ItemType Directory -Force -Path $Target | Out-Null

Get-ChildItem (Join-Path $Repo "skills") -Directory | ForEach-Object {
    $Link = Join-Path $Target $_.Name
    if (-not (Test-Path $Link)) {
        New-Item -ItemType Junction -Path $Link -Target $_.FullName | Out-Null
    }
}
```

macOS/Linux/WSL:

```bash
mkdir -p "$HOME/.config/opencode/skills"
for skill in "$HOME/SKILLS"/skills/*; do
  [ -d "$skill" ] || continue
  ln -sfn "$skill" "$HOME/.config/opencode/skills/$(basename "$skill")"
done
```

### 4. Instalação global no Codex

Diretório:

```text
$HOME/.agents/skills/<nome>/SKILL.md
```

Windows / PowerShell:

```powershell
$Repo = Join-Path $HOME "SKILLS"
$Target = Join-Path $HOME ".agents\skills"
New-Item -ItemType Directory -Force -Path $Target | Out-Null

Get-ChildItem (Join-Path $Repo "skills") -Directory | ForEach-Object {
    $Link = Join-Path $Target $_.Name
    if (-not (Test-Path $Link)) {
        New-Item -ItemType Junction -Path $Link -Target $_.FullName | Out-Null
    }
}
```

macOS/Linux/WSL:

```bash
mkdir -p "$HOME/.agents/skills"
for skill in "$HOME/SKILLS"/skills/*; do
  [ -d "$skill" ] || continue
  ln -sfn "$skill" "$HOME/.agents/skills/$(basename "$skill")"
done
```

No Codex, use `/skills` ou invoque diretamente:

```text
$low-hitl-orchestration conduza esta rodada com um único gate humano final.
```

### 5. Instalação global no Claude Code

Diretório:

```text
~/.claude/skills/<nome>/SKILL.md
```

Windows / PowerShell:

```powershell
$Repo = Join-Path $HOME "SKILLS"
$Target = Join-Path $HOME ".claude\skills"
New-Item -ItemType Directory -Force -Path $Target | Out-Null

Get-ChildItem (Join-Path $Repo "skills") -Directory | ForEach-Object {
    $Link = Join-Path $Target $_.Name
    if (-not (Test-Path $Link)) {
        New-Item -ItemType Junction -Path $Link -Target $_.FullName | Out-Null
    }
}
```

macOS/Linux/WSL:

```bash
mkdir -p "$HOME/.claude/skills"
for skill in "$HOME/SKILLS"/skills/*; do
  [ -d "$skill" ] || continue
  ln -sfn "$skill" "$HOME/.claude/skills/$(basename "$skill")"
done
```

### 6. Instalação local em um projeto

| Host | Diretório recomendado |
|---|---|
| OpenCode | `.opencode/skills/<nome>/SKILL.md` |
| Codex | `.agents/skills/<nome>/SKILL.md` |
| Claude Code | `.claude/skills/<nome>/SKILL.md` |

Para repositórios que participam do mecanismo central de mirrors, prefira `registry.json` + workflow de sincronização em vez de cópias manuais.

### 7. Atualização

Windows / PowerShell:

```powershell
git -C "$HOME\SKILLS" pull --ff-only
python "$HOME\SKILLS\scripts\sync_skills.py" --check
```

macOS/Linux/WSL:

```bash
git -C "$HOME/SKILLS" pull --ff-only
python "$HOME/SKILLS/scripts/sync_skills.py" --check
```

### 8. Diagnóstico rápido

Se uma skill não aparecer:

1. confirme `SKILL.md`;
2. confirme frontmatter `name` e `description`;
3. confirme nome do diretório;
4. confira junction/symlink;
5. reinicie o host se o diretório foi criado depois da sessão;
6. no Codex use `/skills`; no Claude Code invoque `/<nome>`.

### 9. Referências oficiais

- [OpenCode — Agent Skills](https://opencode.ai/docs/skills)
- [OpenAI — Build skills para ChatGPT e Codex](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI — Codex](https://openai.com/codex/)
- [Claude Code — Extend Claude with skills](https://code.claude.com/docs/en/skills)

## Sincronização

Fluxo padrão:

```text
skill canônica → registry.json → validação → workflow genérico do consumidor
→ sync_consumer.py → paths registrados → commit somente se houver diferença
```

Validação central:

```bash
python scripts/sync_skills.py --check
```

O modo `pull` é preferido. `mode: push` permanece como fallback explícito.

## Mirrors genéricos

O [`registry.json`](registry.json) usa `schema_version: 2`. A lógica de sincronização é genérica por consumidor:

- [`.github/workflows/mirror-consumer.yml`](.github/workflows/mirror-consumer.yml);
- [`scripts/sync_consumer.py`](scripts/sync_consumer.py);
- [`templates/sync-central-skills.yml`](templates/sync-central-skills.yml);
- [`scripts/bootstrap_consumers.py`](scripts/bootstrap_consumers.py).

Depois do bootstrap de um consumidor, adicionar outra skill ao mesmo repositório exige apenas um novo mapping no `registry.json`.

## Homologação

`guedesle/download-edicoes-doe` é o consumidor de homologação. O caller genérico recebe:

- `write-technical-content`;
- `review-editorial-quality`.

As oito novas skills de workflow/governança são canônicas e ainda não possuem mirror de projeto específico; hosts globais que apontam para `SKILLS/skills` passam a descobri-las após atualização do clone.

Consulte também [`AGENTS.md`](AGENTS.md), [`general-skills-status.md`](general-skills-status.md) e [`skills-central-governance`](skills/skills-central-governance/SKILL.md).

## Versionamento

O catálogo usa SemVer: **PATCH** para correções compatíveis, **MINOR** para nova capacidade compatível e **MAJOR** para mudança incompatível de contrato. A versão deve constar no README e no `registry.json`.

## Histórico

### 2026-08-21 — workflow geral e baixo HITL
- promovidas oito skills gerais a partir de estratégias do `cyber-skills-framework`;
- formalizado `FAIL → corrigir em lote → revalidar → um gate humano final`;
- adicionados estados de escalation e revisão elevada sem approvals adicionais;
- generalizados batch gate, autotestes de validadores e paridade local/CI;
- generalizados handoffs entre agentes/modelos e continuidade sem repetir decisões;
- generalizados stacked PRs, retarget, preservação de ancestralidade e recuperação segura de divergência;
- generalizado roteamento por papéis `bounded execution`, `context handoff` e `frontier reasoning`;
- generalizados contratos machine-readable fail-closed com ledger de execução;
- generalizada governança de fontes por proveniência, freshness, corroboration e evidence ceilings;
- corrigido índice para `architect-text` e `design-paragraphs` 1.2.0.

### 2026-08-16 — instalação multi-host e mirrors pull genéricos
- documentada instalação global e por projeto em OpenCode, Codex e Claude Code;
- adotado clone canônico + junctions/symlinks;
- `registry.json` migrado para schema v2;
- criado workflow reutilizável central, `sync_consumer.py` e bootstrap genérico;
- homologados mirrors de `write-technical-content` e `review-editorial-quality`.

### 2026-08-14 — baseline `1.0.0`
- materializadas 13 skills canônicas;
- criado `registry.json`, sincronizador, workflow de validação e catálogo navegável.

[↑ Voltar ao topo](#skills--catálogo-central)