---
name: skills-central-governance
description: Governe o catálogo central de skills gerais em guedesle/SKILLS. Use ao criar, promover, versionar, atualizar, documentar ou distribuir uma skill reutilizável entre repositórios. Não promova automaticamente skills estritamente específicas de um projeto.
---

# Central Skills Governance

O repositório `guedesle/SKILLS` é a fonte canônica das skills gerais e reutilizáveis do perfil.

## Regra principal

Toda skill classificada como **geral/reutilizável** deve:

1. existir canonicamente em `skills/<nome>/SKILL.md` neste repositório;
2. possuir versão registrada em `registry.json`;
3. possuir documentação e link no `README.md`;
4. registrar origem/proveniência e, quando houver, repositórios espelho;
5. ser distribuída aos espelhos a partir da versão central;
6. receber primeiro neste repositório qualquer alteração que modifique seu comportamento geral.

## Geral versus específica

Promova para o catálogo central quando a skill puder ser usada em mais de um projeto sem depender de nomes, IDs, caminhos, schemas ou regras institucionais exclusivos de um único repositório.

Mantenha local quando a skill depender essencialmente de um projeto específico. Se houver valor reutilizável, extraia uma versão geral para o catálogo central e mantenha a variante local como adaptação.

## Criação de nova skill

Ao criar uma skill geral:

1. escolha nome estável em kebab-case;
2. crie `skills/<nome>/SKILL.md`;
3. adicione a skill a `registry.json` com versão SemVer;
4. documente no índice e na seção detalhada do `README.md`;
5. registre targets de espelhamento, se existirem;
6. rode `python scripts/sync_skills.py --check`;
7. após revisão, rode `python scripts/sync_skills.py --apply` para atualizar os espelhos.

## Atualização

Mudanças comportamentais devem atualizar a versão:

- PATCH: correções e esclarecimentos sem mudança de contrato;
- MINOR: nova capacidade compatível;
- MAJOR: mudança incompatível de contrato, gatilhos ou saída.

A alteração deve ser feita primeiro na cópia central. Não trate uma cópia espelho como fonte de verdade.

## Segurança

- nunca versionar tokens, PATs ou secrets;
- o sincronizador não apaga skills não gerenciadas;
- `--check` deve ser usado antes de `--apply` em mudanças amplas;
- repositórios espelho somente são alterados quando declarados explicitamente no registro.

## Saída esperada

Ao concluir uma operação de governança, informe: skill, versão anterior/nova, arquivos centrais alterados, espelhos afetados e resultado da validação.