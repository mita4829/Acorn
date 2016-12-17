import Foundation
from sys import exit
#Helper function
def isfloat(n):
    try:
        float(n)
        return True
    except:
        return False

class Tokenizer():
    def __init__(self,array):
        self.tokens = array
        self.current = self.tokens[0] if len(self.tokens) > 0 else None
        self.parsedTokens = []
    def next(self):
        self.tokens = self.tokens[1:]
        self.current = self.tokens[0] if len(self.tokens) > 0 else None

    def grammar(self):
        if(self.current == "print"):
            self.next()
            self.parsedTokens.append(self.print_grammar())
        elif(isfloat(self.current)):
            return self.number_grammar()
        elif(type(self.current) == str):
            return Foundation.S(self.current[1:-1])

        return self.parsedTokens

    def print_grammar(self):
        self.next()
        return Foundation.Print(self.grammar())
    def number_grammar(self):
        result = self.term_grammar()
        while(self.current in ['+','-']):
            if(self.current == '+'):
                self.next()
                result = Foundation.Binary("Plus",result,self.term_grammar())
            elif(self.current == '-'):
                self.next()
                result = Foundation.Binary("Minus",result,self.term_grammar())
        return result
        
    def term_grammar(self):
        result = self.factor_grammar()
        while(self.current in ['*','/']):
            if(self.current == '*'):
                self.next()
                result = Foundation.Binary("Times",result,self.factor_grammar())
            elif(self.current == '/'):
                self.next()
                result = Foundation.Binary("Div",result,self.factor_grammar())
        return result

    def factor_grammar(self):
        result = Foundation.Null()
        if(isfloat(self.current)):
            result = Foundation.N(self.current)
            self.next()
        elif(self.current == '('):
            self.next()
            result = self.number_grammar()
            self.next()

        return result
