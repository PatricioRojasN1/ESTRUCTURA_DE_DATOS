class Bicola:
    def __init__(self, capacidad: int):
        self.capacidad = capacidad
        self.datos = [None] * capacidad
        self.head = 0
        self.tail = 0
        self.tamanio = 0

    def enqueue(self, elemento) -> None:
        if self.tamanio == self.capacidad:
            print("Bicola llena")
            return
        self.datos[self.tail] = elemento
        self.tail = (self.tail + 1) % self.capacidad
        self.tamanio += 1

    def enqueue_front(self, elemento) -> None:
        if self.tamanio == self.capacidad:
            print("Bicola llena")
            return
        self.head = (self.head - 1) % self.capacidad
        self.datos[self.head] = elemento
        self.tamanio += 1

    def dequeue(self):
        if self.is_empty():
            return None
        elemento = self.datos[self.head]
        self.datos[self.head] = None
        self.head = (self.head + 1) % self.capacidad
        self.tamanio -= 1
        return elemento

    def dequeue_back(self):
        if self.is_empty():
            return None
        self.tail = (self.tail - 1) % self.capacidad
        elemento = self.datos[self.tail]
        self.datos[self.tail] = None
        self.tamanio -= 1
        return elemento

    def peek(self):
        return self.datos[self.head]

    def peek_back(self):
        return self.datos[(self.tail - 1) % self.capacidad]

    def is_empty(self) -> bool:
        return self.tamanio == 0

    def size(self) -> int:
        return self.tamanio

    def __str__(self):
        resultado = []
        for i in range(self.tamanio):
            resultado.append(str(self.datos[(self.head + i) % self.capacidad]))
        return "[" + ", ".join(resultado) + "]"


def retiros(saldos: Bicola, retiro: Bicola) -> None:
    r = saldos.peek() - retiro.peek()
    saldos.dequeue()
    retiro.dequeue()
    saldos.enqueue(r)

def depositos(saldos: Bicola, deposito: Bicola) -> None:
    r = saldos.peek() + deposito.peek()
    saldos.dequeue()
    deposito.dequeue()
    saldos.enqueue(r)

def peek(b: Bicola):
    return b.peek()

def is_empty(b: Bicola) -> bool:
    return b.is_empty()

def size(b: Bicola) -> int:
    return b.size()


# === COLAS ===
saldos   = Bicola(10)
retiro   = Bicola(10)
deposito = Bicola(10)

for _ in range(5):
    saldos.enqueue(1000)

retiro.enqueue(500)
retiro.enqueue(400)
retiro.enqueue(300)
retiro.enqueue(200)
retiro.enqueue(100)

deposito.enqueue(300)
deposito.enqueue(300)
deposito.enqueue(300)
deposito.enqueue(300)
deposito.enqueue(300)

print("Saldos iniciales:", saldos)
print("Retiros:", retiro)
print("Depósitos:", deposito)

for _ in range(5):
    retiros(saldos, retiro)
print("\nSaldos tras retiros:", saldos)

for _ in range(5):
    depositos(saldos, deposito)
print("Saldos tras depósitos:", saldos)
