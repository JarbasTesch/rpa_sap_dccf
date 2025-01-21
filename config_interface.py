from tkinter import *

cor_fundo = '#c7d7c6'
cor_btn = '#98c096'

def open_config_interface():
    nova_tela = Toplevel()
    nova_tela.title("Configuração")
    nova_tela.geometry("300x350")
    nova_tela.resizable(False, False)
    nova_tela.config(bg=cor_fundo)


    titulo = Label(nova_tela, text = 'RPA - DPE', bg = cor_fundo, font= ('Arial', 23, 'bold'))
    titulo.pack(pady=5)

    espaco_acima = Frame(nova_tela, height=10, bg= cor_fundo)
    espaco_acima.pack(fill="x")
    label = Label(nova_tela, text="Credenciais", bg= cor_fundo, font= ('Arial', 13, 'bold'))
    label.pack()

    frame_login = Frame(nova_tela, bg=cor_fundo, padx=10, pady=5)
    Label(frame_login, text="Login SAP:", bg= cor_fundo).pack(side=LEFT, padx=1, pady=5)
    Entry(frame_login).pack(side=LEFT, padx=5)
    frame_login.pack()

    frame_senha = Frame(nova_tela, bg=cor_fundo, padx=10, pady=5)
    Label(frame_senha, text="Senha SAP:", bg= cor_fundo).pack(side=LEFT, padx=1, pady=5)
    Entry(frame_senha).pack(side=LEFT, padx=5)
    frame_senha.pack()

    espaco_acima = Frame(nova_tela, height=10, bg= cor_fundo)
    espaco_acima.pack(fill="x")
    label = Label(nova_tela, text="Diretórios", bg= cor_fundo, font= ('Arial', 13, 'bold'))
    label.pack()

    frame_diretorio_aberto = Frame(nova_tela, bg=cor_fundo, padx=10, pady=5)
    Label(frame_diretorio_aberto, text="          Diretorio aberto:", bg= cor_fundo).pack(side=LEFT, padx=1, pady=5)
    Entry(frame_diretorio_aberto).pack(side=LEFT, padx=5, pady=5)
    frame_diretorio_aberto.pack()

    frame_diretorio_consolidado = Frame(nova_tela, bg=cor_fundo, padx=10, pady=5)
    Label(frame_diretorio_consolidado, text="Diretorio consolidado:", bg= cor_fundo).pack(side=LEFT, padx=1, pady=5)
    Entry(frame_diretorio_consolidado).pack(side=LEFT, padx=5, pady=5)
    frame_diretorio_consolidado.pack()

    Button(nova_tela, text= 'SALVAR', bg = '#98c096').pack(pady = 10)

    nova_tela.mainloop()