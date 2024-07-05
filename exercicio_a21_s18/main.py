import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("400x400")
janela.title("Place Layout Example")


label4 = tk.Label(janela, text="yeee", bg="yellow", fg="black")
label4.pack(side="right")
label5 = tk.Label(janela, text="reedd", bg="red", fg="black")
label5.pack(side="right")

# Executar a aplicação
janela.mainloop()

