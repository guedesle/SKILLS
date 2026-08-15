---
name: github-project-drift-audit
description: Audite sem mutação o alinhamento entre um GitHub Project v2 e o estado versionado de um repositório, distinguindo desired, observed e live. Use para diagnosticar sincronização; para aplicar correções use github-project-repo-sync.
---

# GitHub Project Drift Audit

Verifique o alinhamento entre Project v2 e repositório sem alterar Project, issues ou arquivos durante o diagnóstico.

## Estados

Distinga:

- **desired**: intenção versionada;
- **observed**: última leitura confirmada do Project;
- **live**: estado atual consultado diretamente, quando disponível.

Nunca trate desired como prova de mutação concluída, nem observed antigo como estado atual.

## Verificações

1. Identifique Project, repositório e política declarativa.
2. Compare versões/schema das fontes quando aplicável.
3. Confira membership esperado/observado e itens ausentes/inesperados.
4. Confira cronograma, campos e valores gerenciados.
5. Identifique aliases/campos reais em vez de assumir nomes.
6. Separe falhas de autenticação/infraestrutura de drift lógico.
7. Verifique se o observed é posterior às alterações do desired.
8. Classifique o resultado:
   - `IN_SYNC`: compatível e sem divergência conhecida;
   - `DRIFT`: divergência objetiva;
   - `STALE`: observed provavelmente desatualizado;
   - `UNVERIFIED`: evidência insuficiente para confirmar o Project.

## Proibições

Durante a auditoria, não mutar Project, issues, datas, campos ou manifesto apenas para fazer o diagnóstico ficar verde.

## Saída

Informe classificação, evidência principal, diferenças por categoria, ação mínima recomendada e declare explicitamente que nenhuma mutação foi realizada.