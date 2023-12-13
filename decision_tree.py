# from decision_tree import build_decision_tree, bfs, DecisionNode
class DecisionNode:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value  # This could represent score, energy cost, etc.
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def build_decision_tree():    
        # Create nodes
        start = DecisionNode("Start")
        move1 = DecisionNode("Dance Move 1", value=10)
        move2 = DecisionNode("Dance Move 2", value=15)
        rest = DecisionNode("Rest", value=-5)  # Negative value for resting (energy regain)

        # Build the tree
        start.add_child(move1)
        start.add_child(move2)
        move1.add_child(rest)  # After Move 1, the dancer can choose to rest
        move2.add_child(rest)  # Same for Move 2
    def bfs(start_node):
    # BFS traversal logic
    # ...
        pass
