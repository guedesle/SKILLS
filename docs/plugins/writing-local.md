# Writing — instalação e aceite local

## Objetivo

Validar `guedesle-writing` 2.0.0 como plugin skills-only local antes de qualquer distribuição por workspace.

O plugin é derivado da fonte canônica `skills/` e não deve ser editado dentro de `dist/` ou do marketplace materializado.

O domínio do plugin é **escrita humanizada para leitura/publicação**. Ele não deve ser selecionado para conceber, planejar ou especificar artefatos tecnológicos.

## Composição

Entry point:

- `writing-workflow` 2.0.0.

Skills incluídas:

1. `writing-workflow`;
2. `plan-editorial-content`;
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
Test-Path C:\projetos\SKILLS\guedesle-plugin\guedesle-writing-v2.0.0.zip
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

### Positivo 1 — artigo científico ponta a ponta

Prompt:

```text
Use Writing para transformar estas notas e fontes em um artigo científico estruturado, redigido e revisado.
```

Aceite:

- identifica finalidade/público quando necessário;
- estrutura antes de redigir quando a estrutura ainda não existe;
- preserva lacunas de evidência;
- executa QA editorial final;
- não força etapas sem utilidade.

### Positivo 2 — refatoração estrutural editorial

Prompt:

```text
Use Writing para reorganizar este artigo, refatorar os parágrafos problemáticos e revisar o resultado sem mudar os fatos.
```

Aceite:

- usa arquitetura textual quando a ordem global é o problema;
- usa desenho de parágrafos no nível local;
- preserva fatos, números, citações e ressalvas;
- não trata estilo como autorização para alterar conteúdo factual.

### Positivo 3 — material técnico já definido → prosa para leitores

Prompt:

```text
A arquitetura e os requisitos já estão aprovados. Use Writing para transformar este material em um relatório técnico humanizado para apresentação ao conselho.
```

Aceite:

- trabalha apenas a comunicação e a estrutura do texto;
- diferencia evidência de inferência;
- preserva integralmente as decisões técnicas existentes;
- não cria requisitos, interfaces, critérios de aceite ou decisões de arquitetura.

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

### Negativo 3 — especificação de software

Prompt:

```text
Planeje e escreva a especificação técnica de um plugin para o Obsidian, incluindo arquitetura, requisitos e critérios de aceite.
```

Aceite:

- `guedesle-writing` não é selecionado como workflow de desenvolvimento;
- `plan-editorial-content` não é acionado pelo verbo genérico “planeje”;
- não gera outline editorial como substituto da especificação;
- encaminha o trabalho para um workflow de engenharia/produto apropriado.

### Negativo 4 — arquitetura de sistema/agente

Prompt:

```text
Desenhe a arquitetura deste agente de IA com tools, schemas, memória, testes e estratégia de deploy.
```

Aceite:

- `architect-text` não confunde arquitetura textual com arquitetura tecnológica;
- nenhuma skill editorial define componentes, contratos ou comportamento executável.

### Negativo 5 — backlog e implementação

Prompt:

```text
Decomponha este projeto em épicos, histórias, backlog, plano de implementação, migração e CI/CD.
```

Aceite:

- o plugin Writing fica fora do roteamento;
- o resultado deve ser produzido por capacidades de engenharia/produto.

## Estado

Use estes estados separadamente:

- `PLUGIN_BUILD_VERIFIED` — empacotamento e estrutura passaram;
- `LOCAL_DISTRIBUTION_READY` — artifact e marketplace local foram validados;
- `LOCAL_RUNTIME_VERIFIED` — casos funcionais foram observados em host local;
- `WORK_WEB_PORTABLE` — contrato não depende de filesystem/CLI/modelo para sua função principal;
- `WORK_WEB_VERIFIED` — execução real foi observada no ChatGPT Work web.

`WORK_WEB_PORTABLE` não equivale a `WORK_WEB_VERIFIED`.
