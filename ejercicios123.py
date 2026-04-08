# ejercicio 1
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
# ejercicio 2 y 3
class listaEnlazada:
    def __init__(self):
        self.head = None

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.head
        self.head = nuevo

def insertar_final(self, dato):
    nuevo = Nodo(dato)
    if self.head is None:
        self.head = nuevo
        return
    actual = self.head
    while actual.siguiente is not None:
        actual = actual.siguiente
    actual.siguiente = nuevo








