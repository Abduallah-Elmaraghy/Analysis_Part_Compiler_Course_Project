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
                if(char == "~"): # after ~ char is the right rhs
                    self.__flag = (self.__flag+1)%2 # change the flag to enter the else
                    # line = line.replace(keyword, ":")
                    continue
                if(self.__flag == 1):
                    self.__lhs += char
                else:
                    self.__rhs += char
            # get the grammer in the first line
            self.__grammar = self.grammar_util(self.__grammar, self.__lhs, self.__rhs) 
            self.__grammar_first[self.__lhs] = "null"
            self.__grammar_follow[self.__lhs] = "null"

        print("Grammar\n")    
        self.show_grammar(self.__grammar)
        for self.__lhs in self.__grammar:
            if(self.__grammar_first[self.__lhs] == "null"):
                self.__grammar_first = self.first_set(self.__lhs)
        print("\n\n\n")

        print("First Set\n")
        self.show_grammar(self.__grammar_first)

    '''Build a function that helps in :
    1) grammar reading
    2) grouping the implies of the key
    3) first set
    4) follow set
    '''
    def grammar_util(self, grammar, lhs, rhs):
        if(lhs in grammar and rhs not in grammar[lhs] and grammar[lhs] != "null"):
            grammar[lhs].append(rhs)
        elif(self.__lhs not in grammar or grammar[lhs] == "null"):
            grammar[lhs] = [rhs]
        return grammar

    '''Display the grammar'''
    def show_grammar(self, grammar):
        # print(self.__grammar)
        for key in grammar.keys():
            print(key + " : ", end = "")
            for value in  grammar[key]:
                if(value == "`"):
                    print("Epsilon, ", end="")
                else:
                    print(value + ", ", end="")
            print("\b\b")

    '''Firstset'''
    def first_set(self, lhs):
        self.__rhs = self.__grammar[lhs]
        for block in self.__rhs:
            k = 0
            flag = 0
            current = []
            confirm = 0
            flog = 0
            if(lhs in self.__grammar and "`" in self.__grammar[lhs]):
                flog = 1
            while(True):
                check = []
                if(k >= len(block)):
                    if(len(current)==0 or flag == 1 or confirm == k or flog == 1):
                        self.__grammar_first = self.grammar_util(self.__grammar_first, lhs, "`")
                    break	
                if(block[k].isupper()):
                    if(self.__grammar_first[block[k]] == "null"):
                        self.__grammar_first = self.first_set(block[k])
                    for j in self.__grammar_first[block[k]]:
                        self.__grammar_first = self.grammar_util(self.__grammar_first, lhs, j)
                        check.append(j)
                else: 
                    self.__grammar_first = self.grammar_util(self.__grammar_first, lhs, block[k])
                    check.append(block[k])
                if(block[k]=="`"):
                    flag = 1
                current.extend(check)
                if("`" not in check):
                    if(flog == 1):
                        self.__grammar_first = self.grammar_util(self.__grammar_first, lhs, "`")
                    break
                else:
                    confirm += 1
                    k+=1
                    self.__grammar_first[lhs].remove("`")
        return(self.__grammar_first)

       