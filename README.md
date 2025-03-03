# ⚒️ API de cadastro de usuarios (CRUD)
Este projeto é uma API desenvolvida com Flask para gerenciar usuários e autenticação via JWT. incluindo documentação, controle de segurança e manipulação de dados.


### Base URL
A aplicação utiliza como base: `http://127.0.0.1:5000`

### Documentação
Documentação: `http://127.0.0.1:5000/v1-docs/`

## Para testar a API 
```
git clone https://github.com/Erick-IL/Assistente-pessoal
```

## Dependencias 
```
pip install -r requirements.txt
```

## Estrutura do Projeto
```
Flask_API/
│── app/
│   ├── commons/          # Configurações, DTOs e JWT
│   ├── controller/       # Endpoints e lógica de segurança
│   ├── documentation/    # Documentação da API
│   ├── models/           # Modelos do banco de dados
│   ├── __init__.py       # Inicialização da aplicação
│── app.py                # Arquivo principal para rodar a API
│── requirements.txt      # Dependências do projeto
│── README.md             # Documentação do projeto
│── .gitignore            # Arquivos ignorados no versionamento
```

