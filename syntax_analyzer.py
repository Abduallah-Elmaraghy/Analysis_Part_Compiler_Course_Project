from collections import OrderedDict

class SyntaxAnalyzer:

    __file = open('grammar.txt')
    # left hand side 
    __lhs = None
    # right hand side
    __rhs = None
    # flag to separate the lhs from the rhs
    __flag = None
    # save the order of the original grammer
    __grammar = OrderedDict()
    # first set
    __grammar_first = OrderedDict()
    # follow set
    __grammar_follow = OrderedDict()


    '''
    Build a constructor to read the grammer from a text file
    '''
    def __init__(self):
        for line in self.__file:
            line = line.replace("\n", "")
            self.__lhs = ""
            self.__rhs = ""
            self.__flag = 1
            for char in line:
                if(char == "~"): # after this keyword is the right rhs
                    self.__flag = (self.__flag+1)%2 # change the flag to enter the else
                    # line = line.replace(keyword, ":")
                    continue
                if(self.__flag == 1):
                    self.__lhs += char
                else:
                    self.__rhs += char
            # get the grammer in the first line
            self.__grammar = self.grammer_util() 
            self.__grammar_first[self.__lhs] = "null"
            self.__grammar_follow[self.__lhs] = "null"
        self.show_grammar()
            # print(self.__grammar)

    def grammer_util(self):
        if(self.__lhs in self.__grammar and self.__rhs not in self.__grammar[self.__lhs] and self.__grammar[self.__lhs] != "null"):
            self.__grammar[self.__lhs].append(self.__rhs)
        elif(self.__lhs not in self.__grammar or self.__grammar[self.__lhs] == "null"):
            self.__grammar[self.__lhs] = [self.__rhs]
        return self.__grammar

    def show_grammar(self):
        # print(self.__grammar)
        for key in self.__grammar.keys():
            print(key + " : ", end = "")
            for value in  self.__grammar[key]:
                if(value == "`"):
                    print("Epsilon, ", end="")
                else:
                    print(value + ", ", end="")
            print("\b\b")