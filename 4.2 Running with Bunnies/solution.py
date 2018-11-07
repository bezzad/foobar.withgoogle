"""
The Bellman-Ford's complete sources algorithm (shortest path from all to all points)
reference: https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

Graph API:
    iter(graph) gives all nodes
    iter(graph[u]) gives neighbours of u
    graph[u][v] gives weight of edge (u, v)
"""

# Class to represent a graph


class Graph:

    def __init__(self, square_matrix):
        self.graph = square_matrix
        self.V = len(square_matrix)  # No. of vertices

        # Step 1: Initialize distances from src to all other vertices as INFINITE
        #         start admiting that the rest of nodes are very very far
        self.INF = float("Inf")
        self.distances = [[self.INF for _ in xrange(self.V)] for _ in xrange(self.V)]
        self.shortestPath = [[None for _ in xrange(self.V)] for _ in xrange(self.V)]
        self.shortestGraph = [] # keep the graph from shortest paths
        

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm.  The function
    # also detects negative weight cycle
    def BellmanFord(self, src):        
        # keep lower distances from source to another vertexes
        self.distances[src][src] = 0
                
        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1 edges
        for _ in xrange(self.V - 1):  # Run this until is converges
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in queue
            for u in xrange(self.V):
                for v in xrange(self.V):
                    if self.distances[src][u] != self.INF and self.distances[src][u] + self.graph[u][v] < self.distances[src][v]:
                        # Record this lower distance
                        self.distances[src][v] = self.distances[src][u] + self.graph[u][v]
                        self.shortestPath[src][v] = v if src == u else u

        # Step 3: check for negative-weight cycles.  The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there is a cycle.
        for u in xrange(self.V):
            for v in xrange(self.V):
                if self.distances[src][u] != self.INF and self.distances[src][u] + self.graph[u][v] < self.distances[src][v]:
                    # print "Graph contains negative weight cycle"
                    return False

        return True

    def BellmanFordCompleteSource(self):
        for v in xrange(self.V):
            if self.BellmanFord(v):
                vChilds = set(self.shortestPath[v])
                vChilds.remove(None)
                self.shortestGraph.append(vChilds)
            else:
                return False
        return True

    def dfs_paths(self, start, goal):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in self.shortestGraph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

    def longest_paths(self, start, goal, fuel):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in self.shortestGraph[vertex] - set(path):
                if next == goal:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))




def answer(times, time_limit):
    # print all distance
    g = Graph(times)

    # Print input graph:
    print("input: (time_limit="+ str(time_limit) +")")
    for row in xrange(g.V):
        print(row, g.graph[row])

    if g.V < 3: 
        return []

    if g.BellmanFordCompleteSource():
        print("shortest distances:")
        for row in xrange(g.V):
            print(row, g.distances[row])
        print("shortest paths:")
        for c in xrange(g.V):
            print(c, g.shortestPath[c])
        print("shortest graph", g.shortestGraph)
        print("DFS", list(g.longest_paths(0, g.V-1)))
    else:
        return range(g.V-2)

# ======================= Test Case ==========================================
if __name__ == "__main__":

    # print("answer:",
    # answer([[0,  1,  5,  5,  2],
    #         [10, 0,  2,  6,  10],
    #         [10, 10, 0,  1,  5],
    #         [10, 10, 10, 0,  1],
    #         [10, 10, 10, 10, 0]], 5))
    # print("Expected: [0, 1, 2]")
    # print("============================================================================")

    # print("answer:",
    # answer([[0, 1, 3, 4, 2],
    #         [10, 0, 2, 3, 4],
    #         [10, 10, 0, 1, 2],
    #         [10, 10, 10, 0, 1],
    #         [10, 10, 10, 10, 0]], 3))
    # print("Expected: [0, 1, 2]")
    # print("============================================================================")
    
    # print("answer:",
    # answer([[0, 2, 2, 2, -1],
    #         [9, 0, 2, 2, -1],
    #         [9, 3, 0, 2, -1],
    #         [9, 3, 2, 0, -1],
    #         [9, 3, 2, 2, 0]], 1))
    # print("Expected: [1, 2]")
    # print("============================================================================")

    print("answer:",
    answer([[0,  1, 10, 10, 10],
            [10, 0,  1,  1,  2],
            [10, 1,  0, 10, 10],
            [10, 1,  10, 0, 10],
            [10, 10, 10, 10, 0]], 7))
    print("Expected: [0, 1, 2]")
    print("============================================================================")

    # print("answer:",
    # answer([[0, 1, 1, 1, 1],
    #         [1, 0, 1, 1, 1],
    #         [1, 1, 0, 1, 1],
    #         [1, 1, 1, 0, 1],
    #         [1, 1, 1, 1, 0]], 3))
    # print("Expected: [0, 1]")
    # print("============================================================================")

    # print("answer:",
    # answer([[0, 5, 11, 11, 1],
    #         [10, 0, 1, 5, 1],
    #         [10, 1, 0, 4, 0],
    #         [10, 1, 5, 0, 1],
    #         [10, 10, 10, 10, 0]], 10))
    # print("Expected: [0, 1]")
    # print("============================================================================")

    # print("answer:",
    # answer([[1, 1, 1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 1, 1, 1]], 1))
    # print("Expected: []")
    # print("============================================================================")
   
    # print("answer:",
    # answer([[0, 20, 20, 20, -1],
    #         [90, 0, 20, 20, 0],
    #         [90, 30, 0, 20, 0],
    #         [90, 30, 20, 0, 0],
    #         [-1, 30, 20, 20, 0]], 0))
    # print("Expected: [0, 1, 2]")
    # print("============================================================================")

    # print("answer:",
    # answer([[0, 10, 10, 10, 1],
    #         [0, 0, 10, 10, 10],
    #         [0, 10, 0, 10, 10],
    #         [0, 10, 10, 0, 10],
    #         [1, 1, 1, 1, 0]], 5))
    # print("Expected: [0, 1]")
    # print("============================================================================")

    # print("answer:",
    # answer([[0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0]], 0))
    # print("Expected: [0, 1, 2]")
    # print("============================================================================")

    # print("answer:",
    # answer([[2, 2],
    #         [2, 2]], 5))
    # print("Expected: []")
    # print("============================================================================")

    # print("answer:",
    # answer([[0, 10, 10, 1, 10],
    #         [10, 0, 10, 10, 1],
    #         [10, 1, 0, 10, 10],
    #         [10, 10, 1, 0, 10],
    #         [1, 10, 10, 10, 0]], 6))
    # print("Expected: [0, 1, 2]")
    # print("============================================================================")

    # print("answer:",
    # answer([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #         [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #         [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    #         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 5))
    # print("Expected: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]")
    # print("============================================================================")