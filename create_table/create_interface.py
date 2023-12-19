import tkinter as tk
from tkinter import scrolledtext


def create_interface(table: str = None) -> None:
    interface = tk.Tk()  # Cria a janela
    interface.title("Window")  # define o titulo
    interface.iconbitmap("icons/icon_0.ico")  # define o icone da janela
    interface.geometry("500x400")  # define o tamanho
    box = scrolledtext.ScrolledText(
        interface, height=300, width=400
    )  # Cria uma caixa de texto com barra de rolagem
    box.insert(tk.END, table)  # Inserir a tabela na caixa de texto
    box.pack()  # Exibe a tabela na janela
    interface.mainloop()  # Coloca a janela em Loop
