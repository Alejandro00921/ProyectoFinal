# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:15:49 2022

@author: USUARIO
"""

#from clases.menu import Menu, MenuTecnicos
#from clases.equipo import *

from menus.Menu import Menu
from menus.MenuTecnicos import MenuTecnicos

from clases.Equipo import * 
from clases.Prestamo import * 



if __name__ == '__main__':
    menu = Menu("Escuela de ingenieria")
    op = menu.ver()
    if op == "1":
        menu2 = MenuTecnicos()
        op_menu_tecnico =""
        while op_menu_tecnico != "6":
            op_menu_tecnico = menu2.ver()
            if op_menu_tecnico == "1":
                print("\n Formulario Registro de Equipo")
                numero_equipo = input("Numero equipo: ")
                nombre = input("Nombre equipo:")
                proveedor = input("proveedor equipo: ")
                referencia = input("Referencia: ") 
                ciclo = input("Ciclo: ")
                cantidad = int(input("Cantidad :"))
                temp = input("Ingrese fecha(yyyy-mm-dd)")
                (anio, mes, dia)= temp.split("-")
                fum =date(int(anio), int(mes), int(dia))

                #construimo el eqobjeto equipo 
                equipo = Equipo(nombre, proveedor, cantidad, referencia, ciclo, fum)    

                if registrar_equipo(equipo):
                    print("Se registro exitosamente")
                else:
                    print("No se pudo registar")

                imprimir_equipos()
            elif op_menu_tecnico == "2":            
                nombre_equipo = input("Indique el equipo: ")
                equipo = consultar_equipos_por_nombre(nombre_equipo)
                equipo.imprimir_datos_equipo()
            elif op_menu_tecnico == "3":
                imprimir_equipos()
            elif op_menu_tecnico == "4":            

                nombre_equipo = input("Equipo a modificar: ")
            
                equipo = consultar_equipos_por_nombre(nombre_equipo)
                if equipo == None:
                    print("No se encieuntra equipo")
                else:
                    temp = input("Ingrese fecha(yyyy-mm-dd): ")
                    (anio, mes, dia)= temp.split("-")
                    equipo.fum =date(int(anio), int(mes), int(dia))
                    hoy = date.today()            
                    diferencia = hoy  - equipo.fum    
                    equipo.ciclo = diferencia.days
                    equipo.actualizar()
            elif op_menu_tecnico == "5":
                nombre_equipo = input("Equipo a consultar: ")
                equipo = consultar_equipos_por_nombre(nombre_equipo)
                equipo.imprimir_datos_equipo()
            elif op_menu_tecnico == "6":                                    
                print("funcion sin implementar")
            elif op_menu_tecnico =="8":
                nuevo_prestamo = crear_prestamo()
                
                equpo_encontrado = consultar_equipos_por_nombre(nuevo_prestamo.equipo)

                if equpo_encontrado == None:
                    print("El prestamo no se puede hacer por que el equipo no se encuntra en inventario")
                else:
                    equpo_encontrado.cantidad = equpo_encontrado.cantidad-1
                    equpo_encontrado.actualizar()
                    registrar_prestamo(nuevo_prestamo)
                    print("El prestamo se realizo correctament")
