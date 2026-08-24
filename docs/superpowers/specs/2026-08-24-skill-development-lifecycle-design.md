# Skill Development Lifecycle — Design

## Objetivo

Transformar `guedesle/SKILLS` em uma fábrica governada de skills capaz de criar, validar, avaliar, generalizar, promover, distribuir e manter skills reutilizáveis para ChatGPT e Codex com low-HITL por padrão.

## Baseline

O repositório já contém governança central, orquestração low-HITL, batch quality gate, controle de escalonamento, handoff, ciclo GitHub, roteamento adaptativo de modelos, contratos de execução, governança de fontes e empacotamento determinístico para ChatGPT. A nova arquitetura não duplica essas capacidades: compõe e especializa o que já existe.

## Princípios

1. `guedesle/SKILLS` continua sendo a fonte canônica das skills gerais.
2. Skills específicas de projeto não são promovidas por cópia literal: passam por auditoria de portabilidade e extração da parte transversal.
3. Falhas determinísticas não geram HITL: corrigir em lote, revalidar e só escalar decisão material.
4. Construção, validação, avaliação, promoção e distribuição permanecem componentes separados e testáveis.
5. O validador estrutural nunca substitui avaliação comportamental.
6. Maior capacidade de modelo não amplia autorização operacional.
7. O mesmo conteúdo canônico pode ser distribuído para múltiplos hosts, mas instalação e ativação são verificadas por superfície.

## Arquitetura

```text
chatgpt-governed-workflow
        |
        +-- desenvolvimento geral de repositório
        |     +-- low-hitl-orchestration
        |     +-- batch-quality-gate
        |     +-- decision-escalation-control
        |     +-- github-branch-pr-lifecycle
        |
        +-- desenvolvimento de skill
              +-- skill-development-lifecycle
                    +-- skill-authoring
                    +-- skill-validator
                    +-- skill-evaluator
                    +-- skill-portability-audit
                    +-- skill-promotion
                    +-- skill-distribution
```

`chatgpt-governed-workflow` é uma meta-skill fina. Ela seleciona o workflow aplicável e delega, em vez de reimplementar contratos das skills filhas.

`skill-development-lifecycle` é a meta-skill especializada para o ciclo de vida de skills e orquestra as seis capacidades abaixo.

## Componentes

### `skill-authoring`

Responsabilidade: criar ou refatorar uma skill no formato Agent Skills.

Contrato mínimo:
- nome em kebab-case;
- `SKILL.md` com frontmatter YAML válido;
- `name` consistente com diretório e registro;
- `description` orientada a descoberta/ativação;
- instruções com fronteira clara de responsabilidade;
- recursos auxiliares somente quando aumentarem repetibilidade;
- sem segredos, IDs ou paths locais acidentalmente incorporados.

### `skill-validator`

Responsabilidade: validação determinística do pacote e catálogo.

Deve verificar:
- YAML real no frontmatter;
- SemVer;
- consistência `registry.json` ↔ diretório ↔ frontmatter;
- documentação vinculada à skill correta, inclusive versão por entrada;
- referências e recursos locais existentes;
- paths seguros e ausência de symlinks em bundles;
- duplicidade de nomes, paths e mirrors;
- arquivos canônicos não registrados e registros sem arquivo;
- fixtures negativas para evitar falso PASS.

A implementação Python usa `PyYAML>=6,<7` e testes `unittest`, evitando dependência de framework adicional.

### `skill-evaluator`

Responsabilidade: avaliação comportamental baseada em casos declarativos.

Formato inicial: `evals/*.yaml` opcional por skill, com cenários:
- `trigger_positive`: pedidos que devem selecionar a skill;
- `trigger_negative`: pedidos que não devem selecioná-la;
- `behavior`: invariantes de comportamento/saída;
- `portability`: tokens proibidos/permitidos quando aplicável.

Nesta primeira versão, o gate central valida o schema e coerência dos evals e executa checks determinísticos. Execução LLM de trigger/behavior é tratada como camada de host quando disponível; o repositório não deve alegar resultado de avaliação de modelo que não executou.

### `skill-portability-audit`

Responsabilidade: classificar uma skill candidata como:
- `PROJECT_ONLY`;
- `GENERALIZABLE`;
- `GENERAL_WITH_ADAPTER`;
- `GLOBAL_READY`.

Sinais de dependência local incluem nomes de projeto, caminhos absolutos, IDs institucionais, schemas exclusivos, URLs internas e regras que não preservam sentido fora do projeto.

### `skill-promotion`

Responsabilidade: promover capacidade reutilizável para o catálogo central.

Fluxo:
1. receber skill local/candidata;
2. executar auditoria de portabilidade;
3. extrair comportamento transversal;
4. definir versão SemVer e `origin`;
5. criar/atualizar skill central;
6. manter variante/adaptador local quando necessário;
7. atualizar `registry.json`, README e status;
8. executar gate completo antes do merge.

### `skill-distribution`

Responsabilidade: empacotar e orientar distribuição por host sem confundir disponibilidade com instalação efetiva.

Destinos iniciais:
- ChatGPT: bundle determinístico individual quando a superfície de Personal Skills suportar upload;
- Codex USER: `$HOME/.agents/skills/<nome>` por diretório ou symlink;
- projeto/consumidor: mirrors declarados no registro;
- distribuição reutilizável: plugin skill-only quando adotado pelo host.

## Pipeline de validação

```text
L0 syntax/schema
  YAML, SemVer, nomes, paths
L1 integridade
  registry, docs, referências, recursos
L2 segurança
  secrets, symlinks, paths inseguros, dados locais acidentais
L3 trigger eval
  schema/casos positivos e negativos; execução LLM somente quando host suportar
L4 behavioral eval
  invariantes declarativos; execução LLM somente quando host suportar
L5 portability
  classificação e blockers de promoção
L6 distribution
  bundle, manifesto, descoberta/paths esperados
L7 repository gate
  diff, branch, CI, revisão, mergeability
```

Falha determinística em L0–L6 segue:

```text
FAIL -> corrigir automaticamente -> repetir gate afetado -> batch gate completo -> PASS
```

HITL só é exigido para alteração material de escopo, risco, autorização, contrato incompatível, ação irreversível ou informação indispensável não inferível.

## Estrutura de evals

```text
skills/<nome>/
  SKILL.md
  evals/
    trigger-positive.yaml
    trigger-negative.yaml
    behavior.yaml
  references/
  scripts/
  assets/
```

Evals são opcionais para skills legadas na primeira versão, mas obrigatórios para novas meta-skills/skills deste lifecycle. O validador reporta cobertura e diferencia ausência permitida de arquivo inválido.

## Scripts e testes

Adicionar:
- `scripts/skill_validation.py`: biblioteca reutilizável de parsing/validação;
- `scripts/validate_skill_evals.py`: valida evals declarativos;
- `scripts/audit_skill_portability.py`: auditoria determinística de portabilidade;
- `tests/test_skill_validation.py`;
- `tests/test_skill_evals.py`;
- `tests/test_skill_portability.py`;
- `requirements-dev.txt` com PyYAML.

`sync_skills.py` passa a consumir a biblioteca comum, eliminando parser YAML manual e checks de versão globalmente permissivos.

`package_chatgpt_skills.py` também reutiliza o parser comum para evitar duas implementações de frontmatter.

## CI

O workflow central deve:
1. instalar `requirements-dev.txt`;
2. executar `python -m unittest discover -s tests -p "test_*.py"`;
3. executar `python scripts/sync_skills.py --check`;
4. executar `python scripts/validate_skill_evals.py`;
5. executar `python scripts/package_chatgpt_skills.py --check`;
6. compilar scripts Python;
7. executar smoke tests de bundles e mirrors já existentes.

## Versionamento e documentação

As novas skills começam em `1.0.0`.

`skills-central-governance` recebe MINOR quando passar a delegar formalmente para o lifecycle de construção/validação.

README, `general-skills-status.md`, `registry.json` e `AGENTS.md` devem convergir no mesmo lote.

## Critérios de aceite

O lote está pronto para merge quando:
- as oito novas definições (`chatgpt-governed-workflow`, `skill-development-lifecycle` e seis skills especializadas) existem e estão registradas;
- frontmatter inválido produz falha real;
- versão divergente da entrada correta no README/status produz falha;
- evals malformados produzem falha;
- auditoria de portabilidade classifica fixtures project-only/generalizáveis;
- bundles ChatGPT continuam determinísticos e válidos;
- instalação Codex global está documentada como `$HOME/.agents/skills`;
- testes e gates passam;
- PR está mergeável e sem bloqueadores materiais;
- `main` pós-merge é verificado.
