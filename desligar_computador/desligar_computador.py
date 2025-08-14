import tkinter as tk
from tkinter import simpledialog, messagebox
import os

def desligar():
    tempo = simpledialog.askinteger("Desligar", "Desligar em quanto tempo?")
    if tempo is not None:
        os.system(f"shutdown /s /t {tempo}")
        messagebox.showinfo("Tudo certo", f"O computador será desligado em {tempo} segundos.")


def cancelar():
    os.system("shutdown /a")
    messagebox.showinfo("Cancelado", "Desligamento cancelado.")

janela = tk.Tk()
janela.title("Vamos desligar esse PC? >:c")
janela.geometry("400x200")
titulo = tk.Label(janela, text="Escolha uma opção:", font=("Arial", 14))
titulo.pack(pady=10)
btn_desligar = tk.Button(janela, text="Desligar", command=desligar, width=20)
btn_desligar.pack(pady=5)
btn_cancelar = tk.Button(janela, text="Cancelar desligamento", command=cancelar, width=20)
btn_cancelar.pack(pady=5)


janela.mainloop()
