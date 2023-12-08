class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # Assuming the graph is undirected

    def prim(self):
        min_spanning_tree = []
        visited = [False] * self.vertices
        priority_queue = [(0, 0)]  # (weight, vertex)

        while priority_queue:
            priority_queue.sort(reverse=True)  # Sort in descending order based on weight
            weight, current_vertex = priority_queue.pop()

            if visited[current_vertex]:
                continue

            visited[current_vertex] = True
            min_spanning_tree.append((current_vertex, weight))

            for neighbor, edge_weight in self.graph[current_vertex]:
                if not visited[neighbor]:
                    priority_queue.append((edge_weight, neighbor))

        return min_spanning_tree

# Example usage:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

minimum_spanning_tree = g.prim()
print("Edges in the Minimum Spanning Tree:")
sum = 0
for edge in minimum_spanning_tree:
    sum +=edge[1]
    print(f"Edge: {edge[0]}  Weight: {edge[1]}")
print("Minimum cost Spanning Tree:",sum)