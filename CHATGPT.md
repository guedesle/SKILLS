# Skills gerais no ChatGPT

Este repositório é a fonte canônica das skills gerais e reutilizáveis de `guedesle/SKILLS`. O formato adotado é **Agent Skills**: cada skill vive em `skills/<nome>/` e possui `SKILL.md` na raiz, podendo carregar `references/`, `scripts/`, `assets/`, templates e outros recursos.

## Objetivo

Permitir que as skills canônicas sejam instaladas como **Personal Skills** no ChatGPT sem criar cópias divergentes no repositório.

A regra é **uma skill por pacote**. Não crie uma mega-skill contendo todo o catálogo: a instalação separada preserva descoberta automática, gatilhos específicos, versionamento e atualização independente.

## 1. Validar o catálogo

Na raiz do clone:

```bash
python scripts/sync_skills.py --check
python scripts/package_chatgpt_skills.py --check
```

O primeiro comando valida registro, documentação, frontmatter e mirrors. O segundo confirma que todas as skills registradas podem ser empacotadas com segurança para ChatGPT.

## 2. Gerar os pacotes

```bash
python scripts/package_chatgpt_skills.py
```

Saída padrão:

```text
dist/chatgpt/
  manifest.json
  <skill>-v<semver>.zip
  ...
```

Cada ZIP contém `SKILL.md` diretamente na raiz do pacote e inclui os recursos auxiliares da mesma pasta canônica. Os bundles são determinísticos e não incluem caches, metadados de Git ou symlinks.

Para empacotar somente algumas skills:

```bash
python scripts/package_chatgpt_skills.py --skill low-hitl-orchestration --skill prompt-generator
```

## 3. Instalar no ChatGPT

Quando **Personal Skills** estiverem habilitadas para sua conta ou workspace:

1. abra **Plugins** na barra lateral;
2. abra a aba **Skills**;
3. escolha **Criar**;
4. escolha **Upload do computador**;
5. envie um arquivo `<skill>-v<semver>.zip` por vez;
6. conclua a revisão/scan apresentada pelo ChatGPT;
7. repita para as demais skills desejadas.

Depois de instalada, uma Personal Skill pode ser usada automaticamente pelo ChatGPT quando o pedido corresponder ao seu gatilho, ou ser invocada explicitamente quando a superfície oferecer essa opção.

> A disponibilidade de Personal Skills depende do plano, workspace, permissões administrativas e superfície do produto. Consulte a documentação oficial atual antes da instalação. Skills pessoais podem precisar ser adicionadas separadamente em desktop e web/mobile.

## 4. Atualização

O GitHub continua sendo a fonte de verdade. Para atualizar uma skill já instalada:

```bash
git pull --ff-only
python scripts/sync_skills.py --check
python scripts/package_chatgpt_skills.py --skill <nome>
```

Depois, faça upload da nova versão do ZIP na superfície de Skills do ChatGPT.

**Não assuma sincronização automática GitHub → ChatGPT.** O catálogo central controla o conteúdo e a versão; a instalação do ChatGPT é uma etapa de distribuição separada.

## 5. Catálogo geral

Por política deste repositório, toda entrada registrada em `registry.json` é uma skill geral canônica. Skills específicas de projeto permanecem locais até que uma versão transversal seja promovida e registrada.

Assim, o conjunto a empacotar para ChatGPT é derivado diretamente de `registry.json`; não mantenha uma segunda lista manual.

## 6. Segurança e governança

Antes do upload:

- revise instruções, scripts e arquivos auxiliares da skill;
- execute os dois checks do catálogo;
- não inclua segredos, tokens, credenciais ou dados de projeto no pacote;
- mantenha ações materiais sujeitas aos contratos de autorização e HITL definidos pelas skills de governança;
- trate o scan do ChatGPT como controle adicional, não como substituto da revisão do repositório.

## 7. ChatGPT, Codex e API

O mesmo conteúdo canônico pode ser reutilizado entre superfícies compatíveis com Agent Skills, mas a **instalação é independente**:

- **ChatGPT** — Personal Skills via interface de Skills, quando disponível;
- **Codex** — instalação global/local apontando para `skills/<nome>` conforme o README;
- **OpenAI API** — Skills são recursos versionados do projeto e podem receber diretório ou ZIP por API; publicar na API não instala automaticamente a skill no ChatGPT pessoal.

## Referências oficiais

- OpenAI Help Center — *Skills in ChatGPT*;
- OpenAI Developers — *Skills API*;
- documentação indicada no `README.md` para Codex e padrão Agent Skills.
