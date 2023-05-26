class Vehiculo():
    marca = ''
    modelo = ''
    numeroRuedas = 0

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {str(self.numeroRuedas)},ruedas"


class Automovil(Vehiculo):
    velocidad = ""
    cilindrada = ""

    def __str__(self):
        return super().__str__()+f",{self.velocidad} km/h, {self.cilindrada} cc."


class Particular(Automovil):
    def __init__(self, marca, modelo, numeroRuedas, velocidad, cilindrada, numeroPuestos):
        self.marca = marca
        self.modelo = modelo
        self.numeroRuedas = numeroRuedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.numeroPuestos = numeroPuestos

    def __str__(self):
        return super().__str__()+f", Puestos {self.numeroPuestos}"


class Carga(Automovil):
    def __init__(self, marca, modelo, numeroRuedas, velocidad, cilindrada, peso):
        self.marca = marca
        self.modelo = modelo
        self.numeroRuedas = numeroRuedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.peso = peso

    def __str__(self):
        return super().__str__()+f",{self.peso},kg."


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numeroRuedas, tipo):
        self.marca = marca
        self.modelo = modelo
        self.numeroRuedas = numeroRuedas
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+f",Tipo {self.tipo}"


class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numeroRuedas, tipo, motor, cuadro, numeroRadios):
        super().__init__(marca, modelo, numeroRuedas, tipo)
        self.numeroRadios = numeroRadios
        self.cuadro = cuadro
        self.motor = motor

        def __str__(self):
            return super().__str__() + f",aro {self.numeroRadios}, Cuadro: {self.cuadro}, Motor: {self.motor}"
