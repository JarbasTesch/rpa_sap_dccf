from tkinter import *
import funcoes as fcs
import config_interface as confinf
from tkinter import messagebox
import sys
import os

def main():
    main_window = Tk()

    main_window.title('Balanço - DPE')
    main_window.geometry('300x350')
    main_window.resizable(width=False, height=False)
    cor_fundo = '#c7d7c6' ##3443eb
    cor_btn = '#98c096'  ##f5d142
    cor_letra = 'black'
    main_window.config(bg = cor_fundo)

    def caminho_recurso(relative_path):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    caminho_icon_config = caminho_recurso("config_icon.png")

    def executar_script_com_mensagem(funcao_script):
        try:
            # Desativa todos os botões na janela
            for widget in main_window.winfo_children():
                if isinstance(widget, Button):
                    widget.config(state="disabled")

            # Executa a função passada
            erro, mensagem, _ = funcao_script()
            if erro:
                messagebox.showerror("Erro", mensagem)
            else:
                messagebox.showinfo("Sucesso", mensagem)

        except Exception as e:
            # Exibe qualquer erro inesperado em uma mensagem
            messagebox.showerror("Erro", f"Ocorreu um erro durante a execução: {e}")

        finally:
            # Reativa os botões após a execução
            for widget in main_window.winfo_children():
                if isinstance(widget, Button):
                    widget.config(state="normal")


    titulo = Label(main_window, text = 'RPA - DPE', bg = cor_fundo, fg = cor_letra, font= ('Arial', 23, 'bold'))
    titulo.pack(pady=15)

    btn_login = Button(main_window, text = 'Logar no SAP', bg = cor_btn, fg = cor_letra, font= ('Arial', 15), width=12, height=1,
                       command = lambda: executar_script_com_mensagem(fcs.funcao_sap))
    btn_login.pack(pady = 15)

    btn_corrente = Button(main_window, text = 'F.01 - Corrente', bg = cor_btn, fg = cor_letra,font= ('Arial', 15), width=12, height=1,
                        command=lambda: executar_script_com_mensagem(lambda: fcs.balanco_corrente(fcs.funcao_sap.session)))
    btn_corrente.pack(pady = 15)

    btn_consolidado = Button(main_window, text = 'F.01 - Consolidado', bg = cor_btn, fg = cor_letra,font= ('Arial', 15), width=15, height=1,
                        command=lambda: executar_script_com_mensagem(lambda: fcs.balanco_fechado(fcs.funcao_sap.session)))
    btn_consolidado.pack(pady = 15)

    btn_config = Button(main_window, text="Opções", bg = cor_btn, command= lambda: confinf.open_config_interface(main_window))
    img = PhotoImage(file=caminho_icon_config)
    btn_config.config(image=img)
    btn_config.pack(pady = 15)


    main_window.mainloop()