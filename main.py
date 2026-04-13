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

#ejercicio 4
print("\n Recorrido")
lista.recorrer()

# ejercicio 5
print("\n Busqueda")
print(f"Buscar 20 - posicion: {lista.buscar(20)}")
print(f"Buscar 99 - posicion: {lista.buscar(99)}")

# ejercicio 6
print("\n Eliminación")
lista.eliminar_por_valor(20)
lista.recorrer()
lista.eliminar_primero()
lista.recorrer()

#ejercicio 7
print("\n Tamaño")
print(f"Elementos : {lista.tamaño()}")

#ejercicio 8
print("\n Inversion")
lista2 = listaEnlazada()
lista2.insertar_final(10)
lista2.insertar_final(20)
lista2.insertar_final(30)
print("Antes: ", end="")
lista2.recorrer()
lista2.invertir()
print("Despues ", end="")
lista2.recorrer()

# ejercicio 9
print("\n Ordenamiento")
lista3 = listaEnlazada()
for v in [40, 10, 30, 20]:
    lista3.insertar_final(v)
print("Antes: , end="")
lista3.recorrer()
lista3.ordenar()
print("Despues: ", end="")
lista3.recorrer()
    
      


