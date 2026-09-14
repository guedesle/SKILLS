# Persistência da fronteira editorial no ChatGPT

Este documento define como manter, em duas camadas do ChatGPT, a regra de que as skills editoriais existem para produzir e revisar **prosa humanizada para leitura/publicação**, e não para planejar, especificar ou desenvolver artefatos tecnológicos.

A fonte canônica continua sendo `guedesle/SKILLS`. Nenhuma camada do ChatGPT substitui o repositório; elas apenas tornam a política persistente na experiência de uso.

## Regra canônica

> Skills editoriais não devem ser usadas para planejar, conceber, especificar ou desenvolver software, sistemas, agentes, APIs, integrações, schemas, requisitos, critérios de aceite, backlog, roadmap, ADRs, runbooks, planos de implementação, migração, testes de software, CI/CD, plugins, extensões, MCPs, tools, prompts executáveis ou outros artefatos tecnológicos. Elas podem atuar depois, quando a substância técnica já estiver definida, exclusivamente para transformar esse material em prosa humanizada destinada à leitura, apresentação ou publicação, inclusive artigos científicos e técnico-científicos.

## Camada 1 — Memory / Personalização do ChatGPT

### Objetivo

Manter a preferência de domínio disponível mesmo quando nenhuma skill personalizada estiver carregada.

### Entrada recomendada para o Memory summary

```text
As skills de escrita/editoriais do usuário são exclusivamente para textos humanizados destinados à leitura ou publicação, incluindo artigos científicos, acadêmicos, institucionais e técnico-científicos. Não usar essas skills para planejamento técnico, especificação, arquitetura, requisitos, backlog, implementação, testes, CI/CD, agentes, plugins, APIs ou outros artefatos tecnológicos. Em tarefas tecnológicas, usar workflows de engenharia/produto; recorrer às skills editoriais somente depois, para humanizar ou publicar conteúdo técnico já definido.
```

### Procedimento de persistência

1. Abrir `Settings -> Personalization -> Memory summary -> Manage`.
2. Verificar se a regra acima, ou uma formulação semanticamente equivalente, está presente.
3. Se estiver ausente ou ambígua, solicitar a inclusão/ajuste no próprio Memory summary.
4. Não considerar uma confirmação em conversa como prova de que o Memory summary foi alterado.
5. Após qualquer alteração relevante na família de skills editoriais, revisar esta entrada para manter coerência com o contrato canônico.

### Critério de verificação

A camada só deve ser considerada `MEMORY_VERIFIED` quando o conteúdo puder ser observado no Memory summary da conta. Até lá, usar `MEMORY_RULE_DOCUMENTED`.

## Camada 2 — Skill/plugin instalado no ChatGPT

### Objetivo

Garantir que o comportamento operacional venha do pacote versionado e testado, não apenas da memória da conta.

### Fonte e versões de referência

- `guedesle-writing` 2.0.0;
- `writing-workflow` 2.0.0;
- `plan-editorial-content` 1.0.0;
- `architect-text` 2.0.0;
- `write-technical-content` 2.0.0.

O `guedesle-writing` 2.0.0 exclui explicitamente artefatos tecnológicos do domínio editorial e contém evals adversariais de `trigger_negative` e `behavior`.

### Rotas de distribuição

Quando a superfície permitir **Personal Skills**:

```bash
python scripts/package_chatgpt_skills.py --check
python scripts/package_chatgpt_skills.py
```

Quando a superfície permitir plugin **skills-only**:

```bash
python scripts/package_plugins.py --check
python scripts/package_plugins.py
```

O pacote esperado é:

```text
guedesle-writing-v2.0.0.zip
```

### Regra de atualização

Não existe sincronização automática `GitHub -> skill/plugin instalado`.

Após qualquer mudança canônica:

1. executar o gate completo do repositório;
2. gerar novamente o bundle/plugin;
3. atualizar ou reinstalar o artefato na superfície de destino;
4. reiniciar/atualizar a superfície quando necessário;
5. executar os testes de aceite abaixo no runtime real;
6. somente então registrar `INSTALLED`/`VERIFIED`.

## Testes de aceite no runtime do ChatGPT

### Devem acionar o domínio editorial

- `Transforme estas notas e fontes em um artigo científico claro, estruturado e revisado.`
- `Já tenho a arquitetura e os requisitos aprovados; transforme esse material em um artigo técnico para publicação.`
- `Reestruture este relatório institucional para leitura de executivos sem alterar os fatos.`

### Não devem acionar o domínio editorial

- `Planeje a arquitetura de microsserviços desta aplicação.`
- `Crie a especificação técnica de um plugin para o Obsidian com requisitos, arquitetura e critérios de aceite.`
- `Decomponha este projeto de software em épicos, histórias, backlog e roadmap de implementação.`
- `Defina schemas, tools e contratos de um agente de IA para produção.`
- `Escreva um plano de refatoração com testes, CI/CD e estratégia de migração deste repositório.`
- `Crie um ADR para decidir entre PostgreSQL e MongoDB.`
- `Crie um runbook operacional para executar a migração em produção.`

### Resultado esperado nos casos negativos

O runtime deve interromper o roteamento editorial e usar uma capacidade de engenharia/produto apropriada. Não deve produzir outline editorial como substituto de especificação técnica.

## Estados de persistência

Use estados explícitos para evitar alegações não verificadas:

- `SOURCE_MERGED` — política presente em `main` no repositório canônico;
- `CI_VERIFIED` — gate completo do repositório passou no commit/PR relevante;
- `DISTRIBUTION_READY` — bundle/plugin gerado e validado;
- `MEMORY_RULE_DOCUMENTED` — regra para Memory definida, mas não observada na conta;
- `MEMORY_VERIFIED` — regra observada no Memory summary;
- `INSTALLED` — versão instalada observada na superfície ChatGPT de destino;
- `RUNTIME_VERIFIED` — testes de aceite executados na superfície instalada;
- `WORKSPACE_SHARED` — plugin efetivamente compartilhado/listado no workspace, quando aplicável.

Nunca inferir `MEMORY_VERIFIED`, `INSTALLED`, `RUNTIME_VERIFIED` ou `WORKSPACE_SHARED` apenas porque a fonte GitHub passou no CI.

## Manutenção

Sempre que houver nova versão do `guedesle-writing` ou alteração dos gatilhos editoriais:

1. revisar `trigger_positive`, `trigger_negative` e `behavior`;
2. manter casos adversariais de engenharia reais;
3. executar o gate canônico;
4. atualizar este documento se o contrato mudar;
5. verificar as duas camadas do ChatGPT separadamente.

A fronteira de domínio é um requisito de regressão permanente, não uma preferência estilística temporária.
