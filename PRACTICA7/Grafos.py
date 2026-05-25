grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(grafo, cola, visitados):
    if not cola:
        return visitados

    nodo_actual = cola.pop(0)

    for vecino in grafo[nodo_actual]:
        if vecino not in visitados:
            visitados.append(vecino)
            cola.append(vecino)

    print(f"Procesando: {nodo_actual} | Cola: {cola} | Visitados: {visitados}")

    return bfs(grafo, cola, visitados)


nodo_inicio = 'A'
visitados = []
cola      = []

print(f"Cola inicial: {cola} | Visitados: {visitados}")

visitados.append(nodo_inicio)
cola.append(nodo_inicio)

print(f"Encolando '{nodo_inicio}': Cola: {cola} | Visitados: {visitados}")

resultado = bfs(grafo, cola, visitados)
print(f"\nRecorrido final: {resultado}")