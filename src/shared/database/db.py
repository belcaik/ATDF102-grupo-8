import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "property_core.db"
SQL_DIR = Path(__file__).resolve().parent
MIGRATION_FILE = SQL_DIR / "migrate.sql"
SEED_FILE = SQL_DIR / "seed.sql"

FK_LABELS = {
    "regions": "Región",
    "communes": "Comuna",
    "client_types": "Tipo de cliente",
    "clients": "Cliente",
    "condos": "Condominio",
    "house_types": "Tipo de casa",
    "houses": "Propiedad",
    "payment_types": "Tipo de pago",
    "payment_months": "Mes de pago",
    "payment_years": "Año de pago",
}


def get_db_connection():
    """Returns an SQLite connection with foreign keys enabled and row access by column name."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _run_sql_script(cursor, script_path: Path):
    """Executes a SQL script stored in an external file."""
    if not script_path.exists():
        raise FileNotFoundError(f"SQL script not found: {script_path}")

    with script_path.open("r", encoding="utf-8") as sql_file:
        cursor.executescript(sql_file.read())


def _has_seed_data(cursor) -> bool:
    cursor.execute("SELECT count(*) FROM regions")
    return cursor.fetchone()[0] > 0


def ensure_fk_exists(cursor, table: str, fk_id: int):
    """
    Guards writes against orphan references by ensuring the FK target exists.

    Raises:
        ValueError: if the table is not allowed or the FK record is missing.
    """
    if table not in FK_LABELS:
        raise ValueError(f"Tabla de referencia no soportada: {table}")

    cursor.execute(f"SELECT 1 FROM {table} WHERE id = ?", (fk_id,))
    if cursor.fetchone() is None:
        friendly = FK_LABELS[table]
        raise ValueError(f"{friendly} con ID {fk_id} no existe.")


def inicializar_db():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        _run_sql_script(cursor, MIGRATION_FILE)

        if _has_seed_data(cursor):
            print("--> La base de datos ya existe. Saltando carga de datos.")
        else:
            _run_sql_script(cursor, SEED_FILE)

        conn.commit()
        print("--> Base de datos inicializada correctamente.")
    except Exception as e:
        print(f"Error fatal inicializando la DB: {e}")
    finally:
        if conn:
            conn.close()
