# Padrões de arquitetura por motivo textual

Esta referência ajuda `architect-text` a transformar o motivo textual em uma sequência inicial de operações paragrafais. Os padrões são **heurísticas**, não templates rígidos. Adapte-os ao gênero, evidência, risco e extensão.

As tipologias referem-se a `skills/design-paragraphs/references/paragraph-typology.md`.

## 1. Informar estado ou situação

Sequência-base:

`abertura de enquadramento → descrição analítica → sustentação evidencial → síntese/integração → fechamento`

Adicione `classificação` quando houver categorias de estado. Adicione `implicação/recomendação` somente se o texto também tiver função deliberativa.

## 2. Explicar conceito, mecanismo ou causa

Sequência-base:

`abertura → definição/conceituação → explicação causal → exemplificação → contraste/concessão → síntese`

Use `classificação` antes da causalidade quando o objeto tiver subtipos relevantes. Use `sustentação evidencial` entre causa e consequência quando o mecanismo exigir comprovação.

## 3. Analisar problema ou fenômeno

Sequência-base:

`abertura → definição/recorte → descrição analítica → classificação → sustentação evidencial → comparação ou causalidade → síntese → implicação`

Se houver hipóteses concorrentes, introduza `contraste/concessão` e `refutação` antes da síntese.

## 4. Argumentar por uma tese

Sequência-base:

`abertura → tese/proposição → sustentação evidencial → explicação causal ou exemplificação → contraste/concessão → refutação → síntese → fechamento`

Não use `refutação` sem objeção real. Se a tese for pouco controversa, uma concessão pode ser suficiente.

## 5. Recomendar ou apoiar decisão

Sequência-base:

`abertura → problema–resposta → sustentação evidencial → classificação de alternativas → comparação → contraste/concessão → implicação/recomendação → fechamento`

O parágrafo de recomendação deve explicitar critério, condições e risco. Se a decisão depender de lacuna crítica, substitua recomendação definitiva por `implicação` + necessidade de evidência.

## 6. Comparar ou avaliar alternativas

Sequência-base:

`abertura → definição dos critérios → classificação das alternativas → comparação/analogia → sustentação evidencial → síntese/integração → implicação/recomendação`

Mantenha o eixo comparativo constante. Quando critérios conflitarem, use `contraste/concessão` para explicitar trade-offs.

## 7. Instruir execução

Sequência-base:

`abertura de enquadramento → definição de condição/pré-requisito → procedimental/instrucional [repetido por etapa ou grupo] → problema–resposta para exceções → fechamento/verificação`

Prefira listas, tabelas ou procedimentos estruturados quando várias ações forem independentes. O parágrafo não deve ser usado para esconder etapas críticas.

## 8. Documentar ou registrar decisão/estado

Sequência-base:

`abertura → descrição analítica do estado → narrativa/evento quando houver histórico relevante → sustentação evidencial/documental → síntese → implicação/recomendação ou fechamento`

Evite transformar registro em defesa retrospectiva. Separe fato, decisão, justificativa e consequência.

## 9. Narrar ou reconstituir

Sequência-base:

`abertura → narrativa/evento [um ou mais ciclos] → explicação causal ou contraste → síntese → implicação/fechamento`

Cada evento deve alterar estado, conhecimento ou consequência. Corte cronologia sem função.

## 10. Sintetizar múltiplas fontes ou achados

Sequência-base:

`abertura → classificação dos elementos → comparação/contraste → sustentação evidencial → síntese/integração → implicação`

Não faça resumo serial de fonte por fonte se o objetivo for síntese. Organize por questões, padrões, convergências e divergências.

## 11. Texto técnico ou especificação

Sequência-base:

`abertura/escopo → definição/conceituação → classificação de componentes/requisitos → descrição analítica → procedimental/instrucional quando aplicável → problema–resposta/exceções → implicação/critério de aceite → fechamento`

A arquitetura deve separar requisito, justificativa, procedimento e critério de aceite quando essas funções coexistirem.

## 12. Texto acadêmico de pesquisa

Uma sequência comum para seção argumentativa/analítica:

`abertura/questão → definição/estado da questão → sustentação evidencial → contraste entre perspectivas → explicação causal ou análise → refutação/limitação → síntese → implicação`

Não force estrutura IMRaD em partes que não pertencem a esse gênero. O template acadêmico ou institucional prevalece quando for obrigatório.

## Regra de composição de seções

Uma seção não é apenas um agrupamento temático. Defina para cada seção:

1. **função macro** — o que muda no leitor ao terminar a seção;
2. **entrada** — que conhecimento ou conclusão anterior ela pressupõe;
3. **saída** — o que passa a estar estabelecido;
4. **sequência paragrafal** — quais operações produzem essa saída;
5. **evidência** — o que cada operação precisa para ser válida;
6. **ponte** — por que a seção seguinte é necessária.

## Regra de seleção

Para cada parágrafo planejado, responda:

`Por que esta tipologia é necessária neste ponto para realizar o motivo textual?`

Se a resposta for apenas “porque esse assunto precisa aparecer”, a arquitetura ainda está temática, não funcional.
