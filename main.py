from tkinter import *

raiz= Tk()

miFrame=Frame(raiz,width="1200",height="600")
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
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

PasswordLabel=Label(miFrame,text="Password: ")
PasswordLabel.grid(row=3,column=0, sticky="e",padx="10",pady="10")

#barra de texto con scroll


ComentariosLabel=Label(miFrame,text="Comentarios: ")
ComentariosLabel.grid(row=4,column=0, sticky="e",padx="10",pady="10")

textoComentarios=Text(miFrame, width=20, height=5)
textoComentarios.grid(row=4, column=1, padx=10, pady=10)
scrollVertica=Scrollbar(miFrame, command=textoComentarios.yview)
scrollVertica.grid(row=4, column=2,sticky="nsew")
textoComentarios.config(yscrollcommand=scrollVertica.set)
def codigoBoton():
    minombre.set("Juan")


botonEnvio=Button(raiz,text="Enviar", command=codigoBoton)

botonEnvio.pack()

raiz.mainloop()


