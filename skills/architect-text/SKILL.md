---
name: architect-text
description: Transforme motivo textual, briefing, tópicos, outline ou rascunho em um artefato de arquitetura textual operacional, com parâmetros de intenção, mapa de seções, contratos de seção, sequência tipológica de parágrafos, dependências, evidências, transições, riscos e handoff para redação.
---

# Architect Text

## Missão

Converta a intenção do texto em uma **arquitetura funcional de leitura**. A skill não organiza apenas tópicos: ela define que transformação o texto precisa produzir no leitor e quais operações de seção e parágrafo são necessárias, em que ordem, para realizar essa transformação.

A unidade básica de planejamento paragrafal é a tipologia de `design-paragraphs`. `architect-text` escolhe **quais operações paragrafais precisam existir e onde**; `design-paragraphs` executa ou refatora cada operação no nível local.

## Quando usar

Use quando:

- existe um objetivo, tema, briefing, material de pesquisa, template ou rascunho, mas a estrutura ainda precisa ser projetada;
- o texto já possui seções, mas sua progressão temática ou paragrafal é arbitrária;
- é necessário transformar requisitos e conteúdo obrigatório em uma sequência de leitura;
- a redação precisa de um artefato de arquitetura antes de começar;
- um texto precisa ser reestruturado sem ainda entrar na redação final.

Se o objetivo ainda estiver indefinido a ponto de não ser possível identificar o motivo textual, use `plan-content` primeiro.

## Entradas

Aceite como entrada qualquer combinação de:

- pedido do usuário;
- briefing;
- template obrigatório;
- tópicos ou outline;
- rascunho existente;
- fontes/evidências já reunidas;
- requisitos institucionais, acadêmicos ou técnicos;
- restrições de extensão, público ou suporte.

Não exija formulário completo quando os parâmetros puderem ser inferidos do contexto.

## Etapa 1 — Colete o motivo textual

Use [`references/textual-motive.md`](references/textual-motive.md) para coletar ou inferir os parâmetros que governam a arquitetura.

O núcleo mínimo é:

1. **objeto textual**;
2. **ato comunicativo dominante**;
3. **transformação esperada do leitor**;
4. **pergunta, tese, decisão ou tarefa central**;
5. **público primário**;
6. **ação/decisão esperada**;
7. **gênero/artefato de destino**;
8. **regime de evidência**;
9. **escopo e fora de escopo**;
10. **conteúdo obrigatório e restrições**;
11. **riscos de interpretação**;
12. **densidade/extensão esperada**.

Pergunte apenas quando uma ausência alterar materialmente a estrutura e não puder ser inferida com segurança. Caso contrário, registre a hipótese no artefato e prossiga.

## Etapa 2 — Formule a promessa de leitura

Converta o motivo em uma transformação explícita:

`estado inicial do leitor → operações necessárias → estado final esperado`

Produza também uma **frase de controle da arquitetura**, por exemplo:

`partir do problema observado, estabelecer suas causas, comparar alternativas segundo critérios explícitos e conduzir a uma recomendação qualificada.`

Toda seção e todo parágrafo planejado deve contribuir para essa frase.

## Etapa 3 — Escolha o padrão macro por motivo

Consulte [`references/motive-to-paragraph-patterns.md`](references/motive-to-paragraph-patterns.md).

Use o ato comunicativo dominante para obter uma sequência-base e adapte-a segundo:

- gênero;
- evidência disponível;
- nível de controvérsia;
- risco de interpretação;
- conteúdo obrigatório;
- extensão;
- conhecimento prévio do público.

Não trate os padrões como templates rígidos. A arquitetura deve ser justificável pelo motivo textual.

## Etapa 4 — Projete seções por função

Uma seção não existe porque “esse assunto precisa aparecer”; ela existe porque precisa produzir uma mudança no leitor.

Para cada seção defina:

- pergunta que responde;
- função macro;
- estado de entrada;
- estado de saída;
- evidência necessária;
- dependências;
- operações paragrafais previstas;
- ponte para a seção seguinte;
- critério de aceite.

Elimine ou funda seções temáticas que não tenham saída funcional própria.

## Etapa 5 — Construa a matriz paragrafal tipológica

Use as 18 tipologias de [`../design-paragraphs/references/paragraph-typology.md`](../design-paragraphs/references/paragraph-typology.md):

1. abertura de enquadramento;
2. tese ou proposição;
3. definição ou conceituação;
4. explicação causal;
5. sustentação evidencial;
6. exemplificação ou ilustração;
7. classificação ou enumeração analítica;
8. comparação ou analogia;
9. contraste ou concessão;
10. refutação ou objeção–resposta;
11. problema–resposta;
12. descrição analítica;
13. narrativa ou evento;
14. procedimental ou instrucional;
15. transição ou ponte;
16. síntese ou integração;
17. implicação ou recomendação;
18. fechamento ou conclusão local.

Para cada parágrafo, atribua um ID estável `Sx.Py` e registre:

- tipologia dominante;
- missão em formato verbo + objeto;
- âncora;
- núcleo previsto;
- desenvolvimento necessário;
- evidência/insumo;
- virada ou limite quando aplicável;
- pouso/saída;
- relação lógica com o parágrafo anterior;
- dependência do próximo movimento;
- critério de aceite;
- exemplar `CL-*` somente quando sua eficácia estrutural justificar consulta.

Não redija o parágrafo final nesta etapa.

## Etapa 6 — Verifique dependências

Modele o texto como uma cadeia de dependências argumentativas.

Exemplos:

- uma comparação depende da definição prévia dos critérios;
- uma recomendação depende do diagnóstico + evidência + avaliação das alternativas;
- uma refutação depende de uma objeção apresentada de forma justa;
- uma explicação causal depende de evidência suficiente para não transformar correlação em causa;
- uma síntese depende de elementos já estabelecidos.

Se um parágrafo depender de uma premissa ainda não construída, reordene a arquitetura.

## Etapa 7 — Faça o plano de evidências

Associe evidências a operações e afirmações previstas.

Para cada evidência identifique:

- o que sustenta;
- onde será consumida;
- se está disponível;
- se é bloqueante;
- sua natureza: fato, dado, norma, literatura, observação, inferência, hipótese ou opinião.

Não deixe evidência órfã nem parágrafo de sustentação sem fonte/insumo previsto.

Quando causalidade, inferência ou força epistêmica forem materialmente relevantes, prepare handoff para `write-with-evidence`.

## Etapa 8 — Projete transições e ritmo

Defina a relação semântica entre blocos:

- continuação;
- especificação;
- causa;
- consequência;
- contraste;
- concessão;
- mudança de escala;
- síntese;
- transição de etapa;
- implicação.

Não prescreva conectores superficiais por padrão. Planeje **por que** o texto muda de operação.

Calibre ritmo marcando:

- pontos de alta densidade;
- trechos de exemplificação/desaceleração;
- decisões ou viradas que pedem parágrafos mais curtos;
- causalidades ou condicionais que precisam de desenvolvimento maior;
- conteúdo que funciona melhor como lista, tabela, figura ou outro artefato.

## Etapa 9 — Consulte exemplares clássicos de forma seletiva

A arquitetura pode recomendar os assets de [`../design-paragraphs/assets/classic-exemplars.md`](../design-paragraphs/assets/classic-exemplars.md) quando a tipologia possuir eficácia alta ou média para o caso.

O exemplar serve para abstrair sequência estrutural — nunca para impor voz, léxico, ornamentação, posição política ou premissa histórica ao texto-alvo.

Registre apenas o ID `CL-*` na matriz paragrafal; a consulta detalhada fica para `design-paragraphs` durante a execução local.

## Etapa 10 — Gere o artefato de arquitetura textual

Use [`templates/text-architecture-artifact.md`](templates/text-architecture-artifact.md) como contrato de saída.

O artefato deve conter, proporcionalmente à complexidade:

1. identificação;
2. cartão do motivo textual;
3. promessa de leitura;
4. movimento macro;
5. mapa e contratos de seções;
6. matriz paragrafal tipológica;
7. grafo de dependências argumentativas;
8. plano de evidências;
9. plano de transições;
10. ritmo e densidade;
11. lacunas, conflitos e riscos;
12. handoff para redação;
13. critério de prontidão.

Em tarefas pequenas, comprima o artefato sem eliminar os elementos estruturais necessários.

## Etapa 11 — Execute QA da arquitetura

Antes de declarar a arquitetura pronta, confirme:

- o motivo textual explica por que o texto existe;
- a transformação do leitor está explícita;
- cada seção produz uma saída necessária;
- cada parágrafo possui uma tipologia dominante;
- a sequência paragrafal é justificável por dependência lógica;
- conteúdo obrigatório possui posição funcional;
- evidências possuem consumidores identificados;
- não existem conclusões antes das premissas;
- transições possuem relação semântica;
- riscos e lacunas estão classificados;
- a redação pode começar sem precisar inventar a estrutura durante a escrita.

## Saída esperada

Por padrão, entregue o **Artefato de Arquitetura Textual**, e não apenas um outline.

Quando útil, inclua também um diagnóstico curto das principais decisões estruturais tomadas.

## Handoff para `design-paragraphs`

O artefato deve permitir que `design-paragraphs` receba cada contrato `Sx.Py` e execute a construção/refatoração local usando:

- tipologia dominante;
- missão;
- âncora;
- núcleo;
- desenvolvimento;
- evidência;
- virada;
- pouso;
- critério de aceite;
- exemplar estrutural opcional.

Se, durante a redação, um parágrafo não puder cumprir seu contrato sem mudar funções entre seções, o problema retorna a `architect-text`.

## Limites e handoffs

- **Direção editorial ainda indefinida:** `plan-content`.
- **Construção/refatoração local de parágrafos:** `design-paragraphs`.
- **Evidência, causalidade, inferência e incerteza:** `write-with-evidence`.
- **Tom e força argumentativa:** `calibrate-rhetoric`.
- **Legibilidade:** `improve-accessible-writing`.
- **QA editorial final:** `review-editorial-quality`.

Não invente fatos, fontes, requisitos ou intenção do autor. Não transforme uma arquitetura em texto final quando o pedido for apenas de estruturação. Não use tipologia paragrafal como fim em si: cada operação precisa existir por causa do motivo textual e da transformação de leitura pretendida.
