-- Seed data for the property management database
INSERT OR IGNORE INTO regions (id, name) VALUES
  (1, 'Región de Arica y Parinacota'),
  (2, 'Región de Tarapacá'),
  (3, 'Región de Antofagasta'),
  (4, 'Región de Atacama'),
  (5, 'Región de Coquimbo'),
  (6, 'Región de Valparaíso'),
  (7, 'Región Metropolitana'),
  (8, 'Región de O\'Higgins'),
  (9, 'Región del Maule'),
  (10, 'Región de Ñuble'),
  (11, 'Región del Biobío'),
  (12, 'Región de La Araucanía'),
  (13, 'Región de Los Ríos'),
  (14, 'Región de Los Lagos'),
  (15, 'Región de Aysén'),
  (16, 'Región de Magallanes');

INSERT OR IGNORE INTO communes (id, name, region_id) VALUES
  (1, 'Arica', 1),
  (3, 'Iquique', 2),
  (5, 'Antofagasta', 3),
  (9, 'La Serena', 5),
  (11, 'Valparaíso', 6),
  (13, 'Santiago', 7),
  (14, 'Las Condes', 7),
  (21, 'Concepción', 11);

INSERT OR IGNORE INTO client_types (id, name) VALUES
  (1, 'Arrendatario'),
  (2, 'Propietario');

INSERT OR IGNORE INTO clients (id, rut, full_name, email, phone) VALUES
  (1, '12345678-9', 'Juan Gonzalez', 'juan.gonzalez@example.com', '+56911111111'),
  (2, '98765432-1', 'María Perez', 'maria.perez@example.com', '+56922222222'),
  (3, '15975368-2', 'Pedro Diaz', 'pedro.diaz@example.com', '+56933333333'),
  (4, '26483927-3', 'Ana Rojas', 'ana.rojas@example.com', '+56944444444'),
  (5, '37482910-4', 'Luis Soto', 'luis.soto@example.com', '+56955555555'),
  (6, '48592038-5', 'Carolina Silva', 'carolina.silva@example.com', '+56966666666'),
  (7, '59603172-6', 'José Contreras', 'jose.contreras@example.com', '+56977777777'),
  (8, '60714293-7', 'Daniela Muñoz', 'daniela.munoz@example.com', '+56988888888'),
  (9, '71825304-8', 'Felipe Vega', 'felipe.vega@example.com', '+56999999999'),
  (10, '82936415-9', 'Camila Torres', 'camila.torres@example.com', '+56910101010');

INSERT OR IGNORE INTO condos (id, name, street, number, commune_id) VALUES
  (1, 'Condominio Los Álamos', 'Calle Falsa', '101', 13),
  (2, 'Condominio El Roble', 'Calle Falsa', '202', 13),
  (3, 'Condominio Las Palmas', 'Calle Norte', '55', 11),
  (4, 'Condominio Los Jardines', 'Av. Central', '330', 14),
  (5, 'Condominio Río Claro', 'Av. Sur', '440', 21);

INSERT OR IGNORE INTO house_types (id, name) VALUES
  (1, 'Casa'),
  (2, 'Departamento');

INSERT OR IGNORE INTO payment_types (id, name) VALUES
  (1, 'Efectivo'),
  (2, 'Transferencia'),
  (3, 'Crédito'),
  (4, 'Débito');

INSERT OR IGNORE INTO payment_months (id, name, month_number) VALUES
  (1, 'Enero', 1),
  (2, 'Febrero', 2),
  (3, 'Marzo', 3),
  (4, 'Abril', 4),
  (5, 'Mayo', 5),
  (6, 'Junio', 6),
  (7, 'Julio', 7),
  (8, 'Agosto', 8),
  (9, 'Septiembre', 9),
  (10, 'Octubre', 10),
  (11, 'Noviembre', 11),
  (12, 'Diciembre', 12);

INSERT OR IGNORE INTO payment_years (id, year) VALUES
  (1, 2020),
  (2, 2021),
  (3, 2022),
  (4, 2023),
  (5, 2024),
  (6, 2025);

INSERT OR IGNORE INTO houses (id, street, number, type_id, condo_id, client_id) VALUES
  (1, 'Av. Principal', '1001', 1, 1, 1),
  (2, 'Av. Principal', '1002', 2, 1, 2),
  (3, 'Av. Costanera', '301', 2, 3, 3),
  (4, 'Av. Costanera', '302', 1, 3, 4),
  (5, 'Pasaje Los Cedros', '15', 1, 2, 5),
  (6, 'Pasaje Los Cedros', '16', 2, 2, 6),
  (7, 'Calle Lago', '45', 2, 4, 7),
  (8, 'Calle Lago', '46', 1, 4, 8),
  (9, 'Camino Real', '5', 1, 5, 9),
  (10, 'Camino Real', '6', 2, 5, 10);

INSERT OR IGNORE INTO payments (id, id_client, id_house, payment_year_id, payment_month_id, payment_type, amount, description) VALUES
  (1, 1, 1, 6, 1, 2, 95000, 'Gasto común'),
  (2, 1, 1, 6, 2, 3, 97000, 'Gasto común'),
  (3, 2, 2, 6, 3, 1, 88000, 'Gasto común'),
  (4, 2, 2, 6, 4, 2, 91000, 'Gasto común'),
  (5, 3, 3, 6, 5, 4, 76000, 'Gasto común'),
  (6, 3, 3, 6, 6, 2, 78000, 'Gasto común'),
  (7, 4, 4, 6, 7, 1, 82000, 'Gasto común'),
  (8, 4, 4, 6, 8, 3, 84500, 'Gasto común'),
  (9, 5, 5, 6, 9, 2, 90000, 'Gasto común'),
  (10, 5, 5, 6, 10, 4, 93000, 'Gasto común'),
  (11, 6, 6, 5, 2, 2, 70000, 'Gasto común'),
  (12, 6, 6, 5, 3, 1, 72000, 'Gasto común'),
  (13, 7, 7, 5, 4, 2, 81000, 'Gasto común'),
  (14, 7, 7, 5, 6, 1, 83000, 'Gasto común'),
  (15, 8, 8, 5, 7, 3, 77000, 'Gasto común'),
  (16, 8, 8, 5, 9, 4, 80500, 'Gasto común'),
  (17, 9, 9, 5, 10, 2, 69000, 'Gasto común'),
  (18, 9, 9, 5, 12, 1, 71000, 'Gasto común'),
  (19, 10, 10, 5, 5, 2, 88000, 'Gasto común'),
  (20, 10, 10, 5, 11, 3, 91500, 'Gasto común');
