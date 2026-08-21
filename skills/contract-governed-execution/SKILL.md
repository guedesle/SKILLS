---
name: contract-governed-execution
description: Governe execuções de maior risco por contratos machine-readable e fail-closed. Use quando escopo, autorização, limites, stop conditions, aprovação humana e trilha de evidências precisam ser verificáveis automaticamente antes e durante uma ação. Generaliza o padrão sem depender de um domínio específico.
---

# Contract-Governed Execution

Use esta skill para transformar políticas de execução em contratos verificáveis por máquina, reduzindo HITL repetitivo sem permitir que automação atravesse limites não aprovados.

## Princípio

**O runtime não interpreta ausência de regra como permissão.**

Para ações de maior risco, autorização, escopo e limites devem existir em formato estruturado e validar antes da execução.

## Contrato mínimo

Quando aplicável, represente explicitamente:

- identidade/owner do trabalho;
- escopo e alvos permitidos;
- janela temporal;
- ações/capacidades permitidas;
- ações proibidas;
- limites operacionais;
- stop conditions;
- aprovação humana exigida;
- estado de autorização;
- trilha/evidence ledger;
- condição de encerramento.

## Fail-closed

Prefira schemas que:

- rejeitem campos desconhecidos quando isso protege a fronteira;
- exijam os campos críticos;
- usem enums para estados sensíveis;
- não tenham defaults que transformem ausência de decisão em autorização;
- bloqueiem explicitamente combinações proibidas.

## Gates

Antes de executar:

1. validar schema;
2. validar autorização/estado;
3. validar escopo e janela;
4. validar limites e stop conditions;
5. confirmar approver quando exigido;
6. criar/abrir ledger de execução.

Durante a execução:

- registrar ação e alvo;
- registrar resultado e impacto observado;
- reavaliar stop conditions;
- interromper automaticamente quando uma condição de parada for satisfeita;
- não expandir escopo por inferência.

Depois:

- registrar resultado final;
- reconciliar evidência com o contrato;
- apontar desvios;
- exigir revisão humana apenas para decisão material, exceção ou aceitação de risco.

## Autotestes

Valide o próprio contrato com casos negativos, por exemplo:

- autorização ausente;
- escopo vazio;
- ação proibida marcada como permitida;
- stop conditions removidas;
- high-risk marcado como `not-applicable` para autorização;
- campo crítico tornado opcional;
- unknown field aceito quando o contrato exige `additionalProperties: false`.

## Ledger

Uma entrada deve ser suficiente para reconstruir o que aconteceu sem depender da memória do agente. Inclua, quando pertinente:

- timestamp;
- etapa/ação;
- target/recurso;
- executor;
- classe de risco;
- autorização verificada;
- resultado;
- impacto observado;
- stop condition status;
- referência à evidência.

## HITL

Contrato válido permite automatizar checks repetitivos. HITL permanece obrigatório para exceções, alterações de escopo, overrides, autorizações reais, ações irreversíveis ou decisões materiais.

## Saída esperada

Informe contrato utilizado, validações executadas, estado fail-closed, ledger/evidência produzidos, exceções e próximo gate humano quando necessário.

## Origem

Generalizada dos contratos machine-readable e validadores fail-closed usados no `guedesle/cyber-skills-framework`; remove campos e semântica exclusivos de operações de cibersegurança.
