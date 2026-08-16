---
name: architect-text
description: Transforme finalidade, briefing, tópicos, outline ou rascunho em um plano detalhado da estrutura do texto, com sequência de seções, função de cada parágrafo, dependências entre ideias, evidências, ligações, riscos e instruções para a redação.
---

# Architect Text

## Objetivo

Transformar **por que o texto precisa existir** em um plano claro de **como ele deve ser organizado**.

A skill não deve apenas listar assuntos. Ela deve explicar:

- o que o texto precisa fazer;
- o que o leitor deve compreender, decidir ou conseguir fazer ao final;
- que sequência de seções conduz a esse resultado;
- que função cada parágrafo deve cumprir;
- quais ideias e evidências precisam aparecer antes de outras;
- como cada parte se liga à seguinte.

`architect-text` decide **quais parágrafos precisam existir e em que ordem**. `design-paragraphs` recebe esse plano e constrói ou refatora cada parágrafo.

## Regra de linguagem

Use nomes autoexplicativos. Não exponha abreviações, códigos opacos ou metáforas técnicas quando um nome direto funcionar melhor.

Prefira:

- **finalidade do texto** em vez de “motivo textual”;
- **função principal do texto** em vez de “ato comunicativo dominante”;
- **resultado esperado da leitura** em vez de “transformação do leitor”;
- **sequência lógica do texto** em vez de “movimento macro”;
- **objetivo e requisitos da seção** em vez de “contrato de seção”;
- **plano de parágrafos** em vez de “matriz paragrafal”;
- **dependências entre ideias** em vez de “grafo de dependências argumentativas”;
- **instruções para a próxima etapa** em vez de “handoff”.

Para identificar um parágrafo, use um identificador legível como `secao-02-paragrafo-04` e, na apresentação ao usuário, escreva **Seção 2 · Parágrafo 4**.

## Quando usar

Use quando:

- existe um tema, objetivo, briefing, template, material de pesquisa ou rascunho, mas a organização do texto ainda precisa ser projetada;
- o texto já tem seções, porém a ordem das ideias ou dos parágrafos parece arbitrária;
- requisitos obrigatórios precisam ser distribuídos em uma sequência coerente;
- a redação precisa de um plano estrutural antes de começar;
- um texto precisa ser reorganizado sem ainda entrar na redação final.

Se ainda não for possível dizer claramente **para que o texto existe**, use `plan-content` primeiro.

## Etapa 1 — Defina a finalidade do texto

Use [`references/textual-motive.md`](references/textual-motive.md) para coletar ou inferir as informações necessárias.

O mínimo é:

1. **assunto e recorte:** sobre o que exatamente o texto tratará;
2. **função principal:** informar, explicar, analisar, defender uma ideia, recomendar, instruir, documentar, comparar, narrar ou sintetizar;
3. **resultado esperado da leitura:** o que o leitor deve compreender, decidir ou saber fazer ao final;
4. **questão central:** pergunta, ideia a defender, decisão a apoiar ou tarefa a ensinar;
5. **público principal:** quem lerá e o que já sabe;
6. **ação ou decisão esperada:** quando houver;
7. **tipo de documento:** relatório, nota técnica, artigo, manual, parecer, capítulo etc.;
8. **fontes e evidências necessárias:** que tipo de suporte sustenta o texto;
9. **escopo:** o que entra e o que fica de fora;
10. **conteúdo obrigatório:** requisitos, tópicos, dados ou mensagens que precisam aparecer;
11. **restrições e riscos de interpretação:** o que não pode ser perdido, antecipado ou entendido de modo errado;
12. **extensão e nível de detalhe:** quanto desenvolvimento o texto comporta.

Não transforme essa etapa em interrogatório. Pergunte apenas quando uma informação ausente realmente mudar a estrutura e não puder ser inferida com segurança.

## Etapa 2 — Declare o resultado da leitura

Escreva de forma direta:

`o que o leitor sabe/pensa/consegue fazer antes → o que deve saber/pensar/conseguir fazer depois`

Depois resuma a sequência necessária em uma frase, por exemplo:

`apresentar o problema, explicar suas causas, comparar alternativas por critérios explícitos e terminar com uma recomendação condicionada às evidências.`

Essa frase serve para verificar se cada seção e cada parágrafo realmente têm função.

## Etapa 3 — Escolha uma sequência inicial adequada à finalidade

Consulte [`references/motive-to-paragraph-patterns.md`](references/motive-to-paragraph-patterns.md).

Use a função principal do texto para escolher uma sequência inicial e adapte-a conforme:

- tipo de documento;
- evidências disponíveis;
- nível de controvérsia;
- riscos de interpretação;
- conteúdo obrigatório;
- extensão;
- conhecimento prévio do público.

A sequência é uma hipótese de trabalho, não um molde rígido.

## Etapa 4 — Planeje as seções

Cada seção deve existir porque cumpre uma função necessária.

Para cada seção registre:

- **título provisório**;
- **pergunta que responde**;
- **objetivo da seção**;
- **o que o leitor já precisa saber ao entrar**;
- **o que deve estar estabelecido ao sair**;
- **evidências necessárias**;
- **parágrafos previstos e suas funções**;
- **o que depende dessa seção depois**;
- **como a seção prepara a próxima**;
- **critério para considerar a seção pronta**.

Elimine ou una seções que apenas agrupam assunto, mas não produzem nenhum avanço real.

## Etapa 5 — Monte o plano de parágrafos

Use os 18 tipos funcionais de [`../design-paragraphs/references/paragraph-typology.md`](../design-paragraphs/references/paragraph-typology.md).

Para cada parágrafo, use um identificador autoexplicativo, por exemplo `secao-02-paragrafo-04`, e registre:

- **função do parágrafo:** o que ele faz no texto;
- **objetivo específico:** verbo + objeto, como `definir X`, `comparar A e B segundo C` ou `sustentar Y com a evidência Z`;
- **ponto de partida:** o que já foi estabelecido antes;
- **ideia central:** o que precisa ficar claro nesse parágrafo;
- **como desenvolver:** razões, evidências, detalhes, etapas ou distinções necessárias;
- **evidência ou material necessário:** fonte, dado, norma, exemplo ou outro insumo;
- **contraste, ressalva, limite ou consequência:** somente quando realmente fizer parte da lógica;
- **como encerrar e ligar ao próximo:** qual conclusão local ou pergunta deixa preparada;
- **relação com o parágrafo anterior:** continuação, causa, contraste, exemplo, consequência etc.;
- **o que depende deste parágrafo depois**;
- **critério para considerar o parágrafo estruturalmente pronto**;
- **exemplo clássico opcional:** somente quando ajudar a compreender a estrutura, identificado por autor e obra, e não apenas por código interno.

Não escreva o parágrafo final nesta etapa, a menos que o usuário também peça redação.

## Etapa 6 — Confira as dependências entre ideias

Pergunte, para cada parte:

- esta ideia depende de alguma definição anterior?
- esta comparação depende de critérios já apresentados?
- esta recomendação depende de diagnóstico, evidências e avaliação de alternativas?
- esta resposta depende de uma objeção previamente explicada?
- esta conclusão depende de fatos que ainda não apareceram?

Se uma conclusão vier antes do que a sustenta, reordene o plano.

## Etapa 7 — Planeje as evidências

Para cada fonte, dado, norma, observação ou inferência, registre:

- o que ela sustenta;
- em qual parágrafo será usada;
- se já está disponível;
- se sua ausência impede a redação;
- que tipo de evidência é.

Não deixe evidência sem finalidade nem afirmação importante sem suporte previsto.

Quando houver causalidade, inferência ou incerteza relevante, encaminhe essa parte a `write-with-evidence`.

## Etapa 8 — Planeje as ligações entre partes

Para cada mudança de parágrafo ou seção, identifique a relação real:

- continuação;
- detalhamento;
- causa;
- consequência;
- contraste;
- ressalva;
- exemplo;
- mudança de escala;
- síntese;
- passagem para uma nova etapa;
- implicação prática.

Não planeje conectores decorativos. Planeje **por que a próxima parte vem depois da anterior**.

## Etapa 9 — Ajuste extensão e ritmo

Marque:

- partes que precisam de maior desenvolvimento;
- decisões, contrastes e conclusões que devem ser mais curtas e diretas;
- pontos em que um exemplo facilita a compreensão;
- conteúdos que funcionam melhor como lista, tabela, figura ou procedimento do que como parágrafo corrido.

## Etapa 10 — Gere o Plano de Arquitetura do Texto

Use [`templates/text-architecture-artifact.md`](templates/text-architecture-artifact.md).

O plano deve conter, conforme a complexidade:

1. identificação do documento;
2. finalidade do texto;
3. resultado esperado da leitura;
4. sequência lógica do texto;
5. mapa de seções;
6. plano de parágrafos;
7. dependências entre ideias;
8. plano de evidências;
9. ligações entre parágrafos e seções;
10. orientação de extensão e ritmo;
11. lacunas, conflitos e riscos;
12. instruções para a redação;
13. critérios para considerar a arquitetura pronta.

Em tarefas pequenas, reduza a quantidade de campos, mas não perca as decisões estruturais importantes.

## Etapa 11 — Revise a arquitetura

Antes de declarar o plano pronto, confirme:

- a finalidade do texto explica por que ele existe;
- o resultado esperado da leitura está claro;
- cada seção tem objetivo próprio;
- cada parágrafo tem uma função dominante necessária;
- a ordem das ideias pode ser explicada;
- o conteúdo obrigatório tem lugar definido;
- as evidências têm uso definido;
- nenhuma conclusão aparece antes do que a sustenta;
- as ligações entre partes estão claras;
- riscos e lacunas estão registrados;
- a redação pode começar sem que o redator precise inventar a estrutura enquanto escreve.

Use também [`references/architecture-qa.md`](references/architecture-qa.md).

## Saída esperada

Por padrão, entregue o **Plano de Arquitetura do Texto**.

Não use códigos ou rótulos internos como linguagem principal da resposta. Sempre prefira nomes que possam ser compreendidos sem consultar um glossário.

## Entrega para `design-paragraphs`

Para cada parágrafo planejado, `design-paragraphs` deve receber:

- identificação legível;
- função do parágrafo;
- objetivo específico;
- ponto de partida;
- ideia central;
- desenvolvimento necessário;
- evidências;
- contraste, ressalva, limite ou consequência, quando houver;
- forma de encerramento e ligação com o próximo;
- critério de aceite;
- exemplo estrutural opcional.

Se, durante a redação, um parágrafo só puder funcionar mudando a função de seções inteiras, devolva o problema a `architect-text`.

## Limites e próximas etapas

- **Objetivo do conteúdo ainda indefinido:** `plan-content`.
- **Construção ou refatoração de cada parágrafo:** `design-paragraphs`.
- **Evidência, causalidade, inferência e incerteza:** `write-with-evidence`.
- **Tom e força argumentativa:** `calibrate-rhetoric`.
- **Legibilidade:** `improve-accessible-writing`.
- **Revisão editorial final:** `review-editorial-quality`.

Não invente fatos, fontes, requisitos ou intenção do autor. Não use terminologia especializada quando uma expressão direta e autoexplicativa transmitir a mesma decisão com mais clareza.
