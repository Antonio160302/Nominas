import sqlite3

def agregar_empleado(id, nombre, categoria, departamento, sueldo_diario):
    conn = sqlite3.connect('empleados.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO empleados (id, nombre, categoria, departamento, sueldo_diario)
        VALUES (?, ?, ?, ?, ?)
    ''', (id, nombre, categoria, departamento, sueldo_diario))
    conn.commit()
    conn.close()

def mostrar_empleados():
    conn = sqlite3.connect('empleados.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM empleados')
    empleados = cursor.fetchall()
    for empleado in empleados:
        print(empleado)
    conn.close()

# Agregar un nuevo empleado
agregar_empleado(1, 'Juan Pérez', 'Operario', 'Producción', 150)

# Mostrar empleados
mostrar_empleados()
