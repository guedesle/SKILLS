# `architect-text` — arquitetura de textos para leitura humana

Navegação da skill:

- [`SKILL.md`](SKILL.md) — procedimento principal e limite de domínio;
- [`evals/`](evals/) — casos positivos, negativos e comportamentais, incluindo colisões com arquitetura tecnológica;
- [`references/textual-motive.md`](references/textual-motive.md) — finalidade do texto e informações necessárias antes de estruturar;
- [`references/motive-to-paragraph-patterns.md`](references/motive-to-paragraph-patterns.md) — sequências iniciais de parágrafos conforme a finalidade;
- [`templates/text-architecture-artifact.md`](templates/text-architecture-artifact.md) — modelo do Plano de Arquitetura do Texto;
- [`references/architecture-qa.md`](references/architecture-qa.md) — revisão da arquitetura antes da redação;
- [`../design-paragraphs/references/paragraph-typology.md`](../design-paragraphs/references/paragraph-typology.md) — tipos de parágrafo por função;
- [`../design-paragraphs/assets/classic-exemplars.md`](../design-paragraphs/assets/classic-exemplars.md) — exemplos clássicos opcionais para estudar estrutura.

## Limite de domínio

A versão 2.0.0 é exclusivamente editorial. `architect-text` organiza **seções, parágrafos, evidências e sequência de leitura** de textos destinados a leitores humanos.

Não use esta skill para arquitetura de software, sistemas, agentes, dados, infraestrutura, APIs, requisitos, backlog, implementação, migração, testes ou CI/CD. Quando decisões técnicas já estiverem definidas, a skill pode organizar somente a forma de comunicá-las em artigo, relatório, apresentação ou outro texto para leitura humana.

Fluxo:

```text
finalidade do texto
  ↓
resultado esperado da leitura
  ↓
sequência lógica do texto
  ↓
seções e seus objetivos
  ↓
parágrafos e suas funções
  ↓
dependências entre ideias + evidências + ligações
  ↓
revisão da estrutura
  ↓
Plano de Arquitetura do Texto
  ↓
design-paragraphs / redação
```

A arquitetura está pronta quando a redação pode começar sem que o redator precise decidir durante a escrita **qual é a função de cada seção ou parágrafo, que evidência precisa usar e por que cada parte aparece naquela ordem**.

## Vocabulário

A nomenclatura permanece autoexplicativa. Termos internos ou acadêmicos não devem aparecer como linguagem principal dos artefatos quando houver uma expressão direta em português corrente.
