##Desafio API##

Esse projeto se trata de um desafio para aprendizado, utilizando rotas, FastAPI, uvicorn
e ambientes virtuais. 

## 🚀 Tecnologias Utilizadas

 # Desafio API Toolbox

Este repositório contém um pequeno projeto-exemplo em FastAPI com endpoints para gerenciamento simples de usuários (CRUD) e arquivos auxiliares usados durante o desenvolvimento.

## Sumário
- **Descrição** — o que o projeto faz
- **Arquivos** — responsabilidades dos arquivos no repositório
- **Requisitos** — dependências e versão do Python
- **Instalação** — como configurar o ambiente
- **Execução** — comandos para executar a API
- **API** — endpoints disponíveis e exemplos
- **Transparência** — limitações, riscos e observações
- **Como contribuir** — sugestões simples

## Descrição
Este projeto é um exercício para aprender conceitos básicos de FastAPI e criação de endpoints HTTP. Ele oferece rotas para criar, listar, acessar, atualizar e remover usuários em memória (sem persistência).

O código é experimental e serve como material de estudo — não é pronto para produção.

## Arquivos e responsabilidades
- `main.py`: implementação principal da API usando FastAPI; armazena usuários em memória numa lista `usuarios` e fornece endpoints CRUD.
- `cadastro.py`: definição de uma classe `Usuario` com atributos `id`, `nome`, `email` e `idade` e um método para retornar seus dados.
- `Tentativa.py`: versão alternativa/experimentos da API; contém código duplicado e trechos que demonstram abordagens diferentes (e algumas inconsistências).
- `requirements.txt`: dependências do projeto (FastAPI, Uvicorn, pydantic, etc.).

## Requisitos
- Python 3.10+ (recomendado)
- Virtualenv ou outro gerenciador de ambientes
- Dependências listadas em `requirements.txt`

## Instalação (rápido)
1. Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1   # PowerShell (Windows)
```

2. Instale dependências:

```powershell
pip install -r requirements.txt
```

## Execução
Rode a aplicação com Uvicorn (modo de desenvolvimento com `--reload`):

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Para executar a versão em `Tentativa.py` (apenas para testar a versão alternativa):

```bash
uvicorn Tentativa:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints (implementados em `main.py`)
- `GET /` — rota de saúde, retorna uma mensagem simples.
- `POST /usuario` — cria um usuário. Campos esperados (JSON ou form-data): `nome`, `email`, `idade`.
	- Validação básica: impede emails duplicados (checagem em memória).
- `GET /usuario` — lista todos os usuários (lista em memória).
- `GET /usuario/{id}` — obtém dados do usuário por `id`.
- `PUT /usuario/{id}` — atualiza `nome`, `email` e `idade` do usuário.
- `DELETE /usuario/{id}` — remove o usuário com o `id` informado.

Exemplo de `curl` para criar usuário:

```bash
curl -X POST "http://127.0.0.1:8000/usuario" -H "Content-Type: application/json" -d "{\"nome\":\"Ana\",\"email\":\"ana@example.com\",\"idade\":30}"
```

## Transparência — o que o código faz e limites importantes
- Armazenamento: todos os dados ficam em memória (lista `usuarios`). Ao reiniciar a aplicação, os dados são perdidos.
- Concurrency: o projeto não foi escrito para concorrência segura — em execução com múltiplos trabalhadores pode ocorrer condição de corrida no `contador_id` e na lista de usuários.
- Validação: há apenas validação mínima (checa email duplicado em memória). Não há validação de formatos (ex.: formato de email), nem autenticação/autorizações.
- Segurança e privacidade: não há criptografia, nem salvamento seguro de dados sensíveis. Não use este código em produção com dados reais.
- Erros conhecidos / inconsistências:
	- `Tentativa.py` contém código duplicado e referências a variáveis globais (`usuarios`, `contador_id`) que podem não estar inicializadas corretamente.
	- Tipos de retorno não são homogêneos (às vezes retorna instâncias de classe, às vezes dicionários).

## Boas sugestões de melhoria
- Persistir dados com um banco (SQLite/Postgres) e usar modelos com pydantic.
- Adicionar testes automatizados (pytest) para validar endpoints.
- Implementar autenticação e autorização (ex.: OAuth2) e validação de entrada usando pydantic models.
- Tratar concorrência com travas ou migrar lógica para o banco de dados.

## Como contribuir
- Abra uma issue descrevendo a sugestão ou bug.
- Para mudanças pequenas: crie um fork, faça um branch, implemente e envie um pull request.

## Licença
Por padrão, este repositório não especifica uma licença. Adicione uma (ex.: MIT) se quiser permitir uso público.

## Contato
Se quiser que eu ajuste o README (traduzir, detalhar exemplos, adicionar imagens ou postes de rota), diga quais pontos quer que eu aprofunde.
