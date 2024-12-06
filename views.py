import tkinter as tk
from tkinter import messagebox
from controllers import calcular_bono

def mostrar_bono():
    piezas = int(entry_piezas.get())
    bono = calcular_bono(piezas)
    messagebox.showinfo("Bono", f"El bono es: ${bono}")

# Configurar ventana principal
ventana = tk.Tk()
ventana.title("Nomina Empleados")

# Campo para ingresar piezas producidas
label_piezas = tk.Label(ventana, text="Piezas producidas:")
label_piezas.pack()

entry_piezas = tk.Entry(ventana)
entry_piezas.pack()

# Botón para mostrar el bono
btn_calcular = tk.Button(ventana, text="Calcular Bono", command=mostrar_bono)
btn_calcular.pack()

ventana.mainloop()
