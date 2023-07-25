def find_all_paths(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start = 'A'
end = 'F'

paths = find_all_paths(graph, start, end)
if len(paths) == 0:
    print("Нет путей из вершины", start, "в вершину", end)
else:
    print("Все пути из вершины", start, "в вершину", end, ":")
    for path in paths:
        print(' -> '.join(path))
