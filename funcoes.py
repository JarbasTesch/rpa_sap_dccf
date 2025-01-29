from datetime import datetime
import subprocess
import win32com.client
import time
import json
import os
import sys

def caminho_recurso(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

config_file = caminho_recurso('config.json')

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

def funcao_sap():
    # Abrir o exe do SAP
    subprocess.Popen(r'C:\Program Files (x86)\SAP\NWBC65\NWBC')
    print('\nAbrindo o exe do SAP...\n')

    # Esperar até o SAP GUI estar carregado
    time.sleep(1)

    tentativas = 0
    config = carregar_json()  # Carrega o config ANTES das tentativas

    while tentativas <= 25:
        try:
            SapGuiAuto = win32com.client.GetObject("SAPGUISERVER")
            if not SapGuiAuto:
                tentativas += 1
                print("\nSAP GUI não está disponível...\n")
                time.sleep(2)  # Delay entre tentativas
                continue

            application = SapGuiAuto.GetScriptingEngine
            connection = application.Children(0)
            session = connection.Children(0)

            print('\nSAP GUI carregado com sucesso... Vamos realizar o login.\n')

            # Realizar login
            session.findById("wnd[0]").resizeWorkingPane(235, 50, False)  # Tela cheia
            session.findById("wnd[0]/usr/txtRSYST-MANDT").text = "100"  # Cliente
            session.findById("wnd[0]/usr/txtRSYST-BNAME").text = config.get("login", "")  # Usuário
            session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = config.get("senha", "")  # Senha
            session.findById("wnd[0]/usr/txtRSYST-LANGU").text = "PT"  # Idioma
            session.findById("wnd[0]/usr/txtRSYST-LANGU").setFocus()
            session.findById("wnd[0]/usr/txtRSYST-LANGU").caretPosition = 2
            session.findById("wnd[0]").sendVKey(0)

            try:
                session.findById("wnd[1]/tbar[0]/btn[0]").press()
                print("Elemento opcional encontrado e interagido com sucesso.")
            except:
                print("Elemento opcional não encontrado. Continuando a execução.")

            time.sleep(1)

            # Verificar se o login foi bem-sucedido
            try:
                session.findById("wnd[0]/tbar[1]/btn[34]").setfocus()
                print('Login realizado com sucesso')
                funcao_sap.session = session
                return False, "Login realizado com sucesso.", session  # Erro=False, mensagem de sucesso
            except:
                print('Falha ao logar. Login e Senha podem estar errados.')
                session.findById("wnd[0]").close()
                return True, """\nFalha ao Logar. 
                Login ou Senha podem estar errados.
                Aperte no ícone de engrenagem para alterar as credenciais.
                Depois aperte o botão novamente.""", None

        except Exception as e:
            print(f'Erro: {e}\nAguardando o SAP GUI carregar...\n')
            tentativas += 1
            time.sleep(2)  # Delay entre tentativas

    # Caso o loop exceda o limite de tentativas
    return True, "Não foi possível estabelecer conexão com o SAP GUI. Verifique o SAP e tente novamente.", None

hoje = datetime.now()
mes_atual = hoje.month
ano_atual = hoje.year

def balanco_corrente(session):

    config = carregar_json()

    try:
        session.findById("wnd[0]/tbar[0]/okcd").text = "f.01"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtSD_KTOPL-LOW").text = "pcf1"
        session.findById("wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/ctxtBILAVERS").text = "bn01"
        session.findById("wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/ctxtBILASPRA").text = "pt"
        session.findById("wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/txtBILBJAHR").text = ano_atual
        session.findById("wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/txtB-MONATE-LOW").text = "1"
        session.findById("wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/txtB-MONATE-HIGH").text = mes_atual
        session.findById("wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/txtBILVJAHR").text = ano_atual - 1
        session.findById("wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/txtV-MONATE-LOW").text = "1"
        session.findById("wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/txtV-MONATE-HIGH").text = mes_atual
        session.findById("wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/radBILALIST").setFocus()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/mbar/menu[0]/menu[1]/menu[2]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").select()
        session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        #talvez mude ↓
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = config.get("diretorio1", "")
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "balanco_corrente.txt"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
        session.findById("wnd[0]").sendVKey(0)
        return False, "Extração do balanço corrente realizada.", session

    except Exception as e:
        return True, f"Falha na extração do balanço corrente.\n Erro: {e}", session



def mes_ano_balanco(mes, ano):

    mes_balanco = mes - 2
    ano_balanco = ano

    if mes_balanco == 0:
        mes_balanco = 12
        ano_balanco -= 1

    if mes_balanco == -1:
        mes_balanco = 11
        ano_balanco -= 1

    return mes_balanco, ano_balanco


def balanco_fechado(session):
    # print('mês: ', mes_ano_balanco(mes_atual, ano_atual)[0])
    # print('ano: ', mes_ano_balanco(mes_atual, ano_atual)[1])
    config = carregar_json()

    try:
        session.findById("wnd[0]/tbar[0]/okcd").text = "f.01"
        session.findById("wnd[0]").sendVKey(0)
        session.findById("wnd[0]/usr/ctxtSD_KTOPL-LOW").text = "pcf1"
        session.findById(
            "wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/ctxtBILAVERS").text = "bn01"
        session.findById(
            "wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/ctxtBILASPRA").text = "pt"
        session.findById(
            "wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/txtBILBJAHR").text = mes_ano_balanco(mes_atual, ano_atual)[1]
        session.findById(
            "wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/txtB-MONATE-LOW").text = "1"
        session.findById(
            "wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/txtB-MONATE-HIGH").text = mes_ano_balanco(mes_atual, ano_atual)[0]
        session.findById(
            "wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/txtBILVJAHR").text = mes_ano_balanco(mes_atual, ano_atual)[1] - 1
        session.findById(
            "wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/txtV-MONATE-LOW").text = "1"
        session.findById(
            "wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/txtV-MONATE-HIGH").text = mes_ano_balanco(mes_atual, ano_atual)[0]
        session.findById(
            "wnd[0]/usr/tabsTABSTRIP_TABBL1/tabpUCOM1/ssub%_SUBSCREEN_TABBL1:RFBILA00:0001/radBILALIST").setFocus()
        session.findById("wnd[0]/tbar[1]/btn[8]").press()
        session.findById("wnd[0]/mbar/menu[0]/menu[1]/menu[2]").select()
        session.findById(
            "wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").select()
        session.findById(
            "wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").setFocus()
        session.findById("wnd[1]/tbar[0]/btn[0]").press()
        # talvez mude ↓
        session.findById("wnd[1]/usr/ctxtDY_PATH").text = config.get("diretorio2", "")
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").text = "balanco_fechado.txt"
        session.findById("wnd[1]/usr/ctxtDY_FILENAME").caretPosition = 9
        session.findById("wnd[1]/tbar[0]/btn[11]").press()
        session.findById("wnd[0]/tbar[0]/okcd").text = "/n"
        session.findById("wnd[0]").sendVKey(0)
        return False, "Extração do balanço corrente realizada.", session

    except Exception as e:
        return True, f"Falha na extração do balanço corrente.\n Erro: {e}", session