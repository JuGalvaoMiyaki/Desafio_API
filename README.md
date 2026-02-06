# Desafio API Toolbox

Este repositório contém um pequeno projeto-exemplo em FastAPI com endpoints para 
gerenciamento simples de usuários e arquivos auxiliares usados durante o desenvolvimento.

## Sumário

- **Descrição**       — o que o projeto faz
- **Tecnologias**     — tecnologias e documentação utilizada no projeto
- **Estrutura**       — pastas estruturadas do projeto
- **Instalação**      — como configurar o ambiente
- **Execução**        — comandos para executar a API
- **Endpoints**       — endpoints disponíveis e suas descrições
- **Exemplos**        — exemplos de resultados esperados ao acessar as endpoints
- **Observações**     — observações necessárias para rodas os endpoints
- **Transparência**   — limitações e riscos
- **Como contribuir** — sugestões simples
- **Autor**
- **Contato**
- **Licença**



## Descrição

Este projeto é um exercício para aprender conceitos básicos de FastAPI e criação de endpoints HTTP.
Ele oferece rotas para criar, listar, acessar, atualizar e remover usuários em memória.

O código é experimental e serve como material de estudo.


## Tecnologias Utilizadas

1. Python 3.10+ 

2. FastAPI

3. Uvicorn


 
# Estrutura do projeto

|--main.py
|--README.md
|--requirements.txt


# Instalação 

1. Clone o repositório 

git clone https://github.com/JuGalvaoMiyaki/Desafio_API

2. Crie um ambiente virtual (opcional, mas recomendado)

python -m venv venv                     # Para criar o ambiente virtual
source venv/bin/activate   # Linux/Mac  # Para ativar o ambiente virtual
venv\Scripts\activate      # Windows    #Para ativar o ambiente virtual

3. Instale dependências:

pip install -r requirements.txt


## Execução

Rode a aplicação com Uvicorn (modo de desenvolvimento com `--reload`):

uvicorn main:app --reload 


## Endpoints Disponíveis

## | Método | Rota                          
   |GET     |http://127.0.0.1:8000          
   |POST    |http://127.0.0.1:8000/usuario  
   |GET     |http://127.0.0.1:8000/usuario  
   |GET     |http://127.0.0.1:8000/usuario/{id}
   |PUT     |http://127.0.0.1:8000/usuario/{id}
   |DELETE  |http://127.0.0.1:8000/usuario/{id}
   
   


- GET                   Retorna uma mensagem simples.
- POST/usuario          Cria um usuário. Campos esperados (JSON ou form-data): `nome`, `email`, `idade`.
	                    * Validação básica: impede emails duplicados *
- GET/usuario           Lista todos os usuários (lista em memória).
- GET/usuario/{id}      Obtém dados do usuário por `id`.
- PUT/usuario/{id}      Atualiza `nome`, `email` e `idade` do usuário.
- DELETE/usuario/{id}   Remove o usuário com o `id` informado.


# Exemplo:

|GET     |http://127.0.0.1:8000   

"Tudo okay por aqui"

|POST   |http://127.0.0.1:8000/usuario

{
	"id": 0,
	"nome": "rocky",
	"email": "xx@ccb.com",
	"idade": 36
}



|GET   |http://127.0.0.1:8000/usuario  

[
	{
		"id": 0,
		"nome": "rocky",
		"email": "xxo@ccb.com",
		"idade": 9
	},
	
]

|GET   |http://127.0.0.1:8000/usuario/0 

{
	"id": 0,
	"nome": "rocky",
	"email": "xxo@ccb.com",
	"idade": 9
}

|PUT   |http://127.0.0.1:8000/usuario/0 

{
	"id": 0,
	"nome": "rocky",
	"email": "rocky@ccb.com",
	"idade": 9
}

|DELETE  |http://127.0.0.1:8000/usuario/0 


"Usuário removido."


# Observações:

Para as rotas : 

|POST    |http://127.0.0.1:8000/usuario  
|PUT     |http://127.0.0.1:8000/usuario/{id}
|DELETE  |http://127.0.0.1:8000/usuario/{id}


**Utilize Insomnia ou Postman ou acesse http://127.0.0.1:8000/docs para inserir os dados necessários.** 



## Transparência — o que o código faz e limites importantes

- Armazenamento: todos os dados ficam em memória (lista `usuarios`). Ao reiniciar a aplicação, os dados são perdidos.

- Validação: há apenas validação mínima (checa email duplicado em memória). Não há validação de formatos (ex.: formato de email), nem autenticação/autorizações.

- Segurança e privacidade: não há criptografia, nem salvamento seguro de dados sensíveis. Não use este código em produção com dados reais.


# Erros e respostas esperados

Rota: |POST    |http://127.0.0.1:8000/usuario
Caso o usuário insira um email já existente na lista, retornará o erro 400, "Email ja existente"
	
Rota: |GET      |http://127.0.0.1:8000/usuario/{id}
Caso o usuário insira um id inválido na lista, retornará o erro 400 "ID não encontrado, digite um ID válido."

Rota: |DELETE   |http://127.0.0.1:8000/usuario/{id}
Caso o usuário insira um id inválido na lista, retornará o erro 404 " "Usuário não encontrado.".

Rota: |PUT      |http://127.0.0.1:8000/usuario/{id}
Caso o usuário insira um id inválido na lista, retornará o erro 404 " "Usuário não encontrado.".
Caso o usuário insira um email já utilizado por outro ID, retornará o erro 400 " "Email ja existente"


## Como contribuir

- Para mudanças pequenas: crie um fork, faça um branch, implemente e envie um pull request.
- Se quiser que eu ajuste o README (traduzir, detalhar exemplos, adicionar imagens ou postes de rota), diga quais pontos quer que eu aprofunde, entre em contato. 


## Licença

Permitido o uso para fins educacionais. 

# 👩‍💻 Autor

• Juliana Galvão Miyaki

# Contato

**juliana.galvao@tbxtech.com** 


#  Referências Técnicas

Python: https://docs.python.org/pt-br/3/
FastAPI:https://fastapi.tiangolo.com/pt/learn/
Uvicorn: https://uvicorn.dev

*Projeto de estudo com Python, FastAPI, Uvicorn*


