import os
import urllib.request

# Executa uma chamada ao sistema operacional
# https://docs.python.org/3/library/os.html
def executa_comando_so(comando):
  try:
    os.system(comando)
    print(f'Comando: {comando} executado com sucesso!')
  except:
    print(f'Erro ao executar o comando {comando}')

# https://docs.python.org/3/library/urllib.request.html
def meu_download(url, nome):
  try:
    print("download iniciado!")
    filename, headers = urllib.request.urlretrieve(url, filename=nome)
    print(f"download do arquivo {filename} completo!")
  except Exception as ex: 
    print(f"Erro no download: {str(ex)}")

def download_zip(url, nome):
  try:
    print("download iniciado!")
    filename, headers = urllib.request.urlretrieve(url, filename=nome)
    print(f"download do arquivo {filename} completo!")
    print(f"Descompacta o arquivo {filename}")
    try:
      executa_comando_so(comando=f"unzip {filename}")
    except Exception as ex_zip:
      print(f"Erro ao descompactar o arquivo {filename}: {str(ex_zip)}")
  except Exception as ex: 
    print(f"Erro no download: {str(ex)}")