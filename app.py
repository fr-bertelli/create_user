# 1. Objetivo - API para realização de testes simples 
# 2. URL Base - localhost/5000
# 3. Endpoint
  # - localhost/pessoas (GET)
  # - localhost/pessoas (POST)
  # - localhost/pessoas/id (GET)
  # - localhost/pessoas/id (DELETE)

from flask import Flask, jsonify, request
import sqlite as sql
import pdb

app = Flask(__name__)

# pessoas = [
  # {
  #   'id': 1,
  #   'nome': 'Joao',
  #   'sobrenome': 'Alcantara',
  #   'cpf': 12312312312,
  #   'idade': 20,
  #   'email':'joao@teste.com',
  #   'sexo': 'M'
  # }
# ]

pessoas = []

# Consultar(todos)
@app.route('/pessoas', methods=['GET'])
def get_pessoas():

  pessoas = sql.buscar_usuarios_all()
  if pessoas:
    return jsonify(pessoas), 200
  else:
    return jsonify({'message': 'Nenhuma pessoa encontrada.'}), 404

# Consultar(por id)
@app.route('/pessoas/<int:id>', methods=['GET'])
def get_pessoas_id(id):

  pessoas = sql.buscar_usuarios_id(id)
  if pessoas:
      return jsonify(pessoas), 200
  else:
      return jsonify({'message': f"Pessoa com o ID '{id}' não existe."})

# Editar
# @app.route('/pessoas/<int:id>', methods=['PUT'])
# def edit_pessoas_id(id):
#   pessoa_update = request.get_json()
#   for indice, pessoa in enumerate(pessoas):
#     if pessoa.get('id') == id:
#       pessoas[indice].update(pessoa_update)
#       return jsonify(pessoas[indice])

# Criar
@app.route('/pessoas', methods=['POST'])
def create_pessoas():
  data = request.get_json()

  id = data.get('id')
  nome = data.get('nome')
  sobrenome = data.get('sobrenome')
  cpf = data.get('cpf')
  idade = data.get('idade')
  email = data.get('email')
  sexo = data.get('sexo')

  if id and nome and sobrenome and cpf and idade and email and sexo:
    sql.criar_usuario(id, nome, sobrenome, cpf, idade, email, sexo)
    return jsonify({'message': 'Pessoa cadastrada com sucesso!'}), 201
  else:
    return jsonify({'error': 'Parâmetros inválidos'}), 400

# Excluir
@app.route('/pessoas/<int:id>', methods=['DELETE'])
def delete_pessoas(id):

  retorno = sql.excluir_usuario(id)
  if retorno > 0:
    return jsonify({'message': 'Exclusão realizada com sucesso!'}), 200
  elif retorno == 0:
    return jsonify({'message': f'Usuário com id {id} não econtrado.'}), 404
  else:
    return jsonify({'message': f'Erro na exclusão: {retorno}'})


app.run(port=5000,host='localhost',debug=True)