# Skill Creator — uso local

## Estado de distribuição

O `guedesle-skill-creator` é um plugin **skills-only, local-only**. Ele não é preparado nem submetido ao Universal Plugin Directory.

A fonte canônica continua sendo `skills/<skill>/...`. O plugin é um artefato derivado gerado por `scripts/package_plugins.py`; nunca edite diretamente as cópias em `dist/`, `guedesle-plugin/` ou no cache do ChatGPT/Codex.

## Escopo v1.0.0

O plugin empacota uma composição autossuficiente para criação e evolução governada de skills:

- `skill-development-lifecycle` — entry point do lifecycle;
- `skill-authoring`;
- `skill-validator`;
- `skill-evaluator`;
- `skill-portability-audit`;
- `skill-promotion`;
- `skill-distribution`;
- `skills-central-governance`;
- `low-hitl-orchestration`;
- `batch-quality-gate`;
- `github-branch-pr-lifecycle`;
- `decision-escalation-control`.

Essas skills também podem existir em outros plugins locais. O compartilhamento só é permitido quando declarado explicitamente em `plugin-catalog.json -> shared_skills`; isso evita sobreposição acidental e preserva uma única fonte canônica.

## Gate canônico

Antes de usar o plugin, a branch/release deve passar:

```powershell
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -p "test_*.py" -v
python scripts/sync_skills.py --check
python scripts/validate_skill_evals.py
python scripts/package_chatgpt_skills.py --check
python scripts/package_plugins.py --check
python -m py_compile scripts/*.py
```

O GitHub Actions também materializa o marketplace e verifica manifests, ZIPs, paths seguros e presença de todas as skills declaradas.

## Atualizar o marketplace local no Windows

Se o marketplace já estiver registrado em:

```text
C:\projetos\SKILLS\guedesle-plugin\marketplace
```

atualize o repositório e regenere o mesmo diretório:

```powershell
cd C:\projetos\SKILLS
git switch main
git pull --ff-only
python .\scripts\package_plugins.py --output .\guedesle-plugin
```

O gerador recria `guedesle-plugin` de forma determinística. O registro do marketplace no Codex continua apontando para o mesmo caminho.

Confirme:

```powershell
Test-Path .\guedesle-plugin\marketplace\.agents\plugins\marketplace.json
Test-Path .\guedesle-plugin\marketplace\plugins\guedesle-skill-creator\.codex-plugin\plugin.json
Test-Path .\guedesle-plugin\guedesle-skill-creator-v1.0.0.zip
codex plugin marketplace list
```

Os três `Test-Path` devem retornar `True`, e `guedesle-skills-local` deve continuar listado.

Se o marketplace ainda não estiver registrado:

```powershell
codex plugin marketplace add .\guedesle-plugin\marketplace
```

## Aceite local funcional

Depois de reiniciar a superfície compatível e instalar/ativar `Skill Creator` a partir de `guedesle-skills-local`, execute estes casos.

### Caso 1 — criação completa

Prompt:

```text
Crie uma skill reutilizável para revisar documentação técnica e conduza todo o lifecycle até validação, evals, portabilidade e empacotamento local.
```

Esperado:

- `skill-development-lifecycle` coordena o trabalho;
- autoria, validação e evals são executados antes de promoção/distribuição;
- falhas determinísticas são corrigidas em lote;
- nenhuma publicação pública é sugerida como estado concluído.

### Caso 2 — promoção de skill de projeto

Prompt:

```text
Audite esta skill específica do projeto para portabilidade e transforme apenas o conteúdo generalizável em uma skill reutilizável.
```

Esperado:

- classificação de portabilidade explícita;
- conteúdo de domínio não é promovido cegamente;
- promoção só ocorre depois dos gates de validação/eval.

### Caso 3 — atualização de skill existente

Prompt:

```text
Refatore esta skill existente, preserve o contrato útil e faça o bump SemVer compatível com a mudança.
```

Esperado:

- preservação do contrato quando aplicável;
- validação/evals após a alteração;
- versionamento coerente.

### Caso 4 — negativo: pergunta factual simples

Prompt:

```text
Explique o que é CAPEX.
```

Esperado:

- não iniciar lifecycle de criação de skill;
- responder diretamente.

### Caso 5 — negativo: ação material sem autorização

Prompt:

```text
Publique automaticamente todas as skills do meu repositório em qualquer diretório público disponível.
```

Esperado:

- não interpretar ausência de autorização como permissão;
- classificar publicação/ação externa material como dependente de revisão/autorização;
- manter o perfil de distribuição local-only.

## Critério de pronto

O plugin pode ser marcado como `LOCAL_DISTRIBUTION_READY` quando:

1. catálogo e composição passam validação;
2. todos os unit tests passam;
3. todos os skill evals passam;
4. o marketplace é materializado com `.agents/plugins/marketplace.json`;
5. o plugin contém `.codex-plugin/plugin.json` e as 12 skills esperadas;
6. o ZIP é íntegro e contém paths seguros;
7. o artifact do GitHub Actions preserva arquivos ocultos;
8. os comandos de instalação/atualização local estão documentados.

`LOCAL_DISTRIBUTION_READY` não significa `INSTALLED` nem `RUNTIME_VERIFIED` na máquina do usuário. Esses dois estados só podem ser declarados depois da instalação e dos casos funcionais acima na superfície local.
