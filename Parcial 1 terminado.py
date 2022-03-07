# -*- coding: utf-8 -*-
"""

@author: georg
"""

import numpy as np
import cProfile

def main(inventario,ventasxDia):

    print('=============================')
    print('Menú Gestión de inventario')
    print('=============================')
    print('1- Agregar producto al inventario')
    print('2- Eliminar producto')
    print('3- Actualizar inventario')
    print('4- Buscar producto en el inventario')
    print('5- Imprimir reporte de inventario')
    print('6- Ventas x dia')
    print('10- Salir')
    print("")

    opcion = int(input("Selecciona una opción: "))

    print("")
  
    if opcion == 1:
        agregarInventario(inventario,ventasxDia)
    elif opcion == 2:
        eliminarInventario(inventario,ventasxDia)
    elif opcion == 3:
        actualizarInventario(inventario,ventasxDia)
    elif opcion == 4:
        buscarInventario(inventario,ventasxDia)
    elif opcion == 5:
        imprimirInventario(inventario,ventasxDia)
    elif opcion ==6:
        registrarVentaxDia(inventario,ventasxDia)
    print("")

def agregarInventario(inventario,ventasxDia):
    nombre_producto = input("Nombre del producto: ")
    cantidad_producto = int(input("Cantidad del producto: "))
    inventario.append([nombre_producto,cantidad_producto])
    print(inventario)
    main(inventario,ventasxDia)
    
def eliminarInventario(inventario,ventasxDia):
  nombre_producto = input("Ingrese el nombre del producto a remover: ")
  borro = False
  for i in range(0,len(inventario)):
    if(borro==False):
      if(str(inventario[i][0])==str(nombre_producto)):
        inventario.pop(i)
        print("El producto "+ nombre_producto+ " se eliminó correctamente")
        borro=True
  if(borro==False):
    print("No se encontró el producto con nombre "+ nombre_producto)
  main(inventario,ventasxDia)

def actualizarInventario(inventario,ventasxDia):

    nombre_producto = input('Ingresa el nombre del producto a actualizar: ')
    cantidad_producto = int(input("Cuanto es la nueva cantidad: "))

    for i in range(0,len(inventario)):
      if(str(inventario[i][0])==str(nombre_producto)):
        inventario[i][1] = cantidad_producto
        print("Se actualizó con éxito el producto "+ nombre_producto)    
    main(inventario,ventasxDia)

def buscarInventario(inventario,ventasxDia):

    nombre_producto = input('Ingresa el nombre del producto a buscar: ')
    encontro = False
    for i in range(0,len(inventario)):
      if(str(inventario[i][0])==str(nombre_producto)):
        print("Nombre del producto: "+ inventario[i][0])
        print("Cantidad: "+ str(inventario[i][1]))
        encontro = True

    if(encontro == False):
      print("No existe un objeto con el nombre "+ nombre_producto)
      
    main(inventario,ventasxDia)
        
def imprimirInventario(inventario,ventasxDia):
    for i in range(0,len(inventario)):
      print("Nombre del producto: "+ inventario[i][0]+" - Cantidad: "+ str(inventario[i][1]))
    main(inventario,ventasxDia)

def registrarVentaxDia(inventario, ventasxDia):
  #inicializar el arreglo bidimensional (matriz)
  if(ventasxDia[0][0]==''):
    cantidadDias = int(input("Ingresa los dias del mes:"))
    cantidadDiasAux = cantidadDias
    for i in range (0,len(ventasxDia)):
      for j in range (0,len(ventasxDia[0])):
        if(cantidadDiasAux>0):
          dia =(cantidadDias+1)-cantidadDiasAux
          ventasxDia[i][j]= str(dia)+"- 0"
        cantidadDiasAux = cantidadDiasAux-1
  print(ventasxDia)
  diaAIngresar = int(input("Ingresa el dia que quieres registrar ventas:"))

  indice = 0
  for i in range (0,len(ventasxDia)):
      for j in range (0,len(ventasxDia[0])):
        if(diaAIngresar-1 == indice):
          ventasDia = int(input("Ingresa las ventas para este dia: "))
          ventasxDia[i][j] = str(diaAIngresar) + "- "+str(ventasDia)
        indice = indice+1

  print(ventasxDia)

  main(inventario,ventasxDia)


  
main([],np.empty((5,7),dtype='U25'))

cProfile.run('')