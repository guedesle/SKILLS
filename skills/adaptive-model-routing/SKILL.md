---
name: adaptive-model-routing
description: "Distribua trabalho entre modelos/agentes por papel, custo e autoridade cognitiva sem acoplar skills a um fornecedor. Use para separar execução delimitada, síntese/handoff e raciocínio de fronteira, com escalonamento automático quando evidência inesperada altera risco, escopo, severidade ou decisão material. No Codex, aplique o adaptador padrão GPT-5.6: Luna High para tarefas leaf delimitadas, Terra Medium para orquestração/handoff e Sol High para alta complexidade."
---

# Adaptive Model Routing

Use esta skill para escolher o executor pelo **papel do trabalho**, não apenas pelo preço ou nome do modelo.

## Regra principal

A skill permanece agnóstica de fornecedor/modelo no seu contrato geral. O runtime/adaptador escolhe o modelo disponível que melhor cumpre o papel e os evals exigidos.

Um adaptador pode definir defaults concretos para um harness específico sem transformar esses nomes em dependências das demais skills.

## Papéis padrão

### Bounded execution / leaf

Use para:

- extração;
- transformação determinística;
- classificação simples;
- validações estruturais;
- tool actions com escopo já decidido;
- tarefas repetitivas de alto volume;
- implementação leaf cujo contrato, arquivos-alvo e critério de aceite já estejam definidos.

Esse papel **não promove sozinho conclusões materiais** quando elas exigem julgamento especializado.

### Context handoff / orchestration

Use para:

- decomposição de trabalho em subtarefas;
- roteamento entre executores;
- síntese de contexto;
- compactação de histórico;
- handoffs;
- cruzamento de documentos;
- consolidação de estado e evidências;
- preparação de contexto para o próximo executor;
- integração de resultados de tarefas leaf antes de novo roteamento.

### Frontier reasoning / high complexity

Use para:

- heurística profunda;
- decisão arquitetural difícil;
- falsificação/validação complexa;
- resolução de evidência conflitante;
- causalidade e attack-path/reasoning equivalente;
- debugging ambíguo de múltiplos subsistemas;
- julgamento material de QA;
- desenho ou alteração de contratos críticos;
- situações em que erro de conclusão tem impacto alto.

## Adaptador padrão — Codex / GPT-5.6

Quando o host for Codex e a família GPT-5.6 estiver disponível, use este balanceamento como **default operacional**:

| Papel | Modelo | Reasoning effort | Uso padrão |
|---|---|---|---|
| `bounded execution / leaf` | `gpt-5.6-luna` | `high` | tarefa bem delimitada, implementação leaf, testes locais, extração e transformações |
| `context handoff / orchestration` | `gpt-5.6-terra` | `medium` | decomposição, coordenação, síntese, handoff e integração de resultados |
| `frontier reasoning / high complexity` | `gpt-5.6-sol` | `high` | arquitetura, investigação difícil, decisão material, validação profunda e QA de alto impacto |

Forma abreviada:

```text
leaf / bounded       → Luna High
orchestration/handoff → Terra Medium
high complexity       → Sol High
```

`High` e `Medium` descrevem esforço de raciocínio, **não autoridade operacional**.

## Política de composição no Codex

1. Comece pela classe mínima capaz de cumprir o contrato da subtarefa.
2. Use Terra Medium para decompor trabalho multi-etapas e produzir handoffs compactos.
3. Delegue subtarefas leaf e bem definidas a Luna High.
4. Escale para Sol High quando a própria decisão, investigação ou validação for de alta complexidade/materialidade.
5. Depois que Sol reduzir a ambiguidade e fechar o escopo, devolva execução mecânica/leaf a Luna High quando isso reduzir custo sem perder qualidade.
6. Não mantenha Sol em tarefas rotineiras apenas porque ele iniciou a análise.
7. Não use Terra como substituto automático de Sol em julgamento material; Terra coordena e integra, mas deve escalar quando o critério de frontier for atingido.
8. Não use Luna para decidir arquitetura, severidade, causalidade, aceite/rejeição ou mudança de escopo quando essas decisões ainda estiverem abertas.

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

No Codex, isso normalmente significa `Luna High → Terra Medium` quando cresce a necessidade de coordenação/contexto e `Luna High/Terra Medium → Sol High` quando cresce a complexidade ou materialidade da decisão.

## De-escalation

Após uma decisão frontier fechar interfaces, hipóteses e critérios de aceite, rebaixe subtarefas subsequentes para Terra ou Luna quando o risco residual permitir.

O objetivo é otimizar **custo por tarefa concluída com qualidade**, não maximizar permanentemente o tier do modelo.

## Autoridade versus capacidade

Um modelo mais capaz **não aumenta autorização operacional**.

Separe:

- capacidade cognitiva;
- permissão de ação;
- escopo aprovado;
- responsabilidade pelo resultado.

Nenhum adaptador pode transformar um modelo em autorização para agir fora do contrato da tarefa.

## Precedência e overrides

Aplique nesta ordem:

1. política/limite obrigatório do host ou organização;
2. instrução explícita do usuário para a tarefa;
3. contrato de risco/autorização da skill ou projeto;
4. adaptador padrão do harness;
5. heurística de menor custo suficiente.

Um override deve registrar o motivo quando altera o tier esperado por materialidade, disponibilidade, custo, latência ou eval.

## Fallback quando o harness não permite roteamento por subtarefa

Se o ambiente Codex em uso não permitir selecionar modelo/effort separadamente por agente ou subtarefa:

- preserve a classificação de papel;
- registre o modelo/effort desejado no handoff ou plano de execução;
- execute com o modelo efetivamente disponível;
- não alegue que houve troca de modelo quando ela não ocorreu;
- reavalie a configuração quando o harness passar a suportar o adaptador.

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
- taxa de tarefas concluídas sem retry;
- necessidade de escalonamento humano;
- frequência de escalonamento e de-escalation entre tiers.

## Saída esperada

Informe papel escolhido, modelo/adaptador efetivo quando conhecido, reasoning effort, motivo, limites de autoridade, critérios de escalation e executor final responsável pelo julgamento material.

## Origem

Generalizada do roteamento temporário `bounded-execution → context-handoff → frontier-security-reasoning` adotado no `guedesle/cyber-skills-framework`. A versão 1.1.0 mantém o contrato geral agnóstico e adiciona o adaptador operacional padrão para Codex/GPT-5.6: `Luna High → Terra Medium → Sol High` por papel.
