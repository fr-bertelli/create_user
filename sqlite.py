import sqlite3 as sql
import pdb


# bd = sql.connect('pessoas')
# cursor = bd.cursor()

def criar_usuario(id, nome, sobrenome, cpf, idade, email, sexo):
    # Conectar-se ao banco de dados (ou criá-lo se não existir)
    try: 
      bd = sql.connect('pessoas')
      cursor = bd.cursor()

      # Inserir os dados da pessoa na tabela (supondo que você já tenha uma tabela chamada 'pessoas')
      cursor.execute("INSERT INTO pessoas (id, nome, sobrenome, cpf, idade, email, sexo) VALUES (?, ?, ?, ?, ?, ?, ?)",
      (id, nome, sobrenome, cpf, idade, email, sexo))

      # Confirmar a inserção e fechar a conexão com o banco de dados
      bd.commit()
    except sql.Error as e:
      print(f"Erro ao inserir dados no banco: {e}")
    finally:
      bd.close()

def buscar_usuarios_all():
  try:
    bd = sql.connect('pessoas')
    cursor = bd.cursor()

    cursor.execute("SELECT * FROM pessoas")
    resultado = cursor.fetchall()

    pessoas = []
    for linha in resultado:
      pessoa = {
        'id': linha[0],
        'nome': linha[1],
        'sobrenome':linha[2],
        'cpf': linha[3],
        'idade': linha[4],
        'email': linha[5],
        'sexo': linha[6]
      }
      pessoas.append(pessoa)

    return pessoas
  except sql.Error as e:
    print(f"Erro ao buscar pessoas no banco: {e}")
  finally:
    bd.close()

def buscar_usuarios_id(id):
  try:
    bd = sql.connect('pessoas')
    cursor = bd.cursor()

    cursor.execute(f"SELECT * FROM pessoas WHERE id = {id}")
    resultado = cursor.fetchall()

    pessoa = {
      'id': resultado[0][0],
      'nome': resultado[0][1],
      'sobrenome':resultado[0][2],
      'cpf': resultado[0][3],
      'idade': resultado[0][4],
      'email': resultado[0][5],
      'sexo': resultado[0][6]
    }

    return pessoa
  except sql.Error as e:
    print(f"Erro ao buscar pessoa no banco: {e}")
  finally:
    bd.close()

def excluir_usuario(id):
  try:
    bd = sql.connect('pessoas')
    cursor = bd.cursor()

    cursor.execute(f"DELETE FROM pessoas WHERE id = {id}")
    bd.commit()
    linhas_afetadas = cursor.rowcount

    return linhas_afetadas
  except sql.Error as e:
    print(f"Erro ao deletar o usuario: {e}")
  finally:
    bd.close()