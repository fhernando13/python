import os

class parametrosElectricos:
    
    def __init__(self, lista = [], res1 = 0, zona1 = 0, sumatotal = 0, listaval = [], listaest = [] ):
        self.lista = lista
        self.res1 = res1
        self.zona1 = zona1
        self.sumatotal = sumatotal
        self.listaval = listaval
        self.listaest= listaest

    #funciones
    def paso1(self):
        for self.i in range(1,5):
            if self.i < 3:
                for self.j in range(1,3):
                    self.zona= int(input(f'ingrese zona {self.i}, resistencia {self.j}:\n'))
                    while self.zona <= 0 or self.zona >= 590:
                        print('valor incorrecto')
                        self.zona= int(input(f'ingrese zona {self.i}, resistencia {self.j}:\n'))
                    else:
                        self.lista.append(self.zona)
            else:
                self.zona= int(input(f'ingrese zona {self.i}:\n'))
                while self.zona <= 0 or self.zona >= 590:
                    print('valor incorrecto')
                    self.zona= int(input(f'ingrese zona {i}:\n'))
                else:
                    self.lista.append(self.zona)
        self.zonauno = 1/(1/self.lista[0]+1/self.lista[1])
        self.listaest.append(self.zonauno)
        self.zonados = 1/(1/self.lista[2]+1/self.lista[3])
        self.listaest.append(self.zonados)
        self.sumatotal = 1/(1/self.zonauno+1/self.zonados+1/self.lista[4]+1/self.lista[5])
        self.listaest.append(self.lista[4])
        self.listaest.append(self.lista[5])
        print(f'valor total de resistencias: {self.sumatotal}')
        self.lista.append(self.sumatotal)
        self.volt = float(input('Ingrese el voltaje: \n'))
        while self.volt <= 0:
            print('tiene que ser mayor a 0:\n')
            self.volt = float(input('Ingrese el voltaje: \n'))
        else:
            print(f'Ingreso: {self.volt} volts')
            self.lista.append(self.volt)
            self.czona1 = self.volt/self.zonauno
            self.czona2 = self.volt/self.zonados
            self.czona3 = self.volt/self.lista[4]
            self.cboquilla = self.volt/self.lista[5]
            print(f'zona 1 valor amperios: {self.czona1}')
            print(f'zona 2 valor amperios: {self.czona2}')
            print(f'zona 3 valor amperios: {self.czona3}')
            print(f'zona 4(boquilla) valor amperios: {self.cboquilla}')
            self.corrientezona = self.volt/self.sumatotal
            print(f'Corriente consumida de cada estacion: {self.corrientezona}')
            self.voltdif = (self.volt/100)*35
            self.volt2 = self.voltdif+self.volt
            print(f'diferencia: {self.volt2}')
            self.termo1 = self.volt2/self.zonauno
            self.termo2 = self.volt2/self.zonados
            self.termo3 = self.volt2/self.lista[4]
            self.termo4 = self.volt2/self.lista[5]
            print(f'termomagnetico 1: {self.termo1}')
            print(f'termomagnetico 2: {self.termo2}')
            print(f'termomagnetico 3: {self.termo3}')
            print(f'termomagnetico 4: {self.termo4}')
        print(self.listaest)
        
    def paso2(self):
        if self.sumatotal == 0:
            print('Ejecute la opcion 1')
            return main()
        else:
            print('valor de la potencia consumida por cada resistencia')
            self.potresistencia1 = self.lista[7]/self.lista[0]
            print(f' r1: {self.potresistencia1}')
            self.potresistencia2 = self.lista[7]/self.lista[1]
            print(f' r1: {self.potresistencia2}')
            self.potresistencia3 = self.lista[7]/self.lista[2]
            print(f' r1: {self.potresistencia3}')
            self.potresistencia4 = self.lista[7]/self.lista[3]
            print(f' r1: {self.potresistencia4}')
            self.potresistencia5 = self.lista[7]/self.lista[4]
            print(f' r1: {self.potresistencia5}')
            self.potresistencia6 = self.lista[7]/self.lista[5]
            print(f' r1: {self.potresistencia6}')
            print('valor de la potencia consumida por cada zona')
            self.potzona1 = self.lista[7]/self.listaest[0]
            print(f'potencia zona 1: {self.potzona1}')
            self.potzona2 = self.lista[7]/self.listaest[1]
            print(f'potencia zona 1: {self.potzona2}')
            self.potzona3 = self.lista[7]/self.listaest[2]
            print(f'potencia zona 1: {self.potzona3}')
            self.potzona4 = self.lista[7]/self.listaest[3]
            print(f'potencia zona 1: {self.potzona4}')
            print('valor de la potencia consumida por cada estacion')
            self.potestacion = self.lista[6]/self.lista[7]
            print(f'potencia de cada zona: {self.potestacion}')
            print('valor de la potencia consumida por todo el sistema')
            self.potsistema = self.potestacion *4
            print(f'Potencia del sistema: {round(self.potsistema,2)}')
            return main()        

def main():
    obj1 = parametrosElectricos()
    op=0
    while op != 3:
        os.system('cls')
        print("*** Parámetros eléctricos ***")
        print("1.- Cálculo de corriente y termomagnético. \n2.- Cálculo de potencia. \n3. Salir")
        print('')
        op=int(input('numero: '))

        if op == 1:
            obj1.paso1()
            obj1.paso2()
            return main()
            
        elif op == 2:
            print('Primero ejecute la opcion número 1')
            return main()

        elif op == 3:
            print("Hasta luego ....")
            return exit()
    else:
        print("La opcion elegida no esta disponible vuelve a interlo")

if __name__ == "__main__":
    operacion = main()