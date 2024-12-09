import tkinter as tk

# Función para mostrar los empleados en el Listbox
def mostrar_empleados():
    # Limpiar la lista de empleados actual
    listbox_empleados.delete(0, tk.END)
    
    # Lista de empleados (esto puede venir de una base de datos, archivo, etc.)
    empleados = [
        "Juan Pérez - Gerente",
        "María González - Administrativo",
        "Carlos López - Desarrollador",
        "Ana Martínez - Soporte",
        "Luis Sánchez - Vendedor"
    ]
    
    # Insertar los empleados en el Listbox
    for empleado in empleados:
        listbox_empleados.insert(tk.END, empleado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Empleados")

# Crear un Listbox para mostrar los empleados
listbox_empleados = tk.Listbox(ventana, width=50, height=10)
listbox_empleados.pack(pady=20)

# Botón para cargar la lista de empleados
boton_mostrar = tk.Button(ventana, text="Mostrar Empleados", command=mostrar_empleados)
boton_mostrar.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
