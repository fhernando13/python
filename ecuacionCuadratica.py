class ecuacion:

    #Constructor    
    def __init__(self, n1 = 0, n2 = 0, n3 = 0):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        
    def Num1(self, a):
        self.n1=a
    def Num2(self, b):
        self.n2=b
    def Num3(self, c):
        self.n3 = c
        
    def ecuacionCuadratica(self):
        x1=(-self.n2+(((pow(self.n2, 2))-(4*self.n1*self.n3))**0.5))/(2*self.n1)
        x2=(-self.n2-(((pow(self.n2, 2))-(4*self.n1*self.n3))**0.5))/(2*self.n1)
        print(f"el valor de x1 es: {x1}")
        print(f"el valor de x2 es: {x2}")
        
def main():
    obj1=ecuacion()
    a=float(input("Introduzca el valor de a: "))
    b=float(input("Introduzca el valor de b: "))
    c=float(input("Introduzca el valor de c: "))
    obj1.Num1(a)
    obj1.Num2(b)
    obj1.Num3(c)
    if a != 0:
        return obj1.ecuacionCuadratica() 
    else:   
        print("el valor de 'a' no puede valer '0' (cero)")       
    
if __name__ == "__main__":
    operacion = main()  