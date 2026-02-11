calificaciones = [8, 8, 7, 5, 10, 9, 9, 5, 6, 10]

total = 0
n = len(calificaciones)

for cal in calificaciones:
    total += cal

promedio = total / n

aprobados = 0
reprobados = 0

for cal in calificaciones:
    if cal >= 7:
        aprobados += 1
    else:
        reprobados += 1

porc_aprobados = (aprobados / n) * 100
porc_reprobados = (reprobados / n) * 100

print("Promedio del grupo:", promedio)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Porcentaje aprobados:", porc_aprobados, "%")
print("Porcentaje reprobados:", porc_reprobados, "%")
