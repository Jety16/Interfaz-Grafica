from tkinter import *




root =Tk()
frame=Frame(root, width=400, height= 300,)
frame.pack()

minombre=StringVar()
#recuadros de de texto (entrys)

#nombre
cuadrotexto=Entry(frame,textvariable=minombre)
cuadrotexto.grid(row =0, column = 1, pady=3)
cuadrotexto.config (justify = "center")

#apellido
cuadrotexto1=Entry(frame)
cuadrotexto1.grid(row =1, column = 1, pady=3)
cuadrotexto1.config (justify = "center")

#edad
cuadrotexto2=Entry(frame)
cuadrotexto2.grid(row =2, column = 1, pady=3)
cuadrotexto2.config (justify = "center" )

#contraseña
cuadropass=Entry(frame)
cuadropass.grid(row =3, column = 1, pady=3)
cuadropass.config (justify = "center")
#show sirve para ocultar la contraseña en este caso con " * "
cuadropass.config(show= "*")

#textos
textos=Text (frame, width= 16, height=5)
textos.grid (row=4, column = 1,pady=3)

scrollvert=Scrollbar(frame, command=textos.yview)
scrollvert.grid(row=4, column=2, sticky="nsew")

textos.config(yscrollcommand=scrollvert.set)

#botonesss
def codigoBoton():

	minombre.set("Juan")


boton= Button (root, text="enviar",command=codigoBoton)

boton.pack()



#labels (o textos seteados por el creador)
#nombre
nombreLabel = Label (frame, text= "Nombre:")
nombreLabel.grid (row= 0, column = 0,sticky= "w",pady=4)

#apellido
nombreLabel1 = Label (frame, text= "Apellido:")
nombreLabel1.grid (row= 1, column = 0,sticky= "w", pady=4)

#edad
nombreLabel2 = Label (frame, text= "Edad:")
nombreLabel2.grid (row= 2, column = 0,sticky= "w",pady=4)

#contraseña
labelpass = Label (frame, text= "Contraseña:")
labelpass.grid (row= 3, column = 0,sticky= "w",pady=4)

#texto
labelTexto= Label (frame, text = "Texto: ")
labelTexto.grid (row=4, column= 0,sticky= "w", pady=4)







root.mainloop()