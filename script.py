# pyautogui.hotkey -> para conjunto de teclas ou atalhos
# pyautogui.press -> apenas 1 botão
# pyautogui.click -> clicar
# pyautogui.write -> para escrever textos

import sys, os
import pyautogui
import pyperclip # para copiar o texto do cóidigo para o CTRL + V do pc corrigindo erros de digitação do python
import time
import pandas as pd
import numpy
import openpyxl

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("up")
pyautogui.press("up")
pyautogui.press("enter")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

# AQUI PRECISEI PEGAR A POSIÇÃO DO CURSOR PARA CLICAR NO LUGAR CORRETO!

pyautogui.click (x=375, y=342, clicks=2)
time.sleep(2)
pyautogui.click(x=381, y=408)
pyautogui.click(x=1166, y=229)
pyautogui.click(x=978, y=625)
time.sleep(5) #ESPERAR O DOWNLOAD ACABAR

# Criei uma variavel para armazenar os dados da tabela lido pelo python
tabela = pd.read_excel(r"/home/fsociety/Downloads/Vendas - Dez.xlsx")

faturamento = tabela["Valor Final"].sum()
print(faturamento)
quantidade = tabela["Quantidade"].sum()
print(quantidade)

#Enviando por email os indicadores de venda!!
pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=85, y=248)

time.sleep(5)
pyperclip.copy('emailtest@gmail.com')
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")
pyperclip.copy("Relatório de vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab")

# Abrir 3 aspas permite escrever um texto livre
# Colocar o f antes das aspas para chamar variaveis no texto
texto = f"""
Boa noite,
Segue o relatório de vendas.
Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {quantidade:,}
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter") #Enviar email
