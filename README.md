# SKILLS — catálogo central

Repositório canônico das **skills gerais e reutilizáveis**. A fonte de verdade é `guedesle/SKILLS`; skills específicas de projeto podem permanecer locais, mas capacidades reutilizáveis devem ser promovidas para este catálogo.

## Navegação

- [Índice](#índice-de-skills)
- [Como usar](#como-usar)
- [Sincronização](#sincronização)
- [Mirrors genéricos](#mirrors-genéricos)
- [Homologação](#homologação)
- [Versionamento](#versionamento)
- [Histórico](#histórico)

## Índice de skills

| Skill | Versão | Categoria | Função |
|---|---:|---|---|
| [`plan-content`](#plan-content) | **1.0.0** | Editorial | Briefing, tese, escopo, outline e riscos |
| [`architect-text`](#architect-text) | **1.1.0** | Editorial | Motivo textual → seções → matriz paragrafal tipológica → artefato de arquitetura |
| [`design-paragraphs`](#design-paragraphs) | **1.1.0** | Editorial | 18 tipologias, contratos de refatoração, progressão e exemplares clássicos |
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

### `plan-content`
Transforma objetivo e contexto em briefing operacional, escopo, outline, evidências necessárias, riscos e critérios. [SKILL.md](skills/plan-content/SKILL.md) · [↑ Índice](#índice-de-skills)

### `architect-text`
Converte o **motivo textual** em arquitetura funcional de leitura. A versão **1.1.0** coleta parâmetros de intenção, público, transformação esperada, gênero, evidência, escopo e restrições; projeta seções por função; escolhe operações da tipologia de `design-paragraphs`; e entrega um artefato com matriz `Sx.Py`, dependências argumentativas, plano de evidências, transições, ritmo, riscos e handoff para redação. [SKILL.md](skills/architect-text/SKILL.md) · [Motivo textual](skills/architect-text/references/textual-motive.md) · [Padrões por motivo](skills/architect-text/references/motive-to-paragraph-patterns.md) · [Template do artefato](skills/architect-text/templates/text-architecture-artifact.md) · [↑ Índice](#índice-de-skills)

### `design-paragraphs`
Projeta e refatora parágrafos como unidades de operação discursiva. A versão **1.1.0** amplia a skill para 18 tipologias, introduz contratos explícitos de construção/refatoração e incorpora um corpus clássico de domínio público como asset estrutural — com eficácia avaliada por tipologia e bloqueio explícito de imitação estilística. [SKILL.md](skills/design-paragraphs/SKILL.md) · [Tipologia](skills/design-paragraphs/references/paragraph-typology.md) · [Exemplares clássicos](skills/design-paragraphs/assets/classic-exemplars.md) · [Proveniência](skills/design-paragraphs/references/source-provenance.md) · [↑ Índice](#índice-de-skills)

### `write-with-evidence`
Distingue fatos, inferências, estimativas e opiniões e controla causalidade, extrapolação e incerteza. [SKILL.md](skills/write-with-evidence/SKILL.md) · [↑ Índice](#índice-de-skills)

### `write-technical-content`
Estrutura especificações, requisitos, procedimentos, critérios de aceite e rastreabilidade. Mirror homologado em `guedesle/download-edicoes-doe/.agents/skills/write-technical-content`. [SKILL.md](skills/write-technical-content/SKILL.md) · [↑ Índice](#índice-de-skills)

### `calibrate-rhetoric`
Ajusta tom, autoridade, persuasão e força argumentativa à evidência disponível. [SKILL.md](skills/calibrate-rhetoric/SKILL.md) · [↑ Índice](#índice-de-skills)

### `review-editorial-quality`
Executa QA editorial por severidade e declara prontidão somente após os critérios críticos. Mirror homologado em `guedesle/download-edicoes-doe/.agents/skills/review-editorial-quality`. [SKILL.md](skills/review-editorial-quality/SKILL.md) · [↑ Índice](#índice-de-skills)

### `improve-accessible-writing`
Melhora clareza, escaneabilidade e linguagem simples preservando precisão. [SKILL.md](skills/improve-accessible-writing/SKILL.md) · [↑ Índice](#índice-de-skills)

### `assess-editorial-alignment`
Compara conteúdo com princípios editoriais explicitamente fornecidos. [SKILL.md](skills/assess-editorial-alignment/SKILL.md) · [↑ Índice](#índice-de-skills)

### `graphify`
Usa grafo Graphify para reduzir o espaço de busca em código e orientar leitura direta dos arquivos. Origem: `SieDOE`. [SKILL.md](skills/graphify/SKILL.md) · [↑ Índice](#índice-de-skills)

### `github-project-repo-sync`
Reconcilia GitHub Project v2 com intenção versionada no repositório, preservando itens não gerenciados. Origem: `projeto-pos-ibmec`. [SKILL.md](skills/github-project-repo-sync/SKILL.md) · [↑ Índice](#índice-de-skills)

### `github-project-drift-audit`
Audita sem mutação desired, observed e live e classifica `IN_SYNC`, `DRIFT`, `STALE` ou `UNVERIFIED`. Origem: `projeto-pos-ibmec`. [SKILL.md](skills/github-project-drift-audit/SKILL.md) · [↑ Índice](#índice-de-skills)

### `skills-central-governance`
Governa criação, promoção, versão, documentação e distribuição de skills gerais. [SKILL.md](skills/skills-central-governance/SKILL.md) · [↑ Índice](#índice-de-skills)

## Como usar

Cada definição canônica vive em `skills/<nome>/SKILL.md`; o inventário e os mirrors vivem em [`registry.json`](registry.json).

```text
Use $plan-content para planejar este relatório.
Use $architect-text para transformar o motivo textual em um artefato de arquitetura paragrafal.
Use $design-paragraphs para diagnosticar e refatorar a função de cada parágrafo.
Use $graphify para entender as dependências deste módulo.
Use $github-project-drift-audit para auditar o Project sem mutações.
```

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

O modo `pull` é preferido. `mode: push` permanece como fallback explícito e pode ser aplicado com `python scripts/sync_skills.py --apply` quando houver autenticação apropriada.

## Mirrors genéricos

O [`registry.json`](registry.json) usa `schema_version: 2`. A lógica de sincronização não é mais escrita por skill ou por projeto. Três artefatos centrais implementam o runtime:

- [`.github/workflows/mirror-consumer.yml`](.github/workflows/mirror-consumer.yml): workflow reutilizável;
- [`scripts/sync_consumer.py`](scripts/sync_consumer.py): resolve todas as skills `pull` para `owner/repo + branch`;
- [`templates/sync-central-skills.yml`](templates/sync-central-skills.yml): caller padrão e idêntico para consumidores.

Depois que um repositório recebe esse caller uma única vez, **adicionar outra skill ao mesmo consumidor exige apenas alterar o `registry.json`**. A execução seguinte identifica automaticamente todos os mappings.

Para um consumidor novo, o bootstrap também é padronizado:

```bash
python scripts/bootstrap_consumers.py --check
python scripts/bootstrap_consumers.py --apply --repository owner/repo
```

[`scripts/bootstrap_consumers.py`](scripts/bootstrap_consumers.py) cria ou atualiza somente o caller padrão configurado no registry. O bootstrap precisa de permissão para alterar o workflow do consumidor; depois disso, cada mirror `pull` trabalha no contexto do próprio repositório.

## Homologação

`guedesle/download-edicoes-doe` é o consumidor de homologação. O mesmo caller genérico recebe atualmente `write-technical-content` e `review-editorial-quality`.

A segunda skill foi adicionada **somente no `registry.json`**, sem mudar a lógica do workflow consumidor. O commit automático `3c3a8af9b040228d5d0a8870cc988aabf9d75ad6` alterou exclusivamente `.agents/skills/review-editorial-quality/SKILL.md`, confirmando isolamento por path.

A cadência padrão é horária no minuto 17, além de execução manual. O runtime trata concorrência e `non-fast-forward` sem adicionar arquivos fora dos paths registrados.

Consulte também [`AGENTS.md`](AGENTS.md), [`general-skills-status.md`](general-skills-status.md) e [`skills-central-governance`](skills/skills-central-governance/SKILL.md).

## Versionamento

O catálogo usa SemVer: **PATCH** para correções compatíveis, **MINOR** para nova capacidade compatível e **MAJOR** para mudança incompatível de contrato. A versão deve constar no README e no `registry.json`.

## Histórico

### 2026-08-16 — `architect-text` 1.1.0
- motivo textual formalizado como contrato de entrada da arquitetura;
- definidos 20 parâmetros de intenção, audiência, gênero, evidência, escopo, governança, voz e ritmo;
- criados padrões heurísticos que mapeiam atos comunicativos para sequências da tipologia de `design-paragraphs`;
- matriz paragrafal passa a usar IDs estáveis `Sx.Py` e contratos com âncora, núcleo, desenvolvimento, virada, pouso, evidência e critério de aceite;
- criado template canônico do Artefato de Arquitetura Textual, incluindo grafo de dependências, plano de evidências, transições, riscos e handoff;
- integração explícita com os 18 tipos paragrafais e os exemplares `CL-*` da `design-paragraphs`.

### 2026-08-16 — `design-paragraphs` 1.1.0
- tipologia ampliada de 8 funções genéricas para 18 operações paragrafais;
- contratos de construção, refatoração e critérios de aceite documentados por tipologia;
- criado corpus com 10 exemplares clássicos de domínio público de Machado de Assis, Eça de Queirós, Charles Darwin e James Madison;
- eficácia de exemplares clássicos classificada como alta, média ou baixa para cada tipologia;
- proveniência, repositórios GITenberg, arquivos e blob SHAs registrados;
- uso dos clássicos restrito à abstração estrutural, com bloqueio de imitação estilística e de transferência de conteúdo histórico como autoridade atual.

### 2026-08-16 — mirrors pull genéricos
- `registry.json` migrado para schema v2;
- criado workflow reutilizável central;
- criado `scripts/sync_consumer.py` para múltiplas skills por consumidor;
- consumer homologado reduzido a caller padrão;
- segunda skill propagada apenas por alteração do registry;
- criado template e `scripts/bootstrap_consumers.py` para novos consumidores;
- validação central e execução do consumidor concluídas com sucesso.

### 2026-08-16 — primeiro mirror pull
- `guedesle/SKILLS` tornou-se público;
- `write-technical-content` foi propagada para `download-edicoes-doe` sem token global de sincronização;
- commit inicial ficou restrito ao path gerenciado.

### 2026-08-14 — baseline `1.0.0`
- materializadas 13 skills canônicas;
- criado `registry.json`, sincronizador, workflow de validação e catálogo navegável.

[↑ Voltar ao topo](#skills--catálogo-central)
