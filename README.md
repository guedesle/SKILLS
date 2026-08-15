# SKILLS — catálogo central

Repositório canônico das **skills gerais e reutilizáveis** do perfil. A partir deste catálogo, novas skills gerais devem ser criadas, versionadas, documentadas e, quando necessário, clonadas para repositórios consumidores.

> **Fonte de verdade:** `guedesle/SKILLS`. Variantes estritamente específicas de um projeto podem permanecer locais, mas a capacidade geral deve ser promovida e mantida aqui.

## Navegação

- [Índice de skills](#índice-de-skills)
- [Como usar](#como-usar)
- [Política de centralização e sincronização](#política-de-centralização-e-sincronização)
- [Versionamento](#versionamento)
- [Histórico do catálogo](#histórico-do-catálogo)

## Índice de skills

| Skill | Versão | Categoria | O que faz |
|---|---:|---|---|
| [`plan-content`](#plan-content) | **1.0.0** | Editorial | Planejamento de briefing, tese, escopo, outline, riscos e critérios |
| [`architect-text`](#architect-text) | **1.0.0** | Editorial | Arquitetura textual, contratos de seção e matriz paragrafal |
| [`design-paragraphs`](#design-paragraphs) | **1.0.0** | Editorial | Função, progressão, transição, ritmo e densidade de parágrafos |
| [`write-with-evidence`](#write-with-evidence) | **1.0.0** | Editorial | Fatos, fontes, inferências, causalidade, incerteza e evidência |
| [`write-technical-content`](#write-technical-content) | **1.0.0** | Editorial/Técnica | Especificações, requisitos, procedimentos e documentação |
| [`calibrate-rhetoric`](#calibrate-rhetoric) | **1.0.0** | Editorial | Tom, força argumentativa, persuasão e proporcionalidade |
| [`review-editorial-quality`](#review-editorial-quality) | **1.0.0** | QA | Revisão editorial, achados, bloqueios e prontidão |
| [`improve-accessible-writing`](#improve-accessible-writing) | **1.0.0** | Acessibilidade | Clareza, leitura em tela e linguagem simples |
| [`assess-editorial-alignment`](#assess-editorial-alignment) | **1.0.0** | Governança editorial | Aderência a princípios editoriais configuráveis |
| [`graphify`](#graphify) | **1.0.0** | Engenharia de software | Navegação arquitetural de código orientada por grafo |
| [`github-project-repo-sync`](#github-project-repo-sync) | **1.0.0** | GitHub | Reconciliação declarativa Project v2 ↔ repositório |
| [`github-project-drift-audit`](#github-project-drift-audit) | **1.0.0** | GitHub/QA | Auditoria sem mutação de desired, observed e live |
| [`skills-central-governance`](#skills-central-governance) | **1.0.0** | Governança | Criação, promoção, versão e distribuição de skills gerais |

---

### `plan-content`

**Versão:** `1.0.0` · **Status:** canônica

Transforma objetivo e contexto em briefing operacional: público, tese/pergunta central, escopo, fora de escopo, outline, evidências necessárias, riscos e critérios de qualidade.

**Use quando:** a tarefa ainda precisa de direção antes da redação.

**Exemplo:** `Use $plan-content para planejar uma apresentação executiva sobre este projeto.`

[📄 Abrir SKILL.md](skills/plan-content/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

### `architect-text`

**Versão:** `1.0.0` · **Status:** canônica

Organiza briefing, tópicos ou rascunho em mapa de seções, contratos de seção, matriz paragrafal, progressão temática, diagnóstico de fluxo e handoff.

**Origem:** generalização do domínio de Arquitetura Textual do `editor-agent`, incluindo a skill local `editor-structure`.

**Exemplo:** `Use $architect-text para transformar este briefing em arquitetura de relatório.`

[📄 Abrir SKILL.md](skills/architect-text/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

### `design-paragraphs`

**Versão:** `1.0.0` · **Status:** canônica

Projeta e revisa a operação dominante dos parágrafos, progressão, transições, fusão/divisão, ritmo e densidade sem sacrificar precisão.

**Exemplo:** `Use $design-paragraphs para revisar a progressão deste capítulo.`

[📄 Abrir SKILL.md](skills/design-paragraphs/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

### `write-with-evidence`

**Versão:** `1.0.0` · **Status:** canônica

Distingue fatos, inferências, estimativas e opiniões; relaciona afirmações a evidências; controla causalidade, extrapolação, incerteza e força retórica.

**Exemplo:** `Use $write-with-evidence para separar fatos, inferências e lacunas de fonte.`

[📄 Abrir SKILL.md](skills/write-with-evidence/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

### `write-technical-content`

**Versão:** `1.0.0` · **Status:** canônica

Estrutura especificações, requisitos, procedimentos, guias e documentação com linguagem verificável, critérios de aceite, exceções e rastreabilidade.

**Exemplo:** `Use $write-technical-content para converter estas decisões em requisitos testáveis.`

[📄 Abrir SKILL.md](skills/write-technical-content/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

### `calibrate-rhetoric`

**Versão:** `1.0.0` · **Status:** canônica

Ajusta tom, autoridade, persuasão, modalização, cadência e força argumentativa para que a linguagem não ultrapasse a evidência.

**Exemplo:** `Use $calibrate-rhetoric para deixar o texto firme sem soar agressivo.`

[📄 Abrir SKILL.md](skills/calibrate-rhetoric/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

### `review-editorial-quality`

**Versão:** `1.0.0` · **Status:** canônica

Executa QA editorial por severidade, separa bloqueios de melhorias, identifica contradições/lacunas e declara prontidão somente após critérios críticos.

**Exemplo:** `Use $review-editorial-quality para revisar este rascunho antes da entrega.`

[📄 Abrir SKILL.md](skills/review-editorial-quality/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

### `improve-accessible-writing`

**Versão:** `1.0.0` · **Status:** canônica

Melhora clareza, escaneabilidade e linguagem simples preservando precisão técnica, jurídica, científica ou institucional.

**Exemplo:** `Use $improve-accessible-writing para simplificar este texto sem perder precisão.`

[📄 Abrir SKILL.md](skills/improve-accessible-writing/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

### `assess-editorial-alignment`

**Versão:** `1.0.0` · **Status:** canônica

Compara conteúdo com princípios editoriais explicitamente fornecidos, separando não conformidade real de preferência estilística e indicando conflitos que exigem decisão humana.

**Exemplo:** `Use $assess-editorial-alignment usando estes princípios editoriais.`

[📄 Abrir SKILL.md](skills/assess-editorial-alignment/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

### `graphify`

**Versão:** `1.0.0` · **Status:** canônica

Usa um grafo Graphify para reduzir o espaço de busca em código, descobrir relações e dependências e orientar leitura direta dos arquivos. O grafo auxilia a navegação, mas não substitui confirmação no código.

**Origem:** generalização da skill `graphify` usada no `SieDOE`.

**Exemplo:** `Use $graphify para localizar o fluxo entre ingestão, planejamento e persistência.`

[📄 Abrir SKILL.md](skills/graphify/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

### `github-project-repo-sync`

**Versão:** `1.0.0` · **Status:** canônica

Reconcilia um GitHub Project v2 com a intenção versionada no repositório. Separa fonte declarativa, reconciliador e estado observado, preservando itens não gerenciados por padrão.

**Origem:** promovida a partir da implementação criada para `guedesle/projeto-pos-ibmec`.

**Exemplo:** `Use $github-project-repo-sync para reconciliar este Project com o manifesto versionado.`

[📄 Abrir SKILL.md](skills/github-project-repo-sync/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

### `github-project-drift-audit`

**Versão:** `1.0.0` · **Status:** canônica

Audita sem mutação a diferença entre estado desejado, última observação e estado live, classificando o resultado como `IN_SYNC`, `DRIFT`, `STALE` ou `UNVERIFIED`.

**Origem:** promovida a partir da implementação criada para `guedesle/projeto-pos-ibmec`.

**Exemplo:** `Use $github-project-drift-audit para verificar se este Project está sincronizado sem alterar nada.`

[📄 Abrir SKILL.md](skills/github-project-drift-audit/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

### `skills-central-governance`

**Versão:** `1.0.0` · **Status:** canônica

Define o ciclo de vida do catálogo: decidir se a skill é geral, criar no repositório central, registrar versão, atualizar README, declarar espelhos e distribuir alterações.

**Exemplo:** `Use $skills-central-governance para promover esta nova skill ao catálogo geral.`

[📄 Abrir SKILL.md](skills/skills-central-governance/SKILL.md) · [↑ Voltar ao índice](#índice-de-skills)

---

## Como usar

Cada skill possui sua definição canônica em `skills/<nome>/SKILL.md`. O catálogo versionado está em [`registry.json`](registry.json).

Exemplos de invocação:

```text
Use $plan-content para planejar este relatório.
Use $graphify para entender as dependências deste módulo.
Use $github-project-drift-audit para auditar o Project sem mutações.
```

## Política de centralização e sincronização

O fluxo oficial é:

```text
criar/alterar skill geral
        ↓
gu edesle/SKILLS / skills/<nome>
        ↓
registry.json + README.md
        ↓
validação
        ↓
espelhos explicitamente registrados
```

> Observação: o diagrama acima refere-se a `guedesle/SKILLS`; o espaço em `gu edesle` é apenas evitado no bloco visual. O repositório canônico é **`guedesle/SKILLS`**.

Regras:

1. **Central primeiro.** Mudança de comportamento geral nasce neste repositório.
2. **Sem sobrescrever variantes locais por acidente.** Só são atualizados targets presentes em `mirrors` no [`registry.json`](registry.json).
3. **Skills específicas continuam locais.** Quando uma parte for reutilizável, ela deve ser extraída para uma skill geral central.
4. **Nada fora do path gerenciado é apagado.**
5. **README e versão fazem parte da entrega da skill.** Uma skill nova não está completa sem índice, descrição e versão.

Validação local:

```bash
python scripts/sync_skills.py --check
```

Sincronização dos espelhos registrados:

```bash
python scripts/sync_skills.py --apply
```

A automação está em [`.github/workflows/sync-skills.yml`](.github/workflows/sync-skills.yml). Para habilitar pushes automáticos entre repositórios, configure o secret `SKILLS_SYNC_TOKEN` com acesso somente aos repositórios necessários e a variável `SKILLS_AUTO_SYNC=true`. Sem essa configuração, o workflow permanece em modo de validação.

Consulte também [`AGENTS.md`](AGENTS.md) e a própria [`skills-central-governance`](skills/skills-central-governance/SKILL.md).

## Versionamento

O catálogo usa **SemVer**:

- **PATCH** — correções ou esclarecimentos sem alterar o contrato;
- **MINOR** — nova capacidade compatível;
- **MAJOR** — mudança incompatível em gatilhos, procedimento, contrato ou saída.

A versão de cada skill aparece em dois lugares obrigatórios: neste README e no [`registry.json`](registry.json).

## Histórico do catálogo

### 2026-08-14 — baseline central `1.0.0`

- materializadas as nove skills editoriais gerais já declaradas no perfil;
- promovida uma versão geral de `graphify` a partir do uso no `SieDOE`;
- promovidas versões gerais de `github-project-repo-sync` e `github-project-drift-audit` a partir do PFC IBMEC;
- criada `skills-central-governance` para governar novas skills;
- criado `registry.json` como inventário canônico e versionado;
- criado sincronizador central → espelhos e workflow de validação/sincronização;
- README convertido em catálogo navegável com links internos, links para cada `SKILL.md` e versões explícitas.

[↑ Voltar ao topo](#skills--catálogo-central)
