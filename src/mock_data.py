from modules.region import Region
from modules.commune import Commune
from modules.client import Client
from modules.condo import Condo
from modules.house_type import HouseType
from modules.house import House
from modules.payments import Payments
from modules.client_type import ClientType
from modules.payment_type import PaymentType
from modules.payment_month import PaymentMonth
from modules.payment_year import PaymentYear
import random

def generate_rut():
    rut_num = random.randint(5000000, 25000000)
    verif_digit = random.randint(0, 9)
    return f"{rut_num}-{verif_digit}"

def load_mock_data():
    # Mock Regions
    regions = [
        Region(id=1, name="Región de Arica y Parinacota"),
        Region(id=2, name="Región de Tarapacá"),
        Region(id=3, name="Región de Antofagasta"),
        Region(id=4, name="Región de Atacama"),
        Region(id=5, name="Región de Coquimbo"),
        Region(id=6, name="Región de Valparaíso"),
        Region(id=7, name="Región Metropolitana de Santiago"),
        Region(id=8, name="Región del Libertador General Bernardo O'Higgins"),
        Region(id=9, name="Región del Maule"),
        Region(id=10, name="Región de Ñuble"),
        Region(id=11, name="Región del Biobío"),
        Region(id=12, name="Región de La Araucanía"),
        Region(id=13, name="Región de Los Ríos"),
        Region(id=14, name="Región de Los Lagos"),
        Region(id=15, name="Región de Aysén del General Carlos Ibáñez del Campo"),
        Region(id=16, name="Región de Magallanes y de la Antártica Chilena"),
    ]

    # Mock Communes
    communes = [
        Commune(id=1, name="Arica", region_id=1),
        Commune(id=2, name="Camarones", region_id=1),
        Commune(id=3, name="Iquique", region_id=2),
        Commune(id=4, name="Alto Hospicio", region_id=2),
        Commune(id=5, name="Antofagasta", region_id=3),
        Commune(id=6, name="Mejillones", region_id=3),
        Commune(id=7, name="Copiapó", region_id=4),
        Commune(id=8, name="Caldera", region_id=4),
        Commune(id=9, name="La Serena", region_id=5),
        Commune(id=10, name="Coquimbo", region_id=5),
        Commune(id=11, name="Valparaíso", region_id=6),
        Commune(id=12, name="Viña del Mar", region_id=6),
        Commune(id=13, name="Santiago", region_id=7),
        Commune(id=14, name="Las Condes", region_id=7),
        Commune(id=15, name="Rancagua", region_id=8),
        Commune(id=16, name="Machalí", region_id=8),
        Commune(id=17, name="Talca", region_id=9),
        Commune(id=18, name="Curicó", region_id=9),
        Commune(id=19, name="Chillán", region_id=10),
        Commune(id=20, name="Bulnes", region_id=10),
        Commune(id=21, name="Concepción", region_id=11),
        Commune(id=22, name="Talcahuano", region_id=11),
        Commune(id=23, name="Temuco", region_id=12),
        Commune(id=24, name="Padre Las Casas", region_id=12),
        Commune(id=25, name="Valdivia", region_id=13),
        Commune(id=26, name="La Unión", region_id=13),
        Commune(id=27, name="Puerto Montt", region_id=14),
        Commune(id=28, name="Osorno", region_id=14),
        Commune(id=29, name="Coyhaique", region_id=15),
        Commune(id=30, name="Aysén", region_id=15),
        Commune(id=31, name="Punta Arenas", region_id=16),
        Commune(id=32, name="Puerto Natales", region_id=16),
    ]

    # Mock Client Types
    client_types = [
        ClientType(id=1, name="Arrendatario"),
        ClientType(id=2, name="Propietario"),
    ]

    # Mock Clients
    first_names = ["Juan", "María", "Pedro", "Ana", "Luis", "Carolina", "José", "Daniela", "Fernando", "Valentina"]
    last_names = ["González", "Muñoz", "Rojas", "Díaz", "Pérez", "Soto", "Contreras", "Silva", "Martínez", "Sepúlveda"]
    clients = []
    for i in range(1, 21):
        full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        email = f"{full_name.lower().replace(' ', '.')}@example.com"
        phone = f"+569{random.randint(10000000, 99999999)}"
        clients.append(Client(id=i, rut=generate_rut(), full_name=full_name, email=email, phone=phone))

    # Mock Condos
    condo_names = ["Los Álamos", "El Roble", "Las Palmas", "Los Jardines", "El Bosque"]
    street_names = ["Avenida Siempre Viva", "Calle Falsa", "Pasaje Los Aromos", "Avenida del Mar", "Calle Principal"]
    condos = []
    for i in range(1, 6):
        condos.append(Condo(id=i, name=f"Condominio {random.choice(condo_names)}", street=random.choice(street_names), number=str(random.randint(100, 999)), commune_id=random.randint(1, 32)))

    # Mock House Types
    house_types = [
        HouseType(id=1, name="Casa"),
        HouseType(id=2, name="Departamento"),
    ]

    # Mock Houses
    houses = []
    for i in range(1, 21):
        houses.append(House(id=i, street=random.choice(street_names), number=f"{random.randint(1, 100)}{random.choice(['A', 'B', 'C', ''])}", type_id=random.randint(1, 2), condo_id=random.randint(1, 5), client_id=i))

    # Mock Payment Types
    payment_types = [
        PaymentType(id=1, name="Efectivo"),
        PaymentType(id=2, name="Transferencia"),
        PaymentType(id=3, name="Tarjeta de Crédito"),
        PaymentType(id=4, name="Tarjeta de Débito"),
    ]

    # Mock Payment Months
    payment_months = [PaymentMonth(id=i, name=m, month_number=i) for i, m in enumerate([
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ], 1)]

    # Mock Payment Years
    payment_years = [PaymentYear(id=i, year=y) for i, y in enumerate(range(2020, 2026), 1)]

    # Mock Payments
    payments = []
    for i in range(1, 51):
        client_id = random.randint(1, 20)
        house_id = client_id # Assuming one house per client for simplicity
        payments.append(Payments(id=i, id_client=client_id, id_house=house_id, payment_year_id=random.randint(1, 6), payment_month_id=random.randint(1, 12), payment_type=random.randint(1, 4), amount=random.randint(30000, 150000), description=f"Pago de gastos comunes"))

    return {
        "regions": regions,
        "communes": communes,
        "client_types": client_types,
        "clients": clients,
        "condos": condos,
        "house_types": house_types,
        "houses": houses,
        "payment_types": payment_types,
        "payment_months": payment_months,
        "payment_years": payment_years,
        "payments": payments,
    }