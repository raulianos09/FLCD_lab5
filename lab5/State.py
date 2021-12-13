class State:
    def __init__(self):
        self.state = []

    def addToState(self, prod):
        self.state.append(prod)

    def getState(self):
        return self.state