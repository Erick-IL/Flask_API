# ⚒️ API de cadastro de usuarios 
API para cadastro de usuarios em uma base de dados em mysql

## API Endpoints

### Base URL
A aplicação utiliza como base: `http://127.0.0.1:5000`

### Endpoints Disponíveis

- **GET /users/**  
  Retorna uma lista de usuários cadastrados.

- **POST /users/**  
  Cadastra um usuario com base em uma json com nome, email e senha.

- **GET /users/<int:id>**  
  Retorna um json com as informações do usuario correspondente com o ID.

## Para testar a API 
```
git clone https://github.com/Erick-IL/Assistente-pessoal
```

