from deep_translator import GoogleTranslator
import requests
import tkinter as tk
from tkinter import messagebox

# Sua chave de API
CHAVE = 'digite aqui a sua chave de API'

def buscar():
    cidade = entrada_cidade.get()
    if not cidade.strip():
        messagebox.showerror("Erro", "Digite uma cidade.")
        return

    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={CHAVE}&lang=en'
    tradutor = GoogleTranslator(source='auto', target='pt')
    chamada = requests.get(link)
    dicionario = chamada.json()

    if dicionario.get("cod") != 200: #codigo 200 significa que deu tudo certo, então != 200 significa erro
        messagebox.showerror("Erro", f"Cidade '{cidade}' não encontrada.")
        return

    descricao = dicionario['weather'][0]['description']
    descricao_traduzida = tradutor.translate(descricao)
    temperatura_k = dicionario['main']['temp']
    temperatura_c = temperatura_k - 273.15

    resultado_label.config(
        text=f'Previsão do tempo em {cidade}\n'
                f'Temperatura: {int(temperatura_c)}°C\n'
                f'{descricao_traduzida}'
    )

   

def sair():
    janela.destroy()

janela = tk.Tk()
janela.title("Previsão do tempo")
janela.geometry("400x250")

tk.Label(janela, text="Cidade:", font=("Arial", 14)).pack(pady=5)
entrada_cidade = tk.Entry(janela, font=("Arial", 12))
entrada_cidade.pack(pady=5)
btn_buscar = tk.Button(janela, text="Buscar", command=buscar, width=20)
btn_buscar.pack(pady=5)
btn_cancelar = tk.Button(janela, text="Sair", command=sair, width=20)
btn_cancelar.pack(pady=5)
resultado_label = tk.Label(janela, text="", font=("Arial", 12))
resultado_label.pack(pady=10)

janela.mainloop()
