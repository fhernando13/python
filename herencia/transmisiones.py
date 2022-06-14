from time import sleep
from coche import *
import os

class Manual(Coche):
    
    def primera(self):
        if  self.frenado == False and self.atras == False:
            self.velocidad = 1
            texto = 'el cochecito esta en primera'
            print(texto)
        elif self.frenado == False:
            texto = 'el cochecito debe estar frenado'
            print(texto)
        elif self.atras == True:
            texto = 'el cochecito debe estar frenado'
            print(texto)
        
    def segunda(self):
        if self.velocidad == 1:
            self.velocidad = 2
            texto = 'el cochecito esta en segunda'
            print(texto)
        elif self.velocidad == 3:
            self.velocidad = 2
            texto = 'el cochecito esta en segunda'
            print(texto)
        elif self.atras == True:
            texto = 'el cochecito debe estar frenado'
            print(texto)
        else:
            print("no puedes meter esta velocidad")

    def tercera(self):
        if self.velocidad == 2:
            self.velocidad = 3
            texto = 'el cochecito esta en tercera'
            print(texto)
        elif self.velocidad == 4:
            self.velocidad = 3
            texto = 'el cochecito esta en tercera'
            print(texto)
        elif self.atras == True:
            texto = 'el cochecito debe estar frenado'
            print(texto)
        else:
            print("no puedes meter esta velocidad")
        
    def cuarta(self):
        if self.velocidad == 3:
            self.velocidad = 4
            texto = 'el cochecito esta en cuarta'
            print(texto)
        elif self.velocidad == 5:
            self.velocidad = 4
            texto = 'el cochecito esta en cuarta'
            print(texto)
        elif self.atras == True:
            texto = 'el cochecito debe estar frenado'
            print(texto)
        else:
            print("no puedes meter esta velocidad")
        
    def quinta(self):
        if self.velocidad == 4:
            self.velocidad = 5
            texto = 'el cochecito esta en quinta'
            print(texto)
        elif self.atras == True:
            texto = 'el cochecito debe estar frenado'
            print(texto)
        else:
            print("no puedes meter esta velocidad")
    
    def __init__(self,color,modelo,marca,motor,llantas,puertas, combustible, anio):
        super().__init__(color,modelo,marca,motor,llantas,puertas, combustible, anio)

class Automatico(Coche):

    def drive(self):
        if  self.frenado == False and self.atras == False:
            self.endrive = True
            texto = 'el cochecito esta en drive'
            print(texto)
        elif self.frenado == False:
            texto = 'el cochecito debe estar frenado'
            print(texto)
        elif self.atras == True:
            texto = 'el cochecito debe estar frenado'
            print(texto)

    def neutral(self):
        if self.endrive == False:
            self.neu == True
            texto = 'esta en neutral'
            print(texto)
        elif self.endrive == True:
            self.neu = False
            texto =  'para meter neutral el cochiecito\nnecesita estar frenado'
            print(texto)
    
    def __init__(self,color,modelo,marca,motor,llantas,puertas, combustible, anio):
        super().__init__(color,modelo,marca,motor,llantas,puertas, combustible, anio)
        
def main():
    op = 0
    os.system('clear')
    while op != 4:
        print('Elija una transmision')
        print('1.- Manual')
        print('2.- Automatico')
        print('3.- Salir')
        op = input("elija una opcion:\n")
        while not op.isdigit():
            print('solo numeros vuelva aintentarlo')
            op = input("elija una opcion:\n")
        else:
            op = int(op)
            if op == 1:
# -----------------aqui inica el standar-----------------------------------------------------------#
                while op != 4:
                    coche1 = Manual('Nissan','March',2022,'Rojo',1600,'r17',5,'Magna')
                    os.system('clear')
                    print("Cochecito Manual")
                    print("1.- Encender")
                    print('2.- mi cochecito')
                    print("3.- Salir")
                    op = input("elija una opcion:\n")
                    while not op.isdigit():
                        print('solo numeros vuelva aintentarlo')
                        op = input("elija una opcion:\n")
                    else:
                        op = int(op)
                        if op == 1:
                            coche1.encender()
                            op = 0
                            while op != 9:
                                print('1.- 1era')
                                print('2.- 2da')
                                print('3.- 3ra')
                                print('4.- 4ta')
                                print('5.- 5ta')
                                print('6.- reversa')
                                print('7.- frenar')
                                print('8.- luces')
                                print('9.- apagar')
                                op = input("elija una opcion:\n")
                                while not op.isdigit():
                                    print('solo numeros vuelva a intentarlo')
                                    op = input("elija una opcion:\n")
                                else:
                                    op = int(op)
                                    if op == 1:
                                        coche1.primera()
                                    elif op == 2:
                                        coche1.segunda()
                                    elif op == 3:
                                        coche1.tercera()
                                    elif op == 4:
                                        coche1.cuarta()
                                    elif op == 5:
                                        coche1.quinta()
                                    elif op == 6:
                                        coche1.reversa()
                                    elif op == 7:
                                        coche1.frenar()
                                    elif op == 8:
                                        coche1.prender_luces()
                                    elif op == 9:
                                        coche1.apagar()
                                        sleep(3)
                                    else:
                                        print('no disponible\n')
                        elif op == 2:
                            print(coche1)
                            sleep(6)
                        elif op == 3:
                            print('saliendo.')
                            sleep(2)
                            print('saliendo..')
                            sleep(2)
                            print('saliendo...')
                            sleep(2)
                            os.system('clear')
                            return main()
                else:
                    print("opcion no disponible")
# -----------------aqui termina el standar-----------------------------------------------------------#
# -----------------aqui inicia el automatico-----------------------------------------------------------#
            elif op == 2:
                while op != 4:
                    coche1 = Automatico('Nissan','March',2022,'Rojo',1600,'r17',5,'Magna')
                    os.system('clear')
                    print("Cochecito Automatico")
                    print("1.- Encender")
                    print('2.- mi cochecito')
                    print("3.- Salir")
                    op = input("elija una opcion:\n")
                    while not op.isdigit():
                        print('solo numeros vuelva aintentarlo')
                        op = input("elija una opcion:\n")
                    else:
                        op = int(op)
                        if op == 1:
                            coche1.encender()
                            op = 0
                            while op != 6:
                                print('1.- Drive')
                                print('2.- Neutral')
                                print('3.- Reversa')
                                print('4.- Frenar')
                                print('5.- Luces')
                                print('6.- apagar')
                                op = input("elija una opcion:\n")
                                while not op.isdigit():
                                    print('solo numeros vuelva a intentarlo')
                                    op = input("elija una opcion:\n")
                                else:
                                    op = int(op)
                                    if op == 1:
                                        coche1.drive()
                                    elif op == 2:
                                        coche1.neutral()
                                    elif op == 3:
                                        coche1.reversa()
                                    elif op == 4:
                                        coche1.frenar()
                                    elif op == 5:
                                        coche1.prender_luces()
                                    elif op == 6:
                                        coche1.apagar()
                                        sleep(3)
                                    else:
                                        print('no disponible\n')
                        elif op == 2:
                            print(coche1)
                            sleep(6)
                        elif op == 3:
                            print('saliendo.')
                            sleep(2)
                            print('saliendo..')
                            sleep(2)
                            print('saliendo...')
                            sleep(2)
                            os.system('clear')
                            return main()
                else:
                    print("opcion no disponible")
# -----------------aqui termina el automatico-----------------------------------------------------------#
            elif op == 3:
                print('Bye Bye')
                break
            else:
                print('opcion no diponible')
    else:
        print("opcion no disponible")    
    
if __name__ == '__main__':
    main()