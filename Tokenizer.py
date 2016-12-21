import Foundation
import Memory

from sys import exit
#Helper function
def isfloat(n):
    try:
        float(n)
        return True
    except:
        return False

class Tokenizer():
    def __init__(self,array,Mem):
        self.tokens = array
        self.current = self.tokens[0] if len(self.tokens) > 0 else None
        self.parsedTokens = []
        self.MemoryState = Mem
    def next(self):
        self.tokens = self.tokens[1:]
        self.current = self.tokens[0] if len(self.tokens) > 0 else None

    def grammar(self):
        result = Foundation.Null()
        if(self.current == "print"):
            self.next()
            result = self.print_grammar()
            self.next()
            self.next()
        elif(self.current == "if"):
            self.next()
            result = self.if_grammar()
        elif(isfloat(self.current) or (self.current == '-') or (self.current in self.MemoryState.variableNames)):
            return self.logical_grammar()
        elif(self.current == "true" or self.current == "false"):
            return Foundation.B(self.current)
        elif(self.current == "var" or self.current == "const"):
            self.next()
            result = self.malloc_grammar()
        elif(self.current == "function"):
            self.next()
            result = self.function_grammar()
        elif(self.current == "return"):
            self.next()
            if(self.current == ';'):
                return Foundation.Return(Foundation.Null())
            return Foundation.Return(self.grammar())
        elif(self.current == "gets"):
            self.next()
            self.next()
            return Foundation.Input()
        elif(self.current == '}'):
            return
        elif(type(self.current) == str):
            val = Foundation.S(self.current[1:-1])
            self.next() #)
            return val
        else:
            if(len(self.tokens) > 0):
                self.next()
                self.grammar()

        return result

    def print_grammar(self):
        self.next()
        return Foundation.Print(self.grammar())
    def if_grammar(self):
        self.next() #bool
        e1 = self.grammar()
        self.next() #)
        self.next() #{
        e2 = self.grammar()
        #check for more of if statement body
        while(self.current != '}'):
            e2 = Foundation.Seq(e2,self.grammar())
        self.next() #}
        if(self.current == "else"):
            self.next() #{
            self.next() #next expr
            e3 = self.grammar()
            while(self.current != '}'):
                e3 = Foundation.Seq(e3,self.grammar())
            self.next() #}
            self.next() #;
            self.next()
            return Foundation.If(e1,e2,e3)
        return Foundation.If(e1,e2,Foundation.Null())

    def malloc_grammar(self):
        x = Foundation.Var(self.current)
        self.MemoryState.variableNames.append(self.current)
        self.next()
        if(self.current != '='):
            exit("Acorn: Variable must be seeded with value.")
        self.next()
        v = self.grammar()
        return Foundation.Malloc("Var",x,v)

    def function_grammar(self):
        self.next()
        arg = Foundation.Null()
        if(self.current != ')'):
            arg = Foundation.Var(self.current)
            self.MemoryState.variableNames.append(self.current)
            self.next()
        self.next()
        self.next() #{
        body = self.grammar()
        while(self.current != '}'):
            body = Foundation.Seq(body,self.grammar())
        self.next() #;
        self.next() #None
        return Foundation.Function(arg,body)


    def logical_grammar(self):
        result = self.number_grammar()
        while(self.current in ["<=","==",">=","!=",'<','>']):
            if(self.current == '<'):
                self.next()
                result = Foundation.Lt(result,self.number_grammar())
            elif(self.current == "<="):
                self.next()
                result = Foundation.Le(result,self.number_grammar())
            elif(self.current == "=="):
                self.next()
                result = Foundation.Eq(result,self.number_grammar())
            elif(self.current == ">="):
                self.next()
                result = Foundation.Ge(result,self.number_grammar())
            elif(self.current == ">"):
                self.next()
                result = Foundation.Gt(result,self.number_grammar())
            elif(self.current == "!="):
                self.next()
                result = Foundation.Ne(result,self.number_grammar())
        return result

    def number_grammar(self):
        result = self.term_grammar()
        while(self.current in ['+','-']):
            if(self.current == '+'):
                self.next()
                result = Foundation.Binary("Plus",result,self.term_grammar())
            elif(self.current == '-' and isinstance(result,Foundation.Null)):
                self.next()
                result = Foundation.Unary("Neg",self.term_grammar())
            elif(self.current == '-'):
                self.next()
                result = Foundation.Binary("Minus",result,self.term_grammar())
        return result

    def term_grammar(self):
        result = self.factor_grammar()
        while(self.current in ['*','/','(']):
            if(self.current == '*'):
                self.next()
                result = Foundation.Binary("Times",result,self.logical_grammar())
            elif(self.current == '/'):
                self.next()
                result = Foundation.Binary("Div",result,self.logical_grammar())
            elif(self.current == '('):
                arg = Foundation.Null()
                self.next()
                if(self.current != ')'):
                    arg = self.grammar()
                result = Foundation.Call(arg,result)
        return result

    def factor_grammar(self):
        result = Foundation.Null()
        if(isfloat(self.current)):
            result = Foundation.N(self.current)
            self.next()
        elif(self.current in self.MemoryState.variableNames):
            result = Foundation.Var(self.current)
            self.next()
        return result
