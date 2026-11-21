class GreedyBestFirstSearch:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics

    def search(self, start, goal):
        # Tuple format: (heuristic_value, current_city, path_taken)
        open_list = [(self.heuristics[start], start, [start])]
        closed_list = set()

        while open_list:
            # Sorts automatically by the 1st item in the tuple (heuristic_value)
            open_list.sort()
            h, current, path = open_list.pop(0)

            if current == goal:
                return path

            if current in closed_list:
                continue
            closed_list.add(current)

            for neighbor in self.graph.get(current, {}):
                if neighbor not in closed_list:
                    new_h = self.heuristics[neighbor]
                    open_list.append((new_h, neighbor, path + [neighbor]))

        return None

if __name__ == "__main__":
    romania_map = {
        'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
        'Zerind': {'Arad': 75, 'Oradea': 71},
        'Oradea': {'Zerind': 71, 'Sibiu': 151},
        'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
        'Timisoara': {'Arad': 118, 'Lugoj': 111},
        'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
        'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
        'Drobeta': {'Mehadia': 75, 'Craiova': 120},
        'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
        'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
        'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
        'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
        'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
        'Giurgiu': {'Bucharest': 90},
        'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
        'Hirsova': {'Urziceni': 98, 'Eforie': 86},
        'Eforie': {'Hirsova': 86},
        'Vaslui': {'Urziceni': 142, 'Iasi': 92},
        'Iasi': {'Vaslui': 92, 'Neamt': 87},
        'Neamt': {'Iasi': 87}
    }

    sld_to_bucharest = {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
        'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
        'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
        'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
        'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
    }

    gbfs = GreedyBestFirstSearch(romania_map, sld_to_bucharest)
    path = gbfs.search('Arad', 'Bucharest')
    print("Greedy Best-First Path:", " -> ".join(path))    

# ========================================================================================================
# ============================================A* Search=============================================

class AStarSearch:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics

    def search(self, start, goal):
        # Tuple format: (f_cost, g_cost, current_city, path_taken)
        start_f = self.heuristics[start]
        open_list = [(start_f, 0, start, [start])]
        closed_list = {}  # Stores {city: best_g_cost_found}

        while open_list:
            # Sorts automatically by the 1st item in the tuple (f_cost)
            open_list.sort()
            f, g, current, path = open_list.pop(0)

            if current == goal:
                return path, g

            # Skip if we already found a cheaper or equal path to this city
            if current in closed_list and closed_list[current] <= g:
                continue
            closed_list[current] = g

            for neighbor, step_cost in self.graph.get(current, {}).items():
                new_g = g + step_cost
                # Only add to open_list if it's unvisited or we found a shorter path
                if neighbor not in closed_list or new_g < closed_list[neighbor]:
                    new_f = new_g + self.heuristics[neighbor]
                    open_list.append((new_f, new_g, neighbor, path + [neighbor]))

        return None, float('inf')

if __name__ == "__main__":
    romania_map = {
        'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
        'Zerind': {'Arad': 75, 'Oradea': 71},
        'Oradea': {'Zerind': 71, 'Sibiu': 151},
        'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
        'Timisoara': {'Arad': 118, 'Lugoj': 111},
        'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
        'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
        'Drobeta': {'Mehadia': 75, 'Craiova': 120},
        'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
        'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
        'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
        'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
        'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
        'Giurgiu': {'Bucharest': 90},
        'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
        'Hirsova': {'Urziceni': 98, 'Eforie': 86},
        'Eforie': {'Hirsova': 86},
        'Vaslui': {'Urziceni': 142, 'Iasi': 92},
        'Iasi': {'Vaslui': 92, 'Neamt': 87},
        'Neamt': {'Iasi': 87}
    }

    sld_to_bucharest = {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
        'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
        'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
        'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253,
        'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
    }

    astar = AStarSearch(romania_map, sld_to_bucharest)
    path, total_cost = astar.search('Arad', 'Bucharest')
    print("A* Optimal Path:", " -> ".join(path))
    print("Total Cost:", total_cost)

    # ===================================================================
class EightPuzzleAStar:
    def __init__(self, start_board, goal_board):
        self.start = start_board
        self.goal = goal_board

    def heuristic(self, board):
        """Counts the number of misplaced tiles (excluding the blank space ' ')."""
        misplaced = 0
        for r in range(3):
            for c in range(3):
                if board[r][c] != " " and board[r][c] != self.goal[r][c]:
                    misplaced += 1
        return misplaced

    def find_blank(self, board):
        """Finds the (row, col) position of the blank space ' '."""
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    return r, c

    def get_neighbors(self, board):

        neighbors = []
        r, c = self.find_blank(board)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_board = [row[:] for row in board]
                new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
                neighbors.append(new_board)

        return neighbors

    def solve(self):
        start_h = self.heuristic(self.start)
        # Tuple format: (f_cost, g_cost, board, path_of_boards)
        open_list = [(start_h, 0, self.start, [self.start])]
        closed_set = set()

        while open_list:
            # Sorts cleanly by f_cost (index 0) because all board elements are strings
            open_list.sort()
            f, g, current_board, path = open_list.pop(0)

            if current_board == self.goal:
                return path

            board_tuple = tuple(tuple(row) for row in current_board)
            if board_tuple in closed_set:
                continue
            closed_set.add(board_tuple)

            for next_board in self.get_neighbors(current_board):
                next_tuple = tuple(tuple(row) for row in next_board)
                if next_tuple not in closed_set:
                    new_g = g + 1
                    new_h = self.heuristic(next_board)
                    new_f = new_g + new_h
                    open_list.append((new_f, new_g, next_board, path + [next_board]))

        return None

    def display_board(self, board):
        for row in board:
            print(" ".join(row))
        print()

if __name__ == "__main__":
    initial_state = [
        ["1", "2", "3"],
        ["5", "6", " "],
        ["7", "8", "4"]
    ]

    final_state = [
        ["1", "2", "3"],
        ["5", "8", "6"],
        [" ", "7", "4"]
    ]

    solver = EightPuzzleAStar(initial_state, final_state)
    solution_steps = solver.solve()

    if solution_steps:
        print(f"Goal reached in {len(solution_steps) - 1} moves:\n")
        for step, grid in enumerate(solution_steps):
            print(f"Step {step}:")
            solver.display_board(grid)
    else:
        print("No solution found.")