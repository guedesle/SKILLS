---
name: writing-workflow
description: Use when a human-facing text intended for publication or formal reading needs multiple editorial stages such as planning, textual architecture, paragraph design, evidence handling, rhetoric, accessibility, and editorial QA.
---

# Writing Workflow

Use esta skill como **entry point editorial** para transformar intenção de escrita em um fluxo proporcional à tarefa. Seu domínio é **texto para leitura humana**, não desenvolvimento de artefatos tecnológicos.

## Princípio

**Orquestre somente trabalho editorial.**

Uma tarefa de engenharia não deve ser reinterpretada como tarefa de escrita só porque produzirá documentação. O objeto principal da solicitação determina o domínio.

## Gate de entrada: editorial ou técnico?

Antes de carregar qualquer skill editorial, classifique o artefato principal.

### EDITORIAL — pode usar este workflow

Use quando o resultado principal é prosa destinada a leitura humana, por exemplo:

- artigo científico, acadêmico, analítico ou de divulgação;
- ensaio, relatório narrativo ou institucional;
- apresentação, roteiro ou texto editorial;
- texto técnico-científico cuja substância técnica já esteja definida e precise ser comunicada, explicada ou publicada.

### TECNOLÓGICO — não use este workflow

Não use `writing-workflow`, `plan-editorial-content` ou as demais skills editoriais para conceber, planejar ou especificar:

- software, aplicações, sites, plugins, extensões, automações ou MCPs;
- arquitetura de sistemas, agentes, dados, infraestrutura ou integrações;
- requisitos funcionais/não funcionais, critérios de aceite, histórias, épicos, backlog ou roadmap;
- APIs, contratos, schemas, modelos de dados, protocolos ou interfaces;
- planos de implementação, migração, refatoração, testes de software, segurança ou CI/CD;
- ADRs, runbooks ou documentação que funcione como contrato de implementação;
- prompts, tools, skills ou agentes quando o objetivo é definir seu comportamento executável.

Nesses casos, **pare o roteamento editorial** e entregue o controle a um workflow de engenharia/produto apropriado. Não produza um outline editorial como substituto de uma especificação técnica.

As skills editoriais podem ser usadas posteriormente, de forma complementar, apenas quando o usuário pedir para transformar material técnico já definido em texto humanizado para publicação, apresentação ou leitura formal.

## Classificação editorial

Depois de passar pelo gate editorial, determine:

- gênero textual;
- objetivo comunicacional e público;
- se existe texto de partida;
- se a estrutura já está definida;
- se há afirmações que exigem evidência;
- se o conteúdo é científico ou técnico-científico em forma de prosa;
- se tom, acessibilidade, QA ou alinhamento institucional são requisitos materiais.

Pergunte apenas quando uma lacuna realmente impedir uma decisão estrutural ou factual segura.

## Roteamento editorial

Use as skills especializadas conforme a necessidade:

1. `plan-editorial-content` — quando objetivo comunicacional, tese, público, recorte ou outline editorial ainda precisam ser definidos.
2. `architect-text` — quando a ordem de seções, funções dos parágrafos ou dependências entre ideias precisam ser projetadas ou refeitas.
3. `design-paragraphs` — para construir ou refatorar parágrafos pela função discursiva que devem cumprir.
4. `write-with-evidence` — para afirmações materiais, causalidade, inferência, incerteza, fontes e limites da evidência.
5. `write-technical-content` — somente para prosa técnico-científica destinada a leitores humanos, quando a substância técnica já estiver definida; nunca para criar especificações ou decisões de engenharia.
6. `calibrate-rhetoric` — para adequar tom, força argumentativa e intensidade retórica à evidência, ao público e ao contexto.
7. `improve-accessible-writing` — para clareza, legibilidade, leitura em tela e redução de carga cognitiva.
8. `review-editorial-quality` — para QA editorial, achados, bloqueios e prontidão do texto.
9. `assess-editorial-alignment` — quando princípios editoriais, institucionais ou de governança precisam ser verificados explicitamente.

## Fluxos recomendados

### Criação de texto do zero

```text
plan-editorial-content
  ↓
architect-text
  ↓
design-paragraphs
  ↓
redação especializada conforme o gênero
  ↓
calibrate-rhetoric / improve-accessible-writing quando necessários
  ↓
review-editorial-quality
  ↓
assess-editorial-alignment quando aplicável
```

### Artigo científico ou técnico-científico

```text
plan-editorial-content
  ↓
architect-text
  ↓
write-with-evidence
  ↓
design-paragraphs / write-technical-content quando necessário
  ↓
review-editorial-quality
```

### Refatoração estrutural de texto

```text
texto existente
  ↓
architect-text
  ↓
design-paragraphs
  ↓
write-with-evidence se houver afirmações materiais
  ↓
review-editorial-quality
```

### Revisão pontual

Delegue diretamente à capacidade adequada. Exemplos:

- clareza e leitura em tela → `improve-accessible-writing`;
- evidência/causalidade → `write-with-evidence`;
- parágrafo confuso → `design-paragraphs`;
- tom excessivo → `calibrate-rhetoric`;
- prosa técnico-científica para publicação → `write-technical-content`;
- revisão final → `review-editorial-quality`.

Não crie etapas artificiais apenas para usar todas as skills.

## Preservação de conteúdo

Ao revisar ou reescrever:

- preserve fatos, números, citações, ressalvas e requisitos já definidos que não tenham sido explicitamente autorizados a mudar;
- não invente fonte, dado ou intenção do autor;
- não fortaleça uma conclusão além do suporte disponível;
- diferencie problema estrutural, problema de estilo e problema factual;
- mantenha terminologia técnica quando ela for necessária para precisão, mas remova jargão que não produza valor;
- não altere decisões de engenharia, contratos técnicos ou comportamento de sistema sob o pretexto de melhorar a redação.

## Iteração e QA

Quando a tarefa tiver múltiplas etapas editoriais:

1. produza a versão de trabalho;
2. execute o QA editorial pertinente;
3. corrija falhas determinísticas ou claramente editoriais sem pedir aprovação intermediária;
4. retorne à arquitetura textual somente se a revisão revelar problema estrutural real;
5. registre lacunas factuais ou de evidência que não possam ser resolvidas com segurança;
6. encerre quando o texto cumprir objetivo, estrutura, precisão, clareza e critérios definidos.

## Portabilidade de host

O contrato editorial desta skill é independente de filesystem, modelo, CLI ou fornecedor.

- não exija paths locais, scripts ou comandos para executar a função editorial principal;
- use arquivos, conectores e ferramentas disponíveis no host apenas como fontes ou destinos opcionais;
- quando uma capacidade externa não estiver disponível, produza somente o texto, diagnóstico editorial ou handoff que ainda possa ser concluído no próprio host;
- não alegue ter lido, alterado ou salvo um recurso externo quando essa ação não ocorreu.

## Saída esperada

Conforme a tarefa editorial, entregue apenas o necessário entre:

- briefing ou plano de conteúdo;
- arquitetura textual;
- plano/refatoração de parágrafos;
- texto redigido ou revisado;
- mapa de evidências e lacunas;
- ajustes de retórica e acessibilidade;
- relatório de QA editorial;
- estado de prontidão e pendências materiais.

Nunca use esta lista de saídas para substituir artefatos próprios de engenharia, produto ou desenvolvimento.