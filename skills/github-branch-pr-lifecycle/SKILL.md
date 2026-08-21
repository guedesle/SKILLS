---
name: github-branch-pr-lifecycle
description: Gerencie branches e pull requests com baixo HITL, segurança de histórico e gates explícitos. Use para criar feature branches, stacked PRs, resolver divergência local/remota, preservar trabalho antes de reset/rebase, retargetar PRs e ordenar merges sem reintroduzir diffs ou quebrar ancestralidade.
---

# GitHub Branch & PR Lifecycle

Use esta skill para conduzir mudanças em GitHub por branches/PRs com mínimo retrabalho e sem operações destrutivas prematuras.

## Regras de segurança

1. nunca sobrescreva trabalho local sem antes verificar `status` e divergência;
2. preserve commits locais divergentes em branch de backup antes de alinhar uma branch ao remoto;
3. prefira `--ff-only` para sincronizações que não devem criar merge implícito;
4. não use `reset --hard` antes de preservar o estado que pode conter trabalho útil;
5. PR permanece draft enquanto gates técnicos bloqueantes estiverem abertos;
6. merge só ocorre após gate técnico e decisão humana exigida pelo fluxo.

## Feature branch padrão

Ao iniciar trabalho a partir da default branch:

1. confirmar que a base está sincronizada;
2. criar branch dedicada;
3. manter mudanças de escopo coerente no mesmo PR;
4. usar commits pequenos o bastante para rastrear intenção, sem criar micro-HITL por commit.

## Stacked PRs

Use stacked PR quando uma rodada depende de uma fundação ainda não integrada e separar os diffs reduz risco/revisão.

Regras:

- PR filho aponta inicialmente para a branch do PR pai;
- valide o filho contra a base real do stack, não automaticamente contra `main`;
- integre o pai preservando ancestralidade quando o filho depende dela;
- após merge do pai, retargete o filho para `main`/default branch;
- compare novamente o diff e confirme que somente o delta do filho permanece;
- só então faça o segundo merge.

Quando a estratégia do stack depende de ancestralidade, prefira merge commit ao squash/rebase, salvo se houver prova de que a estratégia alternativa não expande/reintroduz o diff.

## Divergência local/remota

Quando `pull --ff-only` falhar:

1. verificar alterações não commitadas;
2. medir divergência com `git rev-list --left-right --count origin/<branch>...<branch>`;
3. inspecionar commits com `git log --left-right`;
4. se houver commits locais úteis, preservar a ponta em `backup/<branch>-before-sync-<timestamp>`;
5. somente depois alinhar a branch ao remoto homologado;
6. recuperar commits úteis seletivamente, por exemplo com `cherry-pick`, após inspeção.

## Base do PR

Resolva a base pelo próprio PR quando possível. Não assuma `origin/main` para stacked branches.

## Gates

Antes de promover um PR:

- working tree/branch coerentes;
- diff restrito ao escopo;
- batch gate técnico `PASS`;
- threads/reviews bloqueantes resolvidos;
- revisão elevada executada quando aplicável;
- decisão humana final obtida quando exigida.

## Merge

Use `expected_head_sha` ou verificação equivalente quando disponível para impedir merge após movimento inesperado da branch.

Após merge:

1. verificar estado do PR;
2. verificar HEAD da default branch;
3. sincronizar checkout local;
4. confirmar divergência `0 0` quando a intenção é igualdade exata;
5. registrar baseline/tag/release quando a rodada exigir congelamento.

## Saída esperada

Informe branch/base/PR, divergência, estratégia de merge, gates, backup criado quando necessário e estado pós-merge.

## Origem

Generalizada dos workflows de stacked PR, retarget, merge ordenado e recuperação segura de divergência local usados no `guedesle/cyber-skills-framework`.
