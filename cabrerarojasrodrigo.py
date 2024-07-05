import csv
csv_data = []

def mostrar_menu():
    while True:
        print("1. Procesar lista de estudiantes")
        print("2. Registrar estudiante")
        print("3. Modificar nota")
        print("4. Eliminar estudiante")
        print("5. Generar promedio de notas")
        print("6. Generar acta de cierre de curso")
        print("7. Salir")
        try:
            opcion = int(input("Ingrese su opción: "))
            if opcion < 1 or opcion > 7: print("Ingrese una opción válida! (1-7)")
            else: return opcion
        except:
            print("Ingrese una opción válida! (1-7)")

def cargar_csv():
    with open("ListaCurso5B.csv","r") as archivo_csv:
        dict = csv.DictReader(archivo_csv)
        for alumno in dict: 
            alumno["Nota 1"] = float(alumno["Nota 1"])
            alumno["Nota 2"] = float(alumno["Nota 2"])
            csv_data.append(alumno)

def validar_rut():
    while True:
        rut = input("Ingrese el RUT del estudiante (XX.XXX.XXX-X): ")
        if "." not in rut or "-" not in rut or rut[-1] == "-":
            print("Ingrese un rut válido! (Debe estar separado con puntos y un guión para el dígito verificador)")
        else: 
            return rut
        
def validar_nombre():
    while True:
        nombre = input("Ingrese el nombre y el apellido del estudiante: ")
        nombre_separado = nombre.split(" ")
        if len(nombre_separado) != 2 or (nombre_separado[0] == "" or nombre_separado[1] == ""):
            print("Ingrese un nombre y un apellido válidos! (El estudiante debe tener Nombre y Apellido)")
        else:
            return nombre

def registrar_estudiante():
    nuevo_estudiante = {}
    rut = validar_rut()
    nombre = validar_nombre()
    print(rut)
    print(nombre)
        

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            cargar_csv()
        elif opcion == 2:
            registrar_estudiante()
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            print("Adiós!")
            break




main()