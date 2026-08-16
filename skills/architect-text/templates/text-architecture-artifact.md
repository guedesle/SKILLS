# Artefato de Arquitetura Textual

> Este template é a saída canônica de `architect-text`. Ele descreve **como o texto deve ser construído**, sem redigir automaticamente o texto final.

## 1. Identificação

- **Título provisório:**
- **Gênero/artefato:**
- **Versão da arquitetura:**
- **Data:**
- **Fonte do briefing/material de entrada:**

## 2. Cartão do motivo textual

- **Objeto:**
- **Ato comunicativo dominante:**
- **Atos secundários:**
- **Transformação do leitor:** `estado inicial → estado desejado`
- **Centro lógico:** pergunta / tese / decisão / tarefa
- **Público primário:**
- **Conhecimento prévio presumido:**
- **Ação/decisão esperada:**
- **Relação de autoridade:**
- **Contexto de circulação:**
- **Regime de evidência:**
- **Nível de controvérsia/incerteza:**
- **Escopo:**
- **Fora de escopo:**
- **Conteúdo obrigatório:**
- **Restrições:**
- **Riscos de interpretação:**
- **Extensão/densidade:**
- **Hipóteses assumidas:**
- **Lacunas bloqueantes:**

## 3. Promessa de leitura

**Ao terminar o texto, o leitor deverá:**

1.
2.
3.

**Frase de controle da arquitetura:**

> [Uma frase que resume a progressão: “partir de X, estabelecer Y, demonstrar Z e conduzir a W”.]

## 4. Movimento macro

Descreva a progressão em operações, não apenas em tópicos.

```text
estado inicial do leitor
  ↓
[operação macro 1]
  ↓
[operação macro 2]
  ↓
[operação macro 3]
  ↓
estado final esperado
```

## 5. Mapa de seções

| ID | Seção | Função macro | Entrada | Saída | Evidência necessária | Dependência | Ponte para próxima seção |
|---|---|---|---|---|---|---|---|
| S1 | | | | | | | |

### Contrato de seção

Para cada seção, registre:

- **ID / título:**
- **Pergunta que a seção responde:**
- **Mudança que deve produzir no leitor:**
- **O que já pode ser presumido na entrada:**
- **O que precisa estar estabelecido na saída:**
- **Evidência mínima:**
- **Operações paragrafais previstas:**
- **Risco estrutural principal:**
- **Critério de aceite:**

## 6. Matriz paragrafal

Use IDs estáveis `Sx.Py`.

| ID | Tipologia dominante | Missão do parágrafo | Núcleo previsto | Desenvolvimento necessário | Evidência/insumo | Virada/limite | Pouso/saída | Relação com anterior | Próximo passo |
|---|---|---|---|---|---|---|---|---|---|
| S1.P1 | abertura de enquadramento | | | | | | | início | |

### Contrato de cada parágrafo

Para cada parágrafo planejado, quando necessário:

- **ID:**
- **Tipologia dominante:** uma das 18 tipologias de `design-paragraphs`;
- **Função secundária:** somente se servir ao núcleo;
- **Missão:** verbo + objeto (`definir X`, `comparar A e B segundo C`, `sustentar Y com Z`);
- **Âncora:** de onde parte;
- **Núcleo:** o que precisa ficar estabelecido;
- **Desenvolvimento:** razões, evidências, detalhes, etapas ou distinções;
- **Virada:** contraste, limite ou consequência quando existir;
- **Pouso:** o que entrega ao parágrafo seguinte;
- **Evidência/insumo obrigatório:**
- **Risco de falha:** duplicação, salto causal, abstração, falta de fonte etc.;
- **Critério de aceite:** condição verificável para considerar o parágrafo estruturalmente pronto;
- **Exemplar `CL-*`:** somente se a eficácia da tipologia justificar consulta; nunca como imitação estilística.

## 7. Grafo de dependências argumentativas

Registre dependências que não podem ser violadas pela redação.

Exemplo:

```text
P1 define X
P2 depende de X para classificar A/B
P3 depende da classificação para comparar
P4 depende da comparação + evidência E1 para recomendar Y
```

Use este bloco para impedir conclusões prematuras e evidência órfã.

## 8. Plano de evidências

| Evidência ID | Afirmação/operação que sustenta | Fonte disponível? | Status | Parágrafos consumidores | Risco |
|---|---|---|---|---|---|
| E1 | | sim/não | disponível/a obter/bloqueante | | |

Distinguir sempre:

- fato;
- dado;
- inferência;
- hipótese;
- opinião/recomendação;
- norma ou requisito.

## 9. Plano de transições

| De | Para | Relação lógica | Como a transição deve funcionar |
|---|---|---|---|
| S1.P1 | S1.P2 | especificação | O enquadramento abre a necessidade de definir X |

Não prescreva conectores lexicalmente sem necessidade. A arquitetura deve especificar a **relação semântica**.

## 10. Ritmo e densidade

- **Trechos de maior densidade:**
- **Trechos de desaceleração/exemplificação:**
- **Parágrafos que devem ser curtos por decisão/virada:**
- **Parágrafos que podem ser mais desenvolvidos por causalidade/condicionais:**
- **Pontos adequados para listas/tabelas/figuras em vez de parágrafos:**

## 11. Lacunas, conflitos e riscos

### Bloqueantes

- [ ]

### Não bloqueantes / hipóteses aceitas

- [ ]

### Riscos de arquitetura

- repetição;
- seção órfã;
- conclusão antes da evidência;
- excesso de contexto;
- mudança de escala sem ponte;
- tipologia inadequada;
- duas operações dominantes no mesmo parágrafo;
- conteúdo obrigatório sem posição funcional;
- evidência sem consumidor;
- recomendação sem critério.

## 12. Handoff para redação

### Ordem de execução

1.
2.
3.

### Regras para `design-paragraphs`

- respeitar a tipologia dominante e o contrato `Sx.Py`;
- consultar `paragraph-typology.md` para construção/refatoração;
- usar exemplares clássicos somente quando a matriz de eficácia recomendar;
- preservar núcleo, evidência, qualificadores e pouso;
- retornar a `architect-text` se a redação revelar necessidade de mover funções entre seções.

### Handoffs adicionais

- `write-with-evidence` para causalidade, inferência e força epistêmica;
- `calibrate-rhetoric` para postura e persuasão;
- `improve-accessible-writing` para leitura e linguagem simples;
- `review-editorial-quality` para QA final.

## 13. Critério de prontidão da arquitetura

A arquitetura está pronta quando:

- [ ] o motivo textual está suficientemente definido;
- [ ] cada seção produz uma mudança explícita no estado do leitor;
- [ ] cada parágrafo possui uma função dominante necessária;
- [ ] a ordem paragrafal é justificável por dependência lógica;
- [ ] evidências possuem consumidores identificados;
- [ ] transições possuem relação semântica definida;
- [ ] não existem conteúdos obrigatórios órfãos;
- [ ] riscos e lacunas estão classificados;
- [ ] o texto pode ser redigido sem o redator precisar inventar a arquitetura durante a escrita.
