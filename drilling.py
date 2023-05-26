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
    # print("Datos del vehiculo", i, ": Marca", vehiculos[i].marca, ", Modelo", vehiculos[i].modelo, ",", str(
    #    vehiculos[i].numeroRuedas), "ruedas", vehiculos[i].velocidad, "km/h,", vehiculos[i].cilindrada, "cc")

print("################## Fin Parte 1 ###############\n")
print("################## Parte 2 ###############")

particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
print("Marca", particular.marca, ", Modelo", particular.modelo, ",", str(particular.numeroRuedas), "ruedas",
      particular.velocidad, "km/h,", particular.cilindrada, "cc", "Puestos:", particular.numeroPuestos)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
print("Marca", carga.marca, ", Modelo", carga.modelo, ",", str(carga.numeroRuedas),
      "ruedas", carga.velocidad, "km/h,", carga.cilindrada, "cc", "Carga:", carga.peso, "kg")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
print("Marca", bicicleta.marca, ", Modelo", bicicleta.modelo, ",",
      str(bicicleta.numeroRuedas), "ruedas Tipo: ", bicicleta.tipo)
motocicleta = Motocicleta(
    "BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
print("Marca", motocicleta.marca, ", Modelo", motocicleta.modelo, ",", str(motocicleta.numeroRuedas), "ruedas Tipo:",
      motocicleta.tipo, "Motor:", motocicleta.motor, ", Cuadro:", motocicleta.cuadro, ",Nro Radios", motocicleta.numeroRadios, "\n")

print("Motocicleta es instancia con relación a Vehículo: ",
      isinstance(motocicleta, Vehiculo))
print("Motocicleta es instancia con relación a Automovil: ",
      isinstance(motocicleta, Automovil))
print("Motocicleta es instancia con relación a Vehículo particular: ",
      isinstance(motocicleta, Particular))
print("Motocicleta es instancia con relación a Vehículo de carga: ",
      isinstance(motocicleta, Carga))
print("Motocicleta es instancia con relación a Bicicleta: ",
      isinstance(motocicleta, Bicicleta))
print("Motocicleta es instancia con relación a Motocicleta: ",
      isinstance(motocicleta, Motocicleta))

print("################## Fin Parte 2 ###############\n")
print("################## Parte 3 ###############")
listaVehiculos = [particular, carga, bicicleta, motocicleta]
print("se guardan los datos en csv")
guardar_datos_csv(listaVehiculos)
print("se leen los datos del csv")
automoviles = leer_datos_csv()

print("################## Fin Parte 3 ###############")
