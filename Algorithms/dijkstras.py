import heapq

def dijkstra(start, adj_list):
    """
    start: source node
    adj_list: dict mapping u → list of (v, weight_uv)
    Returns: dist dict mapping node → shortest distance from start
    """
    dist = {start: 0}
    visited = set()
    heap = [(0, start)]

    while heap:
        d_u, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, w_uv in adj_list.get(u, []):
            if v in visited:
                continue
            new_d = d_u + w_uv
            if new_d < dist.get(v, float('inf')):
                dist[v] = new_d
                heapq.heappush(heap, (new_d, v))

    return dist


# Example:
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('C', 1), ('D', 3)],
    'C': [('D', 2)],
    'D': []
}

distances = dijkstra('A', graph)
print(distances)  # {'A':0, 'B':2, 'C':3, 'D':5}
