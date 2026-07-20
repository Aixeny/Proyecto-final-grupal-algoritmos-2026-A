class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class cola:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def guardar(self, dato):
        nuevo = nodo(dato)
        if not self.cola:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo

    def sacar(self):
        if self.cabeza is None:
            print("No hay elementos en la lista de espera")
            return None
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.cola = None
        print(f"Se cambio el estado de {dato} a Atendida")
        return dato

    def mostrar(self):
        if self.cabeza is None:
            print("No hay elementos en espera")
        else:
            lista_espera = []
            actual = self.cabeza
            while actual is not None:
                lista_espera.append(str(actual.dato))
                actual = actual.siguiente
            print(f"Elementos en espera: {lista_espera}")

class nodoBST:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class BST:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = nodoBST(dato)
        else:
            self._insertar_aux(self.raiz, dato)

    def _insertar_aux(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = nodoBST(dato)
            else:
                self._insertar_aux(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = nodoBST(dato)
            else:
                self._insertar_aux(nodo.derecha, dato)

    def buscar(self, dato):
        return self._buscar_aux(self.raiz, dato)

    def _buscar_aux(self, nodo, dato):
        if nodo is None:
            return False
        if nodo.dato == dato:
            return True
        if dato < nodo.dato:
            return self._buscar_aux(nodo.izquierda, dato)
        else:
            return self._buscar_aux(nodo.derecha, dato)

    def inorden(self):
        self._inorden_aux(self.raiz)
        print()

    def _inorden_aux(self, nodo):
        if nodo:
            self._inorden_aux(nodo.izquierda)
            print(nodo.dato, end=" ")
            self._inorden_aux(nodo.derecha)

    def eliminar(self, dato):
        self.raiz = self._eliminar_aux(self.raiz, dato)

    def _eliminar_aux(self, nodo, dato):
        if nodo is None:
            return None
        if dato < nodo.dato:
            nodo.izquierda = self._eliminar_aux(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self._eliminar_aux(nodo.derecha, dato)
        else:
            if nodo.izquierda is None and nodo.derecha is None:
                return None
            if nodo.izquierda is None:
                return nodo.derecha
            if nodo.derecha is None:
                return nodo.izquierda
            sucesor = self._encontrar_minimo(nodo.derecha)
            nodo.dato = sucesor.dato
            nodo.derecha = self._eliminar_aux(nodo.derecha, sucesor.dato)
        return nodo

    def _encontrar_minimo(self, nodo):
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo
    
drones = []
misiones = []
zona = []
grafo_zonas = {}
rutas = []
cola_misiones = cola()
bst_misiones = BST()

def mostrar_codigos(lista, clave_codigo):
    codigos = []
    for elemento in lista:
        codigos.append(elemento[clave_codigo])
    print(codigos)

def buscar_mision_por_codigo(codigo):
    for m in misiones:
        if m["Codigo"] == codigo:
            return m
    return None

def buscar_dron_disponible():
    for d in drones:
        if d.get("Estado", "").lower() == "disponible":
            return d
    return None

def registrar_dron():
    codigo = input("Código del dron: ")
    modelo = input("Modelo: ")
    velocidad = float(input("Velocidad (km/h): "))
    capacidad = float(input("Ingrese la capacidad del dron: "))
    bateria = float(input("Nivel de batería (%): "))
    estado = input("Ingrese el estado del dron Ejm: Disponible, En mision, En mantenimiento: ")
    dron = {
        "codigo": codigo,
        "modelo": modelo,
        "velocidad": velocidad,
        "Capacidad": capacidad,
        "bateria": bateria,
        "Estado": estado
    }
    drones.append(dron)
    print("Dron registrado correctamente.")

def mostrar_drones():
    print("Drones registrados")
    for i in drones:
        print("Código:", i["codigo"], "| Modelo:", i["modelo"], "| Velocidad:", i["velocidad"],
              "| Capacidad", i["Capacidad"], "| Batería:", i["bateria"], "| Estado:", i["Estado"])
        
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

def registrar_mision():
    codigo = input("Ingrese el codigo de la mision: ")
    nombre_zona = input("Ingrese la zona de la mision: ")
    Tipo = input("Ingrese el tipo de emergencia: ")
    prioridad = int(input("Ingrese el nivel de prioridad ejm: 1.- Maxima prioridad 2.- Alta prioridad solo numeros: "))
    personas = int(input("Ingrese el numero de personas afectadas: "))
    distancia = float(input("Ingrese la distacia a la zona: "))
    estado = input("Ingrese el estado de la mision ejmp pendiente, en curso, terminada: ")
    mision = {
        "Codigo": codigo,
        "Zona": nombre_zona,
        "Tipo": Tipo,
        "Prioridad": prioridad,
        "Personas afectadas": personas,
        "Distancia": distancia,
        "Estado": estado
    }
    misiones.append(mision)
    print("Mision registradad exitosamente")

def mostrar_misiones():
    print("Misiones registradas")
    for i in misiones:
        print("Código:", i["Codigo"], "| Zona:", i["Zona"], "| Tipo:", i["Tipo"],
              "| Prioridad:", i["Prioridad"], "| Personas afectadas:", i["Personas afectadas"],
              "| Distancia:", i["Distancia"], "| Estado:", i["Estado"])
        
def eliminar_mision():
    codigo = input("Código de la misión a eliminar: ")
    posicion = -1
    for i in range(len(misiones)):
        if misiones[i]["Codigo"] == codigo:
            posicion = i
    if posicion != -1:
        misiones.pop(posicion)
        print("Misión eliminada.")
    else:
        print("Misión no encontrada.")

def registrar_zona():
    nombre = input("Ingrese el nombre de la zona: ")
    ya_existe = 0
    for z in zona:
        if z == nombre:
            ya_existe = 1
    if ya_existe == 0:
        zona.append(nombre)
        grafo_zonas[nombre] = {}
        print("Zona registrada exitosamente.")
    else:
        print("La zona ya existe.")

def mostrar_zonas():
    print("Zonas registradas:", zona)

def eliminar_zona():
    nombre = input("Ingrese el nombre de la zona a eliminar: ")
    posicion = -1
    for i in range(len(zona)):
        if zona[i] == nombre:
            posicion = i
    if posicion != -1:
        zona.pop(posicion)
        if nombre in grafo_zonas:
            del grafo_zonas[nombre]
        print("Zona eliminada.")
    else:
        print("Zona no encontrada.")

def registrar_ruta():
    origen = input("Ingrese la zona de origen: ")
    destino = input("Ingrese la zona de destino: ")
    distancia = float(input("Ingrese la distancia en km: "))
    existe_origen = 0
    existe_destino = 0
    for z in zona:
        if z == origen:
            existe_origen = 1
        if z == destino:
            existe_destino = 1
    if existe_origen == 1 and existe_destino == 1:
        grafo_zonas[origen][destino] = distancia
        grafo_zonas[destino][origen] = distancia
        print("Ruta registrada exitosamente.")
    else:
        print("Error: Una o ambas zonas no existen.")

def mostrar_rutas():
    for z in grafo_zonas:
        print(z, "->", grafo_zonas[z])

def eliminar_ruta():
    origen = input("Ingrese la zona de origen de la ruta a eliminar: ")
    destino = input("Ingrese la zona de destino de la ruta a eliminar: ")
    if origen in grafo_zonas and destino in grafo_zonas[origen]:
        del grafo_zonas[origen][destino]
        del grafo_zonas[destino][origen]
        print("Ruta eliminada correctamente.")
    else:
        print("Ruta no encontrada.")

def burbuja_prioridad():
    n = len(misiones)
    for i in range(n):
        for j in range(0, n - i - 1):
            print("Comparando...", misiones[j]["Codigo"], "con", misiones[j + 1]["Codigo"])
            if misiones[j]["Prioridad"] > misiones[j + 1]["Prioridad"]:
                print("Intercambiando...")
                temp = misiones[j]
                misiones[j] = misiones[j + 1]
                misiones[j + 1] = temp
        print("Lista actual:")
        mostrar_codigos(misiones, "Codigo")

def insercion_bateria():
    for i in range(1, len(drones)):
        actual = drones[i]
        j = i - 1
        print("Insertando:", actual["codigo"])
        while j >= 0 and drones[j]["bateria"] > actual["bateria"]:
            print("Moviendo:", drones[j]["codigo"])
            drones[j + 1] = drones[j]
            j = j - 1
        drones[j + 1] = actual
        print("Lista actual:")
        mostrar_codigos(drones, "codigo")

def mergesort_velocidad(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print("Dividiendo")
        mostrar_codigos(lista, "codigo")
        mergesort_velocidad(izquierda)
        mergesort_velocidad(derecha)
        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i]["velocidad"] < derecha[j]["velocidad"]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        print("Mezclando")
        print("Resultado parcial")
        mostrar_codigos(lista, "codigo")

def particion_distancia(lista, inicio, fin):
    pivote = lista[fin]["Distancia"]
    print("Pivote:", lista[fin]["Codigo"])
    i = inicio - 1
    for j in range(inicio, fin):
        if lista[j]["Distancia"] <= pivote:
            i += 1
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
    temp = lista[i + 1]
    lista[i + 1] = lista[fin]
    lista[fin] = temp
    print("Partición")
    mostrar_codigos(lista, "Codigo")
    return i + 1

def quicksort_distancia(lista, inicio, fin):
    if inicio < fin:
        posicion = particion_distancia(lista, inicio, fin)
        quicksort_distancia(lista, inicio, posicion - 1)
        quicksort_distancia(lista, posicion + 1, fin)

def busqueda_lineal_dron():
    codigo = input("Código del dron a buscar: ")
    comparaciones = 0
    encontrado = 0
    for d in drones:
        comparaciones += 1
        print("Elemento comparado:", d["codigo"])
        if d["codigo"] == codigo:
            encontrado = 1
            print("Dron encontrado:", d)
            break
    print("Comparaciones realizadas:", comparaciones)
    if encontrado == 0:
        print("Dron no encontrado.")

def busqueda_lineal_mision():
    codigo = input("Código de la misión a buscar: ")
    comparaciones = 0
    encontrado = 0
    for m in misiones:
        comparaciones += 1
        print("Elemento comparado:", m["Codigo"])
        if m["Codigo"] == codigo:
            encontrado = 1
            print("Misión encontrada:", m)
            break
    print("Comparaciones realizadas:", comparaciones)
    if encontrado == 0:
        print("Misión no encontrada.")

def busqueda_binaria_dron():
    n = len(drones)
    for i in range(n):
        for j in range(0, n - i - 1):
            if drones[j]["codigo"] > drones[j + 1]["codigo"]:
                temp = drones[j]
                drones[j] = drones[j + 1]
                drones[j + 1] = temp
    codigo = input("Código del dron a buscar (Binaria): ")
    low = 0
    high = len(drones) - 1
    encontrado = 0
    while low <= high:
        mid = (low + high) // 2
        print("low:", low, "| high:", high, "| mid:", mid, "| valor medio:", drones[mid]["codigo"])
        if drones[mid]["codigo"] == codigo:
            print("Dron encontrado:", drones[mid])
            encontrado = 1
            break
        elif drones[mid]["codigo"] < codigo:
            low = mid + 1
        else:
            high = mid - 1
    if encontrado == 0:
        print("Dron no encontrado.")

def agregar_mision_cola():
    codigo = input("Código de la misión a encolar: ")
    mision = buscar_mision_por_codigo(codigo)
    if mision is None:
        print("Misión no existe.")
        return
    cola_misiones.agregar(codigo)
    print(f"Misión {codigo} agregada a la cola de espera.")

def atender_mision_cola():
    codigo = cola_misiones.sacar()
    if codigo is None:
        print("No hay misiones en espera.")
        return
    mision = buscar_mision_por_codigo(codigo)
    if mision:
        mision["Estado"] = "Atendida"
        print(f"Misión {codigo} atendida. Estado cambiado a 'Atendida'.")
    else:
        print(f"Advertencia: la misión {codigo} ya no existe en el sistema.")

def mostrar_cola_misiones():
    cola_misiones.mostrar()

def mostrar_siguiente_mision_cola():
    sig = cola_misiones.siguiente()
    if sig:
        print("Siguiente misión en cola:", sig)
    else:
        print("No hay misiones en espera.")

def insertar_mision_bst():
    codigo = input("Código de la misión a insertar en el BST: ")
    mision = buscar_mision_por_codigo(codigo)
    if mision is None:
        print("Misión no existe.")
        return
    bst_misiones.insertar(codigo)
    print(f"Código {codigo} insertado en el BST.")

def buscar_mision_bst():
    codigo = input("Código a buscar en el BST: ")
    encontrado = bst_misiones.buscar(codigo)
    if not encontrado:
        print("Código no encontrado en el BST.")

def mostrar_recorridos_bst():
    print("Preorden:", end=" ")
    bst_misiones.preorden()
    print("Inorden:", end=" ")
    bst_misiones.inorden()
    print("Postorden:", end=" ")
    bst_misiones.postorden()

def bfs(origen, destino):
    if origen not in grafo_zonas or destino not in grafo_zonas:
        print("Una o ambas zonas no existen en el grafo.")
        return False
    visitados = set()
    cola = [origen]
    visitados.add(origen)
    print("Visitando:", origen)
    print("Cola actual:", cola)
    print("Nodos visitados:", visitados)
    while cola:
        actual = cola.pop(0)
        if actual == destino:
            print("¡Camino encontrado!")
            return True
        for vecino in grafo_zonas[actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
                print("Visitando:", vecino)
                print("Cola actual:", cola)
                print("Nodos visitados:", visitados)
    print("No existe camino.")
    return False

def dijkstra(origen, destino):
    if origen not in grafo_zonas or destino not in grafo_zonas:
        print("Una o ambas zonas no existen en el grafo.")
        return None, None
    distancias = {zona: float('inf') for zona in grafo_zonas}
    distancias[origen] = 0
    previos = {zona: None for zona in grafo_zonas}
    no_visitados = set(grafo_zonas.keys())
    while no_visitados:
        actual = min(no_visitados, key=lambda z: distancias[z])
        no_visitados.remove(actual)
        print("Nodo actual:", actual)
        print("Distancias actuales:", distancias)
        if actual == destino:
            break
        for vecino, peso in grafo_zonas[actual].items():
            if vecino in no_visitados:
                nueva_dist = distancias[actual] + peso
                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    previos[vecino] = actual
        print("Ruta parcial:", previos)
    if distancias[destino] == float('inf'):
        print("No hay ruta.")
        return None, None
    camino = []
    actual = destino
    while actual is not None:
        camino.append(actual)
        actual = previos[actual]
    camino.reverse()
    print("Ruta final:", " -> ".join(camino))
    print("Distancia total:", distancias[destino], "km")
    return camino, distancias[destino]

def simulacion_rescate():
    print("---SIMULACIÓN DE RESCATE---")
    print("Paso 1: Registrar nueva misión")
    registrar_mision()
    if not misiones:
        print("No se pudo registrar la misión.")
        return
    mision = misiones[-1]
    codigo = mision["Codigo"]
    zona_afectada = mision["Zona"]
    print("Paso 2: Insertar misión en la cola FIFO")
    cola_misiones.agregar(codigo)
    print(f"Misión {codigo} encolada.")
    print("Paso 3: Insertar código en el BST")
    bst_misiones.insertar(codigo)
    print(f"Código {codigo} insertado en BST.")
    print("Paso 4: Ordenar misiones por prioridad (Burbuja)")
    burbuja_prioridad()
    print("Paso 5: Buscar un dron disponible")
    dron = buscar_dron_disponible()
    if dron is None:
        print("No hay drones disponibles. No se puede continuar.")
        return
    print(f"Dron seleccionado: {dron['codigo']}")
    print("Paso 6: Verificar ruta con BFS")
    if "Base" not in grafo_zonas:
        print("No existe una zona llamada 'Base'. Por favor, créela y agregue rutas.")
        return
    if not bfs("Base", zona_afectada):
        print("No hay ruta hacia la zona afectada. Rescate cancelado.")
        return
    print("Paso 7: Calcular ruta mínima con Dijkstra")
    camino, distancia_total = dijkstra("Base", zona_afectada)
    if camino is None:
        print("No se pudo calcular la ruta.")
        return
    print("Paso 8: Asignar dron a la misión")
    dron["Estado"] = "En mision"
    print(f"Dron {dron['codigo']} asignado. Estado actualizado a 'En mision'.")
    print("Paso 9: Actualizar estado de la misión")
    mision["Estado"] = "En curso"
    print(f"Misión {codigo} actualizada a 'En curso'.")

    print("---SIMULACIÓN COMPLETADA---")
    print(f"Resumen: Misión {codigo} asignada al dron {dron['codigo']}. Ruta: {' -> '.join(camino)}. Distancia: {distancia_total} km.")

def menuchi():
    while True:
        print("1.- Drones")
        print("2.- Misiones")
        print("3.- Zonas")
        print("4.- Rutas")
        print("5.- Ordenar misiones por prioridad (Burbuja)")
        print("6.- Ordenar drones por batería (Inserción)")
        print("7.- Ordenar drones por velocidad (MergeSort)")
        print("8.- Ordenar misiones por distancia (QuickSort)")
        print("9.- Búsqueda lineal de dron")
        print("10.- Búsqueda lineal de misión")
        print("11.- Búsqueda binaria de dron por código")
        print("12. Cola de misiones (FIFO)")
        print("13. Árbol Binario de Búsqueda (BST) de códigos")
        print("14. Verificar ruta (BFS)")
        print("15. Calcular ruta mínima (Dijkstra)")
        print("16. SIMULACIÓN COMPLETA DE RESCATE")
        print("0.- Salir")
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            print("---Menu Drones---")
            print("1.- Registrar dron")
            print("2.- Mostrar dron")
            print("3.- Eliminar dron")
            opciond = int(input("Escoja la opcion para el dron: "))
            if opciond == 1:
                registrar_dron()
            elif opciond == 2:
                mostrar_drones()
            elif opciond == 3:
                eliminar_dron()
        elif opcion == 2:
            print("---Menu Misiones---")
            print("1.- Registrar mision")
            print("2.- Mostrar mision")
            print("3.- Eliminar mision")
            opciond = int(input("Escoja la opcion para la mision: "))
            if opciond == 1:
                registrar_mision()
            elif opciond == 2:
                mostrar_misiones()
            elif opciond == 3:
                eliminar_mision()
        elif opcion == 3:
            print("---Menu Zonas---")
            print("1.- Registrar Zona")
            print("2.- Mostrar Zona")
            print("3.- Eliminar Zona")
            opciond = int(input("Escoja la opcion para la Zona: "))
            if opciond == 1:
                registrar_zona()
            elif opciond == 2:
                mostrar_zonas()
            elif opciond == 3:
                eliminar_zona()
        elif opcion == 4:
            print("---Menu Rutas---")
            print("1.- Registrar Ruta")
            print("2.- Mostrar Ruta")
            print("3.- Eliminar Ruta")
            opciond = int(input("Escoja la opcion para la Ruta: "))
            if opciond == 1:
                registrar_ruta()
            elif opciond == 2:
                mostrar_rutas()
            elif opciond == 3:
                eliminar_ruta()
        elif opcion == 5:
            burbuja_prioridad()
        elif opcion == 6:
            insercion_bateria()
        elif opcion == 7:
            mergesort_velocidad(drones)
        elif opcion == 8:
            quicksort_distancia(misiones, 0, len(misiones) - 1)
            print("Resultado")
            mostrar_codigos(misiones, "Codigo")
        elif opcion == 9:
            busqueda_lineal_dron()
        elif opcion == 10:
            busqueda_lineal_mision()
        elif opcion == 11:
            busqueda_binaria_dron()
        elif opcion == "12":
            while True:
                print("--- COLA DE MISIONES (FIFO) ---")
                print("1. Agregar misión a la cola")
                print("2. Atender misión (sacar y cambiar estado)")
                print("3. Mostrar cola")
                print("4. Mostrar siguiente misión")
                print("5. Volver")
                sub = input("Opción: ")
                if sub == "1":
                    agregar_mision_cola()
                elif sub == "2":
                    atender_mision_cola()
                elif sub == "3":
                    mostrar_cola_misiones()
                elif sub == "4":
                    mostrar_siguiente_mision_cola()
                elif sub == "5":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "13":
            while True:
                print("--- ÁRBOL BINARIO DE BÚSQUEDA (CÓDIGOS) ---")
                print("1. Insertar código de misión")
                print("2. Buscar código")
                print("3. Mostrar recorridos (Preorden, Inorden, Postorden)")
                print("4. Volver")
                sub = input("Opción: ")
                if sub == "1":
                    insertar_mision_bst()
                elif sub == "2":
                    buscar_mision_bst()
                elif sub == "3":
                    mostrar_recorridos_bst()
                elif sub == "4":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "14":
            origen = input("Zona de origen (ej. Base): ")
            destino = input("Zona de destino: ")
            bfs(origen, destino)

        elif opcion == "15":
            origen = input("Zona de origen (ej. Base): ")
            destino = input("Zona de destino: ")
            dijkstra(origen, destino)

        elif opcion == "16":
            simulacion_rescate()
        elif opcion == 0:
            break

if __name__ == '__main__':
    menuchi()