import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

ticker = input("Digite o código da ação desejada:")

dados = yfinance.Ticker(ticker).history(start="2020-01-01", end="2020-12-31")

fechamento = dados.Close

maximo = round(fechamento.max(),2)
minimo = round(fechamento.min(),2)
valor_medio = round(fechamento.mean(),2)



destinatario = "edson3711.es@gmail.com"
assunto = "Análises do projeto 2020"

mensagem = f""" 
Prezado gestor,

Seguem abaixo as análises solicitadas da ação {ticker}

Cotação máxima: R${maximo}
Cotação mínima: R${minimo}
Valor médio: R${valor_medio}  

Qualquer dúvida, estou á disposição!

Atenciosamente,
Edson
"""

# abre o navegador
webbrowser.open("www.gmail.com")
time.sleep(3)

# configurarando uma pausa de 3 segundos
pyautogui.PAUSE = 1

# posiciona o cursor em ecrever e clicar
pyautogui.click(x=2080, y=228)

# digitar o destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

# digitar o assunto e teclar TAB
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

# digitar a mensagem e teclar TAB
pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl', 'v')
pyautogui.click(x=2741, y=870)

# fecha gmail
pyautogui.hotkey('ctrl', 'f4')


print("Email enviado com sucesso")
