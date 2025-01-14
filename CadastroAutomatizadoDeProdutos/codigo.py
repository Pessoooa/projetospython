import pyautogui
import time
import pandas
import openpyxl

pyautogui.PAUSE = 0.5

#abrir o navegador
pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")

#acessar o sistema de cadastros
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

#selecionar o campo de login e inserir os dados
pyautogui.click(x=750, y=369)
pyautogui.write("williamwilliam@gmail.com")
pyautogui.press("tab")
pyautogui.write("williamwilliam")
pyautogui.press("tab")
pyautogui.press("enter")

#tabela de produtos
tabela = pandas.read_csv("produtos.csv")
print(tabela)

#cadastro automatizado dos produtos
for linha in tabela.index:
    pyautogui.click(x=704, y=252)

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.press("home")
