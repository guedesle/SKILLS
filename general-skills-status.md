# Estado das skills gerais

Atualizado em 16 de agosto de 2026.

## Fonte canônica

`guedesle/SKILLS` é a fonte de verdade para skills gerais/reutilizáveis. O inventário operacional está em [`registry.json`](registry.json), atualmente em `schema_version: 2`, e a navegação/versões em [`README.md`](README.md).

Skills específicas de projeto não são promovidas automaticamente. Quando uma capacidade local possui valor transversal, uma versão geral é extraída para este catálogo e a origem fica registrada.

## Catálogo atual

| Skill | Categoria | Versão | Estado |
|---|---|---:|---|
| `plan-content` | Editorial | 1.0.0 | Canônica |
| `architect-text` | Editorial | 1.2.0 | Canônica + Plano de Arquitetura do Texto + nomenclatura autoexplicativa |
| `design-paragraphs` | Editorial | 1.2.0 | Canônica + 18 funções de parágrafo + nomenclatura autoexplicativa + corpus de exemplos |
| `write-with-evidence` | Editorial | 1.0.0 | Canônica |
| `write-technical-content` | Editorial/Técnica | 1.0.0 | Canônica + mirror homologado |
| `calibrate-rhetoric` | Editorial | 1.0.0 | Canônica |
| `review-editorial-quality` | QA | 1.0.0 | Canônica + mirror homologado |
| `improve-accessible-writing` | Acessibilidade | 1.0.0 | Canônica |
| `assess-editorial-alignment` | Governança editorial | 1.0.0 | Canônica |
| `graphify` | Engenharia de software | 1.0.0 | Canônica |
| `github-project-repo-sync` | GitHub automation | 1.0.0 | Canônica |
| `github-project-drift-audit` | GitHub/QA | 1.0.0 | Canônica |
| `skills-central-governance` | Gestão de skills | 1.0.0 | Canônica |

## Origem e promoção

As nove skills editoriais foram generalizadas a partir das capacidades do `editor-agent`, removendo dependências de runtime, identidade específica e schemas exclusivos. `architect-text` preserva a proveniência da skill local `editor-structure`.

`architect-text` está em **1.2.0**. A skill coleta a **finalidade do texto**, define o **resultado esperado da leitura**, organiza a **sequência lógica do texto**, planeja seções e parágrafos e produz o **Plano de Arquitetura do Texto**. Identificadores apresentados ao usuário são descritivos, como **Seção 2 · Parágrafo 4**, e não códigos opacos como `S2.P4`.

`design-paragraphs` está em **1.2.0**. A skill mantém 18 funções de parágrafo e o corpus de exemplos clássicos, mas passa a usar nomes autoexplicativos como **ponto de partida**, **ideia central**, **como desenvolver**, **contraste/ressalva/limite** e **como encerrar e ligar ao próximo**. Os exemplos clássicos devem ser apresentados por autor e obra; códigos `CL-*` ficam apenas como referência interna.

`graphify` foi generalizada a partir do workflow existente no `SieDOE`, mantendo a regra essencial: usar o grafo para descoberta e confirmar detalhes diretamente no código antes de editar.

`github-project-repo-sync` e `github-project-drift-audit` foram promovidas a partir das skills criadas no PFC IBMEC. A versão central remove nomes e IDs exclusivos do PFC e preserva o padrão desired → reconcile/audit → observed/live.

## Política de nomenclatura editorial

Nas skills editoriais, nomes de campos e etapas devem ser compreensíveis sem glossário. Termos acadêmicos, metafóricos, abreviações e códigos podem existir internamente para rastreabilidade, mas não devem ser a linguagem principal mostrada ao usuário quando houver uma expressão direta equivalente.

Exemplos de substituição:

- `motivo textual` → **finalidade do texto**;
- `ato comunicativo dominante` → **função principal do texto**;
- `transformação do leitor` → **resultado esperado da leitura**;
- `movimento macro` → **sequência lógica do texto**;
- `matriz paragrafal` → **plano de parágrafos**;
- `S2.P4` → **Seção 2 · Parágrafo 4**;
- `âncora` → **ponto de partida**;
- `núcleo` → **ideia central**;
- `virada` → **contraste, ressalva, limite ou consequência**;
- `pouso` → **como encerrar e ligar ao próximo**;
- `handoff` → **instruções para a próxima etapa**.

## Critério de maturidade

**Canônica** significa que a skill possui definição central, versão registrada e documentação navegável. Isso não significa, por si só, que todas as skills tenham passado por uma bateria comparativa de evals em produção.

**Plano de Arquitetura do Texto** significa que `architect-text` possui entrada estruturada pela finalidade do texto e um modelo explícito para entregar seções, funções de parágrafo, dependências, evidências, ligações e instruções de redação.

**Tipologia e corpus de exemplos** significa que `design-paragraphs` possui referência operacional separada, exemplos rastreáveis e critérios explícitos para decidir quando exemplos históricos ajudam ou atrapalham a tarefa.

**Mirror homologado** significa que a definição canônica foi propagada automaticamente para um repositório consumidor por um path explicitamente registrado, com GitHub Actions validado e sem alteração de conteúdo fora dos paths gerenciados.

## Política de sincronização

- central: `skills/<nome>/SKILL.md`;
- inventário/versionamento/mappings: `registry.json`;
- documentação: `README.md`;
- validação estrutural: `python scripts/sync_skills.py --check`;
- runtime pull genérico: `.github/workflows/mirror-consumer.yml` + `scripts/sync_consumer.py`;
- caller padrão de consumidores: `templates/sync-central-skills.yml`;
- bootstrap padronizado de consumidor novo: `scripts/bootstrap_consumers.py`;
- fallback push explícito: `python scripts/sync_skills.py --apply`.

No modo preferido `pull`, um repositório consumidor recebe o caller padrão uma única vez. A partir daí, novas skills destinadas ao mesmo consumidor são adicionadas somente como mappings no `registry.json`; o workflow compartilhado resolve automaticamente todas as skills daquele repositório e branch.

O bootstrap de um consumidor totalmente novo ainda exige uma credencial ou integração com permissão para criar/atualizar o arquivo de workflow naquele repositório. Depois do bootstrap, o mirror usa o `GITHUB_TOKEN` do próprio consumidor e não requer PAT global.

Espelhos só são atualizados quando declarados explicitamente em `registry.json`. Variantes locais registradas em `legacy_source` servem para proveniência e não são sobrescritas automaticamente.

## Homologação atual

Consumidor: `guedesle/download-edicoes-doe`, branch `main`.

Mappings ativos:

- `write-technical-content` → `.agents/skills/write-technical-content`;
- `review-editorial-quality` → `.agents/skills/review-editorial-quality`.

A segunda skill foi adicionada apenas ao `registry.json`, sem lógica nova no workflow consumidor, comprovando o modelo multi-skill genérico. O workflow central também executa compilação dos utilitários e smoke test do resolvedor pull para esses dois mappings.

## Próxima evolução de qualidade

Para `architect-text`, criar avaliações que comparem estruturas produzidas a partir do mesmo tema com finalidades diferentes, verificando se a mudança de objetivo altera realmente seções, funções dos parágrafos e dependências. Para `design-paragraphs`, comparar refatorações com e sem exemplos estruturais, julgando clareza, fidelidade, progressão e risco de imitação. Para as demais skills, executar avaliações controladas por família de uso e registrar resultados por versão.
