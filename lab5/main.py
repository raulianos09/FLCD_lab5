from Grammar import Grammar


def printMenu():
    print()
    print("Menu:" + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Display set of nonterminald")
    print("2. Display the set of terminals")
    print("3. Display the set of productions")
    print("4. Display the set of producitons for a given nonterninal")
    print("5. Check CFG")
    print("0. Exit menu")


if __name__ == '__main__':
    myGrammar = Grammar("g1.txt")
    myGrammar.readFromFile()

    while True:
        printMenu()
        operation = int(input("Please enter a command:\n"))
        if operation == 0:
            break
        if operation == 1:
            print(myGrammar.getNonterminals())
        if operation == 2:
            print(myGrammar.getTerminals())
        if operation == 3:
            print(myGrammar.getProductions())
        if operation == 4:
            nonterminal = input("nonterminal = ")
            print(myGrammar.getProductionsForNonterminal(nonterminal))
        if operation == 5:
            print(myGrammar.checkCFG())
        if operation not in range(0, 6):
            print("Inexistent command")
