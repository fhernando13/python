import psycopg2
import random

conexion = psycopg2.connect( host='localhost', user='postgres', password='password', dbname='facturas', port=5432 )

for i in range(1,10000):       
    tipopago = ['efectivo','credito','debito']
    rangopago = random.randint(0,2)
    fechabril = ['01','02','04','05','06','07','08','09','11','12','13','14','15','16','18','19','20','21','22','23','25','26','27','28','29','30']
    fechamayo = ['02','03','04','06','07','09','10','11','12','13','14','16','17','18','19','20','21','23','24','25','26','27','28','30','31']
    abril=random.randint(0,25)
    mayo=random.randint(0,24)
    abril = "2022"+"-04-"+str(fechabril[abril])
    mayo = "2022"+"-05-"+str(fechamayo[mayo])
    fecha = [abril, mayo]
    mes = random.randint(0,1) 
    minuto = random.randint(0,59)
    segundo = random.randint(0,59)
    horadic = ['10','11','12','13','14','15','16','17','18','19','20']
    horarango = random.randint(1,10)
    hora = horadic[horarango]   
    try:
        with conexion:
            with conexion.cursor() as cursor:
                numCliente = random.randint(0,601)
                fechafac = fecha[mes]
                hora = str(hora)+":"+str(minuto)+":"+str(segundo)
                noVendedor = random.randint(0,201)
                monto = random.randint(1500,3000)
                iva = float((monto/100)*16)
                total = float(monto+iva)
                pago = tipopago[rangopago]
                valores = (numCliente, fechafac, hora, noVendedor, monto, iva, total, pago)
                sql = 'insert into abril_mayo (numCliente, fecha, hora, noVendedor, monto, iva, total, tipoPago) values (%s, %s, %s, %s, %s, %s, %s, %s)'                    
                cursor.execute(sql, valores)
                conexion.commit()
                print(f'registro insertado #: {i}')
    except conexion.Error as e:
        conexion.rollback()
        print(f'error: {e}')
