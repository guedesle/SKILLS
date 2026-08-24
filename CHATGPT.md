# Skills gerais no ChatGPT

`guedesle/SKILLS` é a fonte canônica das skills gerais. Cada skill permanece em `skills/<nome>/` com `SKILL.md` na raiz e pode incluir `evals/`, `references/`, `scripts/`, `assets/` e templates.

## Política atual

A distribuição dos plugins deste catálogo é **local-only**.

```text
universal_publication = false
future target = chatgpt-work-workspace-private
```

A meta futura é usar os mesmos plugins de forma privada no ChatGPT Work web por compartilhamento/listagem dentro de um workspace compatível. Isso não implica publicação no diretório universal.

## Estados de distribuição

Não confunda preparação do artefato com instalação ou execução:

- `DISTRIBUTION_READY` — bundle/plugin foi gerado e validado;
- `INSTALLED` — instalação foi observada na superfície de destino;
- `LOCAL_RUNTIME_VERIFIED` — casos de aceite foram executados em host local;
- `WORK_WEB_PORTABLE` — o contrato principal não depende de filesystem/CLI/modelo específico;
- `WORK_WEB_VERIFIED` — casos de aceite foram executados com sucesso no ChatGPT Work web;
- `WORKSPACE_SHARED` — o plugin foi efetivamente compartilhado/listado no workspace.

O repositório pode produzir e validar `DISTRIBUTION_READY` e portabilidade estrutural. Só declare estados de instalação/execução quando houver observação real na superfície de destino.

## 1. Gate canônico

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/sync_skills.py --check
python scripts/validate_skill_evals.py
python scripts/package_chatgpt_skills.py --check
python scripts/package_plugins.py --check
```

Esse gate valida YAML real, registro/documentação, eval schema, bundles individuais e composição de plugins skills-only. Evals declarados não equivalem a execução de modelo.

## 2. Rotas derivadas para ChatGPT

### Rota A — Personal Skill individual

```bash
python scripts/package_chatgpt_skills.py
```

Saída:

```text
dist/chatgpt/
  manifest.json
  <skill>-v<semver>.zip
```

Cada ZIP contém uma única skill com `SKILL.md` na raiz. Use essa rota quando a conta/workspace oferecer upload de Personal Skills.

### Rota B — plugin skills-only local

O catálogo possui três plugins locais:

```text
guedesle-governed-workflow
guedesle-skill-creator
guedesle-writing
```

Valide e gere:

```bash
python scripts/package_plugins.py --check
python scripts/package_plugins.py
```

Saída:

```text
dist/plugins/
  manifest.json
  guedesle-governed-workflow-v1.0.0.zip
  guedesle-skill-creator-v1.0.0.zip
  guedesle-writing-v1.0.0.zip
  marketplace/
    .agents/plugins/marketplace.json
    plugins/
      guedesle-governed-workflow/
      guedesle-skill-creator/
      guedesle-writing/
```

Cada plugin contém `.codex-plugin/plugin.json` e cópias **derivadas** das skills. Não edite essas cópias: mudanças continuam em `skills/<nome>/`.

## 3. Teste local

Quando o Codex/ChatGPT Desktop oferecer marketplace local, use a raiz gerada:

```bash
codex plugin marketplace add ./dist/plugins/marketplace
codex plugin marketplace list
```

Se o marketplace já estiver registrado no mesmo caminho, regenere os artefatos e reinicie/atualize a superfície; não é necessário adicionar a mesma origem repetidamente.

Guias específicos:

- [`docs/plugins/skill-creator-local.md`](docs/plugins/skill-creator-local.md);
- [`docs/plugins/writing-local.md`](docs/plugins/writing-local.md).

## 4. ChatGPT Work web — alvo privado

A documentação oficial atual permite que plugins sejam compartilhados ou listados **dentro do próprio workspace**, sem publicação no diretório universal. Plugins que incluem somente skills não exigem app externo para sua função principal, embora instalação e uso ainda dependam das configurações, função e superfície do workspace.

Nossa estratégia é:

```text
fonte canônica
  ↓
plugin skills-only local
  ↓
LOCAL_RUNTIME_VERIFIED
  ↓
portability gate
  ↓
WORK_WEB_PORTABLE
  ↓
teste real no workspace
  ↓
WORK_WEB_VERIFIED
  ↓
WORKSPACE_SHARED
```

A política detalhada está em [`docs/plugins/work-web-portability.md`](docs/plugins/work-web-portability.md).

### Estado estrutural atual

- `guedesle-writing` — desenhado para `WORK_WEB_PORTABLE`; função editorial principal é host-agnostic.
- `guedesle-governed-workflow` — `GENERAL_WITH_ADAPTER`; ações de repositório dependem das capabilities/apps disponíveis.
- `guedesle-skill-creator` — `GENERAL_WITH_ADAPTER`; authoring/evals são portáveis, mas empacotamento e writes precisam de capabilities equivalentes no host.

Uma rodada posterior deve promover os dois últimos a `WORK_WEB_PORTABLE` antes do teste real no Work web.

## 5. Sem publicação universal

O catálogo não prepara nem executa submissão ao Universal Plugin Directory.

Não criar por padrão:

- listing público;
- marketing público;
- fluxo de submissão universal;
- dependência de aprovação pública;
- afirmação de que o plugin está publicado.

Se essa política mudar no futuro, a mudança deve ser explícita e passar por novo gate de risco/governança.

## 6. Lifecycle project → ChatGPT/Codex

```text
skill local
  ↓
skill-portability-audit
  ↓
PROJECT_ONLY ───────────────→ permanece local
GENERALIZABLE ──────────────→ extrair parte transversal
GENERAL_WITH_ADAPTER ───────→ núcleo geral + adaptador local
GLOBAL_READY
  ↓
skill-promotion
  ↓
skill-validator + skill-evaluator
  ↓
merge no catálogo central
  ↓
skill-distribution
  ├─ bundle individual
  └─ plugin skills-only
       ↓
DISTRIBUTION_READY
```

A meta-skill `skill-development-lifecycle` orquestra esse fluxo. `chatgpt-governed-workflow` é o entry point geral; `writing-workflow` é o entry point editorial.

## 7. Atualização

GitHub permanece a fonte de verdade:

```bash
git pull --ff-only
python -m pip install -r requirements-dev.txt
python scripts/sync_skills.py --check
python scripts/validate_skill_evals.py
python scripts/package_plugins.py --check
python scripts/package_plugins.py
```

**Não existe suposição de sincronização automática GitHub → plugin instalado.** Atualize/refresque o artefato na superfície de destino quando necessário.

## 8. Segurança e portabilidade

Antes de distribuição:

- nenhuma falha do gate canônico pode permanecer;
- não incluir segredos, tokens ou credenciais;
- não promover paths absolutos, endpoints internos ou IDs específicos de projeto como dependências do contrato geral;
- manter guardrails de autorização e contratos fail-closed;
- não transformar ausência de capability em alegação de execução;
- tratar scan/review do host como controle adicional, não substituto do gate do repositório.

## Referências oficiais

- OpenAI Developers — Plugins;
- OpenAI Help Center — Plugins in ChatGPT and Codex;
- documentação de administração e compartilhamento de plugins em workspaces.

Consulte a documentação oficial atual antes de instalação/compartilhamento, porque planos, superfícies e permissões podem mudar.
