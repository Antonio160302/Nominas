import sqlite3

# Conectar a la base de datos (si no existe, la crea)
conn = sqlite3.connect('empleados.db')
cursor = conn.cursor()

# Crear tabla de empleados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        categoria TEXT,
        departamento TEXT,
        sueldo_diario REAL
    )
''')

# Crear tabla de productos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        producto TEXT,
        talla TEXT,
        precio_unitario REAL
    )
''')

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()
