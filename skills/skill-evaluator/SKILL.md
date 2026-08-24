---
name: skill-evaluator
description: "Projete e avalie casos de teste de uma skill, incluindo should-trigger, should-not-trigger e invariantes comportamentais. Use quando a questão é se a skill seleciona e se comporta corretamente; não trate schema válido como evidência de desempenho do modelo."
---

# skill-evaluator

Tornar descoberta e comportamento da skill falsificáveis por casos declarativos e, quando disponível, execução no host.

## Workflow

1. Mapeie vizinhos semânticos e riscos de trigger collision.
2. Crie casos `trigger_positive` e `trigger_negative` com entradas reais e discriminativas.
3. Crie `behavior` cases para invariantes de saída, stop conditions e escalation.
4. Valide o schema deterministicamente antes de qualquer execução de modelo.
5. Quando o host oferecer runner, registre modelo/host, casos executados e resultados observados.
6. Sem runner, reporte somente `EVAL_SCHEMA_PASS` ou `EVALS_DECLARED`; nunca invente acurácia.

## Stop e escalation

- Critério de sucesso não observável.
- Runner/modelo necessário não está disponível e o pedido exige métrica empírica.

## Saída esperada

- casos de eval;
- colisões encontradas;
- status declarado versus executado;
- regressões.
