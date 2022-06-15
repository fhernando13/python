# pip install pymongo

from pymongo import MongoClient
import random

MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)
db = client['facturas']#base de datos
collection = db['AbrilMayo']#coleccion

for i in range(0,10000):
    tipopago = ['efectivo','credito','debito','vales de despensa']
    rangopago = random.randint(0,3)
    #fecha
    fechabril = ['01','02','04','05','06','07','08','09','11','12','13','14','15','16','18','19','20','21','22','23','25','26','27','28','29','30']
    fechamayo = ['02','03','04','06','07','09','10','11','12','13','14','16','17','18','19','20','21','23','24','25','26','27','28','30','31']
    abril=random.randint(0,25)
    mayo=random.randint(0,24)
    abril = "2022"+"-04-"+str(fechabril[abril])
    mayo = "2022"+"-05-"+str(fechamayo[mayo])
    fecha = [abril, mayo]
    mes = random.randint(0,1) 
    #hora
    minuto = random.randint(0,59)
    segundo = random.randint(0,59)
    horadic = ['10','11','12','13','14','15','16','17','18','19','20']
    horarango = random.randint(1,10)
    hora = horadic[horarango]   
#
    numCliente = random.randint(0,601)
    fechafac = fecha[mes]
    hora = str(hora)+":"+str(minuto)+":"+str(segundo)
    noVendedor = random.randint(0,201)
    monto = random.randint(1500,3000)
    iva = float((monto/100)*16)
    total = float(monto+iva)
    pago = tipopago[rangopago]

    collection.insert_one({"numFactura":i,"numCliente" :numCliente,"fecha":fechafac,"hora":hora,"noVendedor":noVendedor,"monto":monto,"iva":iva,"total":total,"tipoPago":pago})
    print(f'registro #:{i} insertado')
