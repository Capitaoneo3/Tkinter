import tkinter as tk
from tkinter import ttk

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de Frame Rolável")
root.geometry("500x200")

# Criar um frame para conter o Canvas e a Scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Criar o Canvas
canvas = tk.Canvas(frame)
canvas.pack(side="left", fill="both", expand=True)

# Adicionar a Scrollbar vertical ao frame
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configurar o Canvas para usar a Scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

# Criar um frame dentro do Canvas
scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Adicionar Labels dentro do frame scrollável
for i in range(20):  # Adiciona 20 Labels como exemplo
    label = tk.Label(scrollable_frame, text=f"Item {i+1}", anchor="w")
    label.pack(fill="x", padx=5, pady=5)

# Iniciar o loop principal
root.mainloop()
