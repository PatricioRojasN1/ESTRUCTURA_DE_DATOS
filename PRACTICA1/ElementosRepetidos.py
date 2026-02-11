x = [1, 2, 4, 4, 4, 5, 7, 9, 11, 11, 13, 14, 15, 16, 16]

y = []

for numero in x:
    if numero not in y:
        y.append(numero)

print("Arreglo original x:", x)
print("Arreglo y sin duplicados:", y)
print("Tamaño de x:", len(x))
print("Tamaño de y:", len(y))

x1 = [1, 2, 4, 4, 4, 5, 7, 9, 11, 11, 13, 14, 15, 16, 16]
for i in range(len(x1)-1, 0, -1):
    if x1[i] == x1[i-1]:
        x1.pop(i)
print("Arreglo x1 sin duplicados:", x1)