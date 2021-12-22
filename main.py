from tkinter import *

raiz= Tk()

miFrame=Frame(raiz,width="1200",height="600")
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1,padx="10",pady="10")
cuadroNombre.config(fg="red",justify="center")

nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=0,column=0, sticky="e",padx="10",pady="10")


cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1,padx="10",pady="10")
cuadroApellido.config(fg="red",justify="center")

nombreLabel=Label(miFrame,text="Apellido: ")
nombreLabel.grid(row=1,column=0, sticky="e",padx="10",pady="10")


cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2,column=1,padx="10",pady="10")
cuadroDireccion.config(fg="red",justify="center")

direccionLabel=Label(miFrame,text="Direccion: ")
direccionLabel.grid(row=2,column=0, sticky="e",padx="10",pady="10")


cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=3,column=1,padx="10",pady="10")
cuadroPassword.config(fg="red",justify="center",show="*")

direccionPassword=Label(miFrame,text="Password: ")
direccionPassword.grid(row=3,column=0, sticky="e",padx="10",pady="10")


raiz.mainloop()


