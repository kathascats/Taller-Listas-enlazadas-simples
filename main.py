from ejercicios123 import ListaEnlazada

# ejercicio 3
print("\n Inserción")
lista = ListaEnlazada()
lista.insertar_final(20)
lista.insertar_final(30)
lista.insertar_iniciio(10)

actual = lista.head
while actual is not None:
    print(actual.dato, end=" ->")
    actual = actual.siguiente
print("null")

# ejercicio 4
print("\n Busqueda")
print(f"Buscar 20 - posicion: {lista.tamaño()}")

