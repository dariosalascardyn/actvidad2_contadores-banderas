import os
import time
os.system("cls")

# creacion de usuarios
usuario1 = None
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None

# menu
banderamenuprinc = True

while banderamenuprinc:
    os.system("cls")
    print("1.- iniciar sesion")
    print("2.- registrar usuario")
    print("3.- salir")
    try:
        opcion = int(input("ingrese opcion\n"))
        if opcion == 1:
            if (usuario1 is None and contrasena1 is None) and (usuario2 is None and contrasena2 is None) and (usuario3 is None and contrasena3 is None):
                os.system("cls")
                print("No existen usuarios para acceder.")
                time.sleep(2)
                continue
            else:

                usuario = input("ingrese su usuario:\t")
                contrasena = input("ingrese clave:\t")
                if (usuario == newuser1 and contrasena == newpass1) or (usuario == newuser2 and contrasena == newpass2) or (usuario == newuser3 and contrasena == newpass3):

                    banderainiciosesion = True
                    while banderainiciosesion:
                        os.system("cls")
                        print("1.- Realizar llamada ")
                        print("2.- Enviar correo electronico")
                        print("3.- Cerrar sesion")
                        try:
                            opcion2 = int(input("seleccione una opcion\n"))
                            if opcion2 is 1:
                                os.system("cls")
                                # solo repite 2 vecex el la validacion del telefono
                                try:
                                    llamada = int(input(
                                        "Ingrese numero de telefono (debe comenzar con 9 y tener 9 dígitos)\t\t"))
                                    while llamada:
                                        if len(llamada) == 9 and llamada.startswith("9"):
                                            print("Llamando al número", llamada)
                                            time.sleep(3)
                                            llamada = False
                                        else:
                                            llamada = int(input(
                                                "Ingrese numero de telefono (debe comenzar con 9 y tener 9 dígitos)\t\t"))

                                except:
                                    print("numero ingresado no valido")

                            elif opcion2 is 2:
                                os.system("cls")
                                print("\t\tCorreo electronico")
                                destinatario = input(
                                    "Ingrese correo destinatario: (debe contener el @)\t\t")
                                while '@' not in destinatario:
                                    destinatario = input(
                                        "Ingrese correo destinatario: (debe contener el @) \t\t")
                                mensaje = input("ingrese mensaje:\n")
                                os.system("cls")
                                print(f"Destinatario: {
                                      destinatario}\nMensaje: {mensaje}\n")
                                time.sleep(4)
                            else:
                                os.system("cls")
                                print("cerrando sesion")
                                banderainiciosesion = False

                                time.sleep(1)
                        except:
                            os.system("cls")
                            print("opcion no valida")
                            time.sleep(1)
                else:
                    print("usuario o clave incorrecta, intentelo denuevo porfavor")
                    time.sleep(1)

        elif opcion == 2:
            os.system("cls")
            print("\t\tregistro de usuario")
            newuser1 = input("ingrese nombre de usuario:\t")
            newpass1 = input("ingrese contraseña:\t\t")
            otrouser = int(
                input("felicidades usuario registrado, desea crear otro\n 1.- si\n 2.- no\n"))
            usuario1 = newuser1
            contrasena1 = newpass1
            if otrouser is 1:
                os.system("cls")
                newuser2 = input("ingrese nombre de usuario:\t")
                newpass2 = input("ingrese contraseña:\t\t")
                otrouser = int(
                    input("felicidades usuario registrado, desea crear otro\n 1.- si\n 2.- no\n"))
                usuario2 = newuser2
                contrasena2 = newpass2
                if otrouser is 1:
                    os.system("cls")
                    newuser3 = input("ingrese nombre de usuario:\t")
                    newpass3 = input("ingrese contraseña:\t\t")
                    print("felicidades usuario registrado")
                    usuario3 = newuser3
                    contrasena3 = newpass3
                else:
                    time.sleep(0)
            else:
                time.sleep(0)
        elif opcion == 3:
            os.system("cls")
            print("Hasta luego")
            time.sleep(2)
            banderamenuprinc = False
    except:
        os.system("cls")
        # print("opcion no valida")
        time.sleep(1)
