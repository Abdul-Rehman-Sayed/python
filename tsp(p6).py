def nearest_neighbor_tsp(graph):
    cities = list(graph.keys())
    all_paths = []
    optimal_path = None
    min_cost = float('inf')
    
    for start in cities:
        visited = [start]
        current_city = start
        total_cost = 0
        
        while len(visited) < len(cities):
            next_city = None
            min_cost_step = float('inf')
            
            for neighbor in graph[current_city]:
                if neighbor not in visited and graph[current_city][neighbor] < min_cost_step:
                    min_cost_step = graph[current_city][neighbor]
                    next_city = neighbor
            
            visited.append(next_city)
            total_cost += min_cost_step
            current_city = next_city
        
        total_cost += graph[current_city][start]
        visited.append(start)
        all_paths.append((visited, total_cost))
        
        if total_cost < min_cost:
            min_cost = total_cost
            optimal_path = visited
    
    print("All Possible Paths with Costs:")
    for path, cost in all_paths:
        print(f"Path: {' -> '.join(path)}, Cost: {cost}")
    
    print("\nOptimal Path with Minimum Cost:")
    print(f"Path: {' -> '.join(optimal_path)}, Cost: {min_cost}")

graph = {
    '1': {'1': 0, '2': 5, '3': 3, '4': 8, '5': 6, '6': 4},
    '2': {'1': 5, '2': 0, '3': 5, '4': 4, '5': 3, '6': 2},
    '3': {'1': 3, '2': 5, '3': 0, '4': 5, '5': 6, '6': 7},
    '4': {'1': 8, '2': 4, '3': 5, '4': 0, '5': 9, '6': 5},
    '5': {'1': 6, '2': 3, '3': 6, '4': 9, '5': 0, '6': 6},
    '6': {'1': 4, '2': 2, '3': 7, '4': 5, '5': 6, '6': 0}
}

nearest_neighbor_tsp(graph)
