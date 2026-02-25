# ai-agent

CLI simples em Python que chama a API do Google Gemini para gerar uma resposta de texto.

## Requisitos

- Python 3.12+
- [uv](https://github.com/astral-sh/uv)

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```sh
GEMINI_API_KEY='sua_chave_aqui'
```

## Instalação

Para criação de um novo ambiente virtual:

```sh
uv venv
```

Para instalação das dependências necessárias:

```sh
uv sync
```

## Execução

```sh
uv run main.py [prompt] <--verbose>
```

O argumento `verbose` retorna a resposta juntamente com o prompt enviado, sua contagem de tokens e a contagem de tokens da resposta.
