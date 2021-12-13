import ParsingTable
from Grammar import Grammar
from Parser import Parser, Production


def printMenu():
    print()
    print("Menu:" + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Display set of nonterminals")
    print("2. Display the set of terminals")
    print("3. Display the set of productions")
    print("4. Display the set of productions for a given nonterminal")
    print("5. Check CFG")
    print("0. Exit menu")


if __name__ == '__main__':
    myGrammar = Grammar("g1.txt")
    myGrammar.readFromFile()
    print("Grammar is: \n" + str(myGrammar.getProductionsNumbers()) + "\n")
    myParser = Parser(myGrammar)
    myStates = myParser.col_can_LR0()
    myParsingTable = ParsingTable.ParsingTable(myGrammar, myParser, myStates)
    print("States are:")
    myParsingTable.print_states()

    while True:
        printMenu()
        operation = int(input("Please enter a command:\n"))
        if operation == 0:
            exit(0)
        if operation == 1:
            print("The set of nonterminals is: ", myGrammar.getNonterminals())
        if operation == 2:
            print("The set of terminals is: ", myGrammar.getTerminals())
        if operation == 3:
            print("The set of productions is: ", myGrammar.getProductions())
        if operation == 4:
            nonterminal = input("nonterminal = ")
            print("The productions for nonterminal '", nonterminal, "' is: ",
                  myGrammar.getProductionsForNonterminal(nonterminal))
        if operation == 5:
            if myGrammar.checkCFG():
                print("The given grammar is Context Free")
            else:
                print("The given grammar is not Context Free")
        if operation not in range(0, 6):
            print("Inexistent command")
