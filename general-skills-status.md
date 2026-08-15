# Estado das skills gerais

Atualizado em 14 de agosto de 2026.

## Objetivo da generalização

Transformar capacidades editoriais do `editor-agent` em skills independentes de projeto. A generalização segue quatro regras:

1. remover caminhos, schemas, comandos e pipelines específicos do runtime;
2. preservar os critérios editoriais reutilizáveis;
3. ampliar formatos e contextos de acionamento;
4. manter limites de segurança, rastreabilidade e revisão humana.

## Mapeamento e maturidade

| Skill geral | Capacidades absorvidas | Maturidade da origem | Estado geral |
|---|---|---:|---|
| `plan-content` | `plan_article`, `plan_editorial` e planejamento de outros formatos | M2 | Validada estruturalmente |
| `architect-text` | `editor-structure`, contratos de seção e matriz paragrafal | M3 | Validada estruturalmente |
| `design-paragraphs` | `paragraph_argument`, `paragraph_explanation`, ritmo e densidade | M2 | Validada estruturalmente |
| `write-with-evidence` | `verify_claims`, ângulo jornalístico, evidência científica e valor público | M2 | Validada estruturalmente |
| `write-technical-content` | Redação técnica, requisitos e rastreabilidade | M2 | Validada estruturalmente |
| `calibrate-rhetoric` | `strengthen_argument`, tom, persuasão e cadência | M2 | Validada estruturalmente |
| `review-editorial-quality` | `full_review`, `publication_review` e handoff de correções | M2 | Validada estruturalmente |
| `improve-accessible-writing` | `simplify_language` e `create_plain_language_summary` | M1 | Validada estruturalmente |
| `assess-editorial-alignment` | `evaluate_editorial_fit` com princípios configuráveis | M1 | Validada estruturalmente |

“Validada estruturalmente” significa que a skill possui metadados válidos, instruções completas e interface registrada. Não significa que já passou por uma bateria comparativa de resultados em produção.

## Diferenças em relação ao editor-agent

- Não dependem de `/editor`, registries, schemas JSON ou artifacts do runtime.
- Não presumem a identidade do Códice Público.
- Não executam publicação automática.
- Pedem critérios do usuário quando o alinhamento editorial não estiver definido.
- Mantêm revisão humana para decisões editoriais, factuais ou institucionais relevantes.

## Exemplos de acionamento

### Planejamento e estrutura

- `Use $plan-content para planejar uma apresentação executiva sobre este projeto.`
- `Use $architect-text para transformar o briefing em mapa de seções e parágrafos.`

### Redação e revisão

- `Use $design-paragraphs para melhorar a progressão deste capítulo.`
- `Use $write-with-evidence para separar fatos, inferências e pendências de fonte.`
- `Use $write-technical-content para converter estes requisitos em especificação.`
- `Use $calibrate-rhetoric para deixar o texto firme sem soar agressivo.`

### Qualidade e alinhamento

- `Use $review-editorial-quality para apontar bloqueios antes da publicação.`
- `Use $improve-accessible-writing para simplificar sem perder precisão.`
- `Use $assess-editorial-alignment usando estes princípios editoriais.`

## Próxima etapa recomendada

Executar casos de teste controlados com três famílias:

1. artigo factual com fontes;
2. documento técnico orientado à decisão;
3. apresentação executiva.

Registrar acertos, falhas e ajustes necessários antes de promover as skills de “validadas estruturalmente” para “testadas em uso”.
