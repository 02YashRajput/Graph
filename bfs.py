from collections import deque

class Graph:
    def __init__(self,vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices)]

    def add_edge(self, u, v):
        
        self.graph[u].append(v)


    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        

# Example usage:
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS Traversal starting from vertex 0:")
g.bfs(0)
