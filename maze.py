#Problem 1 (please check graph image for reference)
#Given the following maze write a Python program that finds a path from S to G. 
#For that you need to represent the problem (state space, actions) as a graph and apply BFS (or DFS) to find the solution for the maze.
steps = {
    "S": ["A"],
    "A": ["B"],
    "B": ["C"],
    "C": ["D", "E"],
    "D": [],
    "E": ['F', 'H', 'Q'],
    'Q': ['R'],
    'R': ['T'],
    'T': ['U'],
    'U': ['V'],
    'V': ['W'],
    'W': ['G'],
    'G': [],
    'X': ['Y', 'W'],
    'Y': [],
    'F': [],
    'H': ['I'],
    'I': ['J'],
    'J': ['K'],
    'K': ['L'],
    'O': ['P'],
    'L': ['M', 'N'],
    'M': [],
    'N': ['O', 'X'],
    'Z': ['W']
}

def bfs(steps, start, target):
    visited = set()
    queue = [start]

    while queue:
        current_node = queue.pop(0)

        if current_node == target:
            print("Reached target:", target)
            break

        visited.add(current_node)
        print("Visited:", current_node)

        neighbors = [neighbor for neighbor in steps[current_node] if neighbor not in visited and neighbor not in queue]
        queue.extend(neighbors)
        print("Added neighbors:", neighbors)

#Run BFS
start_node = "S"
target_node = "G"
bfs(steps, start_node, target_node)
