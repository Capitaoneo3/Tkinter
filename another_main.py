import tkinter as tk

def exibir_texto():
    texto = entrada.get()
    label.config(text=texto)

janela = tk.Tk()
janela.title("Entrada de Texto")
janela.geometry("400x300")

# Adicionar um campo de entrada de texto
entrada = tk.Entry(janela)
entrada.pack()

# Adicionar um botão
botao = tk.Button(janela, text="Exibir Texto", command=exibir_texto)
botao.pack()

# Adicionar um rótulo
label = tk.Label(janela, text="")
label.pack()

janela.mainloop()
