import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("400x400")
janela.title("Place Layout Example")

def custom_label(x_,Y_,str_,color,f_color):
    label1 = tk.Label(janela, text=str_, bg=color, fg=f_color,width=2,height=2)
    label1.place(x=x_, y=Y_)

custom_label(100,0,"  ","blue","white")
custom_label(300,0,"  ","blue","white")


custom_label(40,210,"  ","blue","white")
custom_label(60,240,"  ","blue","white")
custom_label(80,260,"  ","blue","white")
custom_label(120,290,"  ","blue","white")

custom_label(150,300,"  ","blue","white")
custom_label(180,310,"  ","blue","white")
custom_label(210,300,"  ","blue","white")
custom_label(250,300,"  ","blue","white")
custom_label(280,290,"  ","blue","white")
custom_label(320,250,"  ","blue","white")
custom_label(350,200,"  ","blue","white")

# Executar a aplicação
janela.mainloop()

