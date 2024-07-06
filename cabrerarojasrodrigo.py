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
    #TODO: falta agregar validacion por cantidad de numeros dentro de un grupo spliteado por punto (min 1 max 3)
    while True:
        rut = input("Ingrese el RUT del estudiante (XX.XXX.XXX-X): ")
        if "." not in rut or "-" not in rut or rut[-1] == "-":
            print("Ingrese un rut válido! (Debe estar separado con puntos y un guión para el dígito verificador)")
        else: 
            return rut
        
def validar_nombre():
    while True:
        nombre = input("Ingrese el nombre y el apellido del estudiante: ")
        nombre_separado = nombre.strip().split(" ")
        if len(nombre_separado) != 2 or (nombre_separado[0] == "" or nombre_separado[1] == ""):
            print("Ingrese un nombre y un apellido válidos! (El estudiante debe tener Nombre y Apellido)")
        else:
            return " ".join(nombre_separado)

def validar_nota(n_nota = None):
    while True:
        try:
            if n_nota: nota = float(input(f"Ingrese la Nota N°{n_nota} (separado por un punto): "))
            else: nota = float(input(f"Ingrese la nueva nota (separado por un punto): "))
            if nota < 1.0 or nota > 7.0: print("Ingrese una nota válida! (1.0 - 7.0)")
            else: return nota
        except:
            print("Ingrese una nota válida! (Separado por un punto)")

def registrar_estudiante():
    nuevo_estudiante = {}
    rut = validar_rut()
    nombre = validar_nombre()
    nota_1 = validar_nota(1)
    nota_2 = validar_nota(2)
    nuevo_estudiante["Rut"] = rut
    nuevo_estudiante["Nombre"] = nombre
    nuevo_estudiante["Nota 1"] = nota_1
    nuevo_estudiante["Nota 2"] = nota_2
    csv_data.append(nuevo_estudiante)
    print("Estudiante ingresado exitosamente.")

def buscar_estudiante_rut(rut):
    for estudiante in csv_data:
        if estudiante["Rut"] == rut:
            return estudiante
    return False

def modificar_nota():
    while True:
        rut = validar_rut()
        estudiante = buscar_estudiante_rut(rut)
        if not estudiante: print("Estudiante no encontrado. Inténtelo nuevamente.")
        else: break

    while True:
        try:
            opcion = int(input("Ingrese el N° de la Nota a modificar (1-2): "))
            if opcion > 2 or opcion < 1: print("Ingrese un número de nota válido! (1-2)")
            else: break
        except:
            print("Ingrese un número de nota válido! (1-2)")

    if opcion == 1:
        nueva_nota = validar_nota()
        estudiante["Nota 1"] = nueva_nota
    elif opcion == 2:
        nueva_nota = validar_nota()
        estudiante["Nota 2"] = nueva_nota

    print("Nota del estudiante modificada satisfactoriamente.")


def eliminar_estudiante():
    while True:
        rut = validar_rut()
        estudiante = buscar_estudiante_rut(rut)
        if not estudiante: print("Estudiante no encontrado. Inténtelo nuevamente.")
        else: break
    
    print(f"¿Está seguro de eliminar a {estudiante["Nombre"]}?")
    while True:
        opcion = input("Ingrese su opción (Si / No): ").lower().strip()
        print(opcion)
        if opcion != "si" and opcion != "no": print("Ingrese una opción válida! (Si / No)")
        else: break
    if opcion == "no": 
        return
    elif opcion == "si":
        csv_data.remove(estudiante)
        print("Estudiante eliminado satisfactoriamente.")

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == 1:
            cargar_csv()
        elif opcion == 2:
            registrar_estudiante()
        elif opcion == 3:
            modificar_nota()
        elif opcion == 4:
            eliminar_estudiante()
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            print("Adiós!")
            break




main()