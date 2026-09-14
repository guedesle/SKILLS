# Changelog — `architect-text`

## 2.0.0 — 2026-09-14

- restringe o domínio a arquitetura de **textos destinados à leitura humana**;
- proíbe uso para arquitetura de software, sistemas, agentes, dados, infraestrutura, APIs e outros artefatos tecnológicos;
- remove gatilhos editoriais ambíguos associados a requisitos e documentação de implementação;
- substitui a dependência `plan-content` por `plan-editorial-content`;
- adiciona evals `trigger_positive`, `trigger_negative` e `behavior` para distinguir arquitetura textual de arquitetura tecnológica;
- preserva a possibilidade de organizar a comunicação de material técnico já definido sem alterar decisões de engenharia.

## 1.2.0 — 2026-08-16

- substitui nomenclatura abstrata por termos autoexplicativos em português corrente;
- `motivo textual` passa a ser apresentado como **finalidade do texto**;
- `ato comunicativo dominante` passa a ser **função principal do texto**;
- `transformação do leitor` passa a ser **resultado esperado da leitura**;
- `movimento macro` passa a ser **sequência lógica do texto**;
- `contrato de seção` passa a ser **objetivo e requisitos da seção**;
- `matriz paragrafal` passa a ser **plano de parágrafos**;
- `grafo de dependências argumentativas` passa a ser **dependências entre ideias**;
- `handoff` passa a ser **instruções para a próxima etapa**;
- IDs opacos como `S2.P4` deixam de ser apresentados ao usuário; o padrão passa a `secao-02-paragrafo-04` / **Seção 2 · Parágrafo 4**;
- o artefato final passa a se chamar **Plano de Arquitetura do Texto**.

## 1.1.0 — 2026-08-16

- formaliza a finalidade do texto como entrada estruturada;
- adiciona parâmetros de intenção, público, gênero, evidência, escopo, restrições, voz e ritmo;
- integra diretamente os tipos funcionais de `design-paragraphs`;
- adiciona padrões de finalidade → sequência de parágrafos;
- cria planejamento de parágrafos com identificação estável;
- adiciona dependências entre ideias, plano de evidências, ligações e critérios de aceite;
- cria o artefato canônico de arquitetura textual;
- adiciona revisão estrutural e teste de variação;
- formaliza a passagem entre `architect-text` e `design-paragraphs`.

## 1.0.0 — 2026-08-14

- versão inicial canônica: mapa de seções, requisitos de seção, plano de parágrafos, progressão e instruções para redação.
