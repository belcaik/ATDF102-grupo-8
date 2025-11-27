-- Schema for the property management database
CREATE TABLE IF NOT EXISTS regions (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS communes (
    id INTEGER PRIMARY KEY,
    name TEXT,
    region_id INTEGER
);

CREATE TABLE IF NOT EXISTS client_types (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY,
    rut TEXT,
    full_name TEXT,
    email TEXT,
    phone TEXT
);

CREATE TABLE IF NOT EXISTS condos (
    id INTEGER PRIMARY KEY,
    name TEXT,
    street TEXT,
    number TEXT,
    commune_id INTEGER
);

CREATE TABLE IF NOT EXISTS house_types (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS houses (
    id INTEGER PRIMARY KEY,
    street TEXT,
    number TEXT,
    type_id INTEGER,
    condo_id INTEGER,
    client_id INTEGER
);

CREATE TABLE IF NOT EXISTS payment_types (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE IF NOT EXISTS payment_months (
    id INTEGER PRIMARY KEY,
    name TEXT,
    month_number INTEGER
);

CREATE TABLE IF NOT EXISTS payment_years (
    id INTEGER PRIMARY KEY,
    year INTEGER
);

CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY,
    id_client INTEGER,
    id_house INTEGER,
    payment_year_id INTEGER,
    payment_month_id INTEGER,
    payment_type INTEGER,
    amount INTEGER,
    description TEXT
);
