import time, os

os.system("cls")

banderamenu= True
banderarut= True
banderaedad = True
banderapaciente = True
genero = input("ingrese genero")
while genero != 'f' and genero != 'F' and genero != 'm' and genero != 'M':
    genero = input("ingrese genero")

while banderamenu:
    os.system("cls")
    print("1.- Registrar paciente")
    print("2.- Atencion paciente")
    print("3.- Consultar datos paciente")
    print("4.- Salir")
    try:
        opcion = int(input("Seleccione una opcion\n"))
        if opcion == 1:
            os.system("cls")
            print("\t\tRegistro de Paciente")
            while banderarut:
                try:
                    rut = int(input("Ingrese su rut\n"))
                    while rut < 5000000 or rut > 99999999:
                        rut = int(input("Ingrese su rut\n"))
                        banderarut = False
                except:
                    print("el rut solo deben suer numeros enteros dentro del rango de 5000000 y 99999999")
                
            nombre = input("ingrese nombre\n")
            while nombre == "" or nombre == " ":
                nombre = input("ingrese nombre (no debe venir el campo vacio)\n")
           
            direccion = input("ingrese direcion\n")   
           
            correo = input("ingrese su correo electronico\n")
            while '@' not in correo:
                correo = input("ingrese su correo electronico (debe contener el @)\n")
           
            while banderaedad:
                try:
                   edad = int(input("ingrese su edad"))
                   while edad < 0 or edad > 110:
                       edad = int(input("ingrese su edad (debe estar entre 0 y 110)"))
                       banderaedad = False
                except:
                    print("la edad deben ser numeros")
                    
                    
            genero = input("ingrese su genero (F o M)")
            while genero != "f" and genero != "m" and genero != "F" and genero != "M" :
                genero = input("ingrese su genero (F o M)")
                
            registro = ""
            
            previsionsalud= input("ingrese su prevision de salud\n")
            while previsionsalud != "fonasa" or previsionsalud != "isapre":
                previsionsalud= input("ingrese su prevision de salud (debe ser fonasa o isapre)\n")
            
        elif opcion == 2:
            os.system("cls")
            print("\t\tAtencion paciente")
            
            consultarut = int(input("ingrese su rut:\n"))
            if consultarut == rut:
              registro = input ("ingrese fecha dd/mm/aa y observaciones del paciente")
            else:
                print(f"no existe registro para el rut{consultarut}")
            
        elif opcion == 3:
            os.system("cls")
            while banderapaciente: 
                print("\t\tConsultar datos paciente")
                consultarut = int(input("ingrese su rut:\n"))
                if consultarut == rut:
                    print(f"Rut: {rut}")
                    print(f"Nombre: {nombre}")
                    print(f"Direccion: {direccion}")
                    print(f"Correo: {correo}")
                    print(F"Edad: {edad}")
                    print(f"Sexo: {genero}")
                
            
            else:
                print(f"no existe registro para el rut{consultarut}")
            
        else:
            print("Ha salido del sistema…")
            banderamenu = False
        
    except:
        print("Opcion ingresada no valida")
