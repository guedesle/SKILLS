# Estado das skills gerais

Atualizado em 21 de agosto de 2026.

## Fonte canônica

`guedesle/SKILLS` é a fonte de verdade para skills gerais/reutilizáveis. O inventário operacional está em [`registry.json`](registry.json), em `schema_version: 2`, e a navegação/versões em [`README.md`](README.md).

Skills específicas de projeto não são promovidas automaticamente. Quando uma capacidade local possui valor transversal, uma versão geral é extraída para este catálogo e a origem fica registrada.

## Catálogo atual

| Skill | Categoria | Versão | Estado |
|---|---|---:|---|
| `plan-content` | Editorial | 1.0.0 | Canônica |
| `architect-text` | Editorial | 1.2.0 | Canônica + Plano de Arquitetura do Texto |
| `design-paragraphs` | Editorial | 1.2.0 | Canônica + 18 funções de parágrafo + corpus de exemplos |
| `write-with-evidence` | Editorial | 1.0.0 | Canônica |
| `write-technical-content` | Editorial/Técnica | 1.0.0 | Canônica + mirror homologado |
| `calibrate-rhetoric` | Editorial | 1.0.0 | Canônica |
| `review-editorial-quality` | QA | 1.0.0 | Canônica + mirror homologado |
| `improve-accessible-writing` | Acessibilidade | 1.0.0 | Canônica |
| `assess-editorial-alignment` | Governança editorial | 1.0.0 | Canônica |
| `graphify` | Engenharia de software | 1.0.0 | Canônica |
| `github-project-repo-sync` | GitHub automation | 1.0.0 | Canônica |
| `github-project-drift-audit` | GitHub/QA | 1.0.0 | Canônica |
| `skills-central-governance` | Gestão de skills | 1.2.0 | Canônica + low-HITL + default Codex por papel |
| `low-hitl-orchestration` | Orquestração | 1.0.0 | Canônica |
| `batch-quality-gate` | QA automation | 1.0.0 | Canônica |
| `context-handoff` | Context engineering | 1.0.0 | Canônica |
| `github-branch-pr-lifecycle` | GitHub automation | 1.0.0 | Canônica |
| `adaptive-model-routing` | Model routing | 1.1.0 | Canônica + adaptador Codex GPT-5.6 |
| `decision-escalation-control` | Governança de workflow | 1.0.0 | Canônica |
| `contract-governed-execution` | Governança de execução | 1.0.0 | Canônica |
| `knowledge-source-governance` | Governança de conhecimento | 1.0.0 | Canônica |
| `egba-licitacoes-contratos` | Governança de contratações | 1.0.0 | Canônica + síntese do Regulamento EGBA |

## Nova skill — governança de licitações e contratos

Em 23/08/2026 foi promovida ao catálogo central a skill `egba-licitacoes-contratos`, derivada do **Regulamento de Licitações e Contratos da EGBA** fornecido em PDF. A definição central é uma síntese operacional, com oito capítulos sob demanda, glossário, padrões de instrução e cheatsheet de prazos/limites. O pacote preserva referências aos artigos e orienta a confirmar versão oficial, atos de alçada, atualização pelo IPCA-E e parecer jurídico antes de decisões materiais.

## Origem e promoção

As nove skills editoriais foram generalizadas a partir das capacidades do `editor-agent`, removendo dependências de runtime, identidade específica e schemas exclusivos.

`graphify` foi generalizada a partir do workflow existente no `SieDOE`, mantendo a regra essencial: usar o grafo para descoberta e confirmar detalhes diretamente no código antes de editar.

`github-project-repo-sync` e `github-project-drift-audit` foram promovidas a partir das skills criadas no PFC IBMEC. A versão central remove nomes e IDs exclusivos do PFC e preserva o padrão desired → reconcile/audit → observed/live.

### Promoção de estratégias de fluxo e baixo HITL

Em 21/08/2026 foram promovidas **oito capacidades gerais** derivadas do `guedesle/cyber-skills-framework`:

- `low-hitl-orchestration` — `FAIL → corrigir em lote → revalidar → um único gate humano final`; falha determinística não gera HITL;
- `batch-quality-gate` — validação consolidada com modos fast/batch/CI, relatório estruturado, autotestes dos validadores e mesma política local/remota;
- `context-handoff` — estado operacional compacto entre agentes/modelos/conversas, preservando decisões, evidências, débitos e itens que não devem ser perguntados novamente;
- `github-branch-pr-lifecycle` — feature branches, stacked PRs, retarget, preservação de ancestralidade, recuperação segura de divergência e verificação pós-merge;
- `adaptive-model-routing` — separação por papel entre bounded execution, context handoff e frontier reasoning, mantendo skills agnósticas de fornecedor/modelo e adicionando um adaptador operacional Codex;
- `decision-escalation-control` — classificação `AUTO_CONTINUE`, `HUMAN_REVIEW_RECOMMENDED`, `HUMAN_REVIEW_REQUIRED` e `BLOCKED_UNTIL_REVIEW`, com elevated review aumentando profundidade sem multiplicar approvals;
- `contract-governed-execution` — contratos machine-readable e fail-closed para automatizar escopo, limites, stop conditions, approvals e trilha de evidência sem interpretar ausência de regra como permissão;
- `knowledge-source-governance` — Source Registry, proveniência, freshness, corroboration, vetor de qualidade e teto de conclusão para impedir que uma fonte fraca/desatualizada promova sozinha uma decisão material.

A promoção removeu regras exclusivas de cibersegurança. Taxonomias, catálogos, RoE e contratos ofensivos específicos permanecem no projeto de origem; foram generalizados apenas os padrões transversais de execução, QA, handoff, GitHub, escalonamento, governança de contratos e governança de conhecimento.

## Padrão geral low-HITL

Para trabalhos multi-etapas, a estratégia canônica passa a ser:

```text
lote coerente
  ↓
fast gate opcional
  ↓
batch gate
  ↓
FAIL → corrigir todos os bloqueios determinísticos → revalidar
  ↓ PASS
handoff/relatório consolidado
  ↓
1 gate humano final
```

Interromper antes do `PASS` somente quando a continuação depende de decisão material, alteração de escopo, autorização, ação irreversível/produção ou informação que não pode ser inferida com segurança.

`elevated review` não cria approvals adicionais: aumenta o rigor do mesmo gate final.

## Governança de execução por contrato

Para ações de maior risco ou com limites estritos, prefira contratos machine-readable e fail-closed. O contrato deve tornar verificáveis, conforme o domínio: escopo, janela temporal, capacidades permitidas/proibidas, limites operacionais, stop conditions, aprovação humana, estado de autorização e evidence/activity ledger. Ausência de regra crítica não deve virar permissão implícita.

## Governança de fontes e evidência

Fontes devem ser avaliadas por proveniência, authority, freshness, specificity, applicability, corroboration, empirical support e `allowed_outcomes`/`forbidden_outcomes`. Busca aberta pode descobrir fontes; conclusão material deve respeitar o teto de conclusão da fonte e o workflow de validação aplicável.

## Política de roteamento de modelos

Skills gerais continuam sem depender de nomes de modelos no seu contrato funcional. O roteamento concreto é tratado como adaptador do runtime/harness.

### Default Codex / GPT-5.6

A partir de 21/08/2026, o adaptador Codex padrão é:

```text
leaf / bounded        → gpt-5.6-luna  + reasoning high
orchestration/handoff → gpt-5.6-terra + reasoning medium
high complexity       → gpt-5.6-sol   + reasoning high
```

Interpretação operacional:

- **Luna High** executa tarefas leaf bem delimitadas, inclusive implementação, testes, transformações e validações estruturais quando o contrato já está fechado;
- **Terra Medium** atua como orquestrador/handoff padrão, decompõe trabalhos multi-etapas, integra resultados e preserva estado/contexto entre executores;
- **Sol High** atua em alta complexidade: arquitetura, investigação ambígua, debugging profundo, causalidade, falsificação/validação complexa, decisões materiais e QA de alto impacto.

O roteamento começa no menor tier suficiente e escala quando evidência inesperada altera risco, escopo, severidade, causalidade, complexidade ou decisão material. Depois que Sol reduz a ambiguidade e fecha interfaces/critérios, tarefas subsequentes podem voltar a Terra ou Luna.

O default está registrado de forma machine-readable em `registry.json > runtime_adapters.codex` e é herdado transversalmente por `AGENTS.md`. A semântica detalhada permanece em `skills/adaptive-model-routing/SKILL.md`, evitando copiar nomes de modelos para todas as skills e criar drift.

Maior capacidade cognitiva não amplia autorização operacional. Instrução explícita do usuário, política obrigatória do host ou contrato de risco prevalece sobre o default.

## Política de nomenclatura editorial

Nas skills editoriais, nomes de campos e etapas devem ser compreensíveis sem glossário. Termos acadêmicos, metafóricos, abreviações e códigos podem existir internamente para rastreabilidade, mas não devem ser a linguagem principal mostrada ao usuário quando houver uma expressão direta equivalente.

## Critério de maturidade

**Canônica** significa que a skill possui definição central, versão registrada e documentação navegável. Para skills de workflow, o contrato deve explicitar gatilhos, estados de HITL, condições de parada, saída esperada e origem/proveniência. Para skills de QA/gate, validadores críticos devem possuir casos negativos. Para governança de execução, schemas e ledgers devem ser fail-closed nas fronteiras materiais. Para governança de conhecimento, fontes devem declarar freshness/corroboration e limites de conclusão. Para adaptadores de modelos, defaults concretos devem manter separação entre papel, capacidade, reasoning effort e autorização.

## Política de sincronização

- central: `skills/<nome>/SKILL.md`;
- inventário/versionamento/mappings: `registry.json`;
- documentação: `README.md` e `general-skills-status.md`;
- validação estrutural: `python scripts/sync_skills.py --check`;
- runtime pull genérico: `.github/workflows/mirror-consumer.yml` + `scripts/sync_consumer.py`;
- caller padrão de consumidores: `templates/sync-central-skills.yml`;
- bootstrap padronizado de consumidor novo: `scripts/bootstrap_consumers.py`;
- fallback push explícito: `python scripts/sync_skills.py --apply`.

No modo preferido `pull`, um repositório consumidor recebe o caller padrão uma única vez. A partir daí, novas skills destinadas ao mesmo consumidor são adicionadas somente como mappings no `registry.json`.

Espelhos só são atualizados quando declarados explicitamente em `registry.json`. Variantes locais registradas em `legacy_source` servem para proveniência e não são sobrescritas automaticamente.

## Homologação atual

Consumidor: `guedesle/download-edicoes-doe`, branch `main`.

Mappings ativos:

- `write-technical-content` → `.agents/skills/write-technical-content`;
- `review-editorial-quality` → `.agents/skills/review-editorial-quality`.

As oito skills de workflow/governança não possuem mirror específico registrado; são canônicas no catálogo central e podem ser consumidas globalmente pelos hosts que apontam para `SKILLS/skills`.

O default de modelos do Codex não exige mirror individual por skill porque é política transversal do catálogo/harness.

## Próxima evolução de qualidade

- adicionar evals comparativos para as skills de workflow;
- medir número de HITLs evitados versus reversões/erros materiais;
- testar handoffs entre Luna, Terra e Sol com métricas de perda de contexto;
- testar stacked PR e divergência local em fixtures controladas;
- comparar roteamento por custo por sucesso, latência, fidelidade de contexto, retries e taxa de escalonamento;
- calibrar thresholds de escalation/de-escalation com evals reais de Codex;
- criar validator geral de contratos de skill para o catálogo central, complementando `sync_skills.py --check`;
- criar fixtures negativas para `contract-governed-execution` e `knowledge-source-governance`.
