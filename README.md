# Desafio API Toolbox

Este repositório contém um pequeno projeto-exemplo em FastAPI com endpoints para 
gerenciamento simples de usuários e arquivos auxiliares usados durante o desenvolvimento.

## Sumário

- **Descrição**
- **Tecnologias**
- **Estrutura**
- **Instalação**
- **Execução**
- **Endpoints**
- **Exemplos**
- **Observações**
- **Transparência**
- **Como contribuir**
- **Autor**
- **Contato**
- **Licença**

---

## 📌 Descrição

Este projeto é um exercício para aprender conceitos básicos de FastAPI e criação de endpoints HTTP.  
Ele oferece rotas para criar, listar, acessar, atualizar e remover usuários em memória.  

O código é experimental e serve como material de estudo.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- Uvicorn

---

## 📂 Estrutura do projeto

|-- main.py
|-- README.md
|-- requirements.txt

---

## 🚀 Instalação 

1. Clone o repositório:

```bash
git clone https://github.com/JuGalvaoMiyaki/Desafio_API
```

2. Verifique se o Python está instalado:

```bash
python3 --version
```

Se aparecer "command not found", você precisa instalar o Python primeiro.

https://www.python.org/downloads/

3. Se python3 --version não funcionar, instale via Homebrew:

```bash
brew install python
```

4. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python3 -m venv venv
```

5. Ative o ambiente virtual:

```bash
Linux/Mac:

source venv/bin/activate

Windows:


venv\Scripts\activate
```

6. Instale dependências:

```bash
pip install -r requirements.txt

```

## ▶️ Execução

Rode a aplicação com Uvicorn (modo de desenvolvimento com --reload):

```bash
uvicorn main:app --reload
```

## 🔗 Endpoints Disponíveis

| Método | Rota                          |
|--------|-------------------------------|
| GET    | http://127.0.0.1:8000         |
| POST   | http://127.0.0.1:8000/usuario |
| GET    | http://127.0.0.1:8000/usuario |
| GET    | http://127.0.0.1:8000/usuario/{id} |
| PUT    | http://127.0.0.1:8000/usuario/{id} |
| DELETE | http://127.0.0.1:8000/usuario/{id} |

   


| Método | Rota                   | Descrição |
|--------|------------------------|-----------|
| GET    | `/`                    | Retorna uma mensagem simples |
| POST   | `/usuario`             | Cria um usuário. Campos esperados (JSON ou form-data): `nome`, `email`, `idade`. <br> *Validação básica: impede emails duplicados* |
| GET    | `/usuario`             | Lista todos os usuários (em memória) |
| GET    | `/usuario/{id}`        | Obtém dados do usuário por `id` |
| PUT    | `/usuario/{id}`        | Atualiza `nome`, `email` e `idade` do usuário |
| DELETE | `/usuario/{id}`        | Remove o usuário com o `id` informado |


## Exemplos
```bash
GET /

json
"Tudo okay por aqui"
POST /usuario

json
{
  "id": 0,
  "nome": "rocky",
  "email": "xx@ccb.com",
  "idade": 36
}
GET /usuario

json
[
  {
    "id": 0,
    "nome": "rocky",
    "email": "xxo@ccb.com",
    "idade": 9
  }
]
GET /usuario/0

json
{
  "id": 0,
  "nome": "rocky",
  "email": "xxo@ccb.com",
  "idade": 9
}
PUT /usuario/0

json
{
  "id": 0,
  "nome": "rocky",
  "email": "rocky@ccb.com",
  "idade": 9
}
DELETE /usuario/0

json

"Usuário removido."
```

## ⚠️ Observações

Para testar as rotas:

- Use **Insomnia** ou **Postman**
- Ou acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🔍 Transparência

- **Armazenamento**: todos os dados ficam em memória (lista `usuarios`). Ao reiniciar a aplicação, os dados são perdidos.  
- **Validação**: apenas checa email duplicado. Não há validação de formato, autenticação ou autorização.  
- **Segurança**: não há criptografia nem salvamento seguro de dados sensíveis. Não use em produção.  

---

## ❌ Erros esperados

- **POST /usuario** → Email já existente → `400 Email já existente`  
- **GET /usuario/{id}** → ID inválido → `400 ID não encontrado`  
- **DELETE /usuario/{id}** → ID inválido → `404 Usuário não encontrado`  
- **PUT /usuario/{id}** → ID inválido → `404 Usuário não encontrado`  
- **PUT /usuario/{id}** → Email duplicado → `400 Email já existente`  

---

## 🤝 Como contribuir

- Para mudanças pequenas: crie um fork, faça um branch, implemente e envie um pull request.  
- Para ajustes maiores: entre em contato.  

---

## 📜 Licença

Permitido o uso para fins educacionais.  

---

## 👩‍💻 Autor

**Juliana Galvão Miyaki**

---

## 📧 Contato

**juliana.galvao@tbxtech.com**

---

## 📚 Referências Técnicas

- [Python](https://docs.python.org/pt-br/3/)  
- [FastAPI](https://fastapi.tiangolo.com/pt/learn/)  
- [Uvicorn](https://uvicorn.dev)  

