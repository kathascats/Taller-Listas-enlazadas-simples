from lista_enlazada import ListaEnlazada

lista = ListaEnlazada()

lista.insertar_inicio(20)
lista.insertar_inicio(10)
lista.insertar_inicio(30)

# recorrido
actual = lista.cabeza
while actual is not None:
    print(actual.dato, end= " - ")
    actual = actual.siguiente
print("null")