# `architect-text` — arquitetura textual orientada por motivo

Navegação da skill:

- [`SKILL.md`](SKILL.md) — procedimento operacional;
- [`references/textual-motive.md`](references/textual-motive.md) — parâmetros que explicam por que o texto existe e que transformação deve produzir;
- [`references/motive-to-paragraph-patterns.md`](references/motive-to-paragraph-patterns.md) — padrões heurísticos de sequência paragrafal por ato comunicativo;
- [`templates/text-architecture-artifact.md`](templates/text-architecture-artifact.md) — contrato de saída canônico;
- [`references/architecture-qa.md`](references/architecture-qa.md) — QA e teste contrafactual da arquitetura;
- [`../design-paragraphs/references/paragraph-typology.md`](../design-paragraphs/references/paragraph-typology.md) — tipologia operacional consumida pela arquitetura;
- [`../design-paragraphs/assets/classic-exemplars.md`](../design-paragraphs/assets/classic-exemplars.md) — exemplares estruturais opcionais para o handoff paragrafal.

Fluxo:

```text
motivo textual
  ↓
promessa de leitura
  ↓
movimento macro
  ↓
seções funcionais
  ↓
matriz paragrafal Sx.Py
  ↓
dependências + evidências + transições
  ↓
QA da arquitetura
  ↓
Artefato de Arquitetura Textual
  ↓
design-paragraphs / redação
```

A arquitetura está pronta quando a redação pode começar sem que o redator precise decidir durante a escrita **qual é a função de cada seção ou parágrafo e por que eles aparecem naquela ordem**.
