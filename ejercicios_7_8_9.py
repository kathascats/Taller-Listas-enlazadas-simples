def tamano(self):
        # ejercicio 7
        # retorna la cantidad de elementos en la lista
        contador = 0
        actual = self.cabeza
        
        while actual is not None:
            contador += 1
            actual = actual.siguiente
            
        return contador

def invertir(self):
        # ejercicio 8
        # invierte el orden de la lista reestructurando enlaces
        previo = None
        actual = self.cabeza
        siguiente = None

        while actual is not None:
            siguiente = actual.siguiente  # se guardamos el resto de la lista temporalmente
            actual.siguiente = previo     # invertimos el enlace actual
            previo = actual               # avanzamos previo
            actual = siguiente            # avanzamos actual
            
        self.cabeza = previo              # el último nodo se convierte en la nueva cabeza

def ordenar(self):
        # ejercicio 9
        # metodo de burbuija
        # se ordena de forma ascendenmte
        if self.cabeza is None or self.cabeza.siguiente is None:
            return

        hubo_intercambio = True
        fin = None

        while hubo_intercambio:
            hubo_intercambio = False
            actual = self.cabeza
            previo = None

            while actual.siguiente is not fin:
                siguiente = actual.siguiente

                # si el actual es mayor, se hace el intercambio de enlaces
                if actual.dato > siguiente.dato:
                    # 1. reestructuramos los enlaces manualmente
                    actual.siguiente = siguiente.siguiente
                    siguiente.siguiente = actual

                    # 2. eeconectamos con el resto de la lista por detrás
                    if previo is None:
                        self.cabeza = siguiente
                    else:
                        previo.siguiente = siguiente

                    # 3. avanzamos los punteros
                    previo = siguiente
                    hubo_intercambio = True
                else:
                    # si no hay que intercambiar, avanzamos normalmente
                    previo = actual
                    actual = actual.siguiente
            
            # se marca el límite para no evaluar los elementos que ya quedaron ordenados al final
            fin = actual

