---
name: decision-escalation-control
description: Classifique decisões e defina quando continuar autonomamente, recomendar revisão, exigir aprovação ou bloquear. Use para reduzir HITL sem transformar risco alto em automação silenciosa. Separe falhas determinísticas de decisões materiais e faça elevated review aumentar profundidade, não quantidade de approvals.
---

# Decision Escalation Control

Use esta skill para decidir **quando parar** e **quando continuar** em workflows autônomos.

## Objetivo

Evitar dois erros opostos:

- HITL excessivo para problemas corrigíveis automaticamente;
- autonomia excessiva em decisões materiais, irreversíveis ou não autorizadas.

## Classes

### AUTO_CONTINUE

Use quando a ação:

- é reversível;
- está dentro do escopo já aprovado;
- não muda contrato nem intenção;
- possui resultado verificável;
- pode ser corrigida/reexecutada deterministicamente.

### HUMAN_REVIEW_RECOMMENDED

Use quando o trabalho pode continuar, mas a revisão final merece atenção adicional por impacto, novidade, incerteza ou mudança de boundary.

### HUMAN_REVIEW_REQUIRED

Use antes de:

- alterar escopo ou requisito material;
- escolher entre alternativas arquiteturais não equivalentes;
- aceitar risco relevante;
- executar em produção;
- realizar operação destrutiva/irreversível;
- usar autorização, identidade ou credencial que depende do responsável;
- assumir compromisso externo relevante.

### BLOCKED_UNTIL_REVIEW

Use quando a continuação segura é impossível sem decisão/informação humana ou quando o contrato/política proíbe prosseguir.

## Elevated review

`elevated` é atributo da **profundidade da revisão**, não um novo estado de aprovação.

Exemplos de motivos:

- alteração de política ou autorização;
- segurança/privacidade;
- mudança de capability boundary;
- dados sensíveis;
- infraestrutura crítica;
- impacto financeiro/jurídico alto;
- mudança de contrato machine-readable que governa execução.

## Decisão baseada em evidência

Registre:

- evento que disparou a classificação;
- risco/impacto;
- reversibilidade;
- escopo afetado;
- evidência disponível;
- ação permitida antes da revisão;
- condição para desbloquear.

## Escalation por surpresa

Mesmo que uma tarefa tenha começado em `AUTO_CONTINUE`, eleve a classe se evidência inesperada alterar materialmente risco, impacto, severidade, custo, escopo ou premissas.

## Não escalar por

- erro de lint;
- falha de schema corrigível;
- teste determinístico quebrado;
- branch atrasada que admite fast-forward seguro;
- metadata ausente;
- inconsistência que pode ser corrigida sem escolher nova política.

## Integração com low-HITL

A sequência recomendada é:

```text
falha/evento
  ↓
classificar decisão
  ↓
AUTO_CONTINUE → corrigir/agrupar/revalidar
HUMAN_REVIEW_RECOMMENDED → continuar + registrar para gate final
HUMAN_REVIEW_REQUIRED → parar antes da ação material
BLOCKED_UNTIL_REVIEW → não prosseguir
```

## Saída esperada

Retorne classe, motivo, evidência, ação autorizada agora, próximo gate e condição de desbloqueio.

## Origem

Generalizada dos critérios de interrupção e revisão elevada usados no `guedesle/cyber-skills-framework` para manter baixo HITL sem enfraquecer decisões de risco.
