#sistema de ventas
acumuladorprecio = 0
contadorproductos= 0
opcion =int(input("desea llevar el producto Agua\n Precio: $600\n 1.- si\n 2.-no\n"))
if opcion == 1:
    acumuladorprecio = acumuladorprecio + 600
    contadorproductos = contadorproductos + 1
opcion = int(input("desea llevar el producto azucar\n Precio: $1200\n 1.- si\n 2.-no\n"))

if opcion == 1:
    acumuladorprecio = acumuladorprecio + 1200
    contadorproductos = contadorproductos + 1
opcion = int(input("desea llevar el producto aceite\n Precio: $1500\n 1.- si\n 2.-no\n"))
if opcion == 1:
    acumuladorprecio = acumuladorprecio + 1500
    contadorproductos = contadorproductos + 1
opcion = int(input("desea llevar el producto arroz\n Precio: $1250\n 1.- si\n 2.-no\n"))
if opcion == 1:
    acumuladorprecio = acumuladorprecio + 1250
    contadorproductos = contadorproductos + 1
opcion = int(input("desea llevar el producto fideos\n Precio: $790\n 1.- si\n 2.-no\n"))
if opcion == 1:
    acumuladorprecio = acumuladorprecio + 790
    contadorproductos = contadorproductos + 1
opcion = int(input("desea llevar el producto bebida\n Precio: $1780\n 1.- si\n 2.-no\n"))
if opcion == 1:
    acumuladorprecio = acumuladorprecio + 1780
    contadorproductos = contadorproductos + 1
opcion = int(input("desea llevar el producto chocolate\n Precio: $2500\n 1.- si\n 2.-no\n"))
if opcion == 1:
    acumuladorprecio = acumuladorprecio + 2500
    contadorproductos = contadorproductos + 1
opcion = int(input("desea llevar el producto pan molde\n Precio: $1340\n 1.- si\n 2.-no\n"))
if opcion == 1:
    acumuladorprecio = acumuladorprecio + 1340
    contadorproductos = contadorproductos + 1

print(f"total de producto: {contadorproductos}\n")
print(f"total a pagar: ${acumuladorprecio}")

preferencial = 0.75

descuento = int(input("¿es cliente preferencial?\n 1.-si\n 2.-no\n"))
if descuento == 1:
    acumuladorprecio = acumuladorprecio - preferencial
else == 2:
    acumuladorprecio = acumuladorprecio
    
    

   


# ⮚	Agua 		= 	$ 600
# ⮚	Azúcar		= 	$1200
# ⮚	Aceite	=	$1500
# ⮚	Arroz		=	$1250
# ⮚	Fideos		=	$ 790
# ⮚	Bebida		→	$1780
# ⮚	Chocolate	→	$2500
# ⮚	Pan molde	→	$1340
