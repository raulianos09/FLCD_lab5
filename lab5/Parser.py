class Production:
    def __init__(self, lhs, rhs, dot=0):
        self.lhs = lhs
        self.rhs = rhs.strip().split(" ")
        self.dot = dot  # dot position
        # ex: S -> *aSbS =====> lhs = S, rhs = [a,S,b,S], dot = 0
    def __eq__(self, other):
        return self.rhs == other.rhs and self.lhs == other.lhs and self.dot == other.dot

    def __str__(self) -> str:
        rhs = ""
        for letter in self.rhs[:self.dot]:
            rhs += letter
        rhs += "."
        for letter in self.rhs[self.dot:]:
            rhs += letter

        return "Production: {} -> {}".format(self.lhs,rhs)


class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.productions = []
        self.augment_grammar()

    def augment_grammar(self):
        self.grammar.getProductions()['S\''] = self.grammar.getInitialNonterminal()
        for non_terminal in self.grammar.getProductions():
            for production in self.grammar.getProductions()[non_terminal]:
                self.productions.append(Production(non_terminal, production))
        self.grammar.setInitialNonterminal("S\'")

    def canonical_colection(self):
        colection = []
        s0 = self.closure(Production("S\'", "S"))
        colection = [s0]
        while True:
            lenC = len(colection)
            for s in colection:
                for prod in s:
                    for x in self.grammar.getNonterminals():
                        if x in prod.rhs:
                            gt = self.goTo(s, x)
                            if len(gt) > 0 and gt not in colection:
                                colection.append(gt)
                    for x in self.grammar.getTerminals():
                        if x in prod.rhs:
                            gt = self.goTo(s, x)
                            if len(gt) > 0 and gt not in colection:
                                colection.append(gt)
            if len(colection) == lenC:
                break
        return colection

    def closure(self, item):
        closure = [item]
        while True:
            lenC = len(closure)
            for production in closure:
                if production.rhs[production.dot] in self.grammar.getNonterminals():
                    for p in self.grammar.getProductionsForNonterminal(production.rhs[production.dot]):
                        newProd = Production(production.rhs[production.dot], p)
                        if newProd not in closure:
                            closure.append(newProd)
            if len(closure) == lenC:
                break
        return closure

    def goTo(self, s, x):
        gt = []
        for prod in s:
            if x in prod.rhs:
                if prod.rhs.index(x) == prod.dot:
                    if prod.dot + 1 < len(prod.rhs):
                        prod.dot += 1
                        gt = self.closure(prod)
        return gt
