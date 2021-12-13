from Parser import Parser
from State import State


class ParsingTable:
    def __init__(self, grammar, parser, states):
        self.grammar = grammar
        self.parser = parser
        self.states = []
        i = 0
        for s in states:
            state = State(i)
            for prod in s:
                state.addToState(prod)
            self.states.append(state)
            i = i+1
        self.table = []

    def get_actions(self):
        for state in self.states:
            pass

    def action(self,state):
        for production in state:
            cond, nonterminal = self.parser.dot_before_nonterminal(production)
            if cond is True:
                return "shift"
            cond,nonterminal = self.parser.dot_after_nonterminal(production)
            if nonterminal != "S\'":
                return "reduce " + self.states.index(state)
            else:
                return "acc"
        return "error"

    def print_states(self):
        toPrint = ""
        for state in self.states:
            toPrint += str(state) + "\n"
        print(toPrint)