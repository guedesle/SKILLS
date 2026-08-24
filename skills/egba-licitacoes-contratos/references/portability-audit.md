# Auditoria de portabilidade — egba-licitacoes-contratos

**Classificação:** `GLOBAL_READY`

## Sinais avaliados

- nenhum path absoluto Windows/POSIX;
- nenhum endpoint de loopback ou hostname privado;
- nenhum path de skill específico de projeto (`.agents/.claude/.opencode`);
- nenhum ID local, schema operacional ou dependência de repositório necessária para executar a capacidade;
- o nome EGBA e o Regulamento de Licitações e Contratos são o próprio domínio da skill, não uma dependência acidental de projeto.

## Blockers

Nenhum blocker estrutural de portabilidade identificado.

## Guardrails preservados

A classificação `GLOBAL_READY` não converte a skill em autoridade normativa. Permanecem obrigatórios os guardrails de freshness, confirmação da versão oficial, atualização monetária, atos internos de alçada, legislação superveniente e validação jurídica/decisória quando material.

## Resultado

A skill pode ser promovida ao catálogo canônico como capacidade de domínio institucional da EGBA, sem adaptador local. A distribuição deve preservar seus arquivos auxiliares e evals.
