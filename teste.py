from tkinter import *
import funcoes as fcs
import config_interface as confinf
import threading
from tkinter import messagebox
import traceback

main_window = Tk()

main_window.title('Balanço - DPE')
main_window.geometry('300x350')
main_window.resizable(width=False, height=False)
cor_fundo = '#c7d7c6'
cor_btn = '#98c096'
cor_letra = 'black'
main_window.config(bg=cor_fundo)

def executar_script_com_mensagem(funcao_script):
    for widget in main_window.winfo_children():  # Desativando os botões
        if isinstance(widget, Button):
            widget.config(state="disabled")

    # Executa o script em uma thread separada
    def wrapper():
        try:
            funcao_script()  # Executa a função do script
        except Exception as e:
            error_message = f"Ocorreu um erro durante a execução:\n{e}\n\nDetalhes:\n{traceback.format_exc()}"
            main_window.after(0, lambda: messagebox.showerror("Erro", error_message))
        finally:
            main_window.after(0, lambda: ativar_botoes())

    def ativar_botoes():
        for widget in main_window.winfo_children():  # Ativando os botões
            if isinstance(widget, Button):
                widget.config(state="normal")

    # Inicia a thread para executar o script
    thread = threading.Thread(target=wrapper)
    thread.start()

# Componentes da interface
titulo = Label(main_window, text='RPA - DPE', bg=cor_fundo, fg=cor_letra, font=('Arial', 23, 'bold'))
titulo.pack(pady=15)

btn_login = Button(main_window, text='Logar no SAP', bg=cor_btn, fg=cor_letra, font=('Arial', 15), width=12, height=1,
                   command=lambda: executar_script_com_mensagem(fcs.funcao_sap))
btn_login.pack(pady=15)

btn_aberto = Button(main_window, text='F.01 - Aberto', bg=cor_btn, fg=cor_letra, font=('Arial', 15), width=12, height=1,
                    command=lambda: executar_script_com_mensagem(fcs.teste))
btn_aberto.pack(pady=15)

btn_consolidado = Button(main_window, text='F.01 - Consolidado', bg=cor_btn, fg=cor_letra, font=('Arial', 15), width=15, height=1)
btn_consolidado.pack(pady=15)

btn_config = Button(main_window, text="Opções", bg=cor_btn, command=lambda: confinf.open_config_interface(main_window))
img = PhotoImage(file='config_icon.png')
btn_config.config(image=img)
btn_config.pack(pady=15)

main_window.mainloop()
