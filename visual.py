from tkinter import *

root=Tk()

miframe=Frame(root, width=1200, height=600)
miframe.pack()


cuadro=Entry(miframe)
cuadro.grid(row=0, column=1, padx=10, pady=10)
cuadro_texto=Label(miframe, text="Buscar:")
cuadro_texto.grid(row=0, column=0, padx=10, pady=10)


root.mainloop()