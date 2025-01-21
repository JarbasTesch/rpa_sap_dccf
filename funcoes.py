import subprocess
import win32com.client
import time
import pyautogui


def conectar_sap():
    try:
        SapGuiAuto = win32com.client.GetObject("SAPGUISERVER")
        if not SapGuiAuto:
            raise Exception("SAP GUI não encontrado. Certifique-se de que está aberto.")

        application = SapGuiAuto.GetScriptingEngine

        connection = application.Children(0)

        session = connection.Children(0)

        session.findById("wnd[0]").resizeWorkingPane(235, 50, False) # Tela cheia
        session.findById("wnd[0]/usr/txtRSYST-MANDT").text = "100"  # Cliente
        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = "0931221"  # Usuário
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = "@Floki1046967000"  # Senha
        session.findById("wnd[0]/usr/txtRSYST-LANGU").text = "PT"  # Idioma
        session.findById("wnd[0]/usr/txtRSYST-LANGU").setFocus()
        session.findById("wnd[0]/usr/txtRSYST-LANGU").caretPosition = 2
        session.findById("wnd[0]").sendVKey(0)

        print("Login realizado com sucesso!")
        return session

    except Exception as e:
        print(f"Erro ao conectar ao SAP GUI: {e}")
        return None

def iniciar_sap():
    try:
        subprocess.Popen([r'C:\Program Files (x86)\SAP\NWBC65\NWBC'])
        print("Abrindo o SAP")

        imagem = 'gatilho_login.png'

        while True:
            try:
                pyautogui.locateOnScreen(imagem, grayscale=True, confidence=0.9)
                print('SAP carregado. Continuando...')
                break
            except:
                time.sleep(1)
                print('Procurando SAP...')

        print('SAP iniciado com sucesso. Pronto para logar.')
    except Exception as e:
        print(f'Erro ao iniciar o SAP: {e}')

def teste(session):
    session.findById("wnd[0]/tbar[0]/okcd").text = "ME5A"
    session.findById("wnd[0]").sendVKey(0)


def funcao_sap():
    try:

        iniciar_sap()

        session = conectar_sap()

        if session:
            print("Conexão e login bem-sucedidos! Pronto para executar comandos no SAP.")
        else:
            print("Falha ao conectar ao SAP após iniciar.")

    except Exception as e:
        print(f"Erro na execução da 'funcao_sap': {e}")