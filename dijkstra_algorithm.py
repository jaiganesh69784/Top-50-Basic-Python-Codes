import heapq

def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances
