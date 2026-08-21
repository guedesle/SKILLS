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
| `skills-central-governance` | Gestão de skills | 1.0.0 | Canônica |
| `low-hitl-orchestration` | Orquestração | 1.0.0 | Canônica |
| `batch-quality-gate` | QA automation | 1.0.0 | Canônica |
| `context-handoff` | Context engineering | 1.0.0 | Canônica |
| `github-branch-pr-lifecycle` | GitHub automation | 1.0.0 | Canônica |
| `adaptive-model-routing` | Model routing | 1.0.0 | Canônica |
| `decision-escalation-control` | Governança de workflow | 1.0.0 | Canônica |
| `contract-governed-execution` | Governança de execução | 1.0.0 | Canônica |
| `knowledge-source-governance` | Governança de conhecimento | 1.0.0 | Canônica |

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
- `adaptive-model-routing` — separação por papel entre bounded execution, context handoff e frontier reasoning, mantendo skills agnósticas de fornecedor/modelo;
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

Para ações de maior risco ou com limites estritos, prefira contratos machine-readable e fail-closed. O contrato deve tornar verificáveis, conforme o domínio:

- escopo e alvos/recursos permitidos;
- janela temporal;
- capacidades permitidas e proibidas;
- limites operacionais;
- stop conditions;
- aprovação humana;
- estado de autorização;
- evidence/activity ledger.

Ausência de regra crítica não deve virar permissão implícita. Validadores desse contrato devem possuir casos negativos que provem o bloqueio de configurações fail-open.

## Governança de fontes e evidência

Fontes não devem receber autoridade universal apenas por reputação. Registre e avalie separadamente:

- proveniência/owner;
- authority class;
- freshness/TTL;
- specificity;
- applicability;
- corroboration;
- empirical support;
- `allowed_outcomes` e `forbidden_outcomes`.

Busca aberta pode descobrir fontes; uma conclusão material deve respeitar o teto de conclusão da fonte e passar pelo workflow de validação adequado. Preserve counterevidence e versões/snapshots quando a reprodutibilidade for relevante.

## Política de roteamento de modelos

Skills gerais não devem depender de nomes de modelos. O runtime pode manter adaptadores temporários por workspace/harness, mas deve separar:

- `bounded execution` — extração, transformação, validação estrutural e ações delimitadas;
- `context handoff` — síntese, compressão e transferência de contexto;
- `frontier reasoning` — heurística profunda, evidência conflitante e julgamento material de QA.

Evidência inesperada que altere risco, escopo, severidade, causalidade ou decisão material deve escalar para o executor responsável por raciocínio de maior autoridade/capacidade. Modelo mais capaz nunca amplia autorização operacional.

## Política de nomenclatura editorial

Nas skills editoriais, nomes de campos e etapas devem ser compreensíveis sem glossário. Termos acadêmicos, metafóricos, abreviações e códigos podem existir internamente para rastreabilidade, mas não devem ser a linguagem principal mostrada ao usuário quando houver uma expressão direta equivalente.

Exemplos: `motivo textual` → **finalidade do texto**; `transformação do leitor` → **resultado esperado da leitura**; `matriz paragrafal` → **plano de parágrafos**; `handoff` → **instruções para a próxima etapa** quando a interação for editorial e voltada ao usuário final.

## Critério de maturidade

**Canônica** significa que a skill possui definição central, versão registrada e documentação navegável. Isso não significa, por si só, que todas as skills tenham passado por bateria comparativa de evals em produção.

Para skills de workflow, o contrato deve explicitar gatilhos, estados de HITL, condições de parada, saída esperada e origem/proveniência.

Para skills de QA/gate, validadores críticos devem possuir casos negativos capazes de provar que o próprio gate não aceita enfraquecimentos óbvios do contrato.

Para governança de execução, schemas e ledgers devem ser fail-closed nas fronteiras materiais. Para governança de conhecimento, fontes devem declarar freshness/corroboration e limites de conclusão.

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

As oito novas skills de workflow/governança ainda não possuem mirror específico registrado; são canônicas no catálogo central e podem ser consumidas globalmente pelos hosts que apontam para `SKILLS/skills`.

## Próxima evolução de qualidade

- adicionar evals comparativos para as skills de workflow;
- medir número de HITLs evitados versus reversões/erros materiais;
- testar handoffs entre famílias de modelos diferentes;
- testar stacked PR e divergência local em fixtures controladas;
- comparar roteamento de modelos por custo, latência, fidelidade de contexto e taxa de escalonamento;
- criar validator geral de contratos de skill para o catálogo central, complementando `sync_skills.py --check`;
- criar fixtures negativas para `contract-governed-execution` e `knowledge-source-governance`.
