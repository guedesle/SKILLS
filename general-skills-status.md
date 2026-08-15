# Estado das skills gerais

Atualizado em 14 de agosto de 2026.

## Fonte canônica

O repositório `guedesle/SKILLS` passa a ser a fonte de verdade para skills gerais/reutilizáveis do perfil. O inventário operacional está em [`registry.json`](registry.json) e a navegação/versões em [`README.md`](README.md).

Skills específicas de projeto não são promovidas automaticamente. Quando uma capacidade local possui valor transversal, uma versão geral é extraída para este catálogo e a origem fica registrada.

## Catálogo atual

| Skill | Categoria | Versão | Estado |
|---|---|---:|---|
| `plan-content` | Editorial | 1.0.0 | Canônica |
| `architect-text` | Editorial | 1.0.0 | Canônica |
| `design-paragraphs` | Editorial | 1.0.0 | Canônica |
| `write-with-evidence` | Editorial | 1.0.0 | Canônica |
| `write-technical-content` | Editorial/Técnica | 1.0.0 | Canônica |
| `calibrate-rhetoric` | Editorial | 1.0.0 | Canônica |
| `review-editorial-quality` | QA | 1.0.0 | Canônica |
| `improve-accessible-writing` | Acessibilidade | 1.0.0 | Canônica |
| `assess-editorial-alignment` | Governança editorial | 1.0.0 | Canônica |
| `graphify` | Engenharia de software | 1.0.0 | Canônica |
| `github-project-repo-sync` | GitHub automation | 1.0.0 | Canônica |
| `github-project-drift-audit` | GitHub/QA | 1.0.0 | Canônica |
| `skills-central-governance` | Gestão de skills | 1.0.0 | Canônica |

## Origem e promoção

As nove skills editoriais foram generalizadas a partir das capacidades do `editor-agent`, removendo dependências de runtime, identidade específica e schemas exclusivos. `architect-text` preserva a proveniência da skill local `editor-structure`.

`graphify` foi generalizada a partir do workflow existente no `SieDOE`, mantendo a regra essencial: usar o grafo para descoberta e confirmar detalhes diretamente no código antes de editar.

`github-project-repo-sync` e `github-project-drift-audit` foram promovidas a partir das skills criadas no PFC IBMEC. A versão central remove nomes e IDs exclusivos do PFC e preserva o padrão desired → reconcile/audit → observed/live.

## Critério de maturidade

**Canônica** significa que a skill possui definição central, versão registrada e documentação navegável. Isso não significa, por si só, que todas as skills tenham passado por uma bateria comparativa de evals em produção.

## Política de sincronização

- central: `skills/<nome>/SKILL.md`;
- inventário/versionamento: `registry.json`;
- documentação: `README.md`;
- validação: `python scripts/sync_skills.py --check`;
- distribuição para espelhos registrados: `python scripts/sync_skills.py --apply`;
- automação: `.github/workflows/sync-skills.yml`.

Espelhos só são atualizados quando declarados explicitamente em `registry.json`. Variantes locais legadas registradas em `legacy_source` servem para proveniência e não são sobrescritas automaticamente.

## Próxima evolução de qualidade

Para promover maturidade além da validação estrutural, executar evals controlados por família de uso e registrar resultados por versão, sem alterar a versão canônica sem evidência de melhoria ou correção.
