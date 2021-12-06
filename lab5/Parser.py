class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.grammar.addProduct("S\'", self.grammar.getInitialNonterminal())
        self.augment_grammar()
        self.grammar.setInitialNonterminal("S\'")
        print(self.grammar.getProductions()["S\'"][0])

    def augment_grammar(self):
        self.grammar.getProductions()['S\''] = self.grammar.getInitialNonterminal()
        for non_terminal in self.grammar.getProductions():
            for production in self.grammar.getProductions()[non_terminal]:
                self.grammar.setProductions(non_terminal, ". " + production,
                                            self.grammar.getProductions()[non_terminal].index(production))
        print(self.grammar.getProductions())

    def closure(self, i):
        C = [i]
        while True:
            lenC = len(C)
            for elem in C:
                for key in elem.keys():
                    for production in elem[key]:
                        condition, nonterminal = self.check_dot_before_nonTerminal(production)
                        if condition:
                            for productions in self.grammar.getProductions()[nonterminal]:
                                if productions not in C:
                                    C.append(productions)
            if lenC == len(C):
                break
        return C

    def check_dot_before_nonTerminal(self,s):
        dot_index = s.find(".")
        nonterminal = s[dot_index+2: ].split(" ")[0]
        if nonterminal in self.grammar.getNonterminals():
            return True, nonterminal
        return False, None

    def canonical_colection(self):
        C = []
        s0 = self.closure({self.grammar.getInitialNonterminal():
                               self.grammar.getProductions()[self.grammar.getInitialNonterminal()][0]})
        C.append(s0)
        while True:
            lenC = len(C)
            for state in C:
                for x in self.grammar.getNonterminals():
                    gt = self.goTo(state, x)
                    if gt != [] and gt not in C:
                        C.append(gt)
                for x in self.grammar.getTerminals():
                    gt = self.goTo(state, x)
                    if gt != [] and gt not in C:
                        C.append(gt)

            if len(C) == lenC:
                break

    def goTo(self, state, x):
        gt = []
        print("State")
        print(state)
        for productions in state:
            for nonterminal in productions.keys():
                for production in productions[nonterminal]:
                    dot_index = production.find(".")
                    if production[dot_index+2: ].split(" ")[0] == x:
                        gt.append(self.closure(production))
        return gt