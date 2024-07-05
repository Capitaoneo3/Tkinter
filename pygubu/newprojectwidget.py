import tkinter as tk

# Configura��o da janela principal
janela = tk.Tk()
janela.geometry("400x400")
janela.title("Place Layout Example")

def custom_label(x_,Y_,str_,color,f_color):
    label1 = tk.Label(janela, text=str_, bg=color, fg=f_color,width=2,height=2)
    label1.place(x=x_, y=Y_)

custom_label(100,0,"  ","blue","white")
custom_label(300,0,"  ","blue","white")

custom_label(230,280,"  ","blue","white")
custom_label(240,290,"  ","blue","white")
custom_label(230,300,"  ","blue","white")
custom_label(250,300,"  ","blue","white")
custom_label(280,290,"  ","red","white")
custom_label(320,250,"  ","blue","white")
custom_label(350,200,"  ","blue","white")

# Executar a aplica��o
janela.mainloop()

