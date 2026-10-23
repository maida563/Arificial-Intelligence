class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)

    def dls(self, node, goal, limit, depth, path):
        path.append(node)

        if node == goal:
            return True

        if depth == limit:
            # Do not explore any deeper along this branch
            return False 

        for child in self.graph.get(node, []):
            if self.dls(child, goal, limit, depth + 1, path):
#  If any recursive call returns True (goal found), it propagates True(search stop)            
                return True
        return False
    
# ================================================================================

    def ids(self, start, goal, max_depth):
        for limit in range(max_depth + 1):
            path = []
            found = self.dls(start, goal, limit, 0, path)
            nodes_str = " ".join(path)
            print(f"Depth {limit}: {nodes_str}")
            if found:
                print(f"Goal {goal} found at depth {limit}!")
                return True

        print("Goal not found within the maximum depth.")
        return False


# Create graph object
g = Graph()

# Define the tree (exact same original edges preserved)
g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('A', 'D')
g.add_edge('A', 'E')

g.add_edge('B', 'K')
g.add_edge('B', 'J')

g.add_edge('K', 'N')
g.add_edge('K', 'M')

g.add_edge('D', 'G')

g.add_edge('E', 'C')
g.add_edge('E', 'H')
g.add_edge('E', 'I')

g.add_edge('I', 'L')

# 1. Perform DLS
print("Depth-Limited Search (Limit = 2)")
print("---------------------------------")
start = 'A'
goal = 'G'
limit = 2
dls_path = []
found_dls = g.dls(start, goal, limit, 0, dls_path)
print(f"Depth {limit}: {' '.join(dls_path)}")
if found_dls:
    print(f"Goal '{goal}' found!")
else:
    print(f"Goal '{goal}' not found within depth limit {limit}.\n")

# 2. Perform IDS
print("\nIterative Deepening Search (Max Depth = 3)")
print("==========================================")
max_depth = 3
g.ids(start, goal, max_depth)