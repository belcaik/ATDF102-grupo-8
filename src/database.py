import sqlite3
import random

DB_NAME = "property_core.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables(cursor):

    cursor.execute('''CREATE TABLE IF NOT EXISTS regions
                      (
                          id
                          INTEGER
                          PRIMARY
                          KEY,
                          name
                          TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS communes
                      (
                          id
                          INTEGER
                          PRIMARY
                          KEY,
                          name
                          TEXT,
                          region_id
                          INTEGER
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS client_types
                      (
                          id
                          INTEGER
                          PRIMARY
                          KEY,
                          name
                          TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS clients
                      (
                          id
                          INTEGER
                          PRIMARY
                          KEY,
                          rut
                          TEXT,
                          full_name
                          TEXT,
                          email
                          TEXT,
                          phone
                          TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS condos
                      (
                          id
                          INTEGER
                          PRIMARY
                          KEY,
                          name
                          TEXT,
                          street
                          TEXT,
                          number
                          TEXT,
                          commune_id
                          INTEGER
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS house_types
                      (
                          id
                          INTEGER
                          PRIMARY
                          KEY,
                          name
                          TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS houses
                      (
                          id
                          INTEGER
                          PRIMARY
                          KEY,
                          street
                          TEXT,
                          number
                          TEXT,
                          type_id
                          INTEGER,
                          condo_id
                          INTEGER,
                          client_id
                          INTEGER
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS payment_types
                      (
                          id
                          INTEGER
                          PRIMARY
                          KEY,
                          name
                          TEXT
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS payment_months
                      (
                          id
                          INTEGER
                          PRIMARY
                          KEY,
                          name
                          TEXT,
                          month_number
                          INTEGER
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS payment_years
                      (
                          id
                          INTEGER
                          PRIMARY
                          KEY,
                          year
                          INTEGER
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS payments
                      (
                          id
                          INTEGER
                          PRIMARY
                          KEY,
                          id_client
                          INTEGER,
                          id_house
                          INTEGER,
                          payment_year_id
                          INTEGER,
                          payment_month_id
                          INTEGER,
                          payment_type
                          INTEGER,
                          amount
                          INTEGER,
                          description
                          TEXT
                      )''')

def generate_rut():
    return f"{random.randint(5000000, 25000000)}-{random.randint(0, 9)}"


def populate_db(cursor):
    cursor.execute("SELECT count(*) FROM regions")
    if cursor.fetchone()[0] > 0:
        print("--> La base de datos ya existe. Saltando carga de datos.")
        return

    print("--> Generando datos de prueba...")

    regions_list = [
        (1, "Región de Arica y Parinacota"), (2, "Región de Tarapacá"), (3, "Región de Antofagasta"),
        (4, "Región de Atacama"), (5, "Región de Coquimbo"), (6, "Región de Valparaíso"),
        (7, "Región Metropolitana"), (8, "Región de O'Higgins"), (9, "Región del Maule"),
        (10, "Región de Ñuble"), (11, "Región del Biobío"), (12, "Región de La Araucanía"),
        (13, "Región de Los Ríos"), (14, "Región de Los Lagos"), (15, "Región de Aysén"), (16, "Región de Magallanes")
    ]
    cursor.executemany("INSERT INTO regions (id, name) VALUES (?, ?)", regions_list)

    communes_list = [
        (1, "Arica", 1), (3, "Iquique", 2), (5, "Antofagasta", 3), (9, "La Serena", 5),
        (11, "Valparaíso", 6), (13, "Santiago", 7), (14, "Las Condes", 7), (21, "Concepción", 11)
    ]
    cursor.executemany("INSERT INTO communes (id, name, region_id) VALUES (?, ?, ?)", communes_list)

    cursor.executemany("INSERT INTO client_types (id, name) VALUES (?, ?)", [(1, "Arrendatario"), (2, "Propietario")])

    first_names = ["Juan", "María", "Pedro", "Ana", "Luis", "Carolina", "José", "Daniela"]
    last_names = ["González", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto", "Contreras", "Silva"]

    for i in range(1, 21):
        nombre = f"{random.choice(first_names)} {random.choice(last_names)}"
        email = f"{nombre.lower().replace(' ', '.')}@example.com"
        phone = f"+569{random.randint(10000000, 99999999)}"
        cursor.execute("INSERT INTO clients (id, rut, full_name, email, phone) VALUES (?, ?, ?, ?, ?)",
                       (i, generate_rut(), nombre, email, phone))

    condo_names = ["Los Álamos", "El Roble", "Las Palmas", "Los Jardines"]
    for i in range(1, 6):
        name = f"Condominio {random.choice(condo_names)}"
        cursor.execute("INSERT INTO condos (id, name, street, number, commune_id) VALUES (?, ?, ?, ?, ?)",
                       (i, name, "Calle Falsa", str(random.randint(100, 999)), random.randint(1, 8)))

    cursor.executemany("INSERT INTO house_types VALUES (?, ?)", [(1, "Casa"), (2, "Departamento")])
    cursor.executemany("INSERT INTO payment_types VALUES (?, ?)",
                       [(1, "Efectivo"), (2, "Transferencia"), (3, "Crédito"), (4, "Débito")])

    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
             "Noviembre", "Diciembre"]
    cursor.executemany("INSERT INTO payment_months VALUES (?, ?, ?)", [(i + 1, m, i + 1) for i, m in enumerate(meses)])

    cursor.executemany("INSERT INTO payment_years VALUES (?, ?)", [(i, y) for i, y in enumerate(range(2020, 2026), 1)])

    for i in range(1, 21):
        # Crear Casa
        cursor.execute(
            "INSERT INTO houses (id, street, number, type_id, condo_id, client_id) VALUES (?, ?, ?, ?, ?, ?)",
            (i, "Av. Principal", str(random.randint(1, 100)), random.randint(1, 2), random.randint(1, 4), i))

        for _ in range(2):
            cursor.execute(
                '''INSERT INTO payments (id_client, id_house, payment_year_id, payment_month_id, payment_type, amount,
                                         description)
                              VALUES (?, ?, ?, ?, ?, ?, ?)''',
                           (i, i, random.randint(1, 6), random.randint(1, 12), random.randint(1, 4), random.randint(30000, 150000), "Gasto Común"))

def inicializar_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        create_tables(cursor)
        populate_db(cursor)

        conn.commit()
        conn.close()
        print("--> Base de datos inicializada correctamente.")
    except Exception as e:
        print(f"Error fatal inicializando la DB: {e}")

if __name__ == "__main__":
    inicializar_db()