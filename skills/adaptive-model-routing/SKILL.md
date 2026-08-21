---
name: adaptive-model-routing
description: Distribua trabalho entre modelos/agentes por papel, custo e autoridade cognitiva sem acoplar skills a um fornecedor. Use para separar execução delimitada, síntese/handoff e raciocínio de fronteira, com escalonamento automático quando evidência inesperada altera risco, escopo, severidade ou decisão material.
---

# Adaptive Model Routing

Use esta skill para escolher o executor pelo **papel do trabalho**, não apenas pelo preço ou nome do modelo.

## Regra principal

A skill deve permanecer agnóstica de modelo. O runtime/adaptador escolhe o modelo disponível que melhor cumpre o papel e os evals exigidos.

## Papéis padrão

### Bounded execution

Use para:

- extração;
- transformação determinística;
- classificação simples;
- validações estruturais;
- tool actions com escopo já decidido;
- tarefas repetitivas de alto volume.

Esse papel **não promove sozinho conclusões materiais** quando elas exigem julgamento especializado.

### Context handoff

Use para:

- síntese de contexto;
- compactação de histórico;
- handoffs;
- cruzamento de documentos;
- consolidação de estado e evidências;
- preparação de contexto para o próximo executor.

### Frontier reasoning

Use para:

- heurística profunda;
- decisão arquitetural difícil;
- falsificação/validação complexa;
- resolução de evidência conflitante;
- causalidade e attack-path/reasoning equivalente;
- julgamento material de QA;
- situações em que erro de conclusão tem impacto alto.

## Escalonamento automático

Eleve de bounded/context para frontier quando surgir evidência que possa alterar:

- escopo;
- severidade;
- risco;
- exploitability ou viabilidade equivalente;
- causalidade;
- decisão de aprovação/rejeição;
- compromisso de custo/prazo;
- hipótese central do trabalho.

## Autoridade versus capacidade

Um modelo mais capaz **não aumenta autorização operacional**.

Separe:

- capacidade cognitiva;
- permissão de ação;
- escopo aprovado;
- responsabilidade pelo resultado.

Nenhum adaptador pode transformar um modelo em autorização para agir fora do contrato da tarefa.

## Preferências temporárias

O runtime pode manter defaults por período, workspace ou harness, mas deve registrá-los como adaptadores/versionamento operacional, não como dependências das skills.

## Onboarding de novo harness/modelo

Ao mudar de workspace, harness ou família de modelos:

1. importar constraints de acesso, sandbox e policy;
2. rerodar evals por papel;
3. comparar bounded execution, retenção de contexto, validação e QA;
4. alterar defaults somente quando policy ou evidência de eval justificar;
5. preservar adaptadores anteriores para reprodutibilidade.

## Evals recomendados

Avalie separadamente:

- precisão em extração;
- aderência a instruções delimitadas;
- retenção/compressão de contexto;
- taxa de erro em handoff;
- qualidade de falsificação/validação;
- consistência em decisões materiais;
- custo e latência;
- necessidade de escalonamento humano.

## Saída esperada

Informe papel escolhido, modelo/adaptador efetivo quando conhecido, motivo, limites de autoridade, critérios de escalation e executor final responsável pelo julgamento material.

## Origem

Generalizada do roteamento temporário `bounded-execution → context-handoff → frontier-security-reasoning` adotado no `guedesle/cyber-skills-framework`, removendo nomes de modelos e regras exclusivas de cibersegurança.
