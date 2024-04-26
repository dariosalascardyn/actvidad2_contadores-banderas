import time, os

os.system("cls")
deudacredito = 100000
saldotarjeta = 100000
banderamenu = True

while banderamenu:
    print("1.- pago de tarjeta de credito")
    print("2.- comprar productos")
    print("3.-salir")
    opcn = int(input("seleccion una opcion:\n"))
    if opcn == 1:
      try:
        while True:
            os.system("cls")
            pago = int(input("ingresa monto a pagar:\n"))
            if pago>=0 and pago <= saldotarjeta:
              print(f"pago realizado:\t {pago}")
              print(f"saldo actual tarjeta:\t {saldotarjeta - pago}")
              time.sleep(2)
            else : 
                print("el monto ingresado es menor o igual a 0 o excede el saldo actual")
                #return (pago)

      except:
            print("monto no validado ")
            
    if opcn == 2:
         os.system("cls")
        
        while True:
            carritocompras = 0
            print("1.- realizar compra")
            print("2.- salir")
            opcn2 = int(input"ingrese opcion")
            if opcn2 is 1:
                compras = int(input("ingrese monto de la compra: $\t"))
                if compras >= 0:
                    while compras:
                        compras = carritocompras + compras
                        print("total de compras: $ {carritocompras}")
            else:
                print("hasta luego")
        
        
        
        
    if opcn == 3:
        print("hasta luego")
        
        
    else:
        print("opcion invalida")    
