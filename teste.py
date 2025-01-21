import tkinter as tk
from tkinter import filedialog

def selecionar_diretorio():
    diretorio = filedialog.askdirectory(title="Selecione um diretório")
    if diretorio:  # Verifica se um diretório foi selecionado
        entry_diretorio.delete(0, tk.END)  # Limpa o campo atual
        entry_diretorio.insert(0, diretorio)  # Insere o caminho selecionado

# Criação da janela principal
janela = tk.Tk()
janela.title("Seleção de Diretório")

# Campo Entry para exibir o diretório selecionado
entry_diretorio = tk.Entry(janela, width=50)
entry_diretorio.grid(row=0, column=0, padx=10, pady=10)

# Botão para abrir a janela de seleção de diretório
botao_selecionar = tk.Button(janela, text="Selecionar Diretório", command=selecionar_diretorio)
botao_selecionar.grid(row=0, column=1, padx=10, pady=10)

# Loop principal da interface
janela.mainloop()
