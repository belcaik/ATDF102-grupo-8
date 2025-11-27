PRAGMA foreign_keys = ON;

-- Schema for the property management database
CREATE TABLE IF NOT EXISTS regions (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS communes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    region_id INTEGER NOT NULL,
    FOREIGN KEY (region_id) REFERENCES regions (id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS client_types (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY,
    rut TEXT NOT NULL,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    client_type_id INTEGER,
    FOREIGN KEY (client_type_id) REFERENCES client_types (id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS condos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    street TEXT NOT NULL,
    number TEXT NOT NULL,
    commune_id INTEGER NOT NULL,
    FOREIGN KEY (commune_id) REFERENCES communes (id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS house_types (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS houses (
    id INTEGER PRIMARY KEY,
    street TEXT NOT NULL,
    number TEXT NOT NULL,
    type_id INTEGER NOT NULL,
    condo_id INTEGER NOT NULL,
    client_id INTEGER NOT NULL,
    FOREIGN KEY (type_id) REFERENCES house_types (id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (condo_id) REFERENCES condos (id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (client_id) REFERENCES clients (id) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS payment_types (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS payment_months (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    month_number INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS payment_years (
    id INTEGER PRIMARY KEY,
    year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY,
    id_client INTEGER NOT NULL,
    id_house INTEGER NOT NULL,
    payment_year_id INTEGER NOT NULL,
    payment_month_id INTEGER NOT NULL,
    payment_type INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    description TEXT,
    FOREIGN KEY (id_client) REFERENCES clients (id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (id_house) REFERENCES houses (id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (payment_year_id) REFERENCES payment_years (id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (payment_month_id) REFERENCES payment_months (id) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (payment_type) REFERENCES payment_types (id) ON DELETE RESTRICT ON UPDATE CASCADE
);
