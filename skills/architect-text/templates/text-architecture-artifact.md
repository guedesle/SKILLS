# Plano de Arquitetura do Texto

> Esta é a saída padrão de `architect-text`. O documento descreve **como o texto deve ser organizado**, sem necessariamente redigir o texto final.

## 1. Identificação

- **Título provisório:**
- **Tipo de documento:**
- **Versão do plano:**
- **Data:**
- **Material de entrada:**

## 2. Finalidade do texto

- **Assunto e recorte:**
- **Função principal do texto:** informar / explicar / analisar / defender uma ideia / recomendar / instruir / documentar / comparar / narrar / sintetizar
- **Funções secundárias:**
- **Resultado esperado da leitura:** `antes → depois`
- **Questão central:** pergunta / ideia a defender / decisão / tarefa
- **Público principal:**
- **Conhecimento prévio presumido:**
- **O que o leitor deve poder fazer ao final:**
- **Relação entre autor e leitor:**
- **Onde e como o texto será usado:**
- **Tipos de evidência necessários:**
- **Nível de controvérsia ou incerteza:**
- **Escopo:**
- **Fora de escopo:**
- **Conteúdo obrigatório:**
- **Restrições:**
- **Riscos de interpretação:**
- **Extensão e nível de detalhe:**
- **Hipóteses assumidas:**
- **Informações que faltam e impedem avançar:**

## 3. Resultado esperado da leitura

**Ao terminar o texto, o leitor deverá:**

1.
2.
3.

**Resumo da sequência necessária:**

> [Exemplo: “apresentar o problema, explicar suas causas, comparar alternativas segundo critérios explícitos e terminar com uma recomendação condicionada às evidências”.]

## 4. Sequência lógica do texto

Descreva a progressão em ações claras:

```text
situação inicial do leitor
  ↓
[o que a primeira parte precisa fazer]
  ↓
[o que a segunda parte precisa fazer]
  ↓
[o que a terceira parte precisa fazer]
  ↓
resultado final esperado
```

## 5. Mapa de seções

| Seção | Título provisório | Objetivo | O que precisa estar sabido antes | O que deve ficar estabelecido ao final | Evidências necessárias | O que depende desta seção depois | Como prepara a próxima |
|---|---|---|---|---|---|---|---|
| Seção 1 | | | | | | | |

### Objetivo e requisitos de cada seção

Para cada seção, registre:

- **Seção e título:**
- **Pergunta que responde:**
- **Objetivo:**
- **O que o leitor já precisa saber ao entrar:**
- **O que precisa estar estabelecido ao sair:**
- **Evidências mínimas:**
- **Parágrafos previstos e suas funções:**
- **Principal risco estrutural:**
- **Critério para considerar a seção pronta:**

## 6. Plano de parágrafos

Use identificadores autoexplicativos, por exemplo `secao-01-paragrafo-01`. Na apresentação ao usuário, prefira **Seção 1 · Parágrafo 1**.

| Parágrafo | Função | Objetivo específico | Ideia central | Como desenvolver | Evidência necessária | Contraste/ressalva/limite | Como encerrar e ligar ao próximo | Relação com o anterior | O que vem depois e depende dele |
|---|---|---|---|---|---|---|---|---|---|
| Seção 1 · Parágrafo 1 | apresentar assunto e recorte | | | | | | | início | |

### Especificação de cada parágrafo

Quando necessário, registre:

- **Identificação:**
- **Função do parágrafo:** uma das funções definidas em `design-paragraphs`;
- **Função secundária:** somente quando ajudar a função principal;
- **Objetivo específico:** verbo + objeto, como `definir X`, `comparar A e B segundo C` ou `sustentar Y com Z`;
- **Ponto de partida:** o que já foi estabelecido;
- **Ideia central:** o que precisa ficar claro;
- **Como desenvolver:** razões, evidências, detalhes, etapas ou distinções;
- **Contraste, ressalva, limite ou consequência:** quando houver;
- **Como encerrar e ligar ao próximo:** o que deixa preparado;
- **Evidência ou material obrigatório:**
- **Risco de falha:** repetição, salto causal, abstração excessiva, falta de fonte etc.;
- **Critério para considerar o parágrafo pronto:**
- **Exemplo estrutural opcional:** autor e obra, somente quando realmente útil; nunca como imitação de estilo.

## 7. Dependências entre ideias

Registre as relações que não podem ser quebradas pela redação.

Exemplo:

```text
Seção 1 · Parágrafo 1 define X
Seção 1 · Parágrafo 2 usa X para separar A e B
Seção 1 · Parágrafo 3 compara A e B
Seção 1 · Parágrafo 4 usa a comparação + Evidência 1 para recomendar Y
```

## 8. Plano de evidências

| Evidência | O que sustenta | Está disponível? | Situação | Onde será usada | Risco se faltar |
|---|---|---|---|---|---|
| Evidência 1 | | sim/não | disponível / a obter / impede avançar | | |

Distinguir sempre:

- fato;
- dado;
- inferência;
- hipótese;
- opinião ou recomendação;
- norma ou requisito.

## 9. Ligações entre parágrafos e seções

| De | Para | Relação | Como a ligação deve funcionar |
|---|---|---|---|
| Seção 1 · Parágrafo 1 | Seção 1 · Parágrafo 2 | detalhamento | O primeiro apresenta o problema; o segundo define o conceito necessário para examiná-lo |

Não prescreva conectores por padrão. Descreva a relação lógica real.

## 10. Extensão e ritmo

- **Partes que precisam de maior desenvolvimento:**
- **Pontos em que exemplos ajudam a compreensão:**
- **Parágrafos que devem ser curtos e diretos:**
- **Parágrafos que podem exigir maior desenvolvimento:**
- **Pontos em que lista, tabela ou figura funciona melhor que parágrafo:**

## 11. Lacunas, conflitos e riscos

### Impedem avançar

- [ ]

### Não impedem avançar / hipóteses aceitas

- [ ]

### Riscos de estrutura

- repetição;
- seção sem função clara;
- conclusão antes da evidência;
- contexto excessivo;
- mudança de assunto sem ligação;
- função de parágrafo inadequada;
- duas funções principais competindo no mesmo parágrafo;
- conteúdo obrigatório sem lugar definido;
- evidência sem uso definido;
- recomendação sem critério.

## 12. Instruções para a redação

### Ordem recomendada de execução

1.
2.
3.

### Instruções para `design-paragraphs`

- respeitar a função prevista para cada parágrafo;
- consultar `paragraph-typology.md` para construção ou refatoração;
- preservar ideia central, evidências, ressalvas e ligação com o próximo parágrafo;
- usar exemplos clássicos apenas como referência estrutural quando realmente ajudarem;
- retornar a `architect-text` se a redação revelar necessidade de mover funções entre seções.

### Outras skills que podem ser usadas

- `write-with-evidence` para causalidade, inferência e grau de certeza;
- `calibrate-rhetoric` para tom e força argumentativa;
- `improve-accessible-writing` para clareza e linguagem simples;
- `review-editorial-quality` para revisão final.

## 13. Quando considerar a arquitetura pronta

A arquitetura está pronta quando:

- [ ] a finalidade do texto está clara;
- [ ] o resultado esperado da leitura está definido;
- [ ] cada seção tem um objetivo necessário;
- [ ] cada parágrafo tem uma função principal clara;
- [ ] a ordem das ideias pode ser explicada;
- [ ] as evidências têm lugar e finalidade definidos;
- [ ] as ligações entre partes estão claras;
- [ ] nenhum conteúdo obrigatório ficou sem posição;
- [ ] riscos e lacunas estão registrados;
- [ ] o texto pode ser redigido sem que o redator precise inventar a estrutura durante a escrita.
