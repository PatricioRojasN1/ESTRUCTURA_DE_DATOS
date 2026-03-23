class ColaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = -1
        self.final = -1
    
    # Verificar si está vacía
    def esta_vacia(self):
        return self.frente == -1
    
    # Verificar si está llena
    def esta_llena(self):
        return (self.final + 1) % self.capacidad == self.frente
    
    # Insertar turno
    def encolar(self, dato):
        if self.esta_llena():
            print("La cola circular está llena.")
            return
        
        if self.esta_vacia():
            self.frente = 0
            self.final = 0
        else:
            self.final = (self.final + 1) % self.capacidad

        self.cola[self.final] = dato
        print(f"Turno {dato} insertado.")
    
    # Atender turno
    def desencolar(self):
        if self.esta_vacia():
            print("La cola circular está vacía.")
            return None
        
        dato = self.cola[self.frente]

        if self.frente == self.final:
            self.frente = -1
            self.final = -1
        else:
            self.frente = (self.frente + 1) % self.capacidad
        
        print(f"Atendiendo turno {dato}.")
        return dato
    
    # Mostrar turno al frente
    def ver_frente(self):
        if self.esta_vacia():
            print("La cola está vacía.")
            return None
        print(f"Turno al frente: {self.cola[self.frente]}")
        return self.cola[self.frente]
    
    # Mostrar todos los turnos
    def mostrar(self):
        if self.esta_vacia():
            print("Cola vacía.")
            return
        
        elementos = []
        i = self.frente

        while True:
            elementos.append(self.cola[i])
            if i == self.final:
                break
            i = (i + 1) % self.capacidad
        
        print("Cola actual:", elementos)

cola = ColaCircular(5)

print("\n--- Insertando turnos ---")
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)
cola.encolar(4)
cola.encolar(5)

cola.mostrar()

print("\n--- Atendiendo turnos ---")
cola.desencolar()
cola.desencolar()

cola.mostrar()

print("\n--- Insertando más turnos (reutilización) ---")
cola.encolar(6)
cola.encolar(7)

cola.mostrar()

print("\n--- Consultas ---")
cola.ver_frente()

print("¿Está llena?", cola.esta_llena())
print("¿Está vacía?", cola.esta_vacia())