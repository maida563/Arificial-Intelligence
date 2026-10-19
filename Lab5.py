from collections import deque

class Graph:
    def __init__(self):
        self.graph={}

    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def add_edge(self,u,v,directed=True):
        if u not in self.graph:
            self.graph[u]= []
        if v not in self.graph:
            self.graph[v]=[]

        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)

# # ======================================= Task1 and TASK 2 ================================

    def BFS(self,s):
         visited= set()
         Q = deque([s])
         visited.add(s)
         print("Simple BFS:")
         while Q:
             v = Q.popleft()
             print(v, end=" ")

             for w in self.graph[v]:
                 if w not in visited:
                     Q.append(w)
                     visited.add(w)
         print("\n")   

    def bfs_search(self, start_node, goal_node):
        Q = deque([start_node])
        visited = {start_node}
        traversal_path = []

        print(f"Starting BFS search for Goal: '{goal_node}'...\n")

        while Q:
            curr = Q.popleft()
            traversal_path.append(curr)
            print(f"Visited: {curr}")

#          Check if goal node is reached
            if curr == goal_node:
                print("\nGoal Node Found!")
                return traversal_path

#         # Enqueue unvisited children/neighbors
            for child in self.graph[curr]:
                if child not in visited:
                    visited.add(child)
                    Q.append(child)

        print("\nGoal node not found in tree.")
        return traversal_path
    # --------------------------------LAB 6-----------------------------------

    def DFS(self,s):
        stack = [s]
        visited = set()
        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                print(f"Visiting Node: {current_node}")
                visited.add(current_node)
            
            for neighbor in reversed(self.graph[current_node]):
                if neighbor not in visited:
                    stack.append((neighbor))

    def DFS_goal(self, start_node, goal_node):
        stack = [(start_node, [start_node])]
        visited = set()

        print(f"--- Starting DFS Search from '{start_node}' to '{goal_node}' ---")

        while stack:
            current_node, path = stack.pop()
            if current_node not in visited:
                print(f"Visiting Node: {current_node}")
                visited.add(current_node)

                if current_node == goal_node:
                    print(f"\nGoal Node '{goal_node}' Found!")
                    print(f"Path taken: {' --> '.join(path)}")
                    return path

                neighbors = self.graph.get(current_node, [])

                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))

        print(f"\nGoal Node '{goal_node}' was not found.")
        return None

g = Graph()

# Define graph connections
g.add_edge('A','B')
g.add_edge('A','F')
g.add_edge('A','D')
g.add_edge('A','E')
g.add_edge('B','K')
g.add_edge('B','J')
g.add_edge('D','G')
g.add_edge('E','C')
g.add_edge('E','H')
g.add_edge('E','I')
g.add_edge('K','N')
g.add_edge('K','M')
g.add_edge('I','L')
print("Simple BFS Path: ",end=" ")
g.DFS('A')
# Run DFS starting at 'A' and seeking 'G'
print("BFS with Goal: ",end=" ")

g.DFS_goal('A','Z')


g=Graph()
g.add_edge('A','B')
g.add_edge('A','F')
g.add_edge('A','D')
g.add_edge('A','E')

g.add_edge('B','K')
g.add_edge('B','J')

g.add_edge('D','G')

g.add_edge('E','C')
g.add_edge('E','H')
g.add_edge('E','I')

g.add_edge('K','N')
g.add_edge('K','M')

g.add_edge('I','L')

g.BFS('A')
path = g.bfs_search('A','G')
print(f"Path Taken: {path}")


# # =========================================== LAB 5 -- Task 3==========================================

class SortedPriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, item, priority):
        self.queue.append((priority, item))
        # Keep list sorted by priority in descending order
        # so highest priority (lowest number) is always at the end
        self.queue.sort(key=lambda x: x[0], reverse=True)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")

        # Pops the last item in O(1) time
        priority, item = self.queue.pop()
        return item, priority
pq = SortedPriorityQueue()
pq.push("Low priority task", 3)
pq.push("Critical task", 1)
pq.push("Medium priority task", 2)

while not pq.is_empty():
    task, priority = pq.pop()
    print(f"Priority: {priority} -> Task: {task}")

# ==========================================================================
