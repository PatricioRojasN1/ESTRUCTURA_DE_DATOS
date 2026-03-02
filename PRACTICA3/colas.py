def enque(lista, elemento):
    lista.append(elemento)

def deque(lista, lista2):
    enque(lista2, (lista[0]))
    lista.pop(0)

def retiros(lista, lista2):
    r = lista[0] - lista2[0]
    deque(lista, lista2)
    enque(lista, r)

def depositos(lista, lista2):
    r = lista[0] + lista2[0]  
    deque(lista, lista2)
    enque(lista, r)

def peek(lista):
    return lista[0]

def is_empty(lista):
    if lista == []:
        return True
    else:
        return False
    
def size(lista):
    return len(lista)

saldos   = [1000, 1000, 1000, 1000, 1000]
retiro   = [500]
deposito = [300]

print("Saldos iniciales:", saldos)

retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
print("Saldos tras retiros:", saldos)

depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
print("Saldos tras depósitos:", saldos)

