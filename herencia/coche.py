class Coche():
    
    def __init__(self,color,modelo,marca,motor,llantas,puertas, combustible, anio):

        self.color = color
        self.modelo = modelo
        self.marca = marca
        self.anio = anio
        self.motor = motor
        self.llantas = llantas 
        self.puertas = puertas
        self.combustible = combustible
        self.arrancado = False
        self.frenado = False
        self.lights = False
        self.atras = False
        self.prendido = False

    def encender(self):
        if self.prendido == False:
            self.prendido == True
            texto = 'el cochecito esta encendido'
            print(texto)

    def prender_luces(self):
        op = 0
        while op != 2:
            print('Enceder luces')
            print("1. si")
            print("2. no")
            op = input('elija una opcion: ')
            while not op.isdigit():
                print('solo numeros 1 para si o 2 para no')
                op = input('elija una opcion: ')
            else:
                op = int(op)
                if op == 1:
                    self.lights == True
                    print('luces encencidas')
                    break
                elif op == 2:
                    self.lights == False
                    print('luces apagadas')
                    break
                else:
                    print('no disponible')
                    op = int(input('elija una opcion: '))
        else:
            print('no disponible')
            
    def apagar(self):
        if self.prendido == False:
            self.apagado = True
            texto = 'el cochecito esta apagado'
            print(texto)
        else:
            texto = 'el cochecito no esta prendido'
            print(texto)
    
    def reversa(self):
        if self.frenado == True:
            self.atras = True
            texto = 'el cochecito esta en reversa'
            print(texto)
        else:
            texto = 'el cochecito debe estar frenado para meter reversa'
            print(texto)
    
    def frenar(self):
        self.prendido == True
        self.frenado = True
        texto = 'el coche esta frenando'
        print(texto)

    def __str__(self):
        texto = "Caracteristicas del cochecito\n\nMarca: {}\nModelo: {}\nAño: {}\nColor: {}\nCC3 Motor: {}\nRodado: {}\nNumero de puertas: {}\nCombustible: {}"
        return texto.format(self.marca, self.modelo, self.anio, self.color,self.motor,self.llantas,self.puertas,self.combustible)

def main():
    auto = Coche('Nissan','March',2022,'Rojo',1600,'r17',5,'Magna')
    auto.encender()
    auto.prender_luces()
    auto.apagar()
    print(auto)


if __name__ == '__main__':
    main()
