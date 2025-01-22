import subprocess
import win32com.client
import time
import json

config_file = 'config.json'

def carregar_json():
    try:
        with open(config_file, 'r') as file:
            conteudo = file.read().strip()
            if not conteudo:  # Se o arquivo estiver vazio
                raise FileNotFoundError
            return json.loads(conteudo)  # Carrega o JSON do conteúdo
    except (FileNotFoundError, json.JSONDecodeError):
        print('Arquivo JSON não encontrado ou inválido.')
        return {}

def aguardar_sap_pronto():
    """Aguarda até que o SAP GUI esteja pronto, verificando um elemento específico."""
    while True:
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUISERVER")
            if not SapGuiAuto:
                raise Exception("SAP GUI não está disponível.")

            application = SapGuiAuto.GetScriptingEngine
            connection = application.Children(0)
            session = connection.Children(0)

            # Verifica se o elemento específico está disponível
            session.findById("wnd[0]/usr/txtRSYST-MANDT")
            print("SAP GUI pronto para login.")
            return session  # Retorna a sessão para uso
        except Exception:
            print("SAP GUI ainda não está pronto. Aguardando...")
            time.sleep(1)  # Aguarda 1 segundo antes de tentar novamente

def conectar_sap():
    try:
        config = carregar_json()

        session = aguardar_sap_pronto()

        session.findById("wnd[0]").resizeWorkingPane(235, 50, False)  # Tela cheia
        session.findById("wnd[0]/usr/txtRSYST-MANDT").text = "100"  # Cliente
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = config.get("login", "")  # Usuário
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = config.get("senha", "")  # Senha
        session.findById("wnd[0]/usr/txtRSYST-LANGU").text = "PT"  # Idioma
        session.findById("wnd[0]/usr/txtRSYST-LANGU").setFocus()
        session.findById("wnd[0]/usr/txtRSYST-LANGU").caretPosition = 2
        session.findById("wnd[0]").sendVKey(0)

        print("Login realizado com sucesso!")
        return session
    except Exception as e:
        raise RuntimeError(f"Erro ao conectar ao SAP GUI: {e}")

def iniciar_sap():
    try:
        sap_executable = r'C:\Program Files (x86)\SAP\NWBC65\NWBC'

        # Abre o SAP GUI
        subprocess.Popen([sap_executable])
        print("Abrindo o SAP...")

        # Aguarda até que o SAP GUI esteja pronto
        session = aguardar_sap_pronto()
        return session
    except Exception as e:
        print(f"Erro ao iniciar o SAP: {e}")

def funcao_sap():
    session = iniciar_sap()
    if session:
        session = conectar_sap()  # Realiza o login
        if session:
            print("Conexão e login bem-sucedidos! Pronto para executar comandos no SAP.")
        else:
            print("Falha ao conectar ao SAP após iniciar.")
    else:
        print("SAP GUI não foi iniciado corretamente.")

def teste():
    while True:
        print('testando')
