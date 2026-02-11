cadena = "Parangaricutirimicuaro"
cadena1 = list(cadena.lower())

resultado = ""
for letra in "abcdefghijklmnopqrstuvwxyz":
    conteo = cadena1.count(letra)  
    if conteo > 0:
        resultado += f" {letra.upper()}{conteo}"

print(resultado)