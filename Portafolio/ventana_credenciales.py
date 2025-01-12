import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

#Configuración de la Ventana principal
ventana = tk.Tk()
ventana.title('PA- Portafolio automatizado')
ventana.geometry('1280x720')
ventana.resizable(width=False, height=False)

DEPARTAMENTOS = ['Arquitectura y Redes de Computadoras', ]

#Variables globales
nombreProfesor = tk.StringVar()
nombreMateria = tk.StringVar()
grupoCurso = tk.StringVar()
nombre = tk.StringVar()
apellido = tk.StringVar()
departamento = tk.StringVar()
rutaTareas = tk.StringVar()

#Mensaje de ayuda para mostrarle al usuario como se usa el programa.
def boton_ayuda():
    #Configuracion del mensaje
    ventana_ayuda = tk.Toplevel(ventana)
    ventana_ayuda.resizable(width=False, height=False)
    ventana_ayuda.title("Informacion sobre el uso del programa")

    #Mensaje
    mensaje = '''Este es un mensaje de ayuda
    es posible hacer esto?'''

    #configuracion del mensaje de ayuda
    tk.Message(ventana_ayuda, text=mensaje, width=300).pack()

#Funcion para seleccionar carpetas
def seleccion_carpeta():
    carpeta_seleccionada = filedialog.askdirectory()
    if carpeta_seleccionada:
        ruta.config(text=f'Carpeta Seleccionada: {carpeta_seleccionada}')
    else:
        ruta.config(text='No se ha seleccionado ninguna carpeta.')

#Texto que indica ayuda
tk.Label(ventana, text="¿Necesitas ayuda? Pulsa este boton!").place(x=1000, y=14)
#Configuracion del boton imagen
imagen_ayuda = tk.PhotoImage(file = r'.\Portafolio\imagenes\info_button.png')
tk.Button(ventana,image=imagen_ayuda, 
          command= boton_ayuda, 
          width= 38, height=38).place(x=1200, y=0)
#titulo
tk.Label(ventana, text='Portafolio Automatizado', font=('Arial', 16)).pack()
#Boton para seleccionar la ruta de la carpeta donde se quiere guardar




tk.Button(ventana, text='Selecciona la ruta donde quieres guardar el portafolio', command=seleccion_carpeta).pack()
ruta = tk.Label(ventana, text='')
ruta.pack()
#Input nombre de la materia
tk.Label(text='Introduce el nombre de la materia', font=('Inter Bold',16)).pack(anchor=tk.E, ipadx=40)
tk.Entry(ventana, textvariable=nombreMateria, width=50).pack(padx=50)

tk.Label(text='Introduce tu nombre', font=('Inter Bold',16), justify='left').pack()
tk.Entry(ventana, textvariable=nombre, width=50).pack()

tk.Label(text='Introduce tu apellido', font=('Inter Bold',16), justify='left').pack()
tk.Entry(ventana, textvariable=apellido, width=50).pack()


#Boton para crear Portafolio y comprobar la informacion proporcionada
tk.Button(text='Crear Portafolio', height=2,width=20, command=lambda: comprobacion()).pack()

#Comprobacion del estado de la informacion
def comprobacion():
    try:
        if len(str(nombreMateria.get())) == 0:
            messagebox.showwarning('Error!', 'Debes introducir el nombre de la materia que estas cursando.').pack()
    except Exception as MensajeMateria:
        pass

ventana.mainloop()