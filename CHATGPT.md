# Skills gerais no ChatGPT

`guedesle/SKILLS` é a fonte canônica das skills gerais. Cada skill permanece em `skills/<nome>/` com `SKILL.md` na raiz e pode incluir `evals/`, `references/`, `scripts/`, `assets/` e templates.

## Estados de distribuição

Não confunda preparação do artefato com instalação:

- `DISTRIBUTION_READY` — bundle/plugin foi gerado e validado;
- `INSTALLED` — upload/instalação foi observado na superfície de destino;
- `VERIFIED` — a superfície confirmou descoberta/uso;
- `PUBLISHED` — publicação universal/workspace foi confirmada pela plataforma.

O repositório pode produzir e validar `DISTRIBUTION_READY`. Só declare os demais estados quando houver observação no ChatGPT/Codex.

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

## 2. Duas rotas para ChatGPT

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

### Rota B — plugin skills-only

Plugins oficiais podem conter apenas skills e não precisam de MCP. O catálogo inicial deste repositório agrupa as capacidades interdependentes de governança/fábrica em um único plugin:

```text
guedesle-governed-workflow
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
  marketplace/
    .agents/plugins/marketplace.json
    plugins/
      guedesle-governed-workflow/
        .codex-plugin/plugin.json
        skills/
          ...
```

O plugin contém cópias **derivadas** das skills para instalação. Não edite essas cópias: mudanças continuam em `skills/<nome>/`.

## 3. Teste local do plugin

Quando o ChatGPT desktop/Codex oferecer marketplace local, use a raiz gerada:

```bash
codex plugin marketplace add ./dist/plugins/marketplace
codex plugin marketplace list
```

Depois reinicie a superfície compatível, abra o Plugins Directory e procure `Governed Workflow` na fonte local. Instale, abra uma conversa nova e execute casos positivos/negativos representativos.

A documentação oficial atual indica que marketplaces locais servem para autoria, teste e distribuição privada e que plugins skills-only podem ir diretamente ao teste do plugin completo, sem etapa de MCP.

## 4. Conta Plus e Plugin Directory

O Plugins Directory é visível entre os planos do ChatGPT, inclusive web/desktop, mas **instalação e invocação continuam dependentes do plano, superfície, região e rollout**. Plugins que contêm somente skills não exigem um app externo, o que reduz as restrições técnicas, mas este repositório não trata isso como garantia de disponibilidade na conta atual.

Se o plugin local não puder ser instalado na superfície Plus disponível, a rota de distribuição seguinte é submissão ao diretório universal como **Skills only**. A submissão pública é um processo separado de review e não deve ser descrita como bypass de plano.

## 5. Submissão universal

O portal oficial aceita plugins `Skills only`. Antes de submeter:

- use o mesmo conjunto de skills testado localmente;
- prepare pelo menos cinco casos positivos e três negativos;
- revise descrições, starter prompts e escopo do plugin;
- providencie identidade de desenvolvedor/publicador e URLs exigidas pela listagem;
- complete os atestados e o scan de segurança;
- só declare `PUBLISHED` após aprovação e publicação efetiva.

O primeiro plugin foi desenhado para ser skills-only: não possui MCP, OAuth, backend ou UI externa.

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
DISTRIBUTION_READY → INSTALLED → VERIFIED → PUBLISHED (quando aplicável)
```

A meta-skill `skill-development-lifecycle` orquestra esse fluxo. `chatgpt-governed-workflow` é o entry point geral e delega a ela quando o objeto principal é uma skill.

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

**Não existe suposição de sincronização automática GitHub → plugin instalado.** Atualize/reinstale o artefato na superfície de destino quando necessário.

## 8. Segurança

Antes de distribuição:

- nenhuma falha do gate canônico pode permanecer;
- não incluir segredos, tokens ou credenciais;
- não promover paths absolutos, endpoints internos ou IDs específicos de projeto;
- manter guardrails de autorização e contratos fail-closed;
- tratar scan/review do host como controle adicional, não substituto do gate do repositório.

## Referências oficiais

- OpenAI Developers — Plugins: package your plugin;
- OpenAI Developers — connect and test your plugin;
- OpenAI Developers — submit plugins;
- OpenAI Help Center — Plugins in ChatGPT and Codex.

Consulte a documentação oficial atual antes da instalação/publicação, porque planos, superfícies e permissões podem mudar.
