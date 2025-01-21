from tkinter import *
import json
from tkinter import messagebox
from tkinter import filedialog

cor_fundo = '#c7d7c6'
cor_btn = '#98c096'

config_file = 'config.json'

def carregar_json():
    try:
        with open(config_file, 'r') as file:
            conteudo = file.read().strip()
            if not conteudo:  # Se o arquivo estiver vazio
                raise FileNotFoundError
            return json.loads(conteudo)  # Carrega o JSON do conteúdo
    except (FileNotFoundError, json.JSONDecodeError):
        print('Arquivo json não encontrado.')

def salvar_config_json(novas_configs):
    with open(config_file, 'w') as json_config:
        json.dump(novas_configs, json_config, indent=4)
    messagebox.showinfo("Sucesso", "Configurações salvas com sucesso!")


def open_config_interface():
    config = carregar_json()

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
    entry_login = Entry(frame_login)
    entry_login.pack(side=LEFT, padx=5)
    entry_login.insert(0, config.get("login", ""))
    frame_login.pack()

    frame_senha = Frame(nova_tela, bg=cor_fundo, padx=10, pady=5)
    Label(frame_senha, text="Senha SAP:", bg= cor_fundo).pack(side=LEFT, padx=1, pady=5)
    entry_senha = Entry(frame_senha, show = "*")
    entry_senha.pack(side=LEFT, padx=5)
    entry_senha.insert(0, config.get("senha", ""))
    frame_senha.pack()

    espaco_acima = Frame(nova_tela, height=10, bg= cor_fundo)
    espaco_acima.pack(fill="x")
    label = Label(nova_tela, text="Diretórios", bg= cor_fundo, font= ('Arial', 13, 'bold'))
    label.pack()

    def selecionar_diretorio(entry):

        diretorio = filedialog.askdirectory(title="Selecione um diretório")
        if diretorio:
            entry.delete(0, END)
            entry.insert(0, diretorio)

    frame_diretorio_aberto = Frame(nova_tela, bg=cor_fundo, padx=5, pady=5)
    Label(frame_diretorio_aberto, text="Diretorio aberto:", bg=cor_fundo).pack(side=LEFT, padx=1, pady=5)
    entry_dir_aberto = Entry(frame_diretorio_aberto)
    entry_dir_aberto.pack(side=LEFT, padx=5, pady=5)
    entry_dir_aberto.insert(0, config.get("diretorio1", ""))
    botao_dir_aberto = Button(frame_diretorio_aberto, text="Selecionar",
                              command=lambda: selecionar_diretorio(entry_dir_aberto))
    botao_dir_aberto.pack(side=LEFT, padx=5, pady=5)
    frame_diretorio_aberto.pack()

    frame_diretorio_consolidado = Frame(nova_tela, bg=cor_fundo, padx=5, pady=5)
    Label(frame_diretorio_consolidado, text="Diretorio consolidado:", bg=cor_fundo).pack(side=LEFT, padx=1, pady=5)
    entry_dir_consolidado = Entry(frame_diretorio_consolidado)
    entry_dir_consolidado.pack(side=LEFT, padx=5, pady=5)
    entry_dir_consolidado.insert(0, config.get("diretorio2", ""))
    botao_dir_consolidado = Button(frame_diretorio_consolidado, text="Selecionar",
                                   command=lambda: selecionar_diretorio(entry_dir_consolidado))
    botao_dir_consolidado.pack(side=LEFT, padx=5, pady=5)
    frame_diretorio_consolidado.pack()

    def salvar():
        novas_configs = {
            "login": entry_login.get(),
            "senha": entry_senha.get(),
            "diretorio1": entry_dir_aberto.get(),
            "diretorio2": entry_dir_consolidado.get()
        }
        salvar_config_json(novas_configs)

    Button(nova_tela, text= 'SALVAR', bg = '#98c096', command=salvar).pack(pady = 10)

    nova_tela.mainloop()