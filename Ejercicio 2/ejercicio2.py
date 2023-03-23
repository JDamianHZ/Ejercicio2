from tkinter import *
from tkinter import ttk
from tkinter import ttk
import tkinter as ttk
from tkinter import font



raiz=Tk()



mainFrame= ttk.Frame(raiz,width=600, height=200,bg="black") #widget transparete hasta especificar
mainFrame.grid()

sub2_Frame= ttk.Frame(mainFrame,bg="gray40",width=600, height=200) #widget transparete hasta especificar
sub2_Frame.grid(column=0, row=0,sticky=(W,E,N,S))

sub3_Frame= ttk.Frame(mainFrame,bg="black") #widget transparete hasta especificar
sub3_Frame.grid(column=0, row=1,sticky=(W,E,N,S))

sub6_Frame= ttk.Frame(sub3_Frame, width=690, height=240, bg="#482525") #widget transparete hasta especificar
sub6_Frame.grid(column=0, row=4,sticky=(W,E,N,S),padx= 20, pady= 10)

sub4_Frame= ttk.Frame(sub6_Frame,bg="#482525") #widget transparete hasta especificar
sub4_Frame.grid(column=0, row=3,padx= 20, pady= 10,sticky=(W,E,N,S))
     

sub5_Frame= ttk.Frame(sub6_Frame, width=690, height=240, bg="#482525") #widget transparete hasta especificar
sub5_Frame.grid(column=0, row=4,sticky=(W,E,N,S),padx= 20, pady= 10)





#-----frmae con carrito------
imagen = PhotoImage(file="carrito.png")
etqImagen=ttk.Label(sub2_Frame,bg="gray40")
etqImagen.grid(column=0,row=0,sticky=(W))
etqImagen['image']=imagen

timg=ttk.Label(sub2_Frame,text="Product management",font=("Arial",30,"bold"),foreground="white",bg="gray40").grid(column=1,row=0)
ttk.Label(sub2_Frame,text="                                                    ", bg="gray40").grid(column=2,row=0)

#-------frame dentro de negro-------
ttk.Label(sub4_Frame, text="id producto: ",font=("Arial",15,"bold"),foreground="white",bg="#482525").grid(column=0,row=1,sticky=(W))  
ttk.Label(sub4_Frame, text="___________ ",font=("Arial",15,"bold"),foreground="white",bg="#482525",bd=0).grid(column=1,row=1,sticky=(S))  

piesEntry= ttk.Entry(sub4_Frame,width=22,bg="#482525",bd=0)
piesEntry.grid(column=1,row=1,padx=25) 

ttk.Label(sub4_Frame, text="Name: ",font=("Arial",15,"bold"),foreground="white",bg="#482525").grid(column=0,row=2,sticky=(W)) 
ttk.Label(sub4_Frame, text="___________ ",font=("Arial",15,"bold"),foreground="white",bg="#482525",bd=0).grid(column=1,row=2,sticky=(S))  

piesEntry= ttk.Entry(sub4_Frame,width=22,bg="#482525",bd=0)
piesEntry.grid(column=1,row=2,padx=25) 

ttk.Label(sub4_Frame, text="Description: ",font=("Arial",15,"bold"),foreground="white",bg="#482525").grid(column=0,row=3, sticky=(W))  
ttk.Label(sub4_Frame, text="___________ ",font=("Arial",15,"bold"),foreground="white",bg="#482525",bd=0).grid(column=1,row=3,sticky=(S))  

piesEntry= ttk.Entry(sub4_Frame,width=22,bg="#482525",bd=0)
piesEntry.grid(column=1,row=3,padx=25) 

ttk.Label(sub4_Frame, text="quantity: ",font=("Arial",15,"bold"),foreground="white",bg="#482525",bd=0).grid(column=0,row=4,sticky=(W))  
ttk.Label(sub4_Frame, text="___________ ",font=("Arial",15,"bold"),foreground="white",bg="#482525",bd=0).grid(column=1,row=4,sticky=(S))  

piesEntry= ttk.Entry(sub4_Frame,width=22,bg="#482525",bd=0)
piesEntry.grid(column=1,row=4,padx=100,sticky=(N)) 




ttk.Label(sub4_Frame, text="Price: ",font=("Arial",15,"bold"),foreground="white",bg="#482525").grid(column=0,row=5,sticky=(W))  
ttk.Label(sub4_Frame, text="___________ ",font=("Arial",15,"bold"),foreground="white",bg="#482525",bd=0).grid(column=1,row=5,sticky=(S))  

piesEntry= ttk.Entry(sub4_Frame,width=22,bg="#482525",bd=0)
piesEntry.grid(column=1,row=5,padx=25) 




imagen2 = PhotoImage(file="lupa.png")

btnImagen = ttk.Button(sub4_Frame,bg="#482525",bd=0)
btnImagen.grid(column=2,row=0)
btnImagen['image']= imagen2

imagen3 = PhotoImage(file="brocha.png")

btnImagen = ttk.Button(sub4_Frame,bg="#482525", bd=0)
btnImagen.grid(column=3,row=0,sticky=(W))
btnImagen['image']= imagen3

mi_fuente = font.Font(size=10)

boton = Button(sub4_Frame, text= " Back",font= mi_fuente)
boton.grid(sticky=(W), column=4, row=0)

boton.config(bg="#482525", fg="Blue", bd=0)


boton2 = Button(sub4_Frame, text= " SAVE")
boton2.grid(sticky=(W), column=2, row=2,columnspan=3,rowspan=2)

boton2.config(bg="lime green", fg="snow", bd=0,width=15, height=1)


ttk.Label(sub4_Frame, text="        ",font=("Arial",15,"bold"),foreground="white",bg="#482525").grid(column=5,row=2,sticky=(W))  

boton3 = Button(sub4_Frame, text= " Delete ")
boton3.grid(sticky=(W), column=2, row=3,columnspan=3,rowspan=2)

boton3.config(bg="red", fg="snow", bd=0,width=15, height=1)


boton3 = Button(sub4_Frame, text= " Update ")
boton3.grid(sticky=(W), column=2, row=5,columnspan=3,rowspan=2)

boton3.config(bg="DarkOrange", fg="snow", bd=0,width=15, height=1)


#---------tabla-------


# Crear encabezado de la tabla
ttk.Label(sub5_Frame, text="ID", width=10, bg="gray", fg="white").grid(row=0, column=0)
ttk.Label(sub5_Frame, text="Nombre", width=20, bg="gray", fg="white").grid(row=0, column=1)
ttk.Label(sub5_Frame, text="Descripción", width=30, bg="gray", fg="white").grid(row=0, column=2)
ttk.Label(sub5_Frame, text="Cantidad", width=10, bg="gray", fg="white").grid(row=0, column=3)
ttk.Label(sub5_Frame, text="Precio", width=10, bg="gray", fg="white").grid(row=0, column=4)


# Crear datos de la tabla
data = [
    ("1", "Producto 1", "Descripción del producto 1", "10", "$100"),
    ("2", "Producto 2", "Descripción del producto 2", "5", "$50"),
    ("3", "Producto 3", "Descripción del producto 3", "20", "$200"),
    ("4", "Producto 3", "Descripción del producto 3", "20", "$200"),
    ("5", "Producto 3", "Descripción del producto 3", "20", "$200"),
    ("", "", "", "", ""),
    ("", "", "", "", ""),
    ("", "", "", "", "")
 

]

# Mostrar datos en la tabla
for i, row in enumerate(data):
    for j, item in enumerate(row):
        ttk.Label(sub5_Frame, text=item, width=10 if j == 0 else 20 if j == 1 else 30 if j == 2 else 10 if j == 3 else 10, bg="white").grid(row=i+1, column=j)



raiz.mainloop()