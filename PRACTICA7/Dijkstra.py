import heapq

EDGES = [
    (0, 1, 9),
    (0, 4, 6),
    (1, 3, 8),
    (2, 4, 5),
    (2, 5, 6),
    (3, 5, 1),
    (3, 7, 7),
    (4, 6, 3),
    (6, 7, 2),
]
NUM_VERTICES = 8


def build_graph(edges, n):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph


def dijkstra(graph, start):
    n = len(graph)
    cost  = [float('inf')] * n
    path  = [-1] * n
    known = [False] * n

    cost[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)

        if known[u]:
            continue
        known[u] = True

        for v, w in graph[u]:
            nueva_dist = cost[u] + w
            if nueva_dist < cost[v]:
                cost[v] = nueva_dist
                path[v] = u
                heapq.heappush(pq, (nueva_dist, v))

    return cost, path, known


def reconstruir_ruta(path, vertex):
    ruta = []
    actual = vertex
    while actual != -1:
        ruta.append(actual)
        actual = path[actual]
    ruta.reverse()
    return ruta


def imprimir_tabla(cost, path, known):
    print()
    print(f"{'Vertex':<8} {'Known':<8} {'Cost':<8} {'Path':<8}  Ruta completa")
    print("─" * 55)
    for v in range(len(cost)):
        ruta     = reconstruir_ruta(path, v)
        ruta_str = " ".join(map(str, ruta))
        costo_str = str(cost[v]) if cost[v] != float('inf') else "∞"
        print(f"  {v:<6} {'T' if known[v] else 'F':<8} {costo_str:<8} {path[v]:<8}  {ruta_str}")
    print()


if __name__ == "__main__":
    graph = build_graph(EDGES, NUM_VERTICES)

    START = 0
    print(f"\n{'═'*55}")
    print(f"  Dijkstra – Vértice de inicio: {START}")
    print(f"{'═'*55}")

    cost, path, known = dijkstra(graph, START)
    imprimir_tabla(cost, path, known)

    print("  Caminos mínimos desde el vértice", START)
    print("─" * 40)
    for v in range(NUM_VERTICES):
        ruta = reconstruir_ruta(path, v)
        ruta_str = " → ".join(map(str, ruta))
        print(f"  {START} → {v}  costo={cost[v]:<4}  ruta: {ruta_str}")
    