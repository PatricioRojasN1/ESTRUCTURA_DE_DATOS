
cosechas = [12, 24, 16, 15, 20, 18, 6, 10, 12, 11, 15, 12]

total = 0

for i in cosechas:
    total += i

promedio = total / len(cosechas)

mayores = 0
menores = 0

for i in cosechas:
    if i > promedio:
        mayores += 1
    elif i < promedio:
        menores += 1

print("Promedio anual:", promedio)
print("Meses superiores al promedio:", mayores)
print("Meses inferiores al promedio:", menores)
