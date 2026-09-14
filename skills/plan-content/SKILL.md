---
name: plan-content
description: Use when planning human-facing prose intended for publication or formal reading, especially scientific articles, essays, reports, institutional texts, presentations, or other editorial content whose thesis, scope, audience, evidence, and reading flow still need definition.
---

# Plan Content

## Objetivo

Planejar **conteúdo editorial para leitura humana** antes da redação, com foco em clareza, coerência, evidência, recorte e qualidade de leitura.

Esta skill não é uma skill de engenharia, arquitetura de sistemas, produto, software ou especificação técnica.

## Quando usar

Use quando o artefato principal é um texto destinado a leitores humanos e ainda precisa de direção editorial, escopo, tese, público, evidências ou organização antes da redação.

Exemplos adequados:

- artigo científico ou acadêmico;
- ensaio, artigo de divulgação ou texto analítico;
- relatório narrativo ou institucional destinado à leitura humana;
- apresentação, roteiro ou texto editorial;
- conteúdo técnico-científico cuja substância técnica já esteja definida e precise ser comunicada em forma de prosa.

## Quando NÃO usar

Não use esta skill para planejar, conceber ou especificar artefatos tecnológicos. Isso inclui, entre outros:

- arquitetura de software, sistemas, dados, infraestrutura ou agentes;
- especificações funcionais ou técnicas de software;
- requisitos de produto, histórias de usuário, épicos, backlog ou roadmap de implementação;
- APIs, contratos, schemas, modelos de dados ou integrações;
- planos de implementação, refatoração, migração, testes de software ou CI/CD;
- plugins, extensões, aplicações, automações, MCPs, ferramentas ou prompts executáveis;
- decisões de engenharia, ADRs, runbooks ou documentação usada como contrato de implementação.

Se o objeto principal for tecnológico, encerre o roteamento editorial e transfira a tarefa para uma skill ou workflow de engenharia apropriado. As skills editoriais só podem entrar depois, caso o usuário peça para transformar material técnico já definido em texto humanizado para leitura ou publicação.

## Procedimento

1. Explicite objetivo comunicacional, público, contexto e efeito esperado da leitura.
2. Separe fatos conhecidos, hipóteses, restrições editoriais e lacunas de evidência.
3. Formule tese, pergunta central ou promessa de leitura adequada ao gênero textual.
4. Delimite escopo e fora de escopo do texto, não do sistema ou produto.
5. Estruture um outline proporcional à complexidade e à experiência de leitura.
6. Identifique riscos factuais, editoriais, institucionais ou de interpretação.
7. Defina critérios de qualidade textual e evidências necessárias.
8. Produza handoff para estruturação/redação, sem inventar fatos, requisitos técnicos ou decisões de engenharia.

## Saída esperada

- objetivo comunicacional;
- público;
- contexto;
- tese/pergunta central;
- escopo editorial e fora de escopo;
- outline;
- evidências necessárias;
- riscos e lacunas;
- critérios de qualidade textual;
- próximo passo editorial recomendado.

## Limites

Não transforme um pedido de projeto técnico em um plano editorial disfarçado. Não invente comportamento de sistema, requisito, interface, critério de aceite ou decisão de implementação. Não trate hipótese como fato nem invente fonte.