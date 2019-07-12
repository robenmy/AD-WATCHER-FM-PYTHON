from tkinter import*

'''
raiz = Tk()
raiz.title("ADWATCHER FM")
raiz.resizable(False, False)
#para agregar un logo a la ventana:
raiz.iconbitmap("image.ico")
raiz.geometry("900x550")
#Para cambiar color de ventana
raiz.config(bg="blue")
miframe = Frame() # se utiliza para colocar los botones o widget
miframe.pack()
miframe.config(bg="red")
miframe.config(width="900", height="550")
# para colocar imagen en la ventana
# miImagen = PhotoImage(file="mouse.gif")
# label(miframe, image=miImagen).place(x=100,y=200)
miFrame2=Frame(raiz)

miFrame2.pack(side=LEFT)
botonLeer=Button(miFrame2, text="DETENER", command=quit)
botonLeer.grid(row=0, column=0, sticky="n", padx=0,pady=0)

raiz.mainloop()
'''
# segunda parte ----------------------------
'''
# Configuración de la raíz
root = Tk()
root.title("Hola mundo")
root.resizable(1,1)
#root.iconbitmap('hola.ico')

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
#frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

#root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

# Para centrar la ventana en medio de la pantalla
w = root.winfo_reqwidth()
h = root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('+%d+%d' % (x, y))

# Finalmente bucle de la aplicación
root.mainloop()
'''

# Tercera parte de prueba interfaz
import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Posicionar elementos en Tcl/Tk")
        
        main_window.configure(width=900, height=600)
        # Ignorar esto por el momento.
        self.place(relwidth=1, relheight=1)
        self.button = ttk.Button(self, text="Hola, mundo!")
        self.button.place(x=60, y=40, width=200, height=300)

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()