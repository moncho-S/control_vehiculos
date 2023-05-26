import json
import csv
from clases import *


def guardar_datos_csv(objetos):
    try:
        archivo = open("vehiculos.csv", "w", newline='')
        archivo_csv = csv.writer(archivo)
        for objeto in objetos:
            datos = [(objeto.__class__, objeto.__dict__)]
            archivo_csv.writerows(datos)
        archivo.close()
    except:
        print("salta la excepcion en metodo guardar")


def leer_datos_csv():
    try:
        vehiculos = []
        archivo = open("vehiculos.csv", "r")
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
            vehiculos.append(vehiculo)
        archivo.close()
        for vehiculo in vehiculos:
            print("Lista de Vehiculos", vehiculo[0][15:-2])
            print(vehiculo[1], "\n")
    except:
        print("salta la excepcion en metodo leer")


particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta(
    "BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

print("################## Parte 3 ###############")

listaVehiculos = [particular, carga, bicicleta, motocicleta]
print("se guardan los datos en csv")
guardar_datos_csv(listaVehiculos)
print("se leen los datos del csv")
automoviles = leer_datos_csv()

print("################## Fin Parte 3 ###############")
