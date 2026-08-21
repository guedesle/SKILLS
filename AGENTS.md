# Política do catálogo central de skills

Este repositório é a fonte canônica das skills gerais/reutilizáveis do perfil.

## Low-HITL por padrão

Ao criar, promover ou atualizar skills gerais, aplique:

```text
lote coerente
  ↓
validação rápida opcional
  ↓
batch gate
  ↓
FAIL determinístico → corrigir tudo em lote → revalidar
  ↓ PASS
um único gate humano final
```

Não solicite HITL para falhas determinísticas corrigíveis sem mudança de intenção, escopo, risco, autorização ou contrato.

Interrompa antes do `PASS` somente quando houver decisão material, alteração de escopo, ação irreversível/produção, autorização/credencial, aceitação de risco ou informação indispensável que não possa ser inferida com segurança.

`elevated review` aumenta a profundidade do gate final; não cria approvals adicionais.

## Governança do catálogo

Ao criar ou alterar uma skill geral:

1. mantenha a implementação em `skills/<nome>/SKILL.md`;
2. registre/atualize a versão em `registry.json`;
3. atualize o índice, a seção detalhada e o histórico correspondente no `README.md`;
4. atualize `general-skills-status.md` quando o estado do catálogo mudar;
5. use SemVer;
6. valide com `python scripts/sync_skills.py --check`;
7. corrija erros determinísticos antes de pedir revisão;
8. para mirrors `mode: pull`, declare somente `repository`, `branch`, `path` e metadados necessários no `registry.json`; a lógica é centralizada em `.github/workflows/mirror-consumer.yml` e `scripts/sync_consumer.py`;
9. um consumidor precisa do bootstrap genérico apenas uma vez em `.github/workflows/sync-central-skills.yml`;
10. depois do bootstrap, novas skills para o mesmo consumidor são propagadas somente pela alteração do `registry.json`;
11. use `mode: push` apenas quando houver necessidade explícita de escrita cross-repository a partir do catálogo central.

## Skills de processo preferenciais

Quando aplicáveis, componha:

- `low-hitl-orchestration` — autonomia por lotes;
- `batch-quality-gate` — validação consolidada;
- `decision-escalation-control` — decide quando parar;
- `context-handoff` — continuidade sem reabrir decisões;
- `github-branch-pr-lifecycle` — branches/PRs e merges seguros;
- `adaptive-model-routing` — roteamento por papel, sem acoplamento a modelo;
- `contract-governed-execution` — execução de maior risco por contrato fail-closed;
- `knowledge-source-governance` — proveniência, freshness, corroboration e teto de conclusão.

Não promova automaticamente uma skill estritamente específica de projeto. Extraia primeiro a parte reutilizável e registre a origem/variante local.

Não edite uma cópia espelho para mudar comportamento geral. A mudança deve nascer aqui e seguir para os espelhos.

O bootstrap não concede permissões entre repositórios. Depois do bootstrap, o mirror pull usa apenas o `GITHUB_TOKEN` do próprio consumidor.
