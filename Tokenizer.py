import Foundation

parsedTokens = []
def tokenizer(array):
    for i in range(0,len(array)):
        parsedTokens.append(grammar(array[i]))

    return parsedTokens

def isfloat(n):
    try:
        float(n)
        return True
    except:
        return False

def grammar(array):
    for i in range(0,len(array)):
        token = array[i]
        if(token == "print"):
            return print_grammar(array[1:])
        elif(token == '('):
            return grammar(array[1:])
        elif(isfloat(token)):
            return number_grammer(array)
        elif(type(token)==str):
            #Return S object with removed quotes
            return Foundation.S(token[1:-1])

def print_grammar(array):
    return Foundation.Print(grammar(array[1:]))
def number_grammer(array):
    result = term_grammar(array)
    if(array[1] == '+'):
        result = Foundation.Binary("Plus",result,term_grammar(array[2:]))
    elif(array[1] == '-'):
        result = Foundation.Binary("Minus",result,term_grammar(array[2:]))
    return result
def term_grammar(array):
    result = factor_grammar(array)
    if(array[1] == '*'):
        result = Foundation.Binary("Times",result,term_grammar(array[2:]))
    elif(array[1] == '/'):
        result = Foundation.Binary("Div",result,term_grammar(array[2:]))
    return result
def factor_grammar(array):
    return Foundation.N(array[0])

#tokenizer([['5','+','5',';']])
#print(parsedTokens)
