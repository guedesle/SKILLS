---
name: design-paragraphs
description: Projete e refatore parágrafos por função discursiva, progressão, transição, evidência, ritmo e densidade. Use quando a arquitetura geral existe, mas cada bloco precisa de um contrato mais claro, uma tipologia adequada ou uma construção mais eficaz.
---

# Design Paragraphs

## Missão

Trate o parágrafo como **unidade de operação discursiva**, não como recipiente de frases. Cada parágrafo deve executar uma função dominante identificável, avançar o texto e preparar uma interface coerente com o bloco anterior e o seguinte.

A skill atua localmente. Quando a correção exigir mudar a função de seções inteiras, mover vários blocos ou redefinir a tese/outline, faça handoff para `architect-text` em vez de mascarar um problema estrutural com edição paragrafal.

## Entradas úteis

- texto ou conjunto de parágrafos a revisar;
- gênero e público;
- objetivo da seção;
- tese, requisito ou ideia que precisa sobreviver à refatoração;
- evidências, ressalvas e restrições que não podem ser perdidas;
- nível de intervenção permitido: diagnóstico, reordenação, divisão/fusão ou reescrita.

Se parte dessas entradas estiver ausente, infira apenas o necessário a partir do texto e sinalize incertezas que mudem materialmente a decisão.

## Contrato do parágrafo

Antes de reescrever, identifique quando aplicável:

1. **Âncora** — de onde o parágrafo parte;
2. **Núcleo** — qual operação dominante executa;
3. **Desenvolvimento** — que razões, evidências, detalhes ou etapas sustentam o núcleo;
4. **Virada** — que contraste, limite ou consequência muda a direção;
5. **Pouso** — onde o parágrafo entrega o leitor ao próximo movimento.

Não force todas as posições. Use-as para revelar relações ausentes ou concorrência entre ideias.

## Tipologia operacional

Classifique cada parágrafo por uma função dominante da referência [`references/paragraph-typology.md`](references/paragraph-typology.md):

1. abertura de enquadramento;
2. tese ou proposição;
3. definição ou conceituação;
4. explicação causal;
5. sustentação evidencial;
6. exemplificação ou ilustração;
7. classificação ou enumeração analítica;
8. comparação ou analogia;
9. contraste ou concessão;
10. refutação ou objeção–resposta;
11. problema–resposta;
12. descrição analítica;
13. narrativa ou evento;
14. procedimental ou instrucional;
15. transição ou ponte;
16. síntese ou integração;
17. implicação ou recomendação;
18. fechamento ou conclusão local.

Uma função secundária é aceitável apenas quando serve ao núcleo. Se duas operações disputarem o parágrafo, divida ou reordene.

## Procedimento

### 1. Leia o parágrafo na arquitetura da seção

Determine o que o parágrafo **precisa realizar aqui**, não apenas o que suas frases dizem isoladamente. Compare objetivo esperado e função observada.

### 2. Nomeie a função dominante

Use a tipologia operacional. Se nenhuma categoria explicar o bloco sem ambiguidade, verifique se há duas ideias concorrentes, mistura de níveis ou problema de arquitetura maior.

### 3. Extraia o núcleo sem adornos

Formule em uma frase de trabalho a operação do parágrafo: `definir X`, `sustentar Y com evidência Z`, `conceder A e preservar B`, `explicar como C produz D`, `passar de E para F`.

Se isso não for possível, o parágrafo ainda não tem centro claro.

### 4. Refaça a sequência segundo o contrato da tipologia

Consulte a receita específica em [`references/paragraph-typology.md`](references/paragraph-typology.md). Seja assertivo na intervenção:

- antecipe o núcleo quando o leitor demora a descobrir o ponto;
- mova contexto secundário para depois do núcleo;
- aproxime evidência da afirmação que ela sustenta;
- explicite mecanismos causais em vez de depender de conectores vagos;
- coloque concessão antes da virada e a informação decisiva depois dela;
- fortaleça a objeção antes de refutá-la;
- organize detalhes por um eixo único em descrições e classificações;
- converta instrução narrativa em condição → ação → verificação;
- elimine transições que apenas anunciam mudança sem explicar a relação;
- produza síntese de nível superior em vez de repetir frases anteriores.

### 5. Decida divisão, fusão ou manutenção

**Divida** quando houver duas teses, duas mudanças fortes de direção, evidências de objetos diferentes ou mudança de função dominante.

**Funda** quando dois parágrafos curtos executarem metades inseparáveis da mesma operação e a quebra prejudicar causalidade, objeção–resposta ou continuidade.

**Mantenha** quando a unidade já possuir um núcleo, desenvolvimento suficiente e pouso funcional, ainda que precise de edição interna.

### 6. Verifique a interface entre parágrafos

A relação deve ser semanticamente identificável: continuação, causa, contraste, especificação, consequência, mudança de escala, síntese ou transição de etapa.

Prefira continuidade lógica real a conectores artificiais. Um bom parágrafo não precisa começar com “além disso”, “nesse sentido” ou “por outro lado” se a relação já estiver clara pela progressão das ideias.

### 7. Calibre densidade e ritmo

Ajuste extensão à complexidade da operação, não a um número fixo de linhas. Use frases mais curtas para decisões, viradas e critérios; aceite períodos mais desenvolvidos quando precisarem manter relações condicionais, causais ou concessivas sem fragmentação.

Corte:

- duplicação sem ganho;
- frase que apenas repete o núcleo;
- detalhe que não sustenta a função;
- comentário lateral que pertence a outro parágrafo;
- conclusão grandiosa acima da evidência disponível.

### 8. Use exemplares clássicos somente quando agregarem estrutura

Consulte [`assets/classic-exemplars.md`](assets/classic-exemplars.md) e a escala de eficácia por tipologia.

- **Alta:** use o exemplar para abstrair a sequência estrutural.
- **Média:** use apenas como apoio, com adaptação forte ao gênero atual.
- **Baixa:** não use como modelo principal; prefira exemplos contemporâneos do gênero.

O corpus clássico é **asset de arquitetura**, não de imitação estilística. Não transfira arcaísmos, voz autoral, ornamentação, posições políticas, premissas científicas históricas ou efeitos aforísticos para o texto-alvo sem necessidade explícita.

Registre origem e condições do corpus conforme [`references/source-provenance.md`](references/source-provenance.md).

### 9. Preserve verdade e força epistêmica

Não altere fatos para melhorar fluidez. Não remova qualificadores necessários. Não transforme associação em causalidade, hipótese em fato, exemplo em prova ou analogia em demonstração.

Quando a revisão tocar evidência, causalidade ou incerteza de forma relevante, coordene com `write-with-evidence`.

### 10. Execute QA paragrafal

Para cada bloco revisado, confirme:

- uma função dominante clara;
- núcleo identificável;
- desenvolvimento suficiente e pertinente;
- nenhuma ideia concorrente sem tratamento;
- relação explícita ou inferível com o parágrafo anterior;
- pouso que conclui ou encaminha;
- extensão compatível com a complexidade;
- preservação de fatos, evidências, ressalvas e requisitos;
- tipologia coerente com o objetivo da seção;
- exemplar clássico, quando usado, abstraído estruturalmente e não copiado como estilo.

## Saída esperada

Quando o usuário pedir análise, produza conforme necessário:

- diagnóstico por parágrafo;
- função observada e função proposta;
- contrato paragrafal esperado;
- problemas de progressão, transição, densidade ou concorrência;
- recomendação de manter, dividir, fundir ou reordenar;
- instrução de refatoração específica à tipologia;
- versão revisada quando solicitada;
- indicação do exemplar `CL-*` apenas quando ele realmente ajudar a operação.

Não imponha a tabela completa em tarefas simples. Use o nível de detalhe proporcional ao problema.

## Limites e handoffs

- **Arquitetura de seção/texto:** `architect-text`.
- **Evidência, causalidade, inferência e incerteza:** `write-with-evidence`.
- **Tom e força persuasiva:** `calibrate-rhetoric`.
- **Legibilidade e linguagem simples:** `improve-accessible-writing`.
- **QA editorial amplo:** `review-editorial-quality`.

Não altere fatos para obter cadência, não remova qualificadores necessários à precisão e não use prestígio literário como justificativa para uma construção incompatível com o gênero de destino.
