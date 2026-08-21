---
name: knowledge-source-governance
description: Governe fontes de conhecimento e evidência por registry, autoridade, freshness, aplicabilidade, corroboration e teto de conclusão. Use quando agentes/modelos pesquisam múltiplas fontes e você precisa impedir que uma fonte fraca ou desatualizada promova sozinha uma conclusão material.
---

# Knowledge Source Governance

Use esta skill para transformar acesso a fontes em uma supply chain de conhecimento auditável, em vez de permitir que o modelo trate qualquer documento ou resultado de busca como autoridade equivalente.

## Princípio

**Fonte fornece evidência; o contrato define o que essa evidência pode concluir.**

Não use um único `trust score` para todos os fins. Uma fonte pode ser forte em autoridade e fraca em aplicabilidade, ou atual e pouco específica.

## Source Registry

Registre, quando aplicável:

- `source_id`;
- owner/proveniência;
- domínio;
- classe de autoridade;
- URL/origem;
- formato;
- cadence/update mode;
- freshness TTL;
- equipes/workflows autorizados a consumir;
- `allowed_outcomes`;
- `forbidden_outcomes`;
- necessidade de corroboration;
- data da última verificação.

## Vetor de qualidade

Avalie dimensões separadas:

- authority;
- freshness;
- specificity;
- applicability;
- corroboration;
- empirical support.

Evite transformar esse vetor em uma nota única se a decisão depende de dimensões diferentes.

## Teto de conclusão

Defina o máximo que cada classe de fonte pode produzir.

Exemplos gerais:

- issue/discussion → hipótese ou early signal;
- base curada → referência/evidência/candidato;
- score preditivo → priorização, não veredito final;
- guideline/standard → controle/requisito, não prova de ocorrência;
- resultado de scanner → candidato, salvo contrato específico com validação independente;
- fonte primária + evidência do alvo → pode sustentar conclusão somente após o workflow de validação definido.

## Corroboration

Exija corroboration para fontes comunitárias, secundárias, incidentais ou com alta variabilidade. Preserve evidência conflitante em vez de escolher silenciosamente a fonte mais conveniente.

## Freshness

Quando a fonte exceder TTL:

1. marcar `stale`;
2. buscar versão atual ou fonte corroborante;
3. não promover conclusão que dependa de atualidade sem evidência nova;
4. preservar versão/snapshot usado para reprodutibilidade.

## Internet/search

Busca aberta serve principalmente para descoberta. Quando uma conclusão material depender de uma fonte encontrada, classifique-a no registry ou aplique explicitamente a mesma política de autoridade, freshness e corroboration.

## Watchlists

Para ecossistemas que mudam rápido, mantenha watchlists de projetos/fontes com:

- surfaces monitoradas;
- cadence;
- policy de issue/advisory/release;
- estado de manutenção da própria fonte.

Uma issue nova não deve virar conclusão validada apenas por estar recente.

## Pipeline

```text
source discovery
  ↓
provenance + classification
  ↓
freshness check
  ↓
normalization/dedup
  ↓
corroboration + counterevidence
  ↓
applicability/context
  ↓
candidate/evidence
  ↓
workflow de validação
  ↓
conclusão material
```

## HITL

Automatize classificação, freshness, dedup e checks de corroboration. Solicite HITL quando houver conflito de autoridade não resolvível, aceitação explícita de fonte fora da política, mudança de policy ou decisão material com evidência insuficiente.

## Saída esperada

Informe fontes usadas, proveniência, freshness, allowed outcome, corroboration, conflitos, evidência produzida e qual conclusão ainda depende de validação.

## Origem

Generalizada do `Cyber Knowledge Plane` do `guedesle/cyber-skills-framework`, removendo catálogos e regras exclusivas de cibersegurança e preservando o padrão transversal de proveniência, freshness, corroboration e evidence ceilings.
