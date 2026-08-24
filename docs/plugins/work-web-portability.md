# Portabilidade de plugins para ChatGPT Work web

## Decisão

A distribuição corrente do catálogo continua **local-only**. O alvo futuro é permitir uso privado no ChatGPT Work web por compartilhamento/listagem no diretório do próprio workspace, sem publicação universal.

Fonte canônica: `skills/` + `plugin-catalog.json`.

## Princípios

Um plugin candidato a Work web deve:

1. preservar a função principal sem exigir filesystem local, CLI, shell ou nome de modelo específico;
2. usar paths apenas como referências relativas internas ao pacote;
3. tratar apps/conectores externos como capabilities do host, não como autorização implícita;
4. degradar de ação para plano/handoff quando uma capability necessária não estiver disponível;
5. não alegar leitura, escrita, envio ou persistência sem ação realmente observada;
6. manter skills-only quando não houver necessidade real de app/MCP;
7. separar `PORTABLE` de `VERIFIED`: compatibilidade estrutural não prova execução real no Work web.

## Estados

- `LOCAL_READY` — build e marketplace local válidos;
- `GENERAL_WITH_ADAPTER` — núcleo portável, mas alguma etapa depende de capability específica do host;
- `WORK_WEB_PORTABLE` — função principal pode ser executada em host web skills-only sem dependência local obrigatória;
- `WORK_WEB_VERIFIED` — casos de aceite executados com sucesso no ChatGPT Work web;
- `WORKSPACE_SHARED` — plugin efetivamente compartilhado/listado no workspace.

## Baseline dos plugins

### Governed Workflow

Estado: `GENERAL_WITH_ADAPTER`.

O núcleo de governança é portável, mas fluxos de GitHub e outras ações externas precisam resolver capabilities/apps disponíveis no workspace. A rodada de promoção deve adicionar capability preflight e fallback explícito para tarefas que não possam executar writes.

### Skill Creator

Estado: `GENERAL_WITH_ADAPTER`.

Authoring, avaliação e portabilidade são conceitualmente web-portable. Empacotamento, validação de repositório e writes precisam de capabilities equivalentes no host. A promoção deve separar claramente criação/avaliação do target de distribuição local.

### Writing

Estado estrutural esperado: `WORK_WEB_PORTABLE`.

O plugin é skills-only e sua função editorial principal não exige filesystem, CLI, shell, modelo específico ou app externo. Ferramentas de arquivos/conectores são opcionais como fontes/destinos.

## Gate para promoção ao workspace

Antes de compartilhar qualquer plugin no Work web:

1. rerodar validação canônica e evals;
2. revisar manifest e composição;
3. confirmar ausência de dependência local obrigatória no contrato principal;
4. executar casos positivos e negativos no Work web;
5. registrar capabilities ausentes e fallbacks;
6. somente então marcar `WORK_WEB_VERIFIED`;
7. compartilhar inicialmente com grupo piloto;
8. expandir no workspace somente após evidência de uso estável.

## Política de publicação

`universal_publication` permanece `false`.

Compartilhar ou listar um plugin dentro de um workspace não deve ser interpretado como publicação no diretório universal.
