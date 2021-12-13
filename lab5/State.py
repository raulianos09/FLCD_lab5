class State:
    def __init__(self):
        # state = list of productions
        self.state = []

    def addToState(self, production):
        if production not in self.state:
            self.state.append(production)

    def getState(self):
        return self.state