from tkinter import *
import json
from tkinter import messagebox
from tkinter import filedialog

cor_fundo = '#c7d7c6'  ##3443eb
cor_btn = '#98c096'  ##f5d142
cor_letra = 'black'


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



def open_config_interface(main_window):
    main_window.withdraw()

    config = carregar_json()

    img = PhotoImage(file='folder_icon.png')

    config_window = Toplevel()
    config_window.title("Configuração")
    config_window.geometry("300x350")
    config_window.resizable(False, False)
    config_window.config(bg=cor_fundo)

    def on_close():
        main_window.deiconify()
        config_window.destroy()

    config_window.protocol("WM_DELETE_WINDOW", on_close)

    titulo = Label(config_window, text = 'RPA - DPE', bg = cor_fundo, fg = cor_letra, font= ('Arial', 23, 'bold'))
    titulo.pack(pady=5)

    espaco_acima = Frame(config_window, height=10, bg= cor_fundo)
    espaco_acima.pack(fill="x")
    label = Label(config_window, text="Credenciais", bg= cor_fundo, fg = cor_letra, font= ('Arial', 13, 'bold'))
    label.pack()

    frame_login = Frame(config_window, bg=cor_fundo, padx=10, pady=5)
    Label(frame_login, text="Login SAP:", bg= cor_fundo, fg = cor_letra).pack(side=LEFT, padx=1, pady=5)
    entry_login = Entry(frame_login)
    entry_login.pack(side=LEFT, padx=5)
    entry_login.insert(0, config.get("login", ""))
    frame_login.pack()

    frame_senha = Frame(config_window, bg=cor_fundo, padx=10, pady=5)
    Label(frame_senha, text="Senha SAP:", bg= cor_fundo, fg = cor_letra).pack(side=LEFT, padx=1, pady=5)
    entry_senha = Entry(frame_senha, show = "*")
    entry_senha.pack(side=LEFT, padx=5)
    entry_senha.insert(0, config.get("senha", ""))
    frame_senha.pack()

    espaco_acima = Frame(config_window, height=10, bg= cor_fundo)
    espaco_acima.pack(fill="x")
    label = Label(config_window, text="Diretórios", bg= cor_fundo, fg = cor_letra, font= ('Arial', 13, 'bold'))
    label.pack()

    def selecionar_diretorio(entry):

        diretorio = filedialog.askdirectory(title="Selecione um diretório")
        if diretorio:
            entry.delete(0, END)
            entry.insert(0, diretorio)

    frame_diretorio_corrente = Frame(config_window, bg=cor_fundo, padx=5, pady=5)
    Label(frame_diretorio_corrente, text="Dir. corrente:", bg=cor_fundo, fg = cor_letra).pack(side=LEFT, padx=1, pady=5)
    entry_dir_corrente = Entry(frame_diretorio_corrente)
    entry_dir_corrente.pack(side=LEFT, padx=5, pady=5)
    entry_dir_corrente.insert(0, config.get("diretorio1", ""))
    botao_dir_corrente = Button(frame_diretorio_corrente, text="folder", bg = cor_btn,
                              command=lambda: selecionar_diretorio(entry_dir_corrente))
    botao_dir_corrente.config(image=img)
    botao_dir_corrente.pack(side=LEFT, padx=5, pady=5)
    frame_diretorio_corrente.pack()

    frame_diretorio_consolidado = Frame(config_window, bg=cor_fundo, padx=5, pady=5)
    Label(frame_diretorio_consolidado, text="Dir. consolidado:", bg=cor_fundo, fg = cor_letra).pack(side=LEFT, padx=1, pady=5)
    entry_dir_consolidado = Entry(frame_diretorio_consolidado)
    entry_dir_consolidado.pack(side=LEFT, padx=5, pady=5)
    entry_dir_consolidado.insert(0, config.get("diretorio2", ""))
    botao_dir_consolidado = Button(frame_diretorio_consolidado, text="folder", bg = cor_btn,
                                   command=lambda: selecionar_diretorio(entry_dir_consolidado))
    botao_dir_consolidado.config(image=img)
    botao_dir_consolidado.pack(side=LEFT, padx=5, pady=5)
    frame_diretorio_consolidado.pack()

    def voltar_homepg():
        config_window.destroy()
        main_window.deiconify()

    def salvar():
        novas_configs = {
            "login": entry_login.get(),
            "senha": entry_senha.get(),
            "diretorio1": entry_dir_corrente.get(),
            "diretorio2": entry_dir_consolidado.get()
        }
        salvar_config_json(novas_configs)
        voltar_homepg()

    Button(config_window, text='  SALVAR ', bg = cor_btn, command=salvar).pack()
    Button(config_window, text='CANCELAR', bg='#de4b4b', command=voltar_homepg).pack(pady=4)

    config_window.mainloop()