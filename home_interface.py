from tkinter import *
import funcoes as fcs
import config_interface as confinf

janela = Tk()
janela.title('Balanço - DPE')
janela.geometry('300x350')
janela.resizable(width=False, height=False)
cor_fundo = '#c7d7c6'
cor_btn = '#98c096'
janela.config(bg = cor_fundo)

titulo = Label(janela, text = 'RPA - DPE', bg = cor_fundo, font= ('Arial', 23, 'bold'))
titulo.pack(pady=15)

btn_opcao_um = Button(janela, text = 'Logar no SAP', bg = cor_btn, font= ('Arial', 15), width=12, height=1)
btn_opcao_um.pack(pady = 15)

btn_opcao_um = Button(janela, text = 'F.01 - Aberto', bg = cor_btn, font= ('Arial', 15), width=12, height=1)
btn_opcao_um.pack(pady = 15)

btn_opcao_um = Button(janela, text = 'F.01 - Consolidado', bg = cor_btn, font= ('Arial', 15), width=15, height=1)
btn_opcao_um.pack(pady = 15)

btn_config = Button(janela, text="Opções", bg = cor_btn, command=confinf.open_config_interface)
img = PhotoImage(file='config_icon.png')
btn_config.config(image=img)
btn_config.pack(pady = 15)



janela.mainloop()