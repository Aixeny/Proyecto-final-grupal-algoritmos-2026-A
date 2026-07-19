#Proyecto final Joel Paspuel, Isaac Alejandro
Misiones=[[101,"Bosque","Objeto perdido",2,"Campistas",10,"Pendiente"],
          [102,"Monte","Ataque de oso",7,"Campistas",7,"Pendiente"],
          [103,"Pradera","Persona extraviada",5,"Adulto",15,"Atendida"]]

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

