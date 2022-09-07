# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:10:06 2022

@author: USUARIO
"""
from datetime import date
from tabulate import tabulate as t


class Equipo:
    nombre_archivo = "./database/Equipo"
    cabeceras = ["Nombre", "Referencia", "Cantidad",
                 "Proveedor", "Ciclo", "Fecha Ultimo Mantenimiento"]

    def __init__(self, nombre, proveedor, cantidad, referencia, ciclo, fum=date.today()):
        self.nombre = nombre
        self.proveedor = proveedor
        self.cantidad = cantidad
        self.referencia = referencia
        self.ciclo = ciclo
        self.fum = fum

    def actualizar(self):
        lequipos_archivo = Equipo.listar_equipos()
        with open(Equipo.nombre_archivo, 'w') as equipos:
            for r in range(len(lequipos_archivo)):
                fila = lequipos_archivo[r]
                equipo = fila.split(";")
                if self.nombre == equipo[col_nombre]:
                    equipo[col_nombre] = f"{self.nombre}"  
                    equipo[col_referencia] = f"{self.referencia}"  
                    equipo[col_cantidad] = f"{self.cantidad}"  
                    equipo[col_proveedor] = f"{self.proveedor}"  
                    equipo[col_referencia] = f"{self.referencia}"  
                    equipo[col_ciclo] = f"{self.ciclo}"                                          
                    equipo[col_fum] = f"{self.fum}"                    
                    lequipos_archivo[r] = ";".join(equipo)
            for equipo in lequipos_archivo:
                equipo = equipo.replace("\n","")
                equipos.write(f"{equipo}\n")
            #equipos.write("\n")

    def imprimir_datos_equipo(self):
        equipo = [self.nombre, self.referencia, self.cantidad,
                  self.proveedor, self.ciclo, self.fum]
        print(t([equipo], Equipo.cabeceras, tablefmt="grid"))

######################################################################
# Columna de los campos en el archivo
global col_nombre, referencia, cantidad, proveedor, ciclo, fum
col_nombre, col_referencia, col_cantidad, col_proveedor, col_ciclo, col_fum = 0, 1, 2, 3, 4, 5

def listar_equipos():
    with open(Equipo.nombre_archivo, 'r') as equipos:
        lequipos = equipos.readlines()
    return lequipos

def consultar_equipos_por_nombre(nombre_equipo)->Equipo:
    obj_equipo = None
    with open(Equipo.nombre_archivo, 'r') as equipos:
        for equipo in equipos.readlines():
            eq = equipo.split(';')
            if nombre_equipo == eq[col_nombre]:
                obj_equipo = Equipo(eq[col_nombre], eq[col_referencia],
                                    eq[col_cantidad], eq[col_proveedor], eq[col_ciclo], eq[col_fum])
                break
    return obj_equipo   

def imprimir_equipos():
    lequipos = listar_equipos()
    equipos = []
    for equipo in lequipos:
        equipos.append(equipo.split(";"))
    print(t(equipos, Equipo.cabeceras, tablefmt="grid"))

def registrar_equipo(nuevo:Equipo):
    try:
        with open(Equipo.nombre_archivo, 'a') as archivo:
            archivo.write(
                f"{nuevo.nombre};{nuevo.referencia};{nuevo.cantidad};{nuevo.proveedor};{nuevo.ciclo};{nuevo.fum}\n")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False