import os, time

os.system("cls")

useradmin= "dario"
contrasenaadmin= "123"

#crear menu
banderamenu = True

while banderamenu:
    try:
        os.system("cls")
        print("\t\t Sistema de gestion de huespedes")
        print("1.- Registrar huesped")
        print("2.- consultar datos")
        print("3.- Salir")
        opcion= int(input("seleccione una opcion:\n"))
        #crear cada opcion del menu
        if opcion == 1:
            #crear menu de registro y validar cada dato
            print("\t\t Registro de huespedes")
            #validar nombre
            nombre_huesped = input("ingrese su nombre:\n")
            while nombre_huesped == "":
                nombre_huesped= input("ingrese su nombre: (este campo no puede estar vacio)\n")
            
            #validar direccion
            direccion_huesped= input("ingrese su direccion:\n")
            while direccion_huesped == "":
                direccion_huesped= input("ingrese su direccion: (este campo no puede venir vacio)\n")
            
            try:
                #validar numero de reserva
                numeroreserva_huesped = int(input("ingrese su numero de reserva: (el numero debe estar entre 1000 y 9999)\n"))
                while (numeroreserva_huesped < 1000 or numeroreserva_huesped > 9999):
                    numeroreserva_huesped = int(input("ingrese su numero de reserva: (el numero debe estar entre 1000 y 9999)\n"))
            except:
                print("numero de reserva no valido")
            
            try:    
                #validar edad
                edad_huesped= int(input("ingrese su edad: (debe ser mayor de 18 años)\n"))
                while (edad_huesped < 18 or edad_huesped > 120):
                    edad_huesped= int(input("ingrese su edad: (debe ser mayor de 18 años)\n"))
            except:
                print("edad no valida")
                
            #validar correo electronico
            correo_huesped= input("ingrese su correo electronico (debe contener el @)\n")
            while '@' not in correo_huesped:
                correo_huesped= input("ingrese su correo electronico (debe contener el @)\n")
            
            try:
                #validar numero de acompañantes
                numero_acompanantes = int(input("ingrese el numero de acompañantes: \n")) 
                while numero_acompanantes < 0 :
                    numero_acompanantes = int(input("ingrese el numero de acompañantes: (el numero debe ser igual o mayor a 0) \n"))
            except:
                print("dato no valido")
                continue
                
        if opcion == 2:
            os.system("cls")
            #crear menu de vizualicacion admin y verificar
            print("\t\t Consultar datos del huesped")
            usuario = input("ingrese usuario admin:\n")
            contraseña = input("ingrese contraseña admin:\n")
            if (usuario != useradmin) and (contraseña != contrasenaadmin):
                print("no tiene permisos para visualizar esta informacion")
            
            else:
                #validar numero de reserva
                numeroreserva_admin= int(input("ingrese el numero de reserva:\n "))
                while numeroreserva_admin != numeroreserva_huesped:
                    print("el numero de reserva no existe, porfavor ingreselo nuevamente\n")
                    numeroreserva_admin= int(input("ingrese el numero de reserva:\n "))
                    
                #mostrar datos del huesped
                os.system("cls")
                print("\t\t Datos de huesped")
                print(f"Numero de reserva: {numeroreserva_huesped}")
                print(f"Nombre: {nombre_huesped}")
                print(f"Direccion: {direccion_huesped}")
                print(f"Correo electronico: {correo_huesped}")
                print(f"Edad: {edad_huesped}")
                print(f"Numero de acompañantes: {numero_acompanantes}")
                #validar numero de acompañantes si es mayor a 3
                if numero_acompanantes > 3:
                    print("huésped con demasiados acompañantes")
                else:
                    print("huésped dentro de límite de acompañantes")
                time.sleep(5)
                
        if opcion== 3:
            os.system("cls")
            print("Gracias por preferir Hotel 'Paradise Dreams'")
            break
    except:
        print("opcion no valida")
