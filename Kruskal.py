class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def kruskal(self):
        result = []  # To store the resulting minimum spanning tree
        self.graph = sorted(self.graph, key=lambda item: item[2])  # Sort the edges based on weight
        parent = [i for i in range(self.vertices)]

        def find_set(i):
            if parent[i] == i:
                return i
            return find_set(parent[i])

        def union(u, v):
            u_set = find_set(u)
            v_set = find_set(v)
            parent[u_set] = v_set

        for edge in self.graph:
            u, v, w = edge
            if find_set(u) != find_set(v):
                result.append((u, v, w))
                union(u, v)

        return result

# Example usage:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

minimum_spanning_tree = g.kruskal()
print("Edges in the Minimum Spanning Tree:")
sum = 0
for edge in minimum_spanning_tree:
    sum +=edge[2]
    print(f"{edge[0]} -- {edge[1]}  Weight: {edge[2]}")
print("Minimum cost Spanning Tree:",sum)
