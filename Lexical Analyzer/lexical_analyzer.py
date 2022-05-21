import re

program  ='''int var1 = 05 + 10.512'''

tokens = []
lexemes = []

operators = {'=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op','/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
operators_key = operators.keys()

data_type = {'int' : 'Datatype', 'double ' : 'Datatype', 'string ' : 'Datatype' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma', '{}' : 'Statement delimiter','[]' : 'Array delimiter',',' : 'Argument list separator',':' : 'Statement label'}
punctuation_symbol_key = punctuation_symbol.keys()
print(program)
lines = program.split("\n")
for line in lines:
    lexems = line.split(' ')
    for token in lexems:
        lexemes.append(token)
        if token in operators_key:
            tokens.append(operators[token])
        elif token in data_type_key:
            tokens.append(data_type[token])
        elif token in punctuation_symbol_key:
            tokens.append(punctuation_symbol[token])
        elif re.match("^[_a-zA-Z][_a-zA-Z0-9]*$",token) and token not in data_type_key:
            tokens.append("Identifier")
        elif re.match("^(-?)([_1-9][_0-9]*)$",token):
            tokens.append("Integer")
        elif re.match("^(-?)(0|([1-9][0-9]*))(.[0-9]+)?$",token):
            tokens.append("Double")   
        else:
            tokens.append("Error")
    print("=================================")
    print("Lexeme\t\tToken")
    for i in range(0, len(lexemes)):
        print(lexemes[i],"\t\t", tokens[i]) 
    print("=================================")
