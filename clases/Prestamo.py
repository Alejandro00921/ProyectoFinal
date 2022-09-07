
class Prestamo:
    def __init__(self, nombre, carnet, equipo, fecha_prestamo, fecha_entrega):
        self.nombre = nombre
        self.carnet = carnet
        self.equipo = equipo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega

db_prestamos = "database/prestamo.csv"

def registrar_prestamo(nuevo:Prestamo):
    try:
        with open(db_prestamos, 'a') as archivo:
            archivo.write(
                f"{nuevo.nombre};{nuevo.carnet};{nuevo.equipo};{nuevo.fecha_prestamo};{nuevo.fecha_entrega}\n")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def crear_prestamo():
    print("Registrar prestamo")
    nombre=input("Nombre:")
    carnet=input("Carnet:")
    equipo=input("Equipo:")
    fecha_prestamo=input("Fecha de prestamo (yyyy-mm-dd):")
    fecha_entrega=input("Fecha de entrega (yyyy-mm-dd):")
    p=Prestamo(nombre, carnet, equipo, fecha_prestamo, fecha_entrega)
    return p

