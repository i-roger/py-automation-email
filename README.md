Criando um script que vai analisar uma base de dados e enviar por email automaticamente.

# Passo 1 : Entrar no sistema da empresa ( nesse caso é o link do Drive)
# Passo 2 : Navegar no sistema e encontrar a base de vendas (entrar na pasta exportar)
# Passo 3 : Fazer o download da base de vendas
# Passo 4 : Importar a base de vendas pro python
# Passo 5 : Calcular os indicadores da empresa
# Passo 6 : Enviar um e-mail para a diretoria com os indicadores de vendas


Alguns comandos : 
Dica -> importar a biblioteca time e usar em pontos estratégicos.
# import time
# time.sleep(1) milisegundos

Dica 2 -> pyautogui.PAUSE = 1
# Roda o script mais pausadamente

# pyautogui.hotkey -> para conjunto de teclas ou atalhos
# pyautogui.press -> apenas 1 botão
# pyautogui.click -> clicar
# pyautogui.write -> para escrever textos

IMPORTANTE !!!!
AO INVÉS DE UTILIZAR O MÉTODO TIME.SLEEP()
USAR O MÉTODO --> pyautogui.locateOnScreen()
Esse método compara sua tela em tempo real com alguma foto que tenha selecionado!
Por exemplo o print da futura página que irá carregar!
Assim corrigimos o problema de erro no código quando passar o tempo do time.sleep()
o parametro confidence pode ser utilizado em 0.9 assim caso o icone ou algo da tela mude,
o script ainda consigue reconhecer a página.
Para utilizar essa função é necessário instalar :
pip install opencv-python // Biblioteca de reconhecimento de imagens

while not pyautogui.locateOnScreen(imagem.png, confidence=0.9):
	time.sleep(1)
