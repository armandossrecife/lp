import utilidades as util
import pandas as pd
import os
from sys import platform
import ssl

# Permite acessar dados publicos via https sem verifcar SSL
ssl._create_default_https_context = ssl._create_unverified_context

def configura_ambiente():
  try:
    url = "https://raw.githubusercontent.com/armandossrecife/teste/main/archive.zip"
    if platform == "linux" or platform == "linux2":
      print("Instala o zip no Linux")
      util.executa_comando_so(comando="apt install zip")
      util.download_zip(url, 'archive.zip')
    elif platform == "darwin":
      util.download_zip(url, 'archive.zip')
  except Exception as ex:
    print(f"Erro na configuração do ambiente: {str(ex)}")

arquivo_existe = os.path.exists('tabela-fipe-historico-precos.csv')
if not(arquivo_existe):
  print('Baixa o arquivo de trabalho')
  configura_ambiente()
else:
  print('Arquivo tabela-fipe-historico-precos.csv já foi baixado')

df_tabela_fipe = pd.read_csv('tabela-fipe-historico-precos.csv')
print(df_tabela_fipe)

print(df_tabela_fipe.columns)

df_tabela_fipe.drop(['Unnamed: 0'], axis=1, inplace=True)

print(df_tabela_fipe.shape)

print(df_tabela_fipe.info())

lista_marcas_disponiveis = df_tabela_fipe['marca'].unique().tolist()
print(f'Existem {len(lista_marcas_disponiveis)} marcas disponíveis: {lista_marcas_disponiveis}')

lista_carros_disponiveis = df_tabela_fipe['modelo'].unique().tolist()
print(f'Existem {len(lista_carros_disponiveis)} modelos disponíveis.')

print(f"Menor ano de fabricação: {df_tabela_fipe['anoModelo'].min()}, maior ano de fabricação: {df_tabela_fipe['anoModelo'].max()}") 

menor_ano = df_tabela_fipe['anoModelo'].min()
df_carro_mais_antigo = df_tabela_fipe.query(f"anoModelo == {menor_ano}")
print(df_carro_mais_antigo['modelo'].unique()[0])

maior_ano = df_tabela_fipe['anoModelo'].max()
df_carro_mais_novo = df_tabela_fipe.query(f"anoModelo == {maior_ano}")
indice_carro_mais_novo = df_carro_mais_novo.index

print(df_carro_mais_novo['modelo'][indice_carro_mais_novo[0]])

df_carros_toyota_2022 = df_tabela_fipe.query("anoModelo == 2022 and marca=='Toyota'")

lista_carros_toyota_2022 = df_carros_toyota_2022['modelo'].unique().tolist()
print(f"Existem {len(lista_carros_toyota_2022)} modelos da Toyota de fabricação 2022")

carros_corolla_2022 = df_carros_toyota_2022['modelo'].str.contains("Corolla")

print(f"Existem {len(df_carros_toyota_2022[carros_corolla_2022])} registros de Corolas 2022")

df_corollas_2022 = df_carros_toyota_2022[carros_corolla_2022]

df_corollas_2022 = df_corollas_2022.sort_values(by=['valor'])

print(f"preço médio de um Corolla 2022: {round(df_corollas_2022['valor'].mean(), 2)}")