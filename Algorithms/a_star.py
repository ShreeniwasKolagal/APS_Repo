import heapq

def a_star(start, goal, h_func, neighbors):
    """
    start, goal: nodes (e.g., (x,y) tuples)
    h_func(u, goal): heuristic cost estimate from u → goal
    neighbors(u): iterable of (v, cost) pairs for edges u→v
    Returns: (cost, path_list) for the lowest‐f‐cost path, or (inf, []) if unreachable.
    """
    open_set = []
    # f_score[u] = g_score[u] + h(u), g_score[u] = cost from start → u
    g_score = {start: 0}
    f_score = {start: h_func(start, goal)}
    # parent pointers for path reconstruction
    parent = {start: None}

    heapq.heappush(open_set, (f_score[start], start))

    while open_set:
        current_f, u = heapq.heappop(open_set)
        if u == goal:
            # Reconstruct path
            path = []
            node = goal
            while node:
                path.append(node)
                node = parent[node]
            return g_score[goal], path[::-1]

        for v, cost_uv in neighbors(u):
            tentative_g = g_score[u] + cost_uv
            if tentative_g < g_score.get(v, float('inf')):
                parent[v] = u
                g_score[v] = tentative_g
                f_score[v] = tentative_g + h_func(v, goal)
                heapq.heappush(open_set, (f_score[v], v))

    return float('inf'), []


# Example on a 4×4 grid with 4‐way moves; cost = 1 per move.
def grid_neighbors(u):
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    x, y = u
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            yield (nx, ny), 1

def manhattan(u, goal):
    return abs(u[0] - goal[0]) + abs(u[1] - goal[1])

start = (0, 0)
goal = (3, 3)
cost, path = a_star(start, goal, manhattan, grid_neighbors)
print("Cost:", cost)
print("Path:", path)
