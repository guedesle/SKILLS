# Política do catálogo central de skills

Este repositório é a fonte canônica das skills gerais/reutilizáveis do perfil.

Ao criar ou alterar uma skill geral neste repositório:

1. mantenha a implementação em `skills/<nome>/SKILL.md`;
2. registre/atualize a versão em `registry.json`;
3. atualize o índice, a seção detalhada e o histórico correspondente no `README.md`;
4. use SemVer;
5. valide com `python scripts/sync_skills.py --check`;
6. para mirrors `mode: pull`, declare somente `repository`, `branch`, `path` e metadados necessários no `registry.json`; a lógica de sincronização é centralizada em `.github/workflows/mirror-consumer.yml` e `scripts/sync_consumer.py`;
7. um repositório consumidor precisa do bootstrap genérico apenas uma vez em `.github/workflows/sync-central-skills.yml`; use `python scripts/bootstrap_consumers.py --apply` para instalar/atualizar esse caller padrão sem escrever lógica específica por projeto;
8. depois do bootstrap, novas skills para o mesmo consumidor são propagadas somente pela alteração do `registry.json` e pela próxima execução agendada/manual do workflow consumidor;
9. use `mode: push` apenas quando houver uma necessidade explícita de escrita cross-repository a partir do catálogo central.

Não promova automaticamente uma skill estritamente específica de projeto. Extraia primeiro a parte reutilizável e registre a origem/variante local.

Não edite uma cópia espelho para mudar comportamento geral. A mudança deve nascer aqui e seguir para os espelhos.

O bootstrap não concede permissões entre repositórios. Para instalar o workflow em um consumidor novo, a ação que executa `bootstrap_consumers.py --apply` precisa estar autenticada com permissão para alterar workflows naquele repositório. Depois disso, o mirror pull usa apenas o `GITHUB_TOKEN` do próprio consumidor.
