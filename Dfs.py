class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices) ]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        print(start, end=" ")
        visited.add(start)

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage:
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)


print("DFS Traversal starting from vertex 0:")
g.dfs(0)
