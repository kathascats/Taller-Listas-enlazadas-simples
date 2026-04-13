#ejercicio 1
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
#ejercicios 2 y 3
class listaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def mostrar_lista(self):
        if self.cabeza is None:
            print("Lista vacía")
            return
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" -> ".join(elementos))

    def buscar(self, valor):
        actual = self.cabeza
        pos = 1
        while actual:
            if actual.dato == valor:
                return pos
            actual = actual.siguiente
            pos += 1
        return -1

    def eliminar_por_valor(self, valor):
        if self.cabeza is None:
            return
        if self.cabeza.dato == valor:
            self.cabeza = self.cabeza.siguiente
            return
        anterior = None
        actual = self.cabeza
        while actual and actual.dato != valor:
            anterior = actual
            actual = actual.siguiente
        if actual:
            anterior.siguiente = actual.siguiente

    def eliminar_primero(self):
        if self.cabeza:
            self.cabeza = self.cabeza.siguiente

    def tamano(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

    def ordenar(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(actual.dato)
            actual = actual.siguiente
        valores.sort()
        actual = self.cabeza
        for v in valores:
            actual.dato = v
            actual = actual.siguiente
