---
name: writing-workflow
description: Orquestre criação, estruturação, redação e revisão de textos usando as skills editoriais canônicas. Use quando o pedido envolve mais de uma etapa entre planejamento, arquitetura textual, desenho de parágrafos, evidência, redação técnica, retórica, acessibilidade, QA e alinhamento editorial. Para tarefas pontuais, delegue diretamente à skill especializada sem impor um pipeline completo.
---

# Writing Workflow

Use esta skill como **entry point editorial** para transformar intenção de escrita em um fluxo proporcional à tarefa, sem obrigar o usuário a escolher manualmente cada skill do catálogo.

## Princípio

**Orquestre somente o necessário.**

Uma tarefa simples de reescrita, clareza ou revisão não deve acionar automaticamente todo o pipeline editorial. O workflow completo é reservado para criação, refatoração ampla ou revisão multi-etapas.

## Classificação inicial

Determine primeiro:

- o artefato ou gênero textual;
- o objetivo e o público;
- se existe texto de partida;
- se a estrutura já está definida;
- se há afirmações que exigem evidência;
- se o conteúdo é técnico/procedimental;
- se tom, acessibilidade, QA ou alinhamento institucional são requisitos materiais.

Pergunte apenas quando uma lacuna realmente impedir uma decisão estrutural ou factual segura.

## Roteamento editorial

Use as skills especializadas conforme a necessidade:

1. `plan-content` — quando objetivo, tese, público, escopo ou outline ainda precisam ser definidos.
2. `architect-text` — quando a ordem de seções, funções dos parágrafos ou dependências entre ideias precisam ser projetadas ou refeitas.
3. `design-paragraphs` — para construir ou refatorar parágrafos pela função que devem cumprir.
4. `write-with-evidence` — para afirmações materiais, causalidade, inferência, incerteza, fontes e limites da evidência.
5. `write-technical-content` — para requisitos, procedimentos, manuais, documentação e conteúdo técnico operacional.
6. `calibrate-rhetoric` — para adequar tom, força argumentativa e intensidade retórica à evidência, ao público e ao contexto.
7. `improve-accessible-writing` — para clareza, legibilidade, leitura em tela e redução de carga cognitiva.
8. `review-editorial-quality` — para QA editorial, achados, bloqueios e prontidão do texto.
9. `assess-editorial-alignment` — quando princípios editoriais, institucionais ou de governança precisam ser verificados explicitamente.

## Fluxos recomendados

### Criação de texto do zero

```text
plan-content
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

### Refatoração estrutural

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
- documento técnico → `write-technical-content`;
- revisão final → `review-editorial-quality`.

Não crie etapas artificiais apenas para usar todas as skills.

## Preservação de conteúdo

Ao revisar ou reescrever:

- preserve fatos, números, citações, ressalvas e requisitos que não tenham sido explicitamente autorizados a mudar;
- não invente fonte, dado ou intenção do autor;
- não fortaleça uma conclusão além do suporte disponível;
- diferencie problema estrutural, problema de estilo e problema factual;
- mantenha terminologia técnica quando ela for necessária para precisão, mas remova jargão que não produza valor.

## Iteração e QA

Quando a tarefa tiver múltiplas etapas:

1. produza a versão de trabalho;
2. execute o QA editorial pertinente;
3. corrija falhas determinísticas ou claramente editoriais sem pedir aprovação intermediária;
4. retorne à arquitetura somente se a revisão revelar problema estrutural real;
5. registre lacunas factuais ou de evidência que não possam ser resolvidas com segurança;
6. encerre quando o texto cumprir objetivo, estrutura, precisão, clareza e critérios definidos.

## Portabilidade de host

O contrato editorial desta skill é independente de filesystem, modelo, CLI ou fornecedor.

- não exija paths locais, scripts ou comandos para executar a função principal;
- use arquivos, conectores e ferramentas disponíveis no host apenas como fontes ou destinos opcionais;
- quando uma capacidade externa não estiver disponível, produza o texto, diagnóstico, plano ou handoff que ainda possa ser concluído no próprio host;
- não alegue ter lido, alterado ou salvo um recurso externo quando essa ação não ocorreu.

Essa regra preserva compatibilidade entre Codex local e superfícies web de workspace que suportem plugins skills-only.

## Saída esperada

Conforme a tarefa, entregue apenas o necessário entre:

- briefing ou plano de conteúdo;
- arquitetura textual;
- especificação/refatoração de parágrafos;
- texto redigido ou revisado;
- mapa de evidências e lacunas;
- ajustes de retórica e acessibilidade;
- relatório de QA editorial;
- estado de prontidão e pendências materiais.

Não exponha a orquestração interna quando ela não ajudar o usuário a compreender ou revisar o resultado.
