cadena = "Parangaricutirimicuaro"
cadena = cadena.lower()  

resultado = ""
for letra in "abcdefghijklmnopqrstuvwxyz":
    conteo = cadena.count(letra)
    if conteo > 0:
        resultado += f" {letra.upper()}{conteo}"

print(resultado)

