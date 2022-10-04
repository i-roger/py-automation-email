import pandas as pd
import numpy
import openpyxl

# Criei uma variavel para armazenar os dados da tabela lido pelo python
tabela = pd.read_excel(r"/home/fsociety/Downloads/Vendas - Dez.xlsx")
print(tabela)

faturamento = tabela["Valor Final"].sum()
print(faturamento)
quantidade = tabela["Quantidade"].sum()
print(quantidade)

