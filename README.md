# create_user
Api com a finalidade para estudos de testes em API

# Verbos API REST utilizados
[POST] - Cadastrar usuário

payload exemplo:

{
  'id': int,
  'nome': 'string',
  'sobrenome': 'string',
  'cpf': string,
  'idade': int,
  'email':'string',
  'sexo': 'string'
}

[GET] - Buscar todos usuários

http://localhost:5000/pessoas

[GET] - Buscar usuários por id

http://localhost:5000/pessoas/{id}

[DELETE] - Excluir usuário

http://localhost:5000/pessoas/{id}