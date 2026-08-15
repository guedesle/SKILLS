# SKILLS — catálogo central

Repositório canônico das **skills gerais e reutilizáveis** do perfil. Novas skills gerais devem ser criadas, versionadas e documentadas aqui; cópias em outros repositórios são tratadas como espelhos ou adaptações locais.

> **Fonte de verdade:** `guedesle/SKILLS`. Skills estritamente específicas de um projeto podem permanecer locais, mas a capacidade reutilizável deve ser promovida para este catálogo.

## Navegação

- [Índice de skills](#índice-de-skills)
- [Como usar](#como-usar)
- [Centralização e sincronização](#centralização-e-sincronização)
- [Versionamento](#versionamento)
- [Histórico do catálogo](#histórico-do-catálogo)

## Índice de skills

| Skill | Versão | Categoria | Função |
|---|---:|---|---|
| [`plan-content`](#plan-content) | **1.0.0** | Editorial | Briefing, tese, escopo, outline, riscos e critérios |
| [`architect-text`](#architect-text) | **1.0.0** | Editorial | Arquitetura textual, contratos de seção e matriz paragrafal |
| [`design-paragraphs`](#design-paragraphs) | **1.0.0** | Editorial | Função, progressão, transição, ritmo e densidade de parágrafos |
| [`write-with-evidence`](#write-with-evidence) | **1.0.0** | Editorial | Fatos, fontes, inferências, causalidade, incerteza e evidência |
| [`write-technical-content`](#write-technical-content) | **1.0.0** | Editorial/Técnica | Especificações, requisitos, procedimentos e documentação |
| [`calibrate-rhetoric`](#calibrate-rhetoric) | **1.0.0** | Editorial | Tom, força argumentativa, persuasão e proporcionalidade |
| [`review-editorial-quality`](#review-editorial-quality) | **1.0.0** | QA | Achados, bloqueios, correções e prontidão |
| [`improve-accessible-writing`](#improve-accessible-writing) | **1.0.0** | Acessibilidade | Clareza, leitura em tela e linguagem simples |
| [`assess-editorial-alignment`](#assess-editorial-alignment) | **1.0.0** | Governança editorial | Aderência a princípios editoriais configuráveis |
| [`graphify`](#graphify) | **1.0.0** | Engenharia de software | Navegação arquitetural de código orientada por grafo |
| [`github-project-repo-sync`](#github-project-repo-sync) | **1.0.0** | GitHub | Reconciliação declarativa Project v2 ↔ repositório |
| [`github-project-drift-audit`](#github-project-drift-audit) | **1.0.0** | GitHub/QA | Auditoria sem mutação de desired, observed e live |
| [`skills-central-governance`](#skills-central-governance) | **1.0.0** | Governança | Criação, promoção, versão e distribuição de skills gerais |

---

### `plan-content`

**v1.0.0 · canônica** — Transforma objetivo e contexto em briefing operacional: público, tese/pergunta central, escopo, fora de escopo, outline, evidências necessárias, riscos e critérios de qualidade.

`Use $plan-content para planejar uma apresentação executiva sobre este projeto.`

[📄 SKILL.md](skills/plan-content/SKILL.md) · [↑ Índice](#índice-de-skills)

### `architect-text`

**v1.0.0 · canônica** — Organiza briefing, tópicos ou rascunho em mapa de seções, contratos de seção, matriz paragrafal, progressão temática, diagnóstico de fluxo e handoff.

**Origem:** generalização do domínio de Arquitetura Textual do `editor-agent`, incluindo a skill local `editor-structure`.

`Use $architect-text para transformar este briefing em arquitetura de relatório.`

[📄 SKILL.md](skills/architect-text/SKILL.md) · [↑ Índice](#índice-de-skills)

### `design-paragraphs`

**v1.0.0 · canônica** — Projeta e revisa a operação dominante dos parágrafos, progressão, transições, fusão/divisão, ritmo e densidade sem sacrificar precisão.

`Use $design-paragraphs para revisar a progressão deste capítulo.`

[📄 SKILL.md](skills/design-paragraphs/SKILL.md) · [↑ Índice](#índice-de-skills)

### `write-with-evidence`

**v1.0.0 · canônica** — Distingue fatos, inferências, estimativas e opiniões; relaciona afirmações a evidências; controla causalidade, extrapolação, incerteza e força retórica.

`Use $write-with-evidence para separar fatos, inferências e lacunas de fonte.`

[📄 SKILL.md](skills/write-with-evidence/SKILL.md) · [↑ Índice](#índice-de-skills)

### `write-technical-content`

**v1.0.0 · canônica** — Estrutura especificações, requisitos, procedimentos, guias e documentação com linguagem verificável, critérios de aceite, exceções e rastreabilidade.

`Use $write-technical-content para converter estas decisões em requisitos testáveis.`

[📄 SKILL.md](skills/write-technical-content/SKILL.md) · [↑ Índice](#índice-de-skills)

### `calibrate-rhetoric`

**v1.0.0 · canônica** — Ajusta tom, autoridade, persuasão, modalização, cadência e força argumentativa para que a linguagem não ultrapasse a evidência.

`Use $calibrate-rhetoric para deixar o texto firme sem soar agressivo.`

[📄 SKILL.md](skills/calibrate-rhetoric/SKILL.md) · [↑ Índice](#índice-de-skills)

### `review-editorial-quality`

**v1.0.0 · canônica** — Executa QA editorial por severidade, separa bloqueios de melhorias, identifica contradições/lacunas e declara prontidão somente após critérios críticos.

`Use $review-editorial-quality para revisar este rascunho antes da entrega.`

[📄 SKILL.md](skills/review-editorial-quality/SKILL.md) · [↑ Índice](#índice-de-skills)

### `improve-accessible-writing`

**v1.0.0 · canônica** — Melhora clareza, escaneabilidade e linguagem simples preservando precisão técnica, jurídica, científica ou institucional.

`Use $improve-accessible-writing para simplificar este texto sem perder precisão.`

[📄 SKILL.md](skills/improve-accessible-writing/SKILL.md) · [↑ Índice](#índice-de-skills)

### `assess-editorial-alignment`

**v1.0.0 · canônica** — Compara conteúdo com princípios editoriais explicitamente fornecidos, separando não conformidade real de preferência estilística e indicando conflitos que exigem decisão humana.

`Use $assess-editorial-alignment usando estes princípios editoriais.`

[📄 SKILL.md](skills/assess-editorial-alignment/SKILL.md) · [↑ Índice](#índice-de-skills)

### `graphify`

**v1.0.0 · canônica** — Usa um grafo Graphify para reduzir o espaço de busca em código, descobrir relações e dependências e orientar leitura direta dos arquivos. O grafo auxilia a navegação, mas não substitui confirmação no código.

**Origem:** generalização da skill `graphify` usada no `SieDOE`.

`Use $graphify para localizar o fluxo entre ingestão, planejamento e persistência.`

[📄 SKILL.md](skills/graphify/SKILL.md) · [↑ Índice](#índice-de-skills)

### `github-project-repo-sync`

**v1.0.0 · canônica** — Reconcilia um GitHub Project v2 com a intenção versionada no repositório. Separa fonte declarativa, reconciliador e estado observado, preservando itens não gerenciados por padrão.

**Origem:** promovida a partir da implementação criada no `guedesle/projeto-pos-ibmec`.

`Use $github-project-repo-sync para reconciliar este Project com o manifesto versionado.`

[📄 SKILL.md](skills/github-project-repo-sync/SKILL.md) · [↑ Índice](#índice-de-skills)

### `github-project-drift-audit`

**v1.0.0 · canônica** — Audita sem mutação a diferença entre estado desejado, última observação e estado live, classificando o resultado como `IN_SYNC`, `DRIFT`, `STALE` ou `UNVERIFIED`.

**Origem:** promovida a partir da implementação criada no `guedesle/projeto-pos-ibmec`.

`Use $github-project-drift-audit para verificar se este Project está sincronizado sem alterar nada.`

[📄 SKILL.md](skills/github-project-drift-audit/SKILL.md) · [↑ Índice](#índice-de-skills)

### `skills-central-governance`

**v1.0.0 · canônica** — Governa o ciclo de vida do catálogo: decidir se a skill é geral, criar no repositório central, registrar versão, atualizar README, declarar espelhos e distribuir alterações.

`Use $skills-central-governance para promover esta nova skill ao catálogo geral.`

[📄 SKILL.md](skills/skills-central-governance/SKILL.md) · [↑ Índice](#índice-de-skills)

---

## Como usar

Cada definição canônica vive em `skills/<nome>/SKILL.md`. O inventário versionado está em [`registry.json`](registry.json).

```text
Use $plan-content para planejar este relatório.
Use $graphify para entender as dependências deste módulo.
Use $github-project-drift-audit para auditar o Project sem mutações.
```

## Centralização e sincronização

Fluxo oficial:

```text
criar/alterar skill geral
        ↓
guedesle/SKILLS / skills/<nome>
        ↓
registry.json + README.md
        ↓
validação
        ↓
espelhos explicitamente registrados
```

Regras:

1. **Central primeiro.** Mudança de comportamento geral nasce neste repositório.
2. **Sem sobrescrever adaptações locais.** Só são atualizados targets presentes em `mirrors` no [`registry.json`](registry.json).
3. **Skills específicas continuam locais.** Quando uma parte for reutilizável, ela deve ser extraída para uma skill geral central.
4. **Nada fora do path gerenciado é apagado.**
5. **Documentação e versão são parte da entrega.** Uma skill nova não está completa sem índice, descrição e versão.

Validação:

```bash
python scripts/sync_skills.py --check
```

Distribuição para os espelhos registrados:

```bash
python scripts/sync_skills.py --apply
```

A automação está em [`.github/workflows/sync-skills.yml`](.github/workflows/sync-skills.yml). Para permitir pushes automáticos entre repositórios, configure o secret `SKILLS_SYNC_TOKEN` com acesso apenas aos repositórios necessários e a variável `SKILLS_AUTO_SYNC=true`. Sem essa configuração, o workflow permanece em modo de validação.

Consulte também [`AGENTS.md`](AGENTS.md), [`general-skills-status.md`](general-skills-status.md) e [`skills-central-governance`](skills/skills-central-governance/SKILL.md).

## Versionamento

O catálogo usa **SemVer**:

- **PATCH** — correções ou esclarecimentos sem alterar o contrato;
- **MINOR** — nova capacidade compatível;
- **MAJOR** — mudança incompatível em gatilhos, procedimento, contrato ou saída.

A versão aparece obrigatoriamente neste README e no [`registry.json`](registry.json).

## Histórico do catálogo

### 2026-08-14 — baseline central `1.0.0`

- materializadas as nove skills editoriais gerais já declaradas no perfil;
- promovida uma versão geral de `graphify` a partir do uso no `SieDOE`;
- promovidas versões gerais de `github-project-repo-sync` e `github-project-drift-audit` a partir do PFC IBMEC;
- criada `skills-central-governance`;
- criado `registry.json` como inventário canônico e versionado;
- criado sincronizador central → espelhos e workflow de validação/sincronização;
- README convertido em catálogo navegável com links internos, links para cada `SKILL.md` e versões explícitas.

[↑ Voltar ao topo](#skills--catálogo-central)
