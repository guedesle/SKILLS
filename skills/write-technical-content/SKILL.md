---
name: write-technical-content
description: Use when technical or scientific subject matter is already defined and needs to be turned into precise, human-facing prose for publication, formal communication, explanation, or academic/scientific reading.
---

# Write Technical Content

## Objetivo

Redigir ou revisar **prosa técnico-científica para leitura humana** sem assumir o papel de engenharia, produto ou arquitetura.

A skill trabalha a comunicação de conteúdo técnico já definido. Ela não cria o conteúdo normativo ou executável de um sistema.

## Quando usar

Use quando houver material técnico, científico, institucional ou operacional já estabelecido e o objetivo for:

- transformá-lo em texto claro, preciso e legível;
- redigir ou revisar artigo científico, seção metodológica, análise técnica ou relatório para leitores humanos;
- explicar um processo ou decisão já definida;
- melhorar precisão terminológica, coesão e verificabilidade de uma narrativa técnica;
- adaptar conteúdo técnico para publicação, apresentação ou comunicação formal.

## Quando NÃO usar

Não use esta skill para criar ou decidir:

- especificações funcionais ou técnicas de software;
- requisitos de produto ou sistema;
- critérios de aceite de implementação;
- arquitetura, componentes, integrações, APIs, contratos ou schemas;
- modelos de dados, protocolos ou interfaces;
- planos de implementação, migração, refatoração, testes de software, segurança ou CI/CD;
- backlog, épicos, histórias de usuário ou roadmap;
- comportamento executável de plugins, extensões, agentes, MCPs, prompts, tools ou skills;
- ADRs, runbooks ou documentação que seja usada como contrato de engenharia.

Quando o pedido principal for um artefato técnico de desenvolvimento, encerre esta skill e encaminhe para um workflow de engenharia apropriado. Só retorne depois que a substância técnica estiver definida e houver uma tarefa genuína de redação para humanos.

## Procedimento

1. Identifique objetivo comunicacional, audiência e material técnico já definido.
2. Preserve termos, fatos, parâmetros, unidades, versões e decisões técnicas existentes.
3. Separe afirmação, evidência, interpretação, limitação e recomendação quando necessário.
4. Prefira termos definidos e relações verificáveis a formulações vagas.
5. Use passos numerados somente quando estiver explicando uma sequência já estabelecida ao leitor.
6. Explicite incertezas, exceções e limites apenas quando sustentados pelo material-fonte.
7. Melhore coerência, transições, legibilidade e precisão sem alterar o contrato técnico subjacente.
8. Sinalize lacunas técnicas em vez de preenchê-las por inferência.

## Saída esperada

- prosa técnico-científica clara e humanizada;
- terminologia consistente;
- ambiguidades de redação identificadas;
- lacunas técnicas sinalizadas sem serem inventadas;
- versão revisada ou nova redação solicitada para leitura humana.

## Limites

Não invente comportamento do sistema, requisito, interface, critério de aceite, decisão de arquitetura, dado de desempenho ou regra regulatória. Não converta uma solicitação de engenharia em uma tarefa editorial apenas porque o resultado será escrito.