from tkinter import *

# Configuração da janela
janela = Tk()
janela.title('Estilo Relief')
janela.geometry('400x200')

# Diferentes estilos de relief em labels
Label(janela, text="FLAT", relief=FLAT, width=10).pack(pady=5)
Label(janela, text="RAISED", relief=RAISED, width=10).pack(pady=5)
Label(janela, text="SUNKEN", relief=SUNKEN, width=10).pack(pady=5)
Label(janela, text="GROOVE", relief=GROOVE, width=10).pack(pady=5)
Label(janela, text="RIDGE", relief=RIDGE, width=10).pack(pady=5)
btn_config = Button(janela, text="Opções")
img = PhotoImage(file=r"C:\Users\tesch\Downloads\settings.png")
btn_config.config(image=img)
btn_config.pack(pady = 25)
btn_config = Button(janela, text="Opções")
img = PhotoImage(file=r"C:\Users\tesch\Downloads\settings (1).png")
btn_config.config(image=img)
btn_config.pack(pady = 25)
btn_config = Button(janela, text="Opções")
img = PhotoImage(file=r"C:\Users\tesch\Downloads\settings (2).png")
btn_config.config(image=img)
btn_config.pack(pady = 25)
# Loop principal
janela.mainloop()