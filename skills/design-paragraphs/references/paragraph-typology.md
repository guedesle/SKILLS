# Tipologia operacional de parágrafos

Esta referência define contratos de construção e refatoração para `design-paragraphs`. A tipologia descreve **operações discursivas**, não gêneros literários. Um parágrafo deve ter uma função dominante; funções secundárias são aceitáveis apenas quando servem à operação principal sem criar competição interna.

## Modelo comum

Use cinco posições abstratas quando forem úteis:

1. **Âncora** — conecta o parágrafo ao contexto, problema ou parágrafo anterior.
2. **Núcleo** — declara a operação dominante: tese, definição, causa, objeção, evento etc.
3. **Desenvolvimento** — apresenta razões, evidências, detalhes, etapas ou distinções.
4. **Virada** — introduz contraste, limite, consequência ou mudança de direção quando necessária.
5. **Pouso** — encerra a unidade produzindo consequência, síntese local ou ponte para o próximo bloco.

Nem todo tipo usa as cinco posições. Não preencha slots por obrigação; use-os para tornar explícita a lógica do parágrafo.

## Escala de eficácia dos exemplares clássicos

- **Alta** — a arquitetura do parágrafo clássico é diretamente transferível para escrita contemporânea após abstração estrutural.
- **Média** — o exemplar ajuda a visualizar progressão e ritmo, mas precisa de adaptação forte para textos técnicos, institucionais ou digitais.
- **Baixa** — o clássico tende a induzir escolhas inadequadas ao objetivo; prefira modelos contemporâneos do gênero.

A escala avalia **utilidade estrutural**, não qualidade literária.

## 1. Abertura de enquadramento

**Objetivo:** estabelecer rapidamente objeto, situação, tensão ou pergunta que governará o trecho seguinte.

**Construa assim:** contexto mínimo → elemento de interesse/tensão → recorte do que será tratado.

**Na refatoração:** corte preâmbulos genéricos; antecipe o objeto; mova contexto histórico secundário para depois do núcleo; termine indicando por que o tema merece continuação.

**Teste de aceite:** após uma leitura, o leitor sabe de que assunto se trata, em que recorte e qual impulso leva ao próximo parágrafo.

**Exemplar clássico:** **Alta**. Bons modelos: `CL-01`, `CL-04`. Extraia a entrada imediata no objeto e a capacidade de instalar tensão; não copie ornamentação ou voz de época.

## 2. Tese ou proposição

**Objetivo:** afirmar uma ideia que o restante do texto sustentará, qualificará ou testará.

**Construa assim:** proposição explícita → razão ou critério principal → consequência do que foi afirmado.

**Na refatoração:** elimine teses implícitas quando a precisão exigir compromisso; separe duas teses independentes; converta abstrações vagas em proposições verificáveis ou discutíveis.

**Teste de aceite:** é possível resumir a posição central em uma sentença sem perder seu escopo ou qualificadores.

**Exemplar clássico:** **Alta**. `CL-01` mostra decisão justificada; `CL-03` mostra proposição seguida de limite; `CL-10` mostra implicação derivada de uma premissa.

## 3. Definição ou conceituação

**Objetivo:** fixar o sentido operacional de um termo, categoria ou fenômeno.

**Construa assim:** termo → classe ou domínio → características distintivas → fronteira/exclusão quando necessária.

**Na refatoração:** retire exemplos que substituem a definição; explicite o critério que diferencia o conceito de vizinhos; preserve incerteza quando a própria categoria for contestada.

**Teste de aceite:** o leitor consegue decidir, com base no parágrafo, o que entra e o que não entra na categoria.

**Exemplar clássico:** **Alta**. `CL-06` é útil para mostrar definição sob incerteza; `CL-07` é um modelo compacto de definição por atributos e limite normativo.

## 4. Explicação causal

**Objetivo:** explicar por que algo ocorreu ou como uma condição produz um efeito.

**Construa assim:** fenômeno → causa/condição → mecanismo → efeito → limite ou alternativa relevante.

**Na refatoração:** não transforme correlação em causalidade; substitua conectores vagos por mecanismo explícito; diferencie causa necessária, suficiente, contribuinte e contexto.

**Teste de aceite:** cada salto causal possui um mecanismo ou evidência identificável e os qualificadores de certeza foram preservados.

**Exemplar clássico:** **Alta** para arquitetura. `CL-05` e `CL-09` ajudam a observar encadeamento de razão e consequência. Para conteúdo científico atual, use evidência contemporânea, não a autoridade do clássico.

## 5. Sustentação evidencial

**Objetivo:** ligar uma afirmação a evidências e explicitar o que elas permitem concluir.

**Construa assim:** afirmação local → evidência → interpretação → grau de suporte → limite/ressalva.

**Na refatoração:** aproxime evidência da afirmação correspondente; separe dado de inferência; elimine acúmulos de fatos sem interpretação; não aumente o grau de certeza.

**Teste de aceite:** o leitor distingue claramente o que é dado, o que é inferência e qual conclusão é autorizada.

**Exemplar clássico:** **Alta** para progressão, especialmente `CL-05` e passagens argumentativas de Darwin. A validade factual do texto moderno deve vir das fontes atuais do próprio trabalho.

## 6. Exemplificação ou ilustração

**Objetivo:** tornar concreto um princípio, regra ou fenômeno sem deixar o exemplo substituir a generalização.

**Construa assim:** ideia abstrata → exemplo pertinente → traço observado → retorno explícito à ideia.

**Na refatoração:** retire detalhes narrativos que não provam nada; explique por que o caso é representativo; rotule exceções como exceções.

**Teste de aceite:** remover o exemplo empobrece a compreensão, mas não destrói a proposição central.

**Exemplar clássico:** **Média**. A literatura oferece exemplos memoráveis, porém pode estimular detalhe excessivo. Use `CL-04` para observar seleção de detalhes e `CL-09` para analogia curta com retorno ao argumento.

## 7. Classificação ou enumeração analítica

**Objetivo:** decompor um domínio segundo um critério único e útil.

**Construa assim:** universo → critério de divisão → classes → diferença relevante entre elas → consequência da classificação.

**Na refatoração:** não misture critérios na mesma enumeração; torne as classes paralelas; elimine categorias sobrepostas quando o propósito exigir exclusividade.

**Teste de aceite:** o leitor sabe por que os itens estão no mesmo conjunto e segundo qual critério foram separados.

**Exemplar clássico:** **Alta**. `CL-08` demonstra decomposição binária recursiva com critério explícito.

## 8. Comparação ou analogia

**Objetivo:** esclarecer uma relação por semelhança e diferença controladas.

**Construa assim:** eixo comum → elemento A → elemento B → semelhança/diferença relevante → limite da comparação.

**Na refatoração:** declare o eixo comparativo; corte paralelos ornamentais; explicite onde a analogia deixa de valer quando houver risco de extrapolação.

**Teste de aceite:** a comparação produz conhecimento adicional e não depende apenas de efeito retórico.

**Exemplar clássico:** **Alta**. `CL-09` é especialmente útil porque a analogia é curta, funcional e imediatamente reconectada ao argumento.

## 9. Contraste ou concessão

**Objetivo:** reconhecer uma expectativa, objeção parcial ou alternativa e mostrar por que a direção principal ainda se sustenta.

**Construa assim:** posição/expectativa A → concessão válida → marcador de virada → posição B → consequência.

**Na refatoração:** preserve a parte válida da posição oposta; evite `mas` sem mudança lógica real; coloque a informação decisiva depois da virada quando a ênfase exigir isso.

**Teste de aceite:** o leitor consegue identificar o que foi concedido e o que, apesar disso, continua válido.

**Exemplar clássico:** **Alta**. `CL-01`, `CL-03` e `CL-09` exibem viradas claras sem apagar a premissa anterior.

## 10. Refutação ou objeção–resposta

**Objetivo:** apresentar uma objeção relevante de forma justa e respondê-la com razão, evidência ou distinção.

**Construa assim:** objeção forte → parcela válida → falha/limite → resposta → efeito sobre a tese.

**Na refatoração:** fortaleça objeções caricaturadas; não responda a uma versão mais fraca do argumento; identifique exatamente qual premissa é rejeitada.

**Teste de aceite:** um leitor que sustenta a objeção reconheceria sua posição antes de discordar da resposta.

**Exemplar clássico:** **Alta**. `CL-09` mostra uma opção apresentada, testada e rejeitada por consequência indesejável.

## 11. Problema–resposta

**Objetivo:** transformar um estado indesejado em decisão, alternativa ou solução avaliável.

**Construa assim:** problema → impacto → causa ou restrição → resposta proposta → critério de sucesso/limite.

**Na refatoração:** não introduza solução antes de delimitar o problema; evite respostas sem critério de êxito; se houver múltiplas soluções, classifique-as antes de escolher.

**Teste de aceite:** o parágrafo deixa claro qual problema a resposta resolve e como saber se a resposta funciona.

**Exemplar clássico:** **Média/Alta**. `CL-08` ajuda a decompor famílias de solução; combine-o com critérios contemporâneos quando o texto for técnico ou administrativo.

## 12. Descrição analítica

**Objetivo:** descrever um objeto, cenário, sistema ou estado selecionando características que sustentam uma interpretação.

**Construa assim:** identificação → dimensão principal → detalhes selecionados → relação entre detalhes → significado funcional.

**Na refatoração:** corte adjetivos sem função; organize detalhes por eixo espacial, funcional ou hierárquico; faça cada detalhe contribuir para a leitura do todo.

**Teste de aceite:** os detalhes não são uma lista arbitrária e convergem para uma percepção ou conclusão útil.

**Exemplar clássico:** **Alta**. `CL-04` mostra identificação, contraste, detalhes arquitetônicos e explicação do nome dentro da mesma progressão observacional.

## 13. Narrativa ou evento

**Objetivo:** apresentar uma mudança no tempo em que a sequência de acontecimentos produz consequência relevante.

**Construa assim:** situação inicial → evento → reação/mudança → consequência → ponto de chegada.

**Na refatoração:** elimine passos sem consequência; preserve ordem temporal quando ela for causal; antecipe o evento principal se o contexto estiver longo demais.

**Teste de aceite:** cada unidade temporal altera estado, expectativa, decisão ou conhecimento do leitor.

**Exemplar clássico:** **Alta**. `CL-02` e a abertura de *Dom Casmurro* mostram cena curta, evento e consequência nominal/interpretativa. Em texto institucional, use a arquitetura sem teatralização.

## 14. Procedimental ou instrucional

**Objetivo:** orientar execução correta e verificável de uma ação.

**Construa assim:** condição/pré-requisito → ação → parâmetros → verificação → exceção/recuperação quando necessária.

**Na refatoração:** troque narrativa por verbos de ação; não esconda pré-condições; se as etapas forem independentes e numerosas, converta o parágrafo em lista ou procedimento estruturado.

**Teste de aceite:** uma pessoa qualificada consegue executar a ação sem inferir passos críticos ausentes e sabe como verificar o resultado.

**Exemplar clássico:** **Baixa**. Não use prosa literária como modelo padrão. Prefira documentação, normas ou procedimentos atuais; clássicos podem, no máximo, ilustrar ordem lógica.

## 15. Transição ou ponte

**Objetivo:** encerrar uma operação e preparar outra sem criar um parágrafo vazio de conteúdo.

**Construa assim:** retomada mínima → relação lógica → mudança de foco → promessa concreta do próximo movimento.

**Na refatoração:** remova frases como “a seguir veremos” quando nada acrescentam; faça a ponte nomear a relação entre blocos; una ao parágrafo anterior ou seguinte se não houver conteúdo próprio.

**Teste de aceite:** a transição explica **por que** o texto muda de assunto, não apenas **que** mudará.

**Exemplar clássico:** **Alta**. `CL-02` é um modelo claro de retrospecto + pivô + nova pergunta/motivo.

## 16. Síntese ou integração

**Objetivo:** combinar elementos anteriores em uma conclusão de nível superior, sem apenas repeti-los.

**Construa assim:** elementos relevantes → relação entre eles → generalização controlada → limite ou implicação.

**Na refatoração:** elimine paráfrase serial; procure a relação que os elementos juntos revelam; preserve divergências que não podem ser reconciliadas.

**Teste de aceite:** o parágrafo produz uma leitura nova que não existia em nenhuma frase isolada anterior.

**Exemplar clássico:** **Média**. `CL-03` e `CL-10` ajudam na passagem de elementos particulares para uma consequência geral, mas textos analíticos modernos exigem maior rastreabilidade.

## 17. Implicação ou recomendação

**Objetivo:** converter achado, diagnóstico ou princípio em consequência prática ou decisão.

**Construa assim:** achado/premissa → implicação → ação recomendada → condição/risco → critério de decisão.

**Na refatoração:** não faça recomendação sem base explícita; diferencie “decorre dos dados” de “é uma escolha de política”; explicite condições que mudariam a recomendação.

**Teste de aceite:** o leitor entende de qual evidência nasce a ação e sob quais condições ela deve ou não ser adotada.

**Exemplar clássico:** **Média**. `CL-10` demonstra passagem de premissa sobre comportamento humano a requisito institucional; use a técnica, não a autoridade histórica, como modelo.

## 18. Fechamento ou conclusão local

**Objetivo:** encerrar uma unidade produzindo resolução, consequência ou abertura controlada para o próximo nível do texto.

**Construa assim:** núcleo recuperado → resultado acumulado → consequência final ou limite → frase de pouso.

**Na refatoração:** corte resumos redundantes; não introduza evidência nova decisiva na última frase; evite grandiloquência não sustentada.

**Teste de aceite:** o parágrafo pode ser a última unidade da seção sem deixar a operação principal incompleta.

**Exemplar clássico:** **Alta** para cadência e resolução, especialmente `CL-03` e `CL-10`. Reduza o efeito aforístico quando o gênero exigir neutralidade.

## Regras para conflitos de tipologia

1. Se duas funções disputam o núcleo, divida o parágrafo.
2. Se uma função apenas prepara outra, trate-a como posição interna, não como segundo tipo dominante.
3. Se a divisão quebrar uma cadeia causal ou uma objeção–resposta curta, mantenha o bloco unido e torne a relação explícita.
4. Se o parágrafo tiver mais de uma mudança forte de direção, reavalie a arquitetura da seção.
5. Se a correção exigir mover vários parágrafos ou redefinir a função da seção, faça handoff para `architect-text`.
