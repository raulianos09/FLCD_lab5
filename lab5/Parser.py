from copy import deepcopy

class Production:
    def __init__(self, lhs, rhs):
        self.rhs = rhs
        self.lhs = lhs

    def __str__(self):
        return "Production: {} -> {}".format(self.lhs, "".join(self.rhs))

    def __hash__(self):
        return hash(self.lhs)

    def __eq__(self, other):
        return self.rhs == other.rhs and self.lhs == other.lhs

class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.productions = []
        self.augment_grammar()


    def augment_grammar(self):
        self.grammar.addProduct("S\'", "S")
        for non_terminal in self.grammar.getProductions():
            for production in self.grammar.getProductions()[non_terminal]:
                self.productions.append(Production(non_terminal, ["."] + production.strip().split()))
        self.grammar.setInitialNonterminal("S\'")

    def col_can_LR0(self):
        s0 = self.closure(Production("S\'", [".","S"]))
        C = [s0]
        copy_of_C = []
        while copy_of_C != C:
            copy_of_C = deepcopy(C)
            for state in C:
                for x in self.grammar.getAlphabet():
                    gt = self.goTo(state,x)
                    if gt != [] and gt not in C:
                        C.append(gt)
        return C


    def closure(self, item):
        closure = [item]
        closure_copy = []
        while closure_copy != closure:
            closure_copy = deepcopy(closure)
            for production in closure:
                condition, nonterminal = self.dot_before_nonterminal(production)
                if condition is True:
                    for p in self.grammar.getProductionsForNonterminal(nonterminal):
                        newProd = Production(nonterminal,["."] + p.strip().split(" "))
                        if newProd not in closure:
                            closure.append(newProd)
        return closure

    def goTo(self, state, x):
        gt = []
        for production in state:
            if self.dot_before_symbol(production,x):
                newProd = self.move_dot(production)
                c = self.closure(newProd)
                for p in c:
                    if p not in gt:
                        gt.append(p)
        return gt

    def dot_before_symbol(self,production,symbol):
        dot_index = production.rhs.index(".")
        if dot_index + 1 == len(production.rhs):
            return False
        if production.rhs[dot_index + 1] == symbol:
            return True
        return False

    def dot_before_nonterminal(self, production):
        dot_index = production.rhs.index(".")
        if dot_index + 1 == len(production.rhs):
            return False, None
        if production.rhs[dot_index + 1] in self.grammar.getNonterminals():
            return True, production.rhs[dot_index + 1]
        return False, None

    def move_dot(self, production):
        dot_index = production.rhs.index(".")
        return Production(production.lhs, list(production.rhs[:dot_index]) + list(production.rhs[dot_index + 1]) + list(["."]) + list(production.rhs[dot_index+2:]))
