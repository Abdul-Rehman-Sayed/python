def astaralgo(start_node, stop_node):
    open_set = {start_node}
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}
    while open_set:
        n = min(open_set, key=lambda v: g[v] + heuristic(v))
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print(f"Path found: {path}")
            return path
        open_set.remove(n)
        closed_set.add(n)

        for m ,weight in get_neighbours(n):
            if m in closed_set:
                continue
            tentative_g = g[n] + weight
            if m not in open_set or tentative_g < g.get(m, float('inf')):
                open_set.add(m)
                g[m] = tentative_g
                parents[m] = n
    print("Path does not exist")
    return None

def get_neighbours(v):
    return Graph_nodes.get(v, [])

def heuristic(n):
    H_dist = {'A': 4, 'B': 3, 'C': 9, 'D': 7}
    return H_dist.get(n, float('inf'))

Graph_nodes = {
    'A': [('B', 1), ('D', 3), ('C', 5)],
    'B': [('C', 2), ('A', 1)],
    'C': [('B', 2), ('D', 4), ('A', 5)],
    'D': [('C', 4), ('A', 3)]
}

astaralgo('A', 'C')