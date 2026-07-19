#Proyecto final Joel Paspuel, Isaac Alejandro
drones=[]
misiones=[]
zona=[]
rutas=[]

def registrar_dron():
    codigo = input("Código del dron: ")
    modelo = input("Modelo: ")
    velocidad = float(input("Velocidad (km/h): "))
    capacidad = float(input("Ingrese la capacidad del dron: "))
    bateria = float(input("Nivel de batería (%): "))
    estado = input("Ingrese el estado del dron Ejm: Disponible, En mision, En mantenimiento: ")
    dron = {"codigo": codigo, "modelo": modelo, "velocidad": velocidad,"Capacidad": capacidad ,"bateria": bateria, "Estado": estado}
    drones.append(dron)
    print("Dron registrado correctamente.")

def mostrar_drones():
    print("Drones registrados")
    for i in drones:
        print("Código:", i["codigo"], "| Modelo:", i["modelo"], "| Velocidad:", i["velocidad"],"| Capacidad", i["Capacidad"]  , "| Batería:", i["bateria"], "| Estado:", i["Estado"])

def eliminar_dron():
    codigo = input("Código del dron a eliminar: ")
    posicion = -1
    for i in range(len(drones)):
        if drones[i]["codigo"] == codigo:
            posicion = i
    if posicion != -1:
        drones.pop(posicion)
        print("Dron eliminado.")
    else:
        print("Dron no encontrado.")
def registrar_misiones():
    codigo = input("Ingrese el codigo de la mision: ")
    zona = input("Ingrese la zona de la mision: ")
    Tipo = input("Ingrese el tipo de emergencia: ")
    prioridad = int(input("Ingrese el nivel de prioridad ejm: 1.- Maxima prioridad 2.- Alta prioridad 3.- Prioridad Media 3.- Prioridad Baja solo numeros: "))
    personas = int(input("Ingrese el numero de personas afectadas: "))
    distancia = float(input("Ingrese la distacia a la zona: "))
    estado = input("Ingrese el estado de la mision ejmp pendiente, en curso, terminada: ")
    mision = {"Codigo": codigo,"Zona":zona,"Tipo": Tipo, "Prioridad": prioridad, "Personas afectadas":personas, "Distancia": distancia, "Estado": estado}
    misiones.append(mision)
    print("Mision registradad exitosamente")

def mostrar_misiones():
    print("Misiones registradas")
    for i in misiones:
        print("Código:", i["Codigo"], "| Zona:", i["Zona"], "| Tipo:", i["Tipo"], "| Prioridad:", i["Prioridad"], "| Personas afectadas:", i["Personas afectadas"], "| Distancia:", i["Distancia"], "| Estado:", i["Estado"])
def eliminar_mision():
    codigo = input("Código del dron a eliminar: ")
    posicion = -1
    for i in range(len(misiones)):
        if misiones[i]["codigo"] == codigo:
            posicion = i
    if posicion != -1:
        misiones.pop(posicion)
        print("Dron eliminado.")
    else:
        print("Dron no encontrado.")
def menuchi():
    while 1:
        print("1.- Para registrar dron")
        print("2.- Para mostrar drones")
        print("3.- Eliminar mision")
        print("4.- Para registrar misiones")
        print("5.- Mostrar misiones")
        print("6.- Eliminar mision")
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            registrar_dron()
        elif opcion ==2:
            mostrar_drones()
        elif opcion ==3:
            eliminar_dron()
        elif opcion ==4:
            registrar_misiones()
        elif opcion == 5:
            mostrar_misiones()
        elif opcion == 6:
            eliminar_mision()

if __name__ == '__main__':
    menuchi()

class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class cola:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    def guardar(self, dato):
        nuevo=nodo(dato)
        if not self.cola:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo 
    def sacar(self):
        if self.cabeza == None:
            print("No hay elementos en la lista de espera")
        else:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza == None:
                self.cola = None
            print(f"Se cambio el estado de {dato} a Atendida")
    def mostrar(self):
        if self.cabeza == None:
            print("No hay elementos en espera")
        else:
            lista_espera=[]
            actual = self.cabeza
            while actual is not None:
                lista_espera.append(str(actual.dato))
                actual = actual.siguiente
            print(f"Elementos en espera: {lista_espera}")