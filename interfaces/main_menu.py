import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def menu (title: str):
    root = tk.Tk()
    root.title(title)
    root.geometry("720x480")

    title_label = tk.Label(root, text = "Biblioteca 200", font = ("Arial", 16, "bold"))
    title_label.pack(pady = 8)

    frame = ttk.Frame(root, padding = "4")
    frame.pack(expand = True)

    # Create and style the buttons using ttk
    button_libros = ttk.Button(frame, text="Libros", command = lambda: print('Libros'), width=20)
    # button_libros.grid(row=0, column=0, pady=10)
    button_libros.pack(pady = 8)

    button_proveedores = ttk.Button(frame, text="Proveedores", command = lambda: print('Proveedores'), width=20)
    # button_proveedores.grid(row=1, column=0, pady=10)
    button_proveedores.pack(pady = 8)

    button_clientes = ttk.Button(frame, text="Clientes", command = lambda: print('Clientes'), width=20)
    # button_clientes.grid(row=2, column=0, pady=10)
    button_clientes.pack(pady = 8)

    button_empleados = ttk.Button(frame, text="Empleados", command = lambda: print('Empleados'), width=20)
    button_empleados.pack(pady = 8)

    button_prestamos = ttk.Button(frame, text="Prestamos", command = lambda: print('Prestamos'), width=20)
    button_prestamos.pack(pady = 8)

    root.mainloop()