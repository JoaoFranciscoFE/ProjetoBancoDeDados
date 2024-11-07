import psycopg2

# Estabelecendo a conexão com o Banco de dados
def conectardb():
    conexao = psycopg2.connect(database="aula",
                               host="localhost",
                               user="postgres",
                               password="nti123",
                               port="5432")
    return conexao


conexao = conectardb()

def inserir_usuario(nome, email, senha):
    conexao = conectardb()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuario (nome, email, senha) VALUES (%s, %s,  %s)", (nome, email, senha))

    conexao.commit()
    cursor.close()
    conexao.close()

def buscar_usuario(nome):
    conexao = conectardb()
    cursor = conexao.cursor()
    cursor.execute(f"SELECT email,nome FROM usuario where nome= '{nome}' ")

    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado

def listar_usuarios():
    conexao = conectardb()                  # Conecta ao banco.
    cursor = conexao.cursor()             # Cria um cursor para consultas.
    cursor.execute(f"SELECT email,nome FROM usuario")
                                         # Executa o comando SELECT para obter todos os usuários.
    resultado = cursor.fetchall()         # Recupera todos os resultados da consulta em uma lista.
    cursor.close()                        # Fecha o cursor.
    conexao.close()                       # Fecha a conexão com o banco.
    return resultado                      # Retorna a lista de usuários.

def deletar_usuario(id):
    conexao = conectardb()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM usuario WHERE id = %s", (id, ))

    conexao.commit()
    cursor.close()
    conexao.close()
