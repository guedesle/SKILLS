---
name: skills-central-governance
description: Governe o catálogo central de skills gerais em guedesle/SKILLS. Use ao criar, promover, versionar, atualizar, documentar ou distribuir uma skill reutilizável entre repositórios. Aplique low-HITL por padrão: agrupe mudanças coerentes, corrija falhas determinísticas em lote, valide antes de pedir revisão e não promova automaticamente skills estritamente específicas de um projeto. No Codex, aplique também o roteamento padrão por papel: Luna High para leaf/bounded, Terra Medium para orquestração/handoff e Sol High para alta complexidade.
---

# Central Skills Governance

O repositório `guedesle/SKILLS` é a fonte canônica das skills gerais e reutilizáveis do perfil.

## Regra principal

Toda skill classificada como **geral/reutilizável** deve:

1. existir canonicamente em `skills/<nome>/SKILL.md`;
2. possuir versão registrada em `registry.json`;
3. possuir documentação e link no `README.md`;
4. registrar origem/proveniência e, quando houver, repositórios espelho;
5. ser distribuída aos espelhos a partir da versão central;
6. receber primeiro neste repositório qualquer alteração que modifique seu comportamento geral.

## Low-HITL como padrão de governança

Em operações de criação, promoção ou atualização ampla:

1. agrupe mudanças que pertençam ao mesmo objetivo em um lote coerente;
2. use `low-hitl-orchestration` para evitar aprovações intermediárias sem valor;
3. use `batch-quality-gate` para consolidar validações;
4. corrija falhas determinísticas em lote antes de solicitar revisão humana;
5. use `decision-escalation-control` para interromper somente quando houver decisão material, alteração de escopo, ação irreversível, autorização ou informação não inferível com segurança;
6. quando houver mudança de alto impacto, aplique `elevated review` no mesmo gate final, sem multiplicar approvals;
7. use `context-handoff` se o trabalho mudar de agente, modelo, conversa ou executor;
8. para mudanças GitHub mais complexas, use `github-branch-pr-lifecycle`;
9. no Codex, componha `adaptive-model-routing` e aplique o default operacional por papel: `Luna High` para leaf/bounded, `Terra Medium` para orquestração/handoff e `Sol High` para alta complexidade/materialidade.

O padrão recomendado é:

```text
lote coerente → validação → FAIL determinístico → corrigir em lote → revalidar → PASS → um gate humano final
```

## Roteamento padrão de modelos no Codex

O catálogo não replica nomes de modelos dentro de cada skill. O default é herdado pela política central e implementado por `adaptive-model-routing`.

Quando o host for Codex e a família GPT-5.6 estiver disponível:

```text
leaf / bounded        → gpt-5.6-luna  + high
orchestration/handoff → gpt-5.6-terra + medium
high complexity       → gpt-5.6-sol   + high
```

Regras:

- Terra Medium é o coordenador/handoff padrão de fluxos multi-etapas;
- Luna High recebe tarefas leaf com escopo, entradas, arquivos-alvo e critérios de aceite suficientemente fechados;
- Sol High recebe raciocínio de alta complexidade, investigação ambígua, arquitetura, validação profunda e julgamentos materiais;
- escalone automaticamente quando a evidência altera complexidade, risco, escopo, causalidade ou decisão material;
- faça de-escalation depois que a ambiguidade for removida e restarem tarefas mecânicas/delimitadas;
- não confunda maior capacidade cognitiva com maior autorização operacional;
- instrução explícita do usuário ou política obrigatória do host prevalece sobre o default.

## Geral versus específica

Promova para o catálogo central quando a skill puder ser usada em mais de um projeto sem depender de nomes, IDs, caminhos, schemas ou regras institucionais exclusivos de um único repositório.

Mantenha local quando a skill depender essencialmente de um projeto específico. Se houver valor reutilizável, extraia uma versão geral para o catálogo central e mantenha a variante local como adaptação.

## Criação de nova skill

Ao criar uma skill geral:

1. escolha nome estável em kebab-case;
2. crie `skills/<nome>/SKILL.md`;
3. adicione a skill a `registry.json` com versão SemVer;
4. documente no índice e na seção detalhada do `README.md`;
5. atualize `general-skills-status.md` quando a mudança altera o estado do catálogo;
6. registre targets de espelhamento, se existirem;
7. rode `python scripts/sync_skills.py --check`;
8. corrija todos os erros determinísticos antes do gate humano;
9. após revisão, rode `python scripts/sync_skills.py --apply` somente se houver mirrors `mode: push` selecionados.

## Atualização

Mudanças comportamentais devem atualizar a versão:

- PATCH: correções e esclarecimentos sem mudança de contrato;
- MINOR: nova capacidade compatível;
- MAJOR: mudança incompatível de contrato, gatilhos ou saída.

A alteração deve ser feita primeiro na cópia central. Não trate uma cópia espelho como fonte de verdade.

## Promoção a partir de outro projeto

Ao extrair uma capacidade reutilizável:

1. identifique o comportamento transversal;
2. remova nomes, IDs, paths, schemas e políticas exclusivas do projeto;
3. preserve os invariantes que geram valor;
4. registre `origin` no `registry.json`;
5. mantenha no projeto de origem somente a variante específica quando necessário;
6. não copie para o catálogo contratos de autorização ou políticas que só fazem sentido no domínio de origem.

## Segurança e integridade

- nunca versionar tokens, PATs ou secrets;
- o sincronizador não apaga skills não gerenciadas;
- `--check` deve preceder `--apply` em mudanças amplas;
- repositórios espelho somente são alterados quando declarados explicitamente no registro;
- nenhuma falha de validação determinística deve ser convertida em pedido de aprovação humana;
- não use modelo/agente mais capaz como substituto para autorização ou decisão de escopo;
- não promova roteamento específico de um harness a contrato obrigatório de todos os hosts: mantenha-o em adaptadores operacionais.

## Merge e publicação

Antes de merge:

- branch deve estar reconciliada com a base;
- diff deve permanecer restrito ao lote pretendido;
- `registry.json`, README e arquivos canônicos devem concordar;
- validação estrutural deve passar;
- PR deve estar mergeável;
- revisão final deve refletir o nível de risco do lote.

Após merge, confirme a default branch e, quando necessário, sincronize clones/mirrors.

## Saída esperada

Ao concluir uma operação de governança, informe:

- skills e versões afetadas;
- arquivos centrais alterados;
- origem/proveniência;
- espelhos afetados;
- resultado da validação;
- estado do PR/merge;
- roteamento de modelo aplicado quando o host permitir observá-lo;
- HITL solicitado ou evitado e motivo.
