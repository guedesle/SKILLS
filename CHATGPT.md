# Skills gerais no ChatGPT

`guedesle/SKILLS` é a fonte canônica das skills gerais. Cada skill permanece em `skills/<nome>/` com `SKILL.md` na raiz e pode incluir `evals/`, `references/`, `scripts/`, `assets/` e templates.

## Estados de distribuição

Não confunda preparação do artefato com instalação:

- `DISTRIBUTION_READY` — bundle foi gerado e validado;
- `INSTALLED` — upload/instalação foi observado na superfície de destino;
- `VERIFIED` — a superfície confirmou descoberta/uso da skill.

O repositório pode produzir e validar `DISTRIBUTION_READY`. Só declare `INSTALLED` ou `VERIFIED` quando isso tiver sido observado no ChatGPT.

## 1. Gate canônico

```bash
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/sync_skills.py --check
python scripts/validate_skill_evals.py
python scripts/package_chatgpt_skills.py --check
```

Esse gate valida YAML real, registro/documentação, eval schema e empacotabilidade. Evals declarados não equivalem a execução de modelo.

## 2. Gerar pacotes

```bash
python scripts/package_chatgpt_skills.py
```

Saída:

```text
dist/chatgpt/
  manifest.json
  <skill>-v<semver>.zip
```

Cada ZIP contém uma única skill com `SKILL.md` diretamente na raiz. Recursos auxiliares da pasta canônica são incluídos; symlinks, caches e metadados Git não entram no bundle.

Exemplo seletivo:

```bash
python scripts/package_chatgpt_skills.py \
  --skill chatgpt-governed-workflow \
  --skill skill-development-lifecycle \
  --skill skill-validator
```

## 3. Instalar no ChatGPT

Quando a superfície da conta/workspace oferecer criação/upload de Personal Skills:

1. abra a área de Skills/Plugins disponível na interface;
2. escolha criar/adicionar uma skill;
3. envie **um ZIP por skill**;
4. conclua a revisão/scan da superfície;
5. confirme que a skill aparece como instalada/disponível;
6. teste um caso positivo e um caso negativo do diretório `evals/` quando possível.

A disponibilidade e os nomes exatos da interface dependem do produto, plano, workspace e permissões. O repositório não presume que a conta atual tenha essa superfície.

## 4. Lifecycle project → ChatGPT

Uma skill de projeto não deve ser enviada diretamente só porque possui `SKILL.md`.

Fluxo:

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
  ↓
DISTRIBUTION_READY → upload → INSTALLED → teste → VERIFIED
```

A meta-skill `skill-development-lifecycle` orquestra esse fluxo. `chatgpt-governed-workflow` é o entry point geral e delega a ela quando o objeto principal é uma skill.

## 5. Atualização

GitHub permanece a fonte de verdade:

```bash
git pull --ff-only
python -m pip install -r requirements-dev.txt
python scripts/sync_skills.py --check
python scripts/validate_skill_evals.py
python scripts/package_chatgpt_skills.py --skill <nome>
```

Depois gere/suba a nova versão na superfície do ChatGPT quando necessário.

**Não existe suposição de sincronização automática GitHub → ChatGPT.**

## 6. ChatGPT, Codex e consumers

O mesmo conteúdo canônico pode atender múltiplos destinos, mas instalação é independente:

- **ChatGPT** — bundle individual e upload quando suportado;
- **Codex USER** — `$HOME/.agents/skills/<nome>` apontando para a skill canônica;
- **consumers GitHub** — mirrors declarados em `registry.json`;
- **plugin skill-only** — opção de distribuição reutilizável quando adotada pelo host.

Alterações de comportamento geral são feitas primeiro em `guedesle/SKILLS`, nunca em uma cópia instalada ou mirror.

## 7. Segurança

Antes de distribuição:

- nenhuma falha do gate canônico pode permanecer;
- não incluir segredos, tokens ou credenciais;
- não promover paths absolutos, endpoints internos ou IDs específicos de projeto;
- manter guardrails de autorização e contratos fail-closed;
- tratar scan do host como controle adicional, não substituto do gate do repositório.

## Referências

Consulte a documentação oficial atual do ChatGPT/Codex antes de executar passos de instalação, porque superfícies e permissões podem mudar. O README mantém o procedimento canônico do repositório e `AGENTS.md` contém a política transversal de governança.
