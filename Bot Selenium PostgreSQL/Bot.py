import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import randint
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import psycopg2

class Conexion:
    
    def __init__(self):
        self.conexion = False

    #Conexio a PostgreSQL            
    def conectarDB(self):
        self.conexion = False
        if (self.conexion == False):
            try:
                self.conexion = psycopg2.connect( host='localhost', user='postgres', password='password', dbname='ssd', port=5432 )
                self.cursor = self.conexion.cursor()
                print('Conexion exitosa a base de datos PostgreSQL')
            except Exception as e:
                print (f'Error de conexión a base de datos PostgreSQL: {e}')
             
class Bot(Conexion):
    
    def __init__(self):
        self.configurar_driver()
        super().conectarDB()

    def configurar_driver(self):
        #colocar geckodriver.exe en raiz del disco C
        self.s = Service("C:\geckodriver\geckodriver.exe")
        #Al nivel de este script
        #self.s = Service(".\geckodriver.exe")
        self.driver = webdriver.Firefox(service=self.s)
        
    def cargar_pagina(self):
        os.system('cls')
        print('Robotina iniciada')
        print('Ir a mx')
        self.driver.get(f'https://www.mercadolibre.com')
        sleep(randint(1,5))
        #ir a mx
        self.driver.find_element(By.XPATH, '//*[@id="MX"]').click()
        print('Aceptar cookies')
        sleep(randint(1,5))
        #aceptar cookies        
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/button[1]').click()
        print('Buscar producto')
        sleep(randint(1,5))
        #buscar ssd        
        self.driver.find_element(By.XPATH, '//*[@id="cb1-edit"]').send_keys('ssd'+Keys.ENTER)
        print('Cerrar advertecncia de cp')
        sleep(randint(1,5))
        #cerrar CP                
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/button').click()
        sleep(randint(1,5))

    def buscar_producto(self):
        print('Buscando productos')
        self.paginas = self.driver.find_element(By.CLASS_NAME, 'andes-pagination__page-count').text
        print(self.paginas)
        self.pagtotal = (int(self.paginas[3:5])-2) *2
        sleep(3)
        for self.pag in range(0,self.pagtotal,2):
            for self.i in range(1,60,1):
                try:
                    try:
                        with self.conexion:
                            with self.conexion.cursor() as cursor:
                                self.sql="insert into ssd_table (description, vendedor, precio, descuento, meses, pagos, envio) values (%s,%s,%s,%s,%s,%s,%s)"
                                try:
                                    self.description = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[2]/a[1]').text                                 
                                except:
                                    self.description = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[1]/a[1]').text                                 
                                try:
                                    self.vendedor = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[1]/a[2]/p').text
                                    self.vendedor = self.vendedor[12:]
                                except:
                                    try:
                                        self.vendedor = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[2]/a[2]/p').text
                                        self.vendedor = self.vendedor[12:]
                                    except:
                                        self.vendedor = 'Sin informacion del vendedor'
                                try:
                                    self.precio = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[3]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
                                    self.coma = ","
                                    for x in range(len(self.coma)):
                                        self.precio = self.precio.replace(self.coma[x],"")
                                    self.precio = int(self.precio)
                                except:
                                    self.precio = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
                                    self.coma = ","
                                    for x in range(len(self.coma)):
                                        self.precio = self.precio.replace(self.coma[x],"")
                                    self.precio = int(self.precio)
                                try:
                                    self.descuento = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[2]/span').text
                                except:
                                    self.descuento ='0% OFF'
                                try:
                                    self.meses = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[3]/div[1]/div[1]/span',).text
                                    self.meses = self.meses[0:5]
                                    self.meses =self.meses[3:5]
                                    self.meses = int(self.meses)
                                except:
                                    self.meses = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[2]/div[1]/div[1]/span',).text
                                    self.meses = self.meses[0:5]
                                    self.meses =self.meses[3:5]
                                    self.meses = int(self.meses)
                                try:
                                    self.pagos = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[3]/div[1]/div[1]/span/div[2]/div/span/span[2]/span[2]').text
                                    self.pagos = int(self.pagos)
                                except:
                                    self.pagos = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[2]/div[1]/div[1]/span/div[2]/div/span/span[2]/span[2]').text
                                    self.pagos = int(self.pagos)
                                try:
                                    self.envio = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[3]/div[1]/div[2]/div/p').text
                                except:
                                    try:
                                        self.envio = self.driver.find_element(By.XPATH, f'/html/body/main/div/div[1]/section/ol/li[{self.i}]/div/div/div[2]/div[2]/div[1]/div[2]/div/p').text
                                    except:
                                        self.envio = 'Sin informacion'
                                
                                self.valores = (self.description, self.vendedor, self.precio, self.descuento, self.meses, self.pagos, self.envio)
                                cursor.execute(self.sql, self.valores)
                                self.registros = cursor.rowcount
                                print(f'se ha insertado: {self.i}')
                    except Exception as e:
                        self.conexion.rollback()
                        #Saber si hay un error 
                        #print(f'Ocurrió un error: {e}')
                    # esperar 1 segundo entre cada transaccion
                    # sleep(1) 
                except:
                    print('Todos los productos de la pagina')
            print('siguiente pagina') 
            try:
                self.driver.find_element(By.XPATH, '/html/body/main/div/div[1]/section/div[5]/ul/li[4]').click()
            except:
                self.driver.find_element(By.XPATH, '/html/body/main/div/div[1]/section/div[5]/ul/li[3]').click()
                sleep(3)
        print('Fin de la busqueda')
            
    def cerrarbot(self):
        self.driver.close()
        
def main():
    mybot = Bot()
    mybot.cargar_pagina()
    mybot.buscar_producto()
    mybot.cerrarbot()
    
if __name__ == '__main__':
    main()