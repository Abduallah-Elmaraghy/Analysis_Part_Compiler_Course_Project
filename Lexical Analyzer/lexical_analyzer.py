import re

string  ='''int var1 = 05 + 10.512'''

tokens = []
lexemes = []

operators = {'=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op','/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
operators_key = operators.keys()

data_type = {'int' : 'Datatype', 'double ' : 'Datatype', 'string ' : 'Datatype' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma', '{}' : 'Statement delimiter','[]' : 'Array delimiter',',' : 'Argument list separator',':' : 'Statement label'}
punctuation_symbol_key = punctuation_symbol.keys()

count=0
program = string.split("\n")
for line in program:
    count = count + 1
    print("line#" , count, "\n" , line)

    lexems = line.split(' ')
    print("Lexemes are " , lexems , "\n")

    print("Line#", count, "properties \n")
    for token in lexems:
        lexemes.append(token)
        if token in operators_key:
            print(token ,"operator is ", operators[token])
            tokens.append(operators[token])
        elif token in data_type_key:
            print(token, "datatype is ", data_type[token])
            tokens.append(data_type[token])
        elif token in punctuation_symbol_key:
            print (token, "Punctuation symbol is " , punctuation_symbol[token])
            tokens.append(punctuation_symbol[token])
        elif re.match("^[_a-zA-Z][_a-zA-Z0-9]*$",token) and token not in data_type_key:
            print(token, " is an identifier")
            tokens.append("identifier")
        elif re.match("^(-?)([_1-9][_0-9]*)$",token):
            print(token, " is an Integer Number")
            tokens.append("Integer")
        elif re.match("^(-?)(0|([1-9][0-9]*))(.[0-9]+)?$",token):
            print(token, " is a Double Number")
            tokens.append("Double")   
        else:
            print(token, "Error")
            tokens.append("Error")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _")
    print("=================================")
    print("Lexeme\t\tToken")
    for i in range(0, len(lexemes)):
        print(lexemes[i],"\t\t", tokens[i]) 
    print("============================================================================================")
