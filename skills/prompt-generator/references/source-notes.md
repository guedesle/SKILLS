# Proveniência conceitual

Esta skill foi construída por síntese estrutural de materiais de prompt engineering. O objetivo não é reproduzir as obras, mas converter seus princípios, técnicas e critérios em decisões operacionais reutilizáveis.

## Fontes de origem

### Fundamentos de Prompt Engineering

Material didático em português fornecido para a conversão.

Contribuições incorporadas:

- clareza e especificidade como requisito central;
- quatro componentes didáticos: instrução, contexto, dados de entrada e indicador/formato de saída;
- escolha entre prompts abertos e específicos conforme o objetivo;
- zero-shot, instrução com contexto, one-shot e few-shot;
- decomposição de tarefas complexas;
- uso de restrições explícitas de formato, comprimento e escopo;
- exemplos de entrada/saída para reduzir ambiguidade;
- ciclo de vida objetivo → escrita → teste → refinamento;
- atenção à alucinação e necessidade de análise crítica em conteúdo especializado ou recente.

### John Berryman & Albert Ziegler — Prompt Engineering for LLMs: The Art and Science of Building Large Language Model–Based Applications

O’Reilly Media. Material fornecido para a conversão.

Contribuições incorporadas:

- prompt engineering como transformação do problema do usuário para o domínio do modelo e posterior transformação da saída em valor para o usuário;
- separação entre conteúdo estático e contexto dinâmico;
- seleção, triagem, priorização e organização do contexto em vez de simples acumulação;
- few-shot como forma de ensinar interpretação, estilo e formato;
- montagem de prompt por elementos, considerando posição, importância e dependência;
- concisão e filtragem de contexto para reduzir distração e efeitos de informação pouco saliente no meio de prompts longos;
- técnica de refoco/sandwich em prompts extensos;
- tool use, contexto para interações orientadas a tarefa, workflows, papéis e delegação;
- avaliação offline/online, gold standards, partial matching, testes funcionais e A/B testing;
- avaliação SOMA: perguntas específicas, respostas em escala ordinal e cobertura de múltiplos aspectos.

## Decisões de adaptação

A skill não replica automaticamente técnicas históricas quando elas entram em conflito com práticas atuais do host. Em particular:

- referências a chain-of-thought foram convertidas em orientação para **raciocínio interno + artefatos verificáveis**, sem exigir exposição de cadeia de pensamento privada;
- orientações de tool use foram combinadas com contratos explícitos de autorização, stop conditions e evidência observável;
- conteúdo recuperado por RAG é tratado como dado potencialmente não confiável e não pode redefinir regras de maior prioridade;
- nomes de modelos, APIs e preços não são fixados na skill, evitando obsolescência e dependência de fornecedor.

## Princípios preservados

A síntese mantém quatro ideias que atravessam as fontes:

1. **intenção precisa:** a qualidade começa por definir o que a saída precisa fazer;
2. **contexto relevante:** mais contexto não é automaticamente melhor;
3. **saída observável:** formato e critérios de aceite tornam a tarefa verificável;
4. **iteração baseada em teste:** prompts devem ser refinados a partir de falhas observadas.

## Limite de uso

Este arquivo é uma nota de proveniência, não um substituto das fontes. Para estudo detalhado, consulte os materiais originais aos quais você possui acesso. Não copie passagens extensas das obras para esta skill ou para derivados públicos.