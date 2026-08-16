---
name: design-paragraphs
description: Projete e refatore parágrafos pela função que precisam cumprir, pela ideia central, pelo desenvolvimento necessário, pelas evidências e pela ligação com os parágrafos vizinhos.
---

# Design Paragraphs

## Objetivo

Tratar cada parágrafo como uma **parte do texto com uma função clara**.

Cada parágrafo deve:

- cumprir uma função principal;
- deixar uma ideia central identificável;
- desenvolver essa ideia com o material necessário;
- preservar evidências, ressalvas e limites;
- ligar-se de forma coerente ao que veio antes e ao que vem depois.

Quando o problema exigir mudar a função de seções inteiras ou reorganizar vários parágrafos, encaminhe para `architect-text`.

## Regra de linguagem

Use nomes que expliquem diretamente o que cada elemento significa.

Prefira:

- **ponto de partida** em vez de “âncora”;
- **ideia central** em vez de “núcleo”;
- **como desenvolver** em vez de usar “desenvolvimento” como rótulo abstrato;
- **contraste, ressalva, limite ou consequência** em vez de “virada”;
- **como encerrar e ligar ao próximo** em vez de “pouso”;
- **função do parágrafo** em vez de “tipologia dominante”, quando o contexto não exigir o termo técnico;
- **especificação do parágrafo** em vez de “contrato do parágrafo”.

Os nomes técnicos podem permanecer nas referências para rastreabilidade, mas não devem ser a linguagem principal apresentada ao usuário.

## Entradas úteis

- parágrafo ou conjunto de parágrafos;
- finalidade do texto;
- objetivo da seção;
- função esperada do parágrafo;
- público;
- ideia, requisito ou conclusão que precisa ser preservada;
- evidências e ressalvas que não podem ser perdidas;
- nível de intervenção permitido: diagnóstico, reordenação, divisão, união ou reescrita.

## Especificação de um parágrafo

Antes de escrever ou refatorar, identifique quando necessário:

1. **Função do parágrafo** — o que ele precisa fazer;
2. **Ponto de partida** — o que o leitor já sabe ou o que veio antes;
3. **Ideia central** — o que precisa ficar claro;
4. **Como desenvolver** — razões, evidências, detalhes, exemplos, etapas ou distinções necessárias;
5. **Contraste, ressalva, limite ou consequência** — quando houver mudança lógica relevante;
6. **Como encerrar e ligar ao próximo** — que conclusão local ou necessidade deixa preparada.

Não force todos os campos. Use apenas os que ajudam a tornar a lógica explícita.

## Tipos de parágrafo por função

Use a referência [`references/paragraph-typology.md`](references/paragraph-typology.md). Na apresentação ao usuário, prefira estes nomes:

1. **apresentar o assunto e o recorte**;
2. **declarar ou defender uma ideia principal**;
3. **definir um conceito**;
4. **explicar causa e efeito**;
5. **sustentar uma afirmação com evidências**;
6. **dar um exemplo**;
7. **organizar informações em categorias**;
8. **comparar ou usar uma analogia**;
9. **mostrar contraste ou fazer uma ressalva**;
10. **apresentar uma objeção e responder**;
11. **apresentar um problema e uma resposta**;
12. **descrever de modo analítico**;
13. **relatar acontecimentos em sequência**;
14. **ensinar um procedimento**;
15. **ligar uma parte à seguinte**;
16. **integrar ideias e produzir uma síntese**;
17. **mostrar uma implicação ou recomendar uma ação**;
18. **encerrar uma parte do texto**.

Se duas funções principais competirem no mesmo parágrafo, divida ou reorganize.

## Procedimento

### 1. Entenda a função do parágrafo dentro da seção

Pergunte: **o que este parágrafo precisa fazer exatamente aqui?**

Compare a função esperada com o que o texto atual realmente faz.

### 2. Escreva a função em linguagem de ação

Use verbo + objeto:

- `definir X`;
- `explicar como A produz B`;
- `sustentar Y com a evidência Z`;
- `comparar A e B segundo o critério C`;
- `reconhecer a ressalva D e preservar a conclusão E`;
- `ligar o diagnóstico à recomendação`.

Se não for possível formular isso com clareza, o parágrafo provavelmente não tem função bem definida.

### 3. Identifique a ideia central

Resuma em uma frase o que precisa ficar estabelecido ao terminar o parágrafo.

Se houver duas ideias centrais independentes, considere dividir.

### 4. Organize o desenvolvimento

Consulte a receita específica em [`references/paragraph-typology.md`](references/paragraph-typology.md).

Aplique intervenções diretas:

- antecipe a ideia central quando ela aparece tarde demais;
- mova contexto secundário para depois da ideia principal;
- coloque a evidência junto da afirmação que ela sustenta;
- explique mecanismos causais em vez de depender de conectores vagos;
- apresente a ressalva antes de mostrar por que a conclusão principal ainda se sustenta;
- apresente objeções de forma justa antes de responder;
- use um único critério ao organizar categorias;
- transforme instrução narrativa em pré-requisito → ação → verificação;
- remova transições que apenas anunciam o próximo assunto;
- em sínteses, mostre a relação entre os elementos em vez de apenas repeti-los.

### 5. Decida se deve manter, dividir ou unir

**Divida** quando houver:

- duas ideias principais;
- duas mudanças fortes de direção;
- evidências de objetos diferentes;
- mudança de função dentro do mesmo parágrafo.

**Una** quando dois parágrafos curtos executarem partes inseparáveis da mesma função.

**Mantenha** quando o parágrafo já tiver uma função clara e só precisar de melhoria interna.

### 6. Verifique a ligação com os parágrafos vizinhos

A relação deve ser identificável, por exemplo:

- continuação;
- detalhamento;
- causa;
- consequência;
- contraste;
- ressalva;
- exemplo;
- mudança de escala;
- síntese;
- passagem para nova etapa.

Prefira continuidade lógica real a conectores artificiais.

### 7. Ajuste extensão e ritmo

A extensão deve acompanhar a complexidade da função.

Use parágrafos mais curtos para decisões, contrastes e conclusões importantes. Permita maior desenvolvimento quando for necessário explicar causalidade, condições, evidências ou exceções.

Corte:

- repetição sem ganho;
- frase que apenas repete a ideia central;
- detalhe que não ajuda a função do parágrafo;
- comentário lateral que pertence a outra parte;
- conclusão mais forte que a evidência permite.

### 8. Use exemplos clássicos apenas quando ajudarem a estrutura

Consulte [`assets/classic-exemplars.md`](assets/classic-exemplars.md).

Quando indicar um exemplo ao usuário, prefira **autor + obra + trecho/função relevante**, e não apenas um código como `CL-09`.

Use o clássico para observar **ordem das ideias e construção do raciocínio**, nunca para copiar:

- vocabulário antigo;
- pontuação de época;
- voz autoral;
- ornamentação;
- posições políticas históricas;
- premissas científicas desatualizadas.

### 9. Preserve precisão

Não altere fatos para melhorar fluidez. Não retire qualificadores necessários. Não transforme:

- associação em causa;
- hipótese em fato;
- exemplo em prova;
- analogia em demonstração.

Quando isso for relevante, use `write-with-evidence`.

### 10. Revise o parágrafo

Confirme:

- função principal clara;
- ideia central identificável;
- desenvolvimento suficiente e pertinente;
- nenhuma segunda ideia principal competindo;
- ligação compreensível com o parágrafo anterior;
- encerramento que conclui ou prepara o seguinte;
- extensão adequada à função;
- fatos, evidências, ressalvas e requisitos preservados;
- exemplo clássico, se usado, aplicado apenas como referência estrutural.

## Saída esperada

Quando o usuário pedir análise, produza somente o nível de detalhe necessário:

- função atual do parágrafo;
- função recomendada;
- ideia central;
- problema encontrado;
- recomendação de manter, dividir, unir ou reordenar;
- instrução específica de refatoração;
- versão revisada, quando solicitada;
- exemplo estrutural opcional identificado de forma compreensível.

Não imponha tabelas ou códigos internos em tarefas simples.

## Integração com `architect-text`

Quando receber um parágrafo planejado por `architect-text`, use:

- identificação legível, como **Seção 2 · Parágrafo 4**;
- função do parágrafo;
- objetivo específico;
- ponto de partida;
- ideia central;
- como desenvolver;
- evidência necessária;
- contraste, ressalva, limite ou consequência;
- forma de encerrar e ligar ao próximo;
- critério de aceite.

## Limites e próximas etapas

- **Estrutura de seções e ordem global:** `architect-text`.
- **Evidência, causalidade, inferência e incerteza:** `write-with-evidence`.
- **Tom e força argumentativa:** `calibrate-rhetoric`.
- **Clareza e linguagem simples:** `improve-accessible-writing`.
- **Revisão editorial ampla:** `review-editorial-quality`.

Não use jargão como sinal de rigor. Se um termo não for necessário para executar a tarefa, substitua-o por uma expressão que explique diretamente a função.
