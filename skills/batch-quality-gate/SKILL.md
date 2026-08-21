---
name: batch-quality-gate
description: Execute validações técnicas em lote com relatório consolidado e um único gate humano final. Use quando CI estiver indisponível, quando houver vários validadores independentes ou quando quiser reduzir chamadas HITL sem enfraquecer QA. Prefira o mesmo motor local e remoto, autotestes dos validadores e correção coletiva de bloqueios determinísticos.
---

# Batch Quality Gate

Use esta skill para transformar múltiplos checks dispersos em um único gate reproduzível, auditável e de baixo HITL.

## Objetivo

Consolidar validações de estrutura, contratos, sintaxe, segurança, consistência e escopo em um único comando/relatório, evitando aprovações humanas por subteste.

## Princípios

1. **um motor de validação** deve servir localmente e no CI sempre que possível;
2. `fast` pode existir para feedback intermediário, mas não substitui o `batch` final;
3. validadores críticos devem possuir **autotestes positivos/negativos** para reduzir risco de falso `PASS`;
4. uma falha determinística bloqueia o lote, mas não aciona HITL;
5. todas as falhas conhecidas devem ser corrigidas em conjunto antes de nova rodada;
6. o gate humano só ocorre depois de `PASS` técnico consolidado.

## Gates recomendados

Adapte ao projeto, mantendo a ordem lógica:

1. contexto de repositório/base/branch;
2. estrutura obrigatória;
3. contratos ou schemas;
4. autotestes dos validadores;
5. sintaxe/compilação;
6. secrets e higiene básica;
7. testes funcionais relevantes;
8. escopo e tamanho do lote;
9. detecção de mudanças que exigem revisão elevada.

## Modos

### Fast

Use durante desenvolvimento para feedback rápido. Pode omitir checks caros, mas nunca declarar prontidão final.

### Batch

Obrigatório no fechamento do lote. Deve executar todos os gates bloqueantes e gerar um relatório consolidado.

### CI

Quando houver CI remoto, reutilize a mesma política/motor do batch local. Evite regras diferentes entre `local PASS` e `CI FAIL`.

## Autotestes do validador

Para cada regra crítica, inclua ao menos um caso que deve passar e um caso que deve falhar.

Exemplos:

- ID duplicado;
- schema incompleto;
- campo obrigatório removido;
- estado proibido aceito indevidamente;
- segredo de alta confiança;
- configuração fail-open onde o contrato exige fail-closed.

## Relatório

Gere, preferencialmente, dois formatos:

- humano: Markdown/texto;
- máquina: JSON ou equivalente estruturado.

Inclua:

- status global;
- branch/base;
- lista de gates e status;
- tamanho do lote;
- motivos de revisão elevada;
- próximo passo permitido.

## Política de falha

`FAIL` técnico significa:

1. não pedir aprovação humana ainda;
2. agrupar causas;
3. corrigir o lote;
4. rerodar o mesmo gate;
5. só escalar se a correção exigir decisão material.

## Escopo

Marque como `WARN` ou revisão elevada lotes grandes ou alterações de fronteira, mas não multiplique approvals automaticamente.

## Saída esperada

Retorne um resumo semelhante a:

```text
BATCH GATE PASS
- estrutura: PASS
- contratos: PASS
- validator-selftest: PASS
- sintaxe: PASS
- secrets: PASS
- scope: PASS
- review: elevated
- next: one final human gate
```

## Origem

Generalizada do `LOCAL GATE` do `guedesle/cyber-skills-framework`, criado para substituir temporariamente GitHub Actions sem perder rigor nem aumentar HITL.
