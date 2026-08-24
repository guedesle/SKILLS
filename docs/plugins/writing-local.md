# Writing — instalação e aceite local

## Objetivo

Validar `guedesle-writing` 1.0.0 como plugin skills-only local antes de qualquer distribuição por workspace.

O plugin é derivado da fonte canônica `skills/` e não deve ser editado dentro de `dist/` ou do marketplace materializado.

## Composição

Entry point:

- `writing-workflow` 1.0.0.

Skills incluídas:

1. `writing-workflow`;
2. `plan-content`;
3. `architect-text`;
4. `design-paragraphs`;
5. `write-with-evidence`;
6. `write-technical-content`;
7. `calibrate-rhetoric`;
8. `improve-accessible-writing`;
9. `review-editorial-quality`;
10. `assess-editorial-alignment`.

## Regeneração no Windows

A partir do clone real do repositório:

```powershell
cd C:\projetos\SKILLS-repo
git switch main
git pull --ff-only
python .\scripts\package_plugins.py --output C:\projetos\SKILLS\guedesle-plugin
```

Se o marketplace `guedesle-skills-local` já estiver registrado no mesmo caminho, não execute `marketplace add` novamente.

## Validação estrutural

```powershell
Test-Path C:\projetos\SKILLS\guedesle-plugin\marketplace\.agents\plugins\marketplace.json
Test-Path C:\projetos\SKILLS\guedesle-plugin\marketplace\plugins\guedesle-writing\.codex-plugin\plugin.json
Test-Path C:\projetos\SKILLS\guedesle-plugin\guedesle-writing-v1.0.0.zip
```

Resultado esperado: três `True`.

Confirme a presença no marketplace:

```powershell
Get-Content C:\projetos\SKILLS\guedesle-plugin\marketplace\.agents\plugins\marketplace.json
```

O arquivo deve listar:

- `guedesle-governed-workflow`;
- `guedesle-skill-creator`;
- `guedesle-writing`.

## Casos funcionais locais

### Positivo 1 — criação ponta a ponta

Prompt:

```text
Use Writing para transformar estas notas e fontes em um relatório estruturado, redigido e revisado.
```

Aceite:

- identifica finalidade/público quando necessário;
- estrutura antes de redigir quando a estrutura ainda não existe;
- preserva lacunas de evidência;
- executa QA editorial final;
- não força etapas sem utilidade.

### Positivo 2 — refatoração estrutural

Prompt:

```text
Use Writing para reorganizar este artigo, refatorar os parágrafos problemáticos e revisar o resultado sem mudar os fatos.
```

Aceite:

- usa arquitetura textual quando a ordem global é o problema;
- usa desenho de parágrafos no nível local;
- preserva fatos, números, citações e ressalvas;
- não trata estilo como autorização para alterar conteúdo factual.

### Positivo 3 — nota técnica com evidência

Prompt:

```text
Use Writing para redigir uma nota técnica a partir deste briefing e destas evidências, com tom institucional e linguagem clara.
```

Aceite:

- aplica redação técnica;
- diferencia evidência de inferência;
- calibra retórica à força da evidência;
- melhora legibilidade sem eliminar precisão.

### Negativo 1 — tarefa pontual

Prompt:

```text
Deixe este parágrafo mais claro sem mudar o conteúdo.
```

Aceite:

- não cria pipeline completo;
- resolve no nível especializado adequado.

### Negativo 2 — pergunta factual simples

Prompt:

```text
Explique o que é CAPEX.
```

Aceite:

- não transforma a pergunta em workflow editorial multi-etapas.

## Estado

Use estes estados separadamente:

- `PLUGIN_BUILD_VERIFIED` — empacotamento e estrutura passaram;
- `LOCAL_DISTRIBUTION_READY` — artifact e marketplace local foram validados;
- `LOCAL_RUNTIME_VERIFIED` — casos funcionais foram observados em host local;
- `WORK_WEB_PORTABLE` — contrato não depende de filesystem/CLI/modelo para sua função principal;
- `WORK_WEB_VERIFIED` — execução real foi observada no ChatGPT Work web.

`WORK_WEB_PORTABLE` não equivale a `WORK_WEB_VERIFIED`.
