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

        # Initialize distances from src to all other vertices as INFINITE
        # so, start admiting that the rest of nodes are very very far
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
        

    def get_paths(self, start, goal, time):
        stack = [(start, [start], time)]
        while stack:
            (vertex, path, remainTime) = stack.pop()
            for next in self.shortestGraph[vertex]:
                timeToNext = self.graph[path[len(path)-1]][next]
                timeToGoalFromNext = self.distances[next][goal]
                if (0 <= remainTime - timeToNext - timeToGoalFromNext): # can to go next vertex and after that go to bulkhead?
                    nextPath = path + [next] # update path          
                    nextRemainTime = remainTime - timeToNext        
                    stack.append((next, nextPath, nextRemainTime))          
                    if next == goal:
                        freedBunnies = set(nextPath)
                        yield freedBunnies  
                        if len(freedBunnies) == self.V: # all bunnies are released
                            return
                    

def answer(times, time_limit):
    # print all distance
    g = Graph(times)   

    if g.V < 3: 
        return []
    
    maxFreedBunnies = set([])
    if g.BellmanFordCompleteSource():
        print("shortest distances:")
        for row in xrange(g.V):
            print(row, g.distances[row])
        print("shortest paths:")
        for c in xrange(g.V):
            print(c, g.shortestPath[c])
        print("shortest graph", g.shortestGraph)

        for freedBunnies in g.get_paths(0, g.V-1, time_limit):
            print("result", freedBunnies) 
            maxLen = len(maxFreedBunnies)
            freedLen = len(freedBunnies)
            if maxLen < freedLen or (maxLen == freedLen and sum(maxFreedBunnies) > sum(freedBunnies)):
                maxFreedBunnies = freedBunnies            
    else:
        return range(g.V-2)

    return map(lambda x: x-1, sorted(maxFreedBunnies - set([0, g.V-1])))            
    

# ======================= Test Case ==========================================
if __name__ == "__main__":
    import datetime

    def test(times, time_limit, expectedFreedBunnies):
        # Print input graph:
        print("input: (time_limit="+ str(time_limit) +")")
        for row in xrange(len(times)):
            print(row, times[row])
        startTime = datetime.datetime.now()        
        print("answer:", answer(times, time_limit))
        print("Expected", expectedFreedBunnies)
        print("Execution time: "+ str((datetime.datetime.now() - startTime)))
        print("============================================================================")

    
    # test([[0,  1,  5,  5,  2],
    #       [10, 0,  2,  6,  10],
    #       [10, 10, 0,  1,  5],
    #       [10, 10, 10, 0,  1],
    #       [10, 10, 10, 10, 0]], 5, [0, 1, 2]) 

    
    # test([[0, 1, 3, 4, 2],
    #       [10, 0, 2, 3, 4],
    #       [10, 10, 0, 1, 2],
    #       [10, 10, 10, 0, 1],
    #       [10, 10, 10, 10, 0]], 4, [])    
    
        
    # test([[0, 2, 2, 2, -1],
    #       [9, 0, 2, 2, -1],
    #       [9, 3, 0, 2, -1],
    #       [9, 3, 2, 0, -1],
    #       [9, 3, 2, 2, 0]], 1, [1, 2])

        
    # test([[0,  1, 10, 10, 10],
    #       [10, 0,  1,  1,  2],
    #       [10, 1,  0, 10, 10],
    #       [10, 1,  10, 0, 10],
    #       [10, 10, 10, 10, 0]], 7, [0, 1, 2])

        
    # test([[0, 1, 1, 1, 1],
    #       [1, 0, 1, 1, 1],
    #       [1, 1, 0, 1, 1],
    #       [1, 1, 1, 0, 1],
    #       [1, 1, 1, 1, 0]], 3, [0, 1])

        
    # test([[0, 5, 11, 11, 1],
    #       [10, 0, 1, 5, 1],
    #       [10, 1, 0, 4, 0],
    #       [10, 1, 5, 0, 1],
    #       [10, 10, 10, 10, 0]], 10, [0, 1])

        
    # test([[0, 20, 20, 20, -1],
    #       [90, 0, 20, 20, 0],
    #       [90, 30, 0, 20, 0],
    #       [90, 30, 20, 0, 0],
    #       [-1, 30, 20, 20, 0]], 0, [0, 1, 2])

        
    # test([[0, 10, 10, 10, 1],
    #       [0, 0, 10, 10, 10],
    #       [0, 10, 0, 10, 10],
    #       [0, 10, 10, 0, 10],
    #       [1, 1, 1, 1, 0]], 5, [0, 1])

        
    # test([[2, 2],
    #       [2, 2]], 5, [])

        
    # test([[0, 10, 10, 1, 10],
    #       [10, 0, 10, 10, 1],
    #       [10, 1, 0, 10, 10],
    #       [10, 10, 1, 0, 10],
    #       [1, 10, 10, 10, 0]], 6, [0, 1, 2])

        
    # test([[1, 1, 1, 1, 1, 1, 1],
    #       [1, 1, 1, 1, 1, 1, 1],
    #       [1, 1, 1, 1, 1, 1, 1],
    #       [1, 1, 1, 1, 1, 1, 1],
    #       [1, 1, 1, 1, 1, 1, 1],
    #       [1, 1, 1, 1, 1, 1, 1],
    #       [1, 1, 1, 1, 1, 1, 1]], 1, [])
   
        
    # test([[0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0]], 0, [0, 1, 2])

    # test([[0, 0, 1, 1, 1],
    #       [0, 0, 0, 1, 1],
    #       [0, 0, 0, 0, 1],
    #       [0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0]], 0, [0, 1, 2])

    test([[0, 0, 0, 1, 1],
          [0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]], 0, [0, 1, 2])
        
    # test([[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #       [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #       [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    #       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 
    #       5, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])