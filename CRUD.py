from tkinter import Tk, Menu, Frame, Button, Label, Entry, Text, Scrollbar, \
    StringVar, messagebox, END
import sqlite3


# --------------------- FUNCIONES ---------------------

def conexionBBDD():
    con = sqlite3.connect("Usuarios")
    cursor = con.cursor()

    try:
        cursor.execute('''
            CREATE TABLE datosusuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(50),
                password VARCHAR(50),
                apellido VARCHAR(20),
                direccion VARCHAR(50),
                comentarios VARCHAR(100))
            ''')

        messagebox.showinfo("BBDD", "Base de datos creada con éxito")

    except:
        messagebox.showwarning("¡Atención!", "La Base de datos ya existe")


def salir_app():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if valor == "yes":
        root.destroy()


def limpiar_campos():
    id.set("")
    nombre.set("")
    password.set("")
    apellido.set("")
    direccion.set("")
    cuadro_com.delete(1.0, END)


def crear_usuario():
    con = sqlite3.connect("Usuarios")
    cursor = con.cursor()

    cursor.execute("INSERT INTO datosusuarios VALUES (NULL, '" + nombre.get() +
        "','" + password.get() +
        "','" + apellido.get() +
        "','" + direccion.get() +
        "','" + cuadro_com.get("1.0", END) + "')")
    con.commit()

    messagebox.showinfo("BBDD", "El usuario fue creado con éxito")


def leer_usuario():
    con = sqlite3.connect("Usuarios")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM datosusuarios WHERE id=" + id.get())
    usuario = cursor.fetchone()

    if usuario:
        id_user, nomb, pas, ape, dir, com = usuario
        id.set(id_user)
        nombre.set(nomb)
        password.set(pas)
        apellido.set(ape)
        direccion.set(dir)
        cuadro_com.insert(1.0, com)
    else:
        messagebox.showwarning("BBDD", "No se encontro usuario con ese ID")

    con.commit()


def actualizar_usuario():
    con = sqlite3.connect("Usuarios")
    cursor = con.cursor()

    cursor.execute("UPDATE datosusuarios SET nombre='" + nombre.get() +
        "', password='" + password.get() +
        "', apellido='" + apellido.get() +
        "', direccion='" + direccion.get() +
        "', comentarios='" + cuadro_com.get("1.0", END) +
        "' WHERE id=" + id.get())
    con.commit()

    messagebox.showinfo("BBDD", "Usuario actualizado con éxito")


def eliminar_usuario():
    con = sqlite3.connect("Usuarios")
    cursor = con.cursor()

    cursor.execute("DELETE FROM datosusuarios WHERE id=" + id.get())
    con.commit()

    messagebox.showinfo("BBDD", "Usuario eliminado con éxito")


def licencia():
    messagebox.showinfo("Licencia",
        "Producto bajo Licencia Pública General GNU")


def acerca_app():
    messagebox.showinfo("Créditos", "CRUD App Creado por Ana Kloss")


root = Tk()
root.title("CRUD App")

# --------------------- BARRA MENU --------------------- |

barra_menu = Menu(root)
root.config(menu=barra_menu, width=300, height=300)

menu_bbdd = Menu(barra_menu, tearoff=0)
menu_bbdd.add_command(label="Conectar", command=conexionBBDD)
menu_bbdd.add_command(label="Salir", command=salir_app)

menu_borrar = Menu(barra_menu, tearoff=0)
menu_borrar.add_command(label="Borrar campos", command=limpiar_campos)

menu_crud = Menu(barra_menu, tearoff=0)
menu_crud.add_command(label="Crear", command=crear_usuario)
menu_crud.add_command(label="Leer", command=leer_usuario)
menu_crud.add_command(label="Actualizar", command=actualizar_usuario)
menu_crud.add_command(label="Borrar", command=eliminar_usuario)

menu_ayuda = Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Licencia", command=licencia)
menu_ayuda.add_command(label="Acerca de...", command=acerca_app)

barra_menu.add_cascade(label="BBDD", menu=menu_bbdd)
barra_menu.add_cascade(label="Borrar", menu=menu_borrar)
barra_menu.add_cascade(label="CRUD", menu=menu_crud)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)


# --------------------- FRAME GRID --------------------- |

frame = Frame(root)
frame.pack()

id = StringVar()
nombre = StringVar()
password = StringVar()
apellido = StringVar()
direccion = StringVar()

# === CUADROS ===
cuadro_id = Entry(frame, textvariable=id)
cuadro_id.grid(row=0, column=1, padx=10, pady=3)

cuadro_nomb = Entry(frame, textvariable=nombre)
cuadro_nomb.grid(row=1, column=1, padx=10, pady=3)
cuadro_nomb.config(fg="red", justify="right")

cuadro_pass = Entry(frame, textvariable=password)
cuadro_pass.grid(row=2, column=1, padx=10, pady=3)
cuadro_pass.config(show="*")

cuadro_ape = Entry(frame, textvariable=apellido)
cuadro_ape.grid(row=3, column=1, padx=10, pady=3)

cuadro_dir = Entry(frame, textvariable=direccion)
cuadro_dir.grid(row=4, column=1, padx=10, pady=3)

cuadro_com = Text(frame, width=20, height=5)
cuadro_com.grid(row=5, column=1, padx=10, pady=3)
scrollVert = Scrollbar(frame, command=cuadro_com.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
cuadro_com.config(yscrollcommand=scrollVert.set)

# === LABELS ===
label_id = Label(frame, text="ID:")
label_id.grid(row=0, column=0, padx=10, pady=3, sticky="e")

label_nomb = Label(frame, text="Nombre:")
label_nomb.grid(row=1, column=0, padx=10, pady=3, sticky="e")

label_pass = Label(frame, text="Contraseña:")
label_pass.grid(row=2, column=0, padx=10, pady=3, sticky="e")

label_ape = Label(frame, text="Apellido:")
label_ape.grid(row=3, column=0, padx=10, pady=3, sticky="e")

label_dir = Label(frame, text="Dirección:")
label_dir.grid(row=4, column=0, padx=10, pady=3, sticky="e")

label_com = Label(frame, text="Comentarios:")
label_com.grid(row=5, column=0, padx=10, pady=3, sticky="e")

# --------------------- FRAME BOTONES --------------------- |

frame_botones = Frame(root)
frame_botones.pack()

boton_crear = Button(frame_botones, text="Crear", command=crear_usuario)
boton_crear.grid(row=1, column=0, padx=10, pady=3, sticky="e")

boton_leer = Button(frame_botones, text="Leer", command=leer_usuario)
boton_leer.grid(row=1, column=1, padx=10, pady=3, sticky="e")

boton_modif = Button(frame_botones, text="Actualizar", command=actualizar_usuario)
boton_modif.grid(row=1, column=2, padx=10, pady=3, sticky="e")

boton_borrar = Button(frame_botones, text="Borrar", command=eliminar_usuario)
boton_borrar.grid(row=1, column=3, padx=10, pady=3, sticky="e")


root.mainloop()
