# Política do catálogo central de skills

Este repositório é a fonte canônica das skills gerais/reutilizáveis do perfil.

Ao criar ou alterar uma skill geral neste repositório:

1. mantenha a implementação em `skills/<nome>/SKILL.md`;
2. registre/atualize a versão em `registry.json`;
3. atualize o índice, a seção detalhada e o histórico correspondente no `README.md`;
4. use SemVer;
5. valide com `python scripts/sync_skills.py --check`;
6. sincronize espelhos explicitamente registrados com `python scripts/sync_skills.py --apply` quando aplicável.

Não promova automaticamente uma skill estritamente específica de projeto. Extraia primeiro a parte reutilizável e registre a origem/variante local.

Não edite uma cópia espelho para mudar comportamento geral. A mudança deve nascer aqui e seguir para os espelhos.
