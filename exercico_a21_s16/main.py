import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("400x400")
janela.title("Grid Layout with Borders")

# Frame com borda sólida
frame = tk.Frame(janela, borderwidth=2)
frame.pack( fill="both")

# Adicionar labels no frame
label = tk.Label(frame, text="seg", borderwidth=2, relief="solid",bg="black",fg="white")
label.grid(row=0, column=0, sticky="nsew")

label1 = tk.Label(frame, text="ter", borderwidth=2, relief="solid",bg="black",fg="white")
label1.grid(row=0, column=1, sticky="nsew")

label2 = tk.Label(frame, text="quar", borderwidth=2, relief="solid",bg="black",fg="white")
label2.grid(row=0, column=2, sticky="nsew")

label3 = tk.Label(frame, text="quin", borderwidth=2, relief="solid",bg="black",fg="white")
label3.grid(row=0, column=3, sticky="nsew")

label4 = tk.Label(frame, text="sex", borderwidth=2, relief="solid",bg="black",fg="white")
label4.grid(row=0, column=4, sticky="nsew")

label5 = tk.Label(frame, text="sáb", borderwidth=2, relief="solid",bg="black",fg="white")
label5.grid(row=0, column=5, sticky="nsew")

label6 = tk.Label(frame, text="dom", borderwidth=2, relief="solid",bg="black",fg="white")
label6.grid(row=0, column=6, sticky="nsew")

label7 = tk.Label(frame, text="", borderwidth=2,bg="blue")
label7.grid(row=1, column=0, sticky="nsew")

label8 = tk.Label(frame, text="", borderwidth=2,bg="white")
label8.grid(row=1, column=1, sticky="nsew")

label9 = tk.Label(frame, text="", borderwidth=2,bg="blue")
label9.grid(row=1, column=2, sticky="nsew")

label10 = tk.Label(frame, text="", borderwidth=2,bg="white")
label10.grid(row=1, column=3, sticky="nsew")

label11 = tk.Label(frame, text="", borderwidth=2,bg="orange")
label11.grid(row=1, column=4, sticky="nsew")

label12 = tk.Label(frame, text="", borderwidth=2,bg="white")
label12.grid(row=1, column=5, sticky="nsew")

label13 = tk.Label(frame, text="", borderwidth=2,bg="blue")
label13.grid(row=1, column=6, sticky="nsew")


# Configurar as colunas para expandir uniformemente
for i in range(0, 7):
    frame.grid_columnconfigure(i, weight=1)


# Executar a aplicação
janela.mainloop()

