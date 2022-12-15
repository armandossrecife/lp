import sqlite3

class Usuario:
  def __init__(self, idusuario = 0, nome = "", telefone = "", email = "", usuario = "", senha = ""):
    self.info = {}
    self.idusuario = idusuario
    self.nome = nome
    self.telefone = telefone
    self.email = email
    self.usuario = usuario
    self.senha = senha

class Banco():
    cria_usuarios = """create table if not exists usuarios (
	                 idusuario integer primary key autoincrement ,
	                 nome text,
	                 telefone text,
	                 email text,
	                 usuario text,
	                 senha text)"""

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute(self.cria_usuarios)
        self.conexao.commit()
        c.close()   