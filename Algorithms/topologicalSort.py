from collections import deque, defaultdict

def topological_sort(nodes, edges):
    """
    nodes: iterable of all node IDs
    edges: list of (u, v) pairs meaning u → v (u precedes v)
    Returns: a list of nodes in topological order, or [] if a cycle exists.
    """
    indegree = {u: 0 for u in nodes}
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    queue = deque([u for u in nodes if indegree[u] == 0])
    topo_order = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    if len(topo_order) == len(nodes):
        return topo_order
    else:
        return []  # cycle detected


# Example:
nodes = ['A', 'B', 'C', 'D', 'E']
edges = [('A','C'), ('B','C'), ('C','D'), ('D','E')]
print(topological_sort(nodes, edges))
# Possible output: ['A', 'B', 'C', 'D', 'E']
