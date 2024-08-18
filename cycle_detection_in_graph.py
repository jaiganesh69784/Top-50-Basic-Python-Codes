def detect_cycle(graph):
    visited = set()
    stack = set()

    def visit(vertex):
        if vertex in stack:
            return True
        if vertex in visited:
            return False
        visited.add(vertex)
        stack.add(vertex)
        for neighbor in graph[vertex]:
            if visit(neighbor):
                return True
        stack.remove(vertex)
        return False

    return any(visit(v) for v in graph)
