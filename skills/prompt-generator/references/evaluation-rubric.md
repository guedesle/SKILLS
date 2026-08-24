# Rubrica de avaliação de prompts

A avaliação deve responder perguntas específicas sobre o comportamento produzido pelo prompt. Use escala ordinal para qualidade e checks binários para invariantes.

## 1. Estrutura SOMA adaptada

Use três princípios:

- **Perguntas específicas:** cada item avalia um comportamento observável.
- **Escala ordinal:** prefira níveis com significado explícito a um simples `bom/ruim`.
- **Cobertura multiaspecto:** avalie dimensões separadas para evitar que um aspecto forte esconda outro fraco.

### Escala padrão 1–5

| Nota | Interpretação |
|---:|---|
| 1 | falha material; objetivo não atendido |
| 2 | atende parcialmente; erro importante ou retrabalho alto |
| 3 | aceitável com ressalvas; pequenas correções necessárias |
| 4 | bom; atende ao contrato com desvios pouco relevantes |
| 5 | excelente; atende integralmente e de forma consistente |

Não use a escala quando a regra é binária. Para `JSON válido`, `campo obrigatório presente`, `ferramenta proibida não chamada` ou outra invariante, use PASS/FAIL.

## 2. Dimensões padrão

### Aderência ao objetivo

Pergunta: a saída resolve exatamente o problema descrito, sem substituir o objetivo por outro mais fácil?

Falhas típicas:
- responde tema adjacente;
- ignora recorte;
- produz explicação quando era necessária decisão/artefato;
- omite parte material do pedido.

### Grounding e correção

Pergunta: afirmações factuais estão sustentadas pelas fontes/dados permitidos e incertezas materiais são tratadas corretamente?

Checks possíveis:
- não inventa dado ausente;
- cita fonte correta quando exigido;
- distingue inferência de fato;
- respeita data de corte/freshness;
- declara contexto insuficiente quando aplicável.

### Completude relevante

Pergunta: todos os elementos necessários ao objetivo aparecem sem preencher a resposta com material irrelevante?

Avalie cobertura do contrato, não quantidade de texto.

### Formato de saída

Pergunta: a saída obedece estrutura, esquema, ordem, tipos, cardinalidade, idioma e extensão definidos?

Para saída estruturada, valide primeiro sintaxe/esquema; depois semântica.

### Restrições

Pergunta: proibições, limites, prioridades e requisitos obrigatórios foram respeitados?

Conflitos entre restrições devem ser identificados no prompt antes do teste.

### Robustez

Pergunta: o prompt mantém comportamento adequado quando a entrada é incompleta, ambígua, contraditória ou fora do caminho feliz?

### Eficiência

Pergunta: o prompt usa contexto e instruções suficientes sem redundância que prejudique custo, atenção ou manutenção?

Não premie brevidade se ela remove contrato necessário.

### Ferramentas e segurança

Quando aplicável, avalie em ordem:

1. decidiu corretamente se uma ferramenta era necessária;
2. escolheu a ferramenta correta;
3. usou argumentos/formatos corretos;
4. respeitou autorização e limites;
5. interpretou corretamente o retorno;
6. verificou o resultado observável;
7. parou quando uma stop condition ocorreu.

## 3. Suíte mínima de casos

Para prompt reutilizável, mantenha pelo menos:

1. **happy path:** entrada normal e representativa;
2. **fronteira material:** valor limite, caso raro ou ambiguidade conhecida;
3. **entrada incompleta:** informação necessária ausente;
4. **entrada conflitante:** regras ou dados incompatíveis, quando plausível;
5. **formato adverso:** conteúdo que tenta induzir saída fora do contrato;
6. **conteúdo não confiável/prompt injection:** para RAG/agentes, dado recuperado tentando redefinir instruções;
7. **tool routing:** quando houver ferramentas, caso em que deve usar e caso em que não deve usar.

Para tarefas simples, reduza o conjunto sem perder a fronteira mais provável de quebrar.

## 4. Gold standard, partial match e teste funcional

### Gold standard

Use quando existe resposta esperada clara e estável.

Compare elementos materiais da resposta, não apenas igualdade textual.

### Partial match

Use quando várias respostas são aceitáveis, mas uma decisão crítica distingue sucesso de falha.

Escolha um aspecto que seja:

- específico o bastante para detectar quebra real;
- geral o bastante para permitir divergência benigna.

Exemplo: em tool use, verificar a ferramenta correta pode ser mais informativo que exigir argumentos idênticos a uma única solução de referência.

### Teste funcional

Use quando não existe gold standard fácil, mas a saída pode ser executada ou verificada.

Exemplos:

- código compila e passa testes;
- JSON valida contra schema;
- consulta retorna campos esperados;
- plano contém todos os requisitos mandatórios;
- ferramenta foi chamada com sintaxe válida e produziu estado verificável.

## 5. Relatório de falha

Para cada falha, use:

| Campo | Conteúdo |
|---|---|
| Caso | identificador e entrada |
| Esperado | comportamento/saída necessária |
| Observado | comportamento real |
| Dimensão | aspecto que falhou |
| Severidade | bloqueante / importante / menor |
| Causa provável | instrução, contexto, exemplo, formato, ferramenta ou ambiguidade |
| Correção mínima | menor mudança capaz de corrigir a causa |
| Regressão | quais casos precisam ser reexecutados |

## 6. Regra de refinamento

Evite alterar vários componentes sem saber qual resolveu a falha.

Fluxo:

`falha → classificação → hipótese causal → mudança mínima → reexecução → regressão`

Quando várias falhas têm a mesma causa, corrija em lote e reexecute toda a suíte relevante.

## 7. Critério de prontidão

Um prompt de produção está pronto quando:

- invariantes críticos passam;
- não existe falha bloqueante conhecida;
- happy path e fronteira material passam;
- dimensões qualitativas atingem o piso definido para a aplicação;
- não houve regressão nos casos previamente aprovados;
- custo/latência/verbosidade estão dentro do limite, quando medidos;
- para agentes, autorização, ferramentas e stop conditions foram exercitadas em testes.