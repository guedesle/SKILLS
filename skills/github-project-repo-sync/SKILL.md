---
name: github-project-repo-sync
description: Sincronize declarativamente um GitHub Project v2 com um repositório usando estado desejado versionado, associação de issues, campos, cronograma e estado observado. Use para reconciliar/corrigir Project e repositório; para auditoria sem mutação use github-project-drift-audit.
---

# GitHub Project ↔ Repository Sync

Execute reconciliação declarativa entre um repositório e seu GitHub Project v2 sem reconstruir manualmente o backlog.

## Convenção esperada

A implementação concreta pode variar, mas prefira uma estrutura equivalente a:

- manifesto de estado desejado versionado no repositório;
- reconciliador determinístico para GitHub Projects v2;
- estado observado regenerado após execução autenticada;
- política explicitamente não destrutiva para itens não gerenciados.

Quando o repositório já fornecer caminhos/scripts próprios, use-os em vez de inventar novos nomes.

## Pré-condições

1. Identifique Project, owner e repositório gerenciado a partir do manifesto/configuração real.
2. Confirme ferramentas e autenticação exigidas pela implementação existente.
3. Para operações via GitHub CLI/GraphQL, valide escopos suficientes para Projects e repositório.
4. Nunca exponha tokens, PATs ou secrets em logs, commits ou respostas.

## Fluxo

1. Leia a fonte declarativa e identifique membership, campos, datas, status e demais propriedades gerenciadas.
2. Leia o reconciliador apenas quando necessário para validar comportamento ou diagnosticar falha.
3. Execute o reconciliador existente do repositório.
4. Se houver erro de autorização/infraestrutura, corrija essa camada sem enfraquecer a política declarativa.
5. Releia o estado observado/live depois da mutação.
6. Classifique divergências por categoria: membership, timeline, schema/campos, auth/infra ou manifesto desatualizado.
7. Preserve itens não gerenciados por padrão.
8. Não confunda associação ao Project com conclusão do trabalho.

## Mudanças de cronograma ou metadados

Altere primeiro a fonte declarativa canônica e depois sincronize. Editar apenas a interface do Project cria drift e deve ser evitado quando o campo é gerenciado.

## Critérios de sucesso

Só declare sincronização concluída quando:

- a intenção versionada representa o estado esperado;
- o reconciliador termina sem erro;
- o estado observado/live é atualizado após a execução;
- não há divergências gerenciadas conhecidas.

## Saída

Informe Project/repositório, itens alterados, status final, divergências restantes e qualquer bloqueio externo.