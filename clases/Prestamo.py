
class Prestamo:
    def __init__(self, nombre, carnet, equipo, fecha_prestamo, fecha_entrega):
        self.nombre = nombre
        self.carnet = carnet
        self.equipo = equipo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega

db_prestamos = "database/prestamo.csv"

col_nombre = 0
col_carnet = 1
col_equipo = 2
col_fecha_prestamo = 3
col_fecha_entrega = 4

def registrar_prestamo(nuevo:Prestamo):
    try:
        with open(db_prestamos, 'a') as archivo:
            archivo.write(
                f"{nuevo.nombre};{nuevo.carnet};{nuevo.equipo};{nuevo.fecha_prestamo};{nuevo.fecha_entrega}\n")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def consultar_prestamos_por_nombre_equipo(equipo_prestado:str)->list[Prestamo]:
    lista_prestamos = []

    with open(db_prestamos, 'r') as archivo:
        for linea in  archivo.readlines():
            datos = linea.split(";")
            print(datos)
            if datos[col_equipo] == equipo_prestado:
                prestamo = Prestamo(datos[col_nombre], datos[col_carnet], datos[col_equipo],datos[col_fecha_prestamo], datos[col_fecha_entrega])
                lista_prestamos.append(prestamo)



    return lista_prestamos


def eliminar_prestamo(prestamo_eliminar:Prestamo)->bool:
    try:
        with open(db_prestamos, 'a') as archivo:
            for linea in  archivo.readlines():
                datos = linea.split(";")
                if datos[col_nombre] == prestamo_eliminar.nombre and datos[col_carnet] == prestamo_eliminar.carnet and datos[col_equipo]==prestamo_eliminar.equipo:
                   print("Se elimina registro")
                else:
                    archivo.write(datos)

    except Exception as e:
        print(f"Error: {e}")
        return False
    return





