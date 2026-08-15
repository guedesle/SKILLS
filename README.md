# Skills gerais

Este repositório documenta as skills editoriais gerais derivadas do projeto [editor-agent](https://github.com/guedesle/editor-agent) e disponibilizadas no perfil do autor.

As versões gerais removem dependências do runtime e da identidade específica do Códice Público. Elas podem ser usadas em artigos, relatórios, notícias, apresentações, roteiros, documentação técnica e outros conteúdos.

## Estado atual

| Skill | Escopo geral | Origem principal | Estado |
|---|---|---|---|
| `plan-content` | Briefing, tese, escopo, outline, riscos e critérios | Domínio 01 — Planejamento | Instalada e validada |
| `architect-text` | Mapa de seções, contratos e matriz paragrafal | Domínio 02 — Arquitetura Textual | Instalada e validada |
| `design-paragraphs` | Composição, transição, ritmo e densidade de parágrafos | Domínios 03 e 04 | Instalada e validada |
| `write-with-evidence` | Fatos, fontes, inferências, causalidade e interesse público | Domínios 05, 07 e 08 | Instalada e validada |
| `write-technical-content` | Especificações, guias, procedimentos e documentação | Domínio 06 | Instalada e validada |
| `calibrate-rhetoric` | Tom, persuasão, autoridade, cadência e proporcionalidade | Domínio 09 | Instalada e validada |
| `review-editorial-quality` | QA, achados, bloqueios, correções e prontidão | Domínio 10 | Instalada e validada |
| `improve-accessible-writing` | Clareza, leitura em tela e linguagem simples | Domínio 11 | Instalada e validada |
| `assess-editorial-alignment` | Aderência a princípios editoriais configuráveis | Generalização do domínio 12 | Instalada e validada |

Consulte [Estado das skills gerais](general-skills-status.md) para critérios, diferenças em relação ao projeto de origem e exemplos de acionamento.

## Uso

As skills podem ser acionadas pelo nome, por exemplo:

- `Use $plan-content para planejar um artigo sobre...`
- `Use $architect-text para organizar este relatório.`
- `Use $review-editorial-quality para revisar este rascunho.`

O projeto `editor-agent` continua sendo a fonte do runtime editorial, pipelines, schemas, fixtures e integrações. Este repositório registra apenas a camada geral e reutilizável do perfil.
