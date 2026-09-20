---
name: langgraph-gemini-agent-setup
description: "Crie ou corrija um ambiente local de desenvolvimento Python com uv, LangChain, LangGraph Dev, Google Gemini e Tavily. Use para protótipos e depuração local de agentes; não use para deploy produtivo, arquitetura de RAG ou troca de provedor sem requisitos explícitos."
---

# Ambiente de desenvolvimento LangChain, LangGraph e Gemini

Use esta skill para montar um ambiente reproduzível de desenvolvimento de
agentes com Python, `uv`, LangChain, LangGraph Dev, Google Gemini e busca
Tavily. O resultado é um projeto local importável pelo LangGraph Dev Server,
com segredos fora do Git e sem efeitos colaterais durante a importação.

## Quando usar

- iniciar um projeto local de agentes em Windows, Linux ou macOS;
- corrigir um setup que mistura `uv`, LangChain, LangGraph, Gemini e Tavily;
- preparar um exemplo mínimo para depuração no LangGraph Dev Server;
- revisar uma skill de setup quanto a dependências, segurança e
  importabilidade.

## Não use para

- publicar um agente em produção ou configurar observabilidade, persistência,
  filas ou infraestrutura;
- projetar um sistema RAG completo ou escolher banco vetorial;
- migrar para outro provedor de modelo sem requisitos definidos;
- executar chamadas reais a APIs quando o pedido é apenas validar a estrutura.

## Entradas e saída

Entrada mínima: sistema operacional, versão alvo do Python (recomenda-se
3.12 ou 3.13), provedor/modelo desejado e se a busca Tavily será usada.

Saída esperada:

- `pyproject.toml` e `uv.lock` reproduzíveis;
- `.env.example` sem credenciais reais e `.gitignore` correspondente;
- agente importável e `langgraph.json` apontando para o grafo;
- comandos de execução e uma validação local sem chamada externa;
- riscos residuais, especialmente dependências de APIs e nomes de modelos.

## Procedimento

### 1. Pré-requisitos

Verifique `python --version` e `uv --version`. Se `uv` não existir, instale-o
seguindo a documentação oficial do Astral. Não baixe scripts de instalação de
fontes não oficiais.

### 2. Criar o projeto

```powershell
mkdir meu-projeto-agentes
cd meu-projeto-agentes
uv init --python 3.12
```

Para um diretório existente, preserve o `pyproject.toml` e o lockfile; não
reinicialize o projeto sem necessidade.

### 3. Adicionar dependências

```powershell
uv add langchain langchain-core langchain-google-genai langchain-groq
uv add python-dotenv langchain-tavily
uv add "langgraph-cli[inmem]"
```

Use `python-dotenv`, não o pacote homônimo `dotenv`, para fornecer
`from dotenv import load_dotenv`. O lockfile deve ser atualizado pelo `uv` e
versionado junto com o `pyproject.toml`.

### 4. Configurar segredos

Crie `.env.example`:

```env
GOOGLE_API_KEY="cole_sua_chave_do_google_ai_studio"
TAVILY_API_KEY="cole_sua_chave_da_tavily"
MODEL="google_genai:gemini-3.5-flash-lite"
```

O desenvolvedor copia o exemplo para `.env` e preenche as chaves localmente.
O `.gitignore` deve conter `.env`, `.venv/`, `.langgraph_api/`,
`__pycache__/` e arquivos compilados. Nunca inclua chaves reais em commits,
notebooks, exemplos ou mensagens de erro. Se uma chave aparecer em um arquivo
versionado ou em uma saída compartilhada, revogue-a e gere outra.

### 5. Criar o agente

Use um módulo sem efeitos colaterais na importação:

```python
import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch

load_dotenv()

model = init_chat_model(
    os.getenv("MODEL", "google_genai:gemini-3.5-flash-lite")
)

agent = create_agent(
    model=model,
    system_prompt="Responda somente com informações sustentadas pelas fontes disponíveis.",
    tools=[TavilySearch(max_results=5)],
)


def ask(question: str) -> str:
    response = agent.invoke(
        {"messages": [{"role": "user", "content": question}]}
    )
    return response["messages"][-1].text


if __name__ == "__main__":
    print(ask("Qual é a temperatura atual em Salvador, Bahia?"))
```

Não execute `agent.invoke(...)` no corpo do módulo: o LangGraph Dev Server
importa o grafo e uma chamada automática torna cada inicialização uma operação
externa inesperada.

Escolha o nome do modelo a partir da documentação atual do provedor. O valor
do exemplo é configurável por `MODEL` e não deve ser tratado como garantia de
disponibilidade futura.

### 6. Configurar o LangGraph Dev Server

Crie `langgraph.json`:

```json
{
  "dependencies": ["."],
  "graphs": {
    "agent": "./agent.py:agent"
  },
  "env": ".env"
}
```

### 7. Validar e executar

Primeiro valide a importação sem fazer uma pergunta ao modelo:

```powershell
uv sync
uv run python -c "import agent; print(agent.agent.name)"
```

Depois, com as chaves configuradas, execute:

```powershell
uv run python agent.py
uv run langgraph dev
```

Registre quais comandos realmente foram executados. Importação bem-sucedida
prova apenas a integridade estrutural; não prova acesso ao Gemini, Tavily,
qualidade da resposta ou prontidão para produção.

## Critérios de aceite

- `uv sync` termina sem erro e o lockfile acompanha o manifesto;
- `.env` não aparece no diff do Git;
- `import agent` não dispara chamada de modelo ou busca;
- `langgraph.json` aponta para um símbolo existente;
- a execução real só é feita após confirmar as chaves e o modelo;
- o relatório separa validação estrutural de teste externo e de produção.

## Fontes oficiais

- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangChain agents](https://docs.langchain.com/oss/python/langchain/agents)
- [Google Gemini models](https://ai.google.dev/gemini-api/docs/models)
- [Tavily integration](https://docs.langchain.com/oss/python/integrations/tools/tavily)
- [uv](https://docs.astral.sh/uv/)
