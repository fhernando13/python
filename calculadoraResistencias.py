import os

class ColoresRes:
    
    def Num1(self, a):
        self.n1=a
    def Num2(self, b):
        self.n2=b
    def Num3(self, c):
        self.n3=c
    def Num5(self, d):
        self.n5=d
               
    def calcular(self):
        self.banda2=(str(self.n1) + str(self.n2))
        if self.n3 == 0:
            self.n4 = 1 * 1 
        elif self.n3 == 1:
            self.n4 = 1 * 10
        elif self.n3 == 2:
            self.n4 = 1 * 100
        elif self.n3 == 3:
            self.n4 = 1 * 1000
        elif self.n3 == 4:
            self.n4 = 1 * 10000
        elif self.n3 == 5:
            self.n4 = 1 * 100000
        elif self.n3 == 6:
            self.n4 = 1 * 1000000
        elif self.n3 == 7:
            self.n4 = 1 * 10000000
        elif self.n3 == 8:
            self.n4 = 1 * 100000000
        elif self.n3 == 9:
            self.n4 = 1 * 1000000000
        self.banda3=(float(self.banda2) * self.n4)
        if self.n5 == 1:
            self.n6 = (self.banda3 / 100) * 2
            print(f'la resistencia tiene un valor de: {self.banda3} Ohm\'s, valor minimo: {self.banda3-self.n6} Ohm\'s, valor maximo: {self.banda3+self.n6} Ohm\'s')
            main()
        elif self.n5 == 2:
            self.n6 = (self.banda3 / 100) * 5
            print(f'la resistencia tiene un valor de: {self.banda3} Ohm\'s, valor minimo: {self.banda3-self.n6} Ohm\'s, valor maximo: {self.banda3+self.n6} Ohm\'s')
            main()
        elif self.n5 == 3:
            self.n6 = (self.banda3 / 100) * 10
            print(f'la resistencia tiene un valor de: {self.banda3} Ohm\'s, valor minimo: {self.banda3-self.n6} Ohm\'s, valor maximo: {self.banda3+self.n6} Ohm\'s')
            main()

def main():
    op = 0
    #linux
    os.system('clear')
    #windows
    #os.system('cls')
    obj1 = ColoresRes()
    while op != 1:
        print("*** calculadora de resistencias ***")
        print("Desea calcular el valor de una resistencia:")
        res = input('presione s para continuar o n para salir')
        if (res.lower() == "no" or res.lower() == "n"):
            print("hasta pronto")
            break
        elif (res.lower() == "s" or res.lower() == "si"):
            print("Eliga el color de la primera banda: ")
            a=int(input(" 0) negro\n 1) cafe\n 2) rojo\n 3) naranja\n 4) amarillo\n 5) verde\n 6) azul\n 7) violeta\n 8) gris\n 9) blanco\n"))
            if ( a < 0):
                print("opcion no disponible, eliga una opcion entre 0-9")
                return main()
            elif ( a > 9):
                print("opcion no disponible, eliga una opcion entre 0-9")
                return main()
            else: 
                print("Eliga el color de la segunda banda: ")
                b=int(input(" 0) negro\n 1) cafe\n 2) rojo\n 3) naranja\n 4) amarillo\n 5) verde\n 6) azul\n 7) violeta\n 8) gris\n 9) blanco\n"))
                if ( b < 0):
                    print("opcion no disponnible")
                    return main()
                elif (b > 9 ):
                    print("opcion no disponible")
                    return main()
                else:
                    print("Eliga el color de la tercera banda: ")
                    c=int(input(" 0) negro\n 1) cafe\n 2) rojo\n 3) naranja\n 4) amarillo\n 5) verde\n 6) azul\n 7) violeta\n 8) gris\n 9) blanco\n"))
                    if ( c < 0):
                        print("opcion no disponnible")
                        return main()
                    elif (c > 9 ):
                        print("opcion no disponible")
                        return main()
                    else:
                        print("Eliga el color de la cuarta banda: ")
                        d=int(input(" 1) rojo\n 2) dorado\n 3) plata\n"))
                        if ( d < 0):
                            print("opcion no disponnible")
                            return main()
                        elif (d > 3 ):
                            print("opcion no disponible")
                            return main()
                        else:
                            obj1.Num1(a)
                            obj1.Num2(b)
                            obj1.Num3(c)
                            obj1.Num5(d)
                            return obj1.calcular()
        else:
            print("vueve a intentarlo")         
            return main()
        
if __name__ == "__main__" :
    main()
        

        


       
                
            
            


        