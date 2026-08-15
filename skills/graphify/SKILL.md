---
name: graphify
description: Use um grafo Graphify de repositório para descobrir relações arquiteturais antes de buscas amplas no código, atualizando o grafo após mudanças relevantes e confirmando detalhes diretamente nos arquivos antes de editar.
---

# Graphify

## Quando usar

Use em repositórios que possuam `graphify-out/graph.json` ou outro grafo Graphify configurado e quando a pergunta envolver dependências, fluxo, arquitetura, chamadas ou localização provável de comportamento.

## Workflow

1. Se existir grafo local, consulte primeiro: `graphify query "<pergunta>"`.
2. Use o resultado para reduzir o espaço de busca e localizar relações relevantes.
3. Leia diretamente os arquivos candidatos antes de modificar código.
4. Após alterar código que mude relações relevantes, atualize o grafo com `graphify update .`.
5. Quando houver grafo legado/externo explicitamente configurado, consulte-o com `--graph <caminho>` apenas como referência comparativa.

## Regras

- o grafo acelera navegação, mas não substitui leitura dos arquivos alterados;
- grafos desatualizados não são autoridade sobre o código atual;
- grafos legados/externos são referências comparativas, salvo declaração explícita em contrário;
- não invente caminhos de grafo: descubra-os no repositório ou configuração.

## Saída esperada

Relate relações encontradas, arquivos confirmados, eventuais divergências entre grafo e código e se o grafo precisa ser atualizado.