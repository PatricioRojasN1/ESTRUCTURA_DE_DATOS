import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start, None)]  # (peso, nodo, padre)
    mst = []

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)

        if parent is not None:
            mst.append((parent, node, weight))

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, node))

    return mst


# 🔹 Grafo usando números (Root = 2)
graph = {
    2: [(0, 20), (3, 20), (4, 33)],
    0: [(2, 20), (1, 10)],
    1: [(0, 10), (3, 50), (4, 10)],
    3: [(2, 20), (1, 50), (4, 20), (5, 2)],
    4: [(2, 33), (1, 10), (3, 20), (5, 1)],
    5: [(4, 1), (3, 2)]
}

resultado = prim(graph, 2)

print(resultado)