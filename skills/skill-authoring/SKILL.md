---
name: skill-authoring
description: "Crie ou refatore uma skill reutilizável no formato Agent Skills. Use quando o trabalho principal for escrever o contrato de uma skill, seu SKILL.md e recursos auxiliares; não use para apenas validar, promover ou distribuir uma skill já pronta."
---

# skill-authoring

Converter um comportamento desejado em um pacote Agent Skills claro, delimitado e testável.

## Responsabilidade

Esta skill possui responsabilidade específica no lifecycle. Componha as skills de governança existentes em vez de duplicar seus contratos.

## Workflow

1. Fixe objetivo, usuários, gatilhos, não-gatilhos, entradas, saídas e critérios de aceite.
2. Escolha nome estável em kebab-case e mantenha `SKILL.md` como ponto de entrada.
3. Escreva `description` discriminativa para descoberta implícita e explicite fronteiras de responsabilidade.
4. Inclua `references/`, `scripts/`, `assets/` ou templates somente quando aumentarem repetibilidade.
5. Crie evals positivos, negativos e comportamentais para novas skills deste catálogo.
6. Entregue o pacote para `skill-validator`; não declare prontidão com base apenas em revisão textual.

## Stop e escalation

- Escopo funcional material ainda não definido.
- A skill exigiria secret, credencial ou política local como parte do contrato geral.
- A alteração incompatível exige decisão de versionamento MAJOR.

## Saída esperada

- pacote de skill;
- decisões de fronteira;
- recursos auxiliares necessários;
- handoff para validação.
