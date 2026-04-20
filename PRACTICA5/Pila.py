class Pila:
    def __init__(self):
        self.items = []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


dulces = [11890.0, 12500.5, 13010.35, 13650.8, 13999.0, 
          14100.0, 14780.4, 14999.99, 15120.0, 15550.75, 
          15800.0, 16250.25]

pila = Pila()

for d in dulces:
    pila.push(d)

print("Pila completa:", pila.items)
print("Elemento en la cima (top):", pila.peek())
print("Tamaño:", pila.size())

