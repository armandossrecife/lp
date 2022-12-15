import entidades

def insertUser(usuario):
  meu_banco = entidades.Banco()
  try:
    c = meu_banco.conexao.cursor()
    c.execute("insert into usuarios (nome, telefone, email, usuario, senha) values ('" + usuario.nome + "', '" + usuario.telefone + "', '" + usuario.email + "', '" + usuario.usuario + "', '" + usuario.senha + "' )")
    meu_banco.conexao.commit()
    c.close()
    return "Usuário cadastrado com sucesso!"
  except:
    return "Ocorreu um erro na inserção do usuário"

def updateUser(usuario):
  meu_banco = entidades.Banco()
  try:
    c = meu_banco.conexao.cursor()
    c.execute("update usuarios set nome = '" + usuario.nome + "', telefone = '" + usuario.telefone + "', email = '" + usuario.email + "', usuario = '" + usuario.usuario + "', senha = '" + usuario.senha + "' where idusuario = " + usuario.idusuario + " ")  
    meu_banco.conexao.commit()
    c.close()
    return "Usuário atualizado com sucesso!"
  except:
    return "Ocorreu um erro na alteração do usuário"

def deleteUser(usuario):
  meu_banco = entidades.Banco()
  try:
    c = meu_banco.conexao.cursor()
    c.execute("delete from usuarios where idusuario = " + usuario.idusuario + " ")
    meu_banco.conexao.commit()
    c.close()
    return "Usuário excluído com sucesso!"
  except:
    return "Ocorreu um erro na exclusão do usuário"

def selectUser(usuario, idusuario):
    meu_banco = entidades.Banco()
    try:
      c = meu_banco.conexao.cursor()
      c.execute("select * from usuarios where idusuario = " + idusuario + "  ")
      for linha in c:
        usuario.idusuario = linha[0]
        usuario.nome = linha[1]
        usuario.telefone = linha[2]
        usuario.email = linha[3]
        usuario.usuario = linha[4]
        usuario.senha = linha[5]
      c.close()
      return "Busca feita com sucesso!"
    except:
      return "Ocorreu um erro na busca do usuário"