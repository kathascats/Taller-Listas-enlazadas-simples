from ejercicios123 import lista_enlazada

lista = ListaEnlazada()

lista.insertar_inicio(20)
lista.insertar_inicio(10)
lista.insertar_inicio(30)

# recorrido
actual = lista.head
while actual is not None:
    print(actual.dato, end= " - ")
    actual = actual.siguiente
print("null")