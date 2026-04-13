# punto 4 
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_lista(self):
        actual = self.head
        while actual is not None:
            print(f"{actual.dato} ->", end=" ")
            actual = actual.siguiente
        print("null")

  # punto 5

    def buscar(self, valor_buscado):
        actual = self.head
        posicion = 0
        while actual is not None:
            if actual.dato == valor_buscado:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1

    # Ejercicio 6. Eliminación [cite: 40]
    def eliminar_primero(self):
        if self.head is not None:
            self.head = self.head.siguiente

    def eliminar_por_valor(self, valor_a_eliminar):
        if self.head is None:  # Caso lista vacía
            return

        if self.head.dato == valor_a_eliminar:
            self.head = self.head.siguiente
            return

        actual = self.head
        while actual.siguiente is not None:
            if actual.siguiente.dato == valor_a_eliminar:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

