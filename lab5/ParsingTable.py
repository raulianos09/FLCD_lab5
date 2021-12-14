from Parser import Parser, Production
from State import State
from prettytable import PrettyTable


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
            i = i + 1
        self.literals = grammar.getNonterminals()
        self.literals.extend(grammar.getTerminals())
        self.table = []


    def isAlreadyAState(self, newState):
        for index in range(len(self.states)):
            if self.states[index] == newState:
                return index
        return -1


    def findProductionInGrammar(self, production):
        productionToFind = production.lhs + " = " + str(production.rhs[:-1])
        if productionToFind in self.grammar.getProductionsNumbers().keys():
            return self.grammar.getProductionsNumbers()[productionToFind]
        return -1


    def constructParsingTable(self):
        for state in self.states:
            row = ["-" for literal in self.literals]
            row.append("-")
            self.table.append(row)
            for production in state.getProductions():
                action, literal = self.action(production)
                if action != first_action:
                    print(first_action + "-" + action + " conflict on state s" + str(state))
                    return
                first_action = action
                row[0] = action
                if action == "shift":
                    newState = State(79)
                    newState.setProductions(self.parser.goTo(state.getProductions(), literal))
                    if newState.getProductions():
                        index = self.isAlreadyAState(newState)
                        row[int(self.literals.index(literal)) + 1] = index
                if action == "reduce":
                    reduceToIndex = self.findProductionInGrammar(production)
                    row[0] += str(reduceToIndex)


    def action(self, production):
        if production == Production("S\'", ["S", "."]):
            return "acc", None

        index_dot = production.rhs.index(".")
        if 0 <= index_dot < len(production.rhs) - 1:
            return "shift", production.rhs[index_dot + 1]

        if production.rhs[len(production.rhs) - 1] == ".":
            return "reduce", None

        return "error", None

    def print_states(self):
        toPrint = ""
        for state in self.states:
            toPrint += str(state) + "\n"
        print(toPrint)

    def printTable(self):
        tableHeader = [" ", "Action"]
        for literal in self.literals:
            tableHeader.append(literal)
        t = PrettyTable(tableHeader)
        index = 0
        for i in self.table:
            row = ["s" + str(index)]
            index += 1
            for j in i:
                row.append(j)
            t.add_row(row)

        print(t)
