import tkinter as tk
def verificar_tamanho(event):
    entrada_texto = text.get(1.0,2.0)
    if len(entrada_texto) > 20:
        label.config(text="O nome é muito grande.")
        text.config(state="disabled")
    else:
        label.config(text="")
# Configuração da janela principal
janela = tk.Tk()
janela.title("Verificação de Nome")
label = tk.Label(janela,text="",background="blue")
label.pack()
text = tk.Text(janela, height=10)
text.insert("1.0","aAAAAAAAAAAAAAAAAAAAAAA")
text.pack()
text.bind("<KeyRelease>", verificar_tamanho)#bind significa evento, vamos aprender logo mais. key release é tecla solta após pressionar.
text.delete("1.0", tk.END)


janela.mainloop()


