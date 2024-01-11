def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception
    if node in visited:
        return

    visited.add(node)  # if visited is list use .append()
    cycles.add(node)  # if cycles is list use .append()

    for child in graph[node]:
        dfs(child, graph, visited, cycles)
    cycles.remove(node)


visited = set()
graph = {}
while True:
    line = input()
    if line == 'End':
        break

    key, value = line.split('-')
    if key not in graph:
        graph[key] = []
    if value not in graph:
        graph[value] = []
    graph[key].append(value)


try:
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')

