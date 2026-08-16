# Estado das skills gerais

Atualizado em 16 de agosto de 2026.

## Fonte canônica

`guedesle/SKILLS` é a fonte de verdade para skills gerais/reutilizáveis. O inventário operacional está em [`registry.json`](registry.json), atualmente em `schema_version: 2`, e a navegação/versões em [`README.md`](README.md).

Skills específicas de projeto não são promovidas automaticamente. Quando uma capacidade local possui valor transversal, uma versão geral é extraída para este catálogo e a origem fica registrada.

## Catálogo atual

| Skill | Categoria | Versão | Estado |
|---|---|---:|---|
| `plan-content` | Editorial | 1.0.0 | Canônica |
| `architect-text` | Editorial | 1.1.0 | Canônica + artefato de arquitetura paragrafal |
| `design-paragraphs` | Editorial | 1.1.0 | Canônica + tipologia e corpus de exemplares |
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

`architect-text` foi elevada para **1.1.0** e agora trata o **motivo textual** como contrato de entrada da arquitetura. A skill coleta ou infere intenção, transformação do leitor, público, gênero, evidência, escopo, restrições e riscos; transforma esses parâmetros em seções funcionais e em uma matriz paragrafal que consome a tipologia de `design-paragraphs`; e produz um Artefato de Arquitetura Textual com IDs `Sx.Py`, dependências argumentativas, plano de evidências, transições, ritmo e critérios de aceite.

`design-paragraphs` foi elevada para **1.1.0** com uma tipologia operacional de 18 funções, contratos assertivos de construção/refatoração e um corpus de exemplares clássicos de domínio público. Os assets registram fonte, repositório, arquivo e blob SHA e são usados apenas para abstrair arquitetura paragrafal; a skill proíbe tratar prestígio literário, posições históricas ou voz autoral como modelo automático para o texto-alvo.

`graphify` foi generalizada a partir do workflow existente no `SieDOE`, mantendo a regra essencial: usar o grafo para descoberta e confirmar detalhes diretamente no código antes de editar.

`github-project-repo-sync` e `github-project-drift-audit` foram promovidas a partir das skills criadas no PFC IBMEC. A versão central remove nomes e IDs exclusivos do PFC e preserva o padrão desired → reconcile/audit → observed/live.

## Critério de maturidade

**Canônica** significa que a skill possui definição central, versão registrada e documentação navegável. Isso não significa, por si só, que todas as skills tenham passado por uma bateria comparativa de evals em produção.

**Artefato de arquitetura paragrafal** significa que `architect-text` possui contrato de entrada por motivo textual, padrões de composição por ato comunicativo e um template explícito para entregar seções, operações paragrafais, dependências e handoff reproduzível.

**Tipologia e corpus de exemplares** significa que a skill possui referência operacional separada do runtime principal, assets rastreáveis e critérios explícitos para decidir quando exemplos históricos ajudam ou atrapalham a tarefa.

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

Para `architect-text`, criar evals que comparem arquiteturas produzidas a partir do mesmo tema com motivos textuais diferentes, verificando se a mudança de intenção realmente altera seções, sequência tipológica e dependências. Para `design-paragraphs`, executar evals comparativos por tipologia: parágrafo original → diagnóstico → refatoração sem exemplar → refatoração com exemplar estrutural → julgamento de clareza, fidelidade, progressão e risco de imitação. Para as demais skills, executar evals controlados por família de uso e registrar resultados por versão.
