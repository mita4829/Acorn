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

def isint(n):
    try:
        int(n)
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
        elif(isfloat(self.current) or  isint(self.current) or (self.current == '-') or (self.current in self.MemoryState.variableNames)):
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
        elif(self.current == "stdin"):
            self.next()
            self.next()
            return Foundation.Input()
        elif(self.current == "for"):
            self.next()
            self.next()
            return self.forEach_grammar()
        elif(self.current == '['):
            self.next()
            return self.array_grammar()
        elif(type(self.current) == str):
            val = Foundation.S(self.current[1:-1])
            self.next() #)
            return val
        else:
            print("Acorn: This is embarrassing, there seems to be a problem with the tokenizer. Please report your code to help fix this issue")
            exit()
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

    def array_grammar(self):
        array = []
        while(self.current != ']' and self.current != ';'):
            if(self.current != ','):
                v = self.logical_grammar()
                array.append(v)
            self.next()
        self.next()
        self.next()
        self.next()
        return Foundation.Array(array)

    def forEach_grammar(self):
        indexVar = self.current
        self.MemoryState.variableNames.append(indexVar)
        self.next()#=
        self.next()
        start = self.factor_grammar()
        closure = self.current
        self.next()
        end = self.factor_grammar()
        self.next()
        self.next()
        scope = self.grammar()
        #check for more of if statement body
        while(self.current != '}'):
            scope = Foundation.Seq(scope,self.grammar())
        self.MemoryState.variableNames.remove(indexVar)
        return Foundation.ForEach(indexVar,start,end,scope,closure)
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
        while(self.current in ["<=","==",">=","!=",'<','>','=']):
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
            elif(self.current == "="):
                self.next()
                result = Foundation.Assign(result,self.number_grammar())
        return result

    def number_grammar(self):
        result = self.term_grammar()
        while(self.current in ['+','-']):
            if(self.current == '+'):
                self.next()
                result = Foundation.Binary("Plus",result,self.grammar())
            elif(self.current == '-' and isinstance(result,Foundation.Null)):
                self.next()
                result = Foundation.Unary("Neg",self.grammar())
            elif(self.current == '-'):
                self.next()
                result = Foundation.Binary("Minus",result,self.grammar())
        return result

    def term_grammar(self):
        result = self.factor_grammar()
        while(self.current in ['*','/','(']):
            if(self.current == '*'):
                self.next()
                result = Foundation.Binary("Times",result,self.grammar())
            elif(self.current == '/'):
                self.next()
                result = Foundation.Binary("Div",result,self.grammar())
            elif(self.current == '('):
                arg = Foundation.Null()
                self.next()
                if(self.current != ')'):
                    arg = self.grammar()
                result = Foundation.Call(arg,result)
        return result

    def factor_grammar(self):
        result = Foundation.Null()
        if(isfloat(self.current) or isint(self.current)):
            result = Foundation.N(self.current)
            self.next()
        elif(self.current in self.MemoryState.variableNames):
            result = Foundation.Var(self.current)
            self.next()#Work here to detect array indexing
            if(self.current == '['):
                self.next()
                if(self.current != ']'):
                    i = self.number_grammar()
                    if(not isinstance(i,Foundation.N) and (not isinstance(i,Foundation.Binary)) and (not isinstance(i,Foundation.Var))):
                        exit("Acorn: Array index expected integer")
                    if(self.current != ']'):
                        exit("Acorn: Expected termination of bracket with array")
                    self.next()
                    result = Foundation.Index(result,i)
                else:
                    exit("Acorn: Array index cannot be empty")
        else:
            result = Foundation.S(self.current[1:-1])
            self.next()
        return result
