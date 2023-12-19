import sys
import time as t

import pyautogui

"""
hotkey - metodo usado para fazer combinações de teclas
typewrite - metodo usado para escrever strings
press - metodo usado para pressionar uma unica tecla
"""

hz = 5
list = sys.argv

# abre o bloco de notas, pelo executar do windows
pyautogui.hotkey("win", "r")
pyautogui.typewrite("notepad")
pyautogui.press("enter")
t.sleep(hz)

# digita todos os argumentos recebidos no arquivo
for i in range(1, len(list)):
    pyautogui.typewrite(list[i])
    pyautogui.press("enter")

# salva o arquivo com o nome 'file.txt'
pyautogui.hotkey("ctrl", "s")
pyautogui.typewrite("file.txt")
pyautogui.press("enter")
