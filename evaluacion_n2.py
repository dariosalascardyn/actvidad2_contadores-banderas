import os, time

os.system("cls")
# crear menu
#opcion 1 formulario de registros
# validar campos
#opcion 2 crear resumen del alumno
# solo el admin puede acceder a datos del alumno
# crear condicion para evaluar el nem
# opcion 3 romper ciclo salir
usser = "admin"
password = "admin"
banderamenu = True
nem_alumno = 0
while banderamenu:
    os.system("cls")
    print("-----Sistema de Gestión de Alumnos-----")
    print("1.- registrar alumno")
    print("2.- consultar datos de alumno")
    print("3.- salir")
    try:
       opcion = int(input("seleccione una opcion\n"))
               
    if opcion == 1:
      os.system("cls")
      print("-----regsitro de alumnos-----")
      nombre_alumno = input("ingrese nombre:\n")
      while nombre_alumno == "":
          nombre_alumno = input("el nombre no puede venir vacio, ingrese nombre nuevamente:\n")
     
      
      direccion_alumno = input("ingrese su direccion:\n")
      while direccion_alumno == "":
          direccion_alumno = input("la direccion no puede venir vacio, ingrese direccion nuevamente:\n")
      
      rut_alumno = int(input("ingrese su rut: (sin dígito verificador ni puntos).)\n"))
      if rut_alumno < 5000000 or rut_alumno > 39999999:
          print("el rut es invalido, ingrese denuevo: (sin dígito verificador ni puntos)\n")
      
      edad_alumno = int(input("ingrese su edad: (debe ser mayor a 17 años)\n"))
      if edad_alumno <= 17 and rut_alumno >= 90:
          edad_alumno = int(input("la edad debe estar entre 17 y 90 años, ingrese denuevo porfavor:\n"))
      
      correo_alumno = input("ingrese su correo electronico, recuerde que debe tener @\n")
      while '@' not in correo_alumno:
          correo_alumno= input("su correo no contiene el @, porfavor ingrese nuevamente:\n")
        
      nem_alumno = float(input("ingrese su NEM\n"))
      while nem_alumno<= 100 or nem_alumno >= 1000:  
         nem_alumno = float(input("ingrese su NEM\n"))
    
      time.sleep(2)
        
        
    elif opcion == 2:      
        os.system("cls")         
        print("consultar datos")
        usuario = input("ingrese su usario\n")
        contraseña = input("ingrese contraseña\n")
        if usser == usser and contraseña == password:
            rut_consulta= int(input("ingrese rut del alumno que desea consultar:\n"))
            if rut_consulta == rut_alumno:
                print(f"Rut: {rut_alumno}\n Nombre: {nombre_alumno}\n Direccion: {direccion_alumno}\n Correo electronico: {correo_alumno}\n Edad: {edad_alumno}\n NEM: {nem_alumno}\n ")
                if nem_alumno <= 520.0:
                    print("alumno no cumple con requisitos NEM")
                else:
                    print("alumno cumple con los requisitos NEM")
            else:
                print("rut ingresado no existe en la plataforma")
        else:
            print("no tiene permisos para acceder")
        time.sleep(2)
    elif opcion == 3:
        os.system("cls")
        print("Ha salido del sistema…")
        time.sleep(2)
    else:
      print("opcion no valida")   
    except:
        print("opcion no valida")     
