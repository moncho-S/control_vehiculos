import json
import csv
from clases import *

print("################## Parte 1 ###############")

cantidadVehiculos = int(input("Cuantos vehiculos desea insertar: "))
vehiculos = [0]
for i in range(1, cantidadVehiculos+1):
    vehiculo = Automovil()
    print("Datos del vehiculo", i)
    vehiculo.marca = input("Inserte la marca del automovil ")
    vehiculo.modelo = input("Inserte el modelo del automovil ")
    vehiculo.numeroRuedas = int(input("Inserte el numero de ruedas "))
    vehiculo.velocidad = input("Inserte la velocidad en km/h ")
    vehiculo.cilindrada = input("Inserte el cilindraje en cc ")
    vehiculos.append(vehiculo)
    print("")

print("Imprimiendo por pantalla los vehiculos")
for i in range(1, len(vehiculos)):
    print(vehiculos[i].__str__())

print("################## Fin Parte 1 ###############\n")
