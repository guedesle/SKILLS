# QA do Artefato de Arquitetura Textual

Use esta referência para revisar o artefato produzido por `architect-text` antes do handoff para redação.

## 1. Motivo textual

- O objeto está delimitado?
- O ato comunicativo dominante está claro?
- A transformação `leitor antes → leitor depois` é verificável?
- Existe um centro lógico único ou uma decomposição explícita de centros?
- Público, gênero e contexto de circulação justificam as escolhas estruturais?

**Falha crítica:** arquitetura que poderia permanecer idêntica se o ato comunicativo mudasse de explicar para recomendar, argumentar ou instruir.

## 2. Seções

- Cada seção possui função macro própria?
- Entrada e saída são diferentes?
- A saída de uma seção alimenta a próxima?
- Há seções que existem apenas por tradição de outline, sem produzir mudança no leitor?
- Conteúdo obrigatório foi colocado em uma seção funcional adequada?

**Falha crítica:** seção temática sem pergunta, saída ou dependência justificável.

## 3. Matriz paragrafal

- Cada `Sx.Py` possui uma tipologia dominante?
- A missão está formulada como operação (`verbo + objeto`)?
- Núcleo e desenvolvimento são distinguíveis?
- Virada aparece apenas quando existe mudança lógica real?
- O pouso prepara uma consequência ou dependência concreta?
- Duas operações dominantes estão competindo no mesmo contrato?

**Falha crítica:** parágrafo planejado apenas como “falar sobre X”.

## 4. Sequência tipológica

- A ordem decorre do motivo textual?
- Definições aparecem antes de operações que dependem delas?
- Critérios aparecem antes de comparações?
- Evidência aparece antes de síntese/recomendação que dela depende?
- Objeção existe antes de refutação?
- Diagnóstico e alternativas existem antes de recomendação?

**Falha crítica:** conclusão ou recomendação antes da construção das premissas necessárias.

## 5. Evidências

- Cada evidência possui consumidor identificado?
- Cada parágrafo evidencial possui fonte/insumo previsto?
- Fato, inferência, hipótese, norma e recomendação estão separados?
- Lacunas bloqueantes foram identificadas?

**Falha crítica:** arquitetura exigir uma afirmação que não possui fonte nem tratamento explícito como hipótese/lacuna.

## 6. Transições

- A relação entre blocos foi definida semanticamente?
- Mudanças de escala ou foco possuem ponte?
- Existem parágrafos de transição vazios que apenas anunciam o próximo tópico?

**Falha crítica:** salto lógico que obriga o redator a inventar a relação durante a escrita.

## 7. Ritmo e suporte

- A densidade está adequada ao público e ao gênero?
- Listas, tabelas ou figuras foram preferidas quando a informação não funciona bem em parágrafo?
- Decisões e viradas importantes possuem destaque proporcional?
- Exemplificação não ocupa espaço maior que a função que serve?

## 8. Integração com `design-paragraphs`

- O contrato contém informação suficiente para a redação local?
- A tipologia corresponde à referência canônica?
- O exemplar `CL-*`, se indicado, tem eficácia adequada à tipologia?
- O exemplar foi recomendado por arquitetura estrutural, não por prestígio autoral?

## 9. Teste contrafactual

Antes de aprovar, faça três perguntas:

1. **Se o público mudasse, a arquitetura deveria mudar?** Se sim, o artefato registra por quê?
2. **Se o ato comunicativo mudasse, a sequência paragrafal mudaria?** Se não, talvez a arquitetura esteja apenas temática.
3. **Se um parágrafo fosse removido, qual dependência quebraria?** Se nenhuma, ele pode ser redundante.

## 10. Estados de QA

- **READY** — arquitetura executável sem decisões estruturais relevantes pendentes.
- **READY_WITH_ASSUMPTIONS** — executável, com hipóteses não bloqueantes explicitadas.
- **BLOCKED** — falta parâmetro, evidência ou decisão que altera materialmente a estrutura.
- **REARCHITECT** — o artefato contém falhas de dependência, tipologia ou progressão que exigem redesenho.
