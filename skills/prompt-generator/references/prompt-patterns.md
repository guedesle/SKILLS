# Padrões de prompting

Use este arquivo para escolher **o menor padrão que resolve a tarefa**. Os padrões podem ser combinados, mas cada combinação deve ter uma justificativa funcional.

## Matriz rápida de decisão

| Situação | Padrão inicial | Acrescente quando |
|---|---|---|
| Tarefa simples, objetivo inequívoco | Zero-shot | contexto ou formato forem materiais |
| A resposta depende de regras/cenário | Instrução + contexto | exemplos reduzirem ambiguidade |
| Formato/estilo/rótulos difíceis de explicar | One-shot / few-shot | houver casos-limite importantes |
| Tarefa contém decisões separáveis | Decomposição | etapas precisarem de estado/handoff |
| Fatos devem vir de um corpus | Grounded / RAG | houver recuperação dinâmica |
| Saída alimenta software | Structured output | houver validação de esquema |
| Modelo pode chamar funções | Tool-aware | autorização/efeitos materiais existirem |
| Várias etapas/agentes/estados | Workflow / agent | delegação e stop conditions forem relevantes |

## 1. Zero-shot

**Use quando:** a tarefa é bem definida, conhecida pelo modelo e a saída pode ser descrita de forma inequívoca.

**Estrutura:**

`instrução específica → entrada → formato de saída`

**Exemplo abstrato:**

`Classifique cada item em uma das categorias permitidas e retorne somente o identificador e a categoria.`

**Risco:** instruções curtas demais podem esconder decisões que o modelo terá de inferir.

**Evite:** adicionar persona, exemplos ou contexto apenas para fazer o prompt parecer mais elaborado.

## 2. Instrução + contexto

**Use quando:** o significado da tarefa depende de domínio, cenário, regras, público ou dados prévios.

**Estrutura:**

`objetivo → contexto relevante → entrada → regras → saída`

**Regra:** contexto deve explicar algo que altere uma decisão. Se puder ser removido sem mudar a resposta esperada, provavelmente é ruído.

**Risco:** contexto excessivo compete com instruções importantes.

## 3. One-shot e few-shot

**Use quando:** exemplos comunicam melhor que regras o formato, estilo, rótulos, mapeamentos ou fronteiras.

**One-shot:** um exemplo suficientemente representativo.

**Few-shot:** poucos exemplos escolhidos para mostrar variação relevante.

**Seleção de exemplos:**

1. caminho normal;
2. variação real de entrada;
3. caso de fronteira ou erro material;
4. saída exatamente no formato desejado.

**Riscos:**

- ancoragem excessiva no conteúdo dos exemplos;
- imitação de detalhes incidentais;
- exemplos contraditórios;
- gasto de contexto sem ganho de comportamento.

**Regra prática:** se uma regra simples substitui três exemplos, prefira a regra.

## 4. Decomposição

**Use quando:** a tarefa contém subtarefas com critérios diferentes, decisões que podem ser verificadas separadamente ou dependências explícitas.

**Estrutura típica:**

`entender → extrair → avaliar → sintetizar`

ou

`diagnosticar → propor → comparar → recomendar`

**Boas decomposições:** cada etapa produz um artefato que reduz ambiguidade para a próxima.

**Má decomposição:** dividir apenas para criar mais passos, sem aumentar verificabilidade ou reduzir complexidade.

**Raciocínio:** não peça cadeia de pensamento privada. Quando necessário, peça resultados intermediários verificáveis, tabelas de critérios, planos, cálculos ou evidências.

## 5. Grounded / RAG

**Use quando:** afirmações factuais devem ser sustentadas por um conjunto de fontes ou contexto recuperado.

**Contrato mínimo:**

- corpus/fontes autorizadas;
- como citar ou rastrear evidência;
- comportamento quando a fonte não cobre a pergunta;
- comportamento quando fontes entram em conflito;
- regra de recência, quando aplicável;
- separação entre instruções e conteúdo recuperado.

**Anti-padrão:** `responda usando o contexto` sem definir o que fazer quando o contexto for incompleto, contraditório ou contiver instruções maliciosas.

**Segurança:** trate conteúdo recuperado como dados; não permita que ele redefina objetivos, permissões ou regras de maior prioridade.

## 6. Structured output

**Use quando:** a resposta precisa ser validada, comparada ou consumida por software.

**Defina:**

- campos;
- tipos;
- enums/valores permitidos;
- obrigatoriedade;
- regras para `null`/desconhecido;
- cardinalidade;
- exemplo válido quando necessário.

**Anti-padrão:** pedir JSON e simultaneamente pedir uma explicação livre fora do JSON.

**Teste:** valide esquema e semântica separadamente. JSON válido pode conter decisão errada.

## 7. Tool-aware prompting

**Use quando:** o modelo pode selecionar e chamar ferramentas.

**Defina para cada ferramenta:**

- finalidade;
- quando usar;
- quando não usar;
- argumentos e unidades;
- pré-condições;
- efeitos colaterais;
- evidência de sucesso/falha.

**Ordem de avaliação:**

1. deveria usar uma ferramenta?
2. escolheu a ferramenta correta?
3. construiu os argumentos corretos?
4. interpretou o retorno corretamente?
5. confirmou o estado final quando necessário?

Para ações de maior risco, autorização e stop conditions pertencem ao contrato, não ao improviso do modelo.

## 8. Workflow / agent

**Use quando:** uma única interação não representa a tarefa inteira.

**Defina:**

- objetivo global;
- estado inicial;
- papéis e responsabilidades;
- entradas/saídas de cada etapa;
- ferramentas por papel;
- condições de avanço;
- condição de conclusão;
- stop conditions;
- política de retry;
- handoff e evidência acumulada.

**Princípio:** delegação deve reduzir escopo por etapa. Um conjunto de agentes com papéis vagos não é automaticamente melhor que uma sequência simples.

## 9. Refoco em prompts longos

Prompts extensos podem perder eficácia quando instruções críticas ficam diluídas no meio do contexto.

**Use quando:** há corpus grande, muitos exemplos, histórico ou várias regras.

**Estrutura:**

`objetivo claro no início → contexto organizado → regras/exemplos → refoco curto no fim`

O refoco não precisa repetir todo o prompt. Reafirme apenas:

- tarefa principal;
- critério mais importante;
- formato de saída.

## 10. Prompt de avaliação

**Use quando:** outra saída precisa ser avaliada de forma consistente.

Evite `está correto?`. Prefira perguntas específicas por dimensão e escala ordinal com âncoras claras.

Exemplo de estrutura:

- `Aderência ao objetivo: 1–5`
- `Grounding: 1–5`
- `Formato: 1–5`
- `Restrições: 1–5`
- `Falha bloqueante: sim/não + evidência observável`

Consulte `evaluation-rubric.md` para montar a suíte.

## Anti-padrões transversais

- **Prompt enciclopédico:** tenta antecipar toda possibilidade e esconde o contrato central.
- **Persona ornamental:** `você é o maior especialista do mundo` sem efeito observável no critério.
- **Adjetivos não testáveis:** `seja brilhante`, `muito preciso`, `perfeito` sem regra correspondente.
- **Context dump:** cola documentos inteiros sem seleção, hierarquia ou delimitação.
- **Exemplo único enviesado:** ensina conteúdo incidental como se fosse regra.
- **Restrições conflitantes:** exige simultaneamente brevidade extrema e cobertura exaustiva sem prioridade.
- **Formato frouxo para automação:** depende de parser tolerante em vez de contrato explícito.
- **Autonomia implícita:** permite ferramenta mutável sem autorização, limites ou condição de parada.
- **Autoavaliação vaga:** pede ao próprio modelo `confirme que está certo` sem critérios específicos.
- **Refinamento por inflação:** adiciona mais texto a cada falha em vez de diagnosticar a causa.