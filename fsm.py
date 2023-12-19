class FSM:
    def __init__(self, initial_state):
        # Dictionary (input_symbol, current_state) --> (action, next_state).
        self.state_transitions = {}
        self.current_state = initial_state
        self.direction = None

    def add_transition(self, num_points, state, direction, action=None, next_state=None):
        self.state_transitions[(num_points, state, direction)] = (action, next_state)


    def get_transition(self, num_points, state, direction):
        return self.state_transitions[(num_points, state, direction)]

    def process(self, num_points):
        my_tuple = self.get_transition(num_points, self.current_state, self.direction)
        
        action = my_tuple[0]
        next_state = my_tuple[1]
        if action:
            action()
        if next_state:
            self.current_state = next_state

    