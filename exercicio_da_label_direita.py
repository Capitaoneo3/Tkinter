import tkinter as tk
from tkinter import ttk

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de Scrollbar Visível")
root.geometry("300x200")
frame1 = tk.Frame(root,bg="blue")
frame1.pack(fill="both")
frame2 = tk.Frame(root,bg="blue")
frame2.pack(fill="both")


# Criar o frame para conter o Listbox e a Scrollbar
label1 = tk.Label(frame1,text="shakira",background="yellow")
label1.pack(side="right")
label2 = tk.Label(frame2,text="HHHHHHHH",background="red")
label2.pack(side="right")


root.mainloop()
