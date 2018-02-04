import Foundation
import Memory

WHITE = "\x1B[0m"
RED = "\x1B[31m"
MAGENTA = "\x1B[35m"
YELLOW = "\x1B[33m"
GREEN = "\x1B[32m"
CYAN = "\x1B[36m"

# Acorn: Cocoa Butter. Alpha 2.0 lexer
# Address incomplete parsing of dangling lexems
# New design of lexer from scratch to minimize undefined behavior and ease when refactoring
# More extensive error checking of invalid passed-in code
# All grammar functions will self complete its statement before moving onto next statement

#What's new in features
#else if statements
#Lexical scoping
#const has been deprecated
#Boolean operators
#


from sys import exit
#Helper function
def isfloat(n):
    try:
        float(n)
        return True
    except:
        return False

#Helper function
def isint(n):
    try:
        int(n)
        return True
    except:
        return False

#Helper function
def ishex(n):
    try:
        int(n,16)
        return True
    except:
        return False

def isstr(str):
    if(str[0] == '"' and str[-1] == '"'):
        return True
    return False

def cAssert(current,c,errorMsg):
    if(current == c):
        return True
    else:
        print(YELLOW+"Error: Parser expected "+str(c)+" instead recieved "+WHITE+str(current))
        print(YELLOW+errorMsg+WHITE)
        exit()

def cNotAssert(current, c, errorMsg):
    if(current != c):
        return True
    else:
        print("Error: Parser expected "+str(c)+" instead recieved "+str(current))
        print(errorMsg)
        exit()

class Tokenizer():
    def __init__(self,array,Mem):
        self.tokens = array
        self.current = self.tokens[0] if len(self.tokens) > 0 else None
        self.parsedTokens = []
        self.MemoryState = Mem
        self.i = 0
    def next(self):
        self.i = self.i + 1
        if(self.i < len(self.tokens)):
            self.current = self.tokens[self.i]
        else:
            print("End of tokens")
            self.current = None
    #Define backtrack, usage may lead to infinate loops due to left recursion. Usage needed due to nature of the implementation of arithmetic parsing.
    def back(self):
        self.i = self.i - 1
        if(self >= 0):
            self.current = self.tokens[self.i]
        else:
            print("Unable to backtrack")
            self.current = None


    #grammar returns a Founation object
    def grammar(self):
        result = Foundation.Null()
        #Syscall type tokens
        if(self.current in ["print","stdin","println"]):
            if(self.current == "print"):
                self.next()
                rtn = self.print_grammar()
                return rtn
            elif(self.current == "println"):
                self.next()
                rtn = self.println_grammar()
                return rtn
            elif(self.current == "stdin"):
                self.next()
                rtn = self.stdin_grammar()
                return rtn
        #Conditional statement
        elif(self.current in ["if"]):
            if(self.current == "if"):
                self.next()
                rtn = self.if_grammar()
                return rtn
        #Memory
        elif(self.current in ["var"]):
            rtn = self.malloc_grammar()
            return rtn
        
        #Functions
        elif(self.current in ["function"]):
            self.next()
            rtn = self.function_grammar()
            return rtn

        #Foreach
        elif(self.current == "foreach"):
            self.next()
            return self.forEach_grammar()
        
        elif(self.current == "for"):
            self.next()
            return self.for_grammar()
        
        elif(self.current == "while"):
            self.next()
            return self.while_grammar()

        #Return
        elif(self.current == "return"):
            self.next()
            if(self.current == ';'):
                return Foundation.Return(Foundation.Null())
            return Foundation.Return(self.union_grammar())

        #Array
        elif(self.current == '['):
            self.next()
            return self.array_grammar()

        #Atomic token
        else:
            rtn = self.union_grammar()
            return rtn

        #Unexpected lexem
        return result

    #Syscall Print [Self terminate semi-colon]
    def print_grammar(self):
        cAssert(self.current,'(',"Print statement needs (")
        self.next()
        rtn = Foundation.Print(self.grammar())
        cAssert(self.current,')',"Print statement needs closing )")
        self.next()
        cAssert(self.current,';',"Print function cannot be futher binded with futher expressions.")
        return rtn
    
    def println_grammar(self):
        cAssert(self.current,'(',"Print statement needs (")
        self.next()
        rtn = Foundation.Println(self.grammar())
        cAssert(self.current,')',"Print statement needs closing )")
        self.next()
        cAssert(self.current,';',"Print function cannot be futher binded with futher expressions.")
        return rtn
    
    def stdin_grammar(self):
        cAssert(self.current,'(',"Stdin statement needs (")
        self.next()
        cAssert(self.current,')',"Stdin statement needs closing )")
        self.next()
        cAssert(self.current,';',"Stdin cannot be further binded, requires ;")
        return Foundation.Input()
    
    #If statement [Self terminate semi-colon]
    def if_grammar(self):
        cAssert(self.current,'(',"If statement needs (")
        self.next()
        e1 = self.grammar()
        cAssert(self.current,')',"If statement needs closing )")
        self.next()
        cAssert(self.current,'{',"If statement needs starting {")
        self.next()
    
        e2 = self.grammar()
        #complete body of if clause
        while(self.current != '}'):
            if(self.current == ';'):
                self.next()
            if(self.current == '}'):
                self.next()
                break
            e2 = Foundation.Seq(e2,self.grammar())
            self.next()
        if(self.current == '}'):
            self.next()
        c = self.current
        #No else clause
        if(c == ';'):
            return Foundation.If(e1,e2,Foundation.Null())
        self.next()
        cn = self.current
        if(c == "else" and cn != "if"):
            self.next()
            e3 = self.grammar()
            while(self.current != '}'):
                if(self.current == ';'):
                    self.next()
                if(self.current == '}'):
                    self.next()
                    break
                e3 = Foundation.Seq(e3,self.grammar())
                self.next()
            if(self.current == '}'):
                self.next()
            cAssert(self.current,';',"If else statement needs semi-colon")

            return Foundation.If(e1,e2,e3)
        #else if statement
        if(c == "else" and cn == "if"):
            self.next()
            e3 = self.if_grammar()
            return Foundation.If(e1,e2,e3)


    #Memory and variables
    def malloc_grammar(self):
        if(self.current == "var"):
            self.next()
            lval = Foundation.Var(self.current)
            self.MemoryState.variableNames.append(self.current)
            self.next()
            cAssert(self.current,'=',"Variables need to be given a value")
            self.next()
            rval = self.grammar()
            return Foundation.Malloc("Var",lval,rval)


    #Helper function grammar, vaildation of list arguments
    def arg_function_grammar(self):
        argList = []
        stateIn = False
        cNotAssert(self.current,',',"Invaild syntax for function argument list")
        while(self.current != ')'):
            if(not stateIn):
                cNotAssert(self.current,',',"Invaild syntax for function argument list")
                argList.append(Foundation.Var(self.current))
                self.MemoryState.variableNames.append(self.current)
                stateIn = True
            elif(stateIn and self.current == ','):
                stateIn = False
            else:
                print("Invaild syntax for function argument")
                exit()
            self.next()
        
        return argList
    

    #Function grammar [Non self terminate semi-colon]
    def function_grammar(self):
        cAssert(self.current,'(',"Function syntax requires (")
        self.next()
        argList = self.arg_function_grammar()
        self.next()
        cAssert(self.current,'{',"Function syntax requires { for function body")
        self.next()
        body = self.grammar()
        while(self.current != '}'):
            if(self.current == ';'):
                self.next()
            if(self.current == '}'):
                self.next()
                break
            body = Foundation.Seq(body,self.grammar())
            self.next()
        if(self.current == '}'):
            self.next()

        cAssert(self.current,';',"Function statement needs semi-colon")
        return Foundation.Function(argList,body)

    #ForEach grammar
    def forEach_grammar(self):
        cAssert(self.current,'(',"For loop syntax requires starting (")
        self.next()
        indexVar = self.current
        self.MemoryState.variableNames.append(indexVar)
        self.next()
        cAssert(self.current,'=',"For loop expected declariation of index variable")
        self.next()
        start = self.number_grammar()
        #Work here
        closure = self.current
        self.next()
        end = self.number_grammar()
        cAssert(self.current,')',"Foreach loop syntax expected ending )")
        self.next()
        cAssert(self.current,'{',"Foreach loop expected starting {")
        self.next()
        scope = self.grammar()
        #Body of forloop
        while(self.current != '}'):
            if(self.current == ';'):
                self.next()
            if(self.current == '}'):
                self.next()
                break
            scope = Foundation.Seq(scope,self.grammar())
            self.next()
        
        if(self.current == '}'):
            self.next()
        self.MemoryState.variableNames.remove(indexVar)
        cAssert(self.current,';',"Foreach loop excepted ending ;")
        return Foundation.ForEach(indexVar,start,end,scope,closure)
    
    def for_grammar(self):
        cAssert(self.current,'(',"For loop expected starting (")
        self.next()
        index = self.malloc_grammar()
        cAssert(self.current,';',"For loop expected ; for terms")
        self.next()
        condition = self.logical_grammar()
        cAssert(self.current,';',"For loop expected ; for terms")
        self.next()
        count = self.logical_grammar()
        cAssert(self.current,')',"For loop expected closing )")
        self.next()
        cAssert(self.current,'{',"Foreach loop expected starting {")
        self.next()
        scope = [self.grammar()]
        
        while(self.current != '}'):
            if(self.current == ';'):
                self.next()
            if(self.current == '}'):
                self.next()
                break
            scope.append(self.grammar())
            self.next()

        if(self.current == '}'):
            self.next()
        self.MemoryState.variableNames.remove(index.expr2().X())
        cAssert(self.current,';',"Foreach loop expected ending ;")
        
        return Foundation.For(index,condition,count,scope)
    
    def while_grammar(self):
        cAssert(self.current,'(',"While loop needs starting (")
        self.next()
        condition = self.union_grammar()
        cAssert(self.current,')',"While loop expected )")
        self.next()
        cAssert(self.current,'{',"While loop expected {")
        self.next()
        scope = self.grammar()
        while(self.current != '}'):
            if(self.current == ';'):
                self.next()
            if(self.current == '}'):
                self.next()
                break
            scope = Foundation.Seq(scope,self.grammar())
            self.next()
        
        if(self.current == '}'):
            self.next()
        cAssert(self.current,';',"While loop expected ending ;")
        return Foundation.While(condition,scope)
            
    #Array [Delegate terminate semi-colon]
    def array_grammar(self):
        array = []
        cNotAssert(self.current,',',"Invalid array syntax")
        while(self.current != ']'):
            if(self.current != ','):
                #Restrict to primative types
                element = self.union_grammar()
                array.append(element)
            else:
                self.next()
        return Foundation.Array(array)

    #Numerical tokenizer for expressions [Delegete terminate semi-colon]
    def union_grammar(self):
        result = self.intersect_grammar()
        while(self.current in ["||"]):
            if(self.current == "||"):
                self.next()
                result = Foundation.Or(result,self.intersect_grammar())
        return result

    def intersect_grammar(self):
        result = self.logical_grammar()
        while(self.current in ["&&"]):
            if(self.current == "&&"):
                self.next()
                result = Foundation.And(result,self.logical_grammar())
        return result

    def logical_grammar(self):
        result = self.number_grammar()
        while(self.current in ["<=","==",">=","!=",'<','>','=',"<<",">>"]):
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
                result = Foundation.Assign(result,self.grammar())
            elif(self.current == "<<"):
                self.next()
                result = Foundation.LeftShift(result,self.number_grammar())
            elif(self.current == ">>"):
                self.next()
                result = Foundation.RightShift(result,self.number_grammar())
        return result

    def number_grammar(self):
        result = self.factor_grammar()
        while(self.current in ['+','-']):
            if(self.current == '+'):
                self.next()
                result = Foundation.Binary("Plus",result,self.factor_grammar())
            elif(self.current == '-'):
                self.next()
                result = Foundation.Binary("Minus",result,self.factor_grammar())
        return result

    def factor_grammar(self):
        result = self.bitUnion_grammar()
        while(self.current in ['*','%','/',"~>"]):
            if(self.current == '*'):
                self.next()
                result = Foundation.Binary("Times",result,self.bitUnion_grammar())
            elif(self.current == '%'):
                self.next()
                result = Foundation.Binary("Mod",result,self.bitUnion_grammar())
            elif(self.current == '/'):
                self.next()
                result = Foundation.Binary("Div",result,self.bitUnion_grammar())
            elif(self.current == "~>"):
                self.next()
                tau = self.cast_grammar();
                result = Foundation.Cast(result,tau)

        return result


    def bitUnion_grammar(self):
        result = self.bitIntersect_grammar()
        while(self.current in ["|"]):
            if(self.current == "|"):
                self.next()
                result = Foundation.BitwiseOr(result,self.bitIntersect_grammar())
        return result


    def bitIntersect_grammar(self):
        result = self.nots_grammar()
        while(self.current in ["&"]):
            if(self.current == "&"):
                self.next()
                result = Foundation.BitwiseAnd(result,self.nots_grammar())
        return result

    def nots_grammar(self):
        result = self.atom_grammar()
        while(self.current in ['!','-','~'] and isinstance(result,Foundation.Null)):
            if(self.current == '!'):
                self.next()
                result = Foundation.Unary("Not",self.atom_grammar())
            elif(self.current == '-' ):
                self.next()
                result = Foundation.Unary("Neg",self.atom_grammar())
            elif(self.current == '~'):
                self.next()
                result = Foundation.Unary("Inv",self.atom_grammar())
        return result

    def atom_grammar(self):
        result = Foundation.Null()
        if(self.current in self.MemoryState.variableNames):
            result = self.atomic_variable_grammar()
        elif(isfloat(self.current) or isint(self.current) or ishex(self.current)):
            result = Foundation.N(self.current)
            self.next()
        elif(self.current == '('):
            self.next()
            result = self.union_grammar()
            cAssert(self.current,')',"Expected ending )")
            self.next()
        elif(self.current == "true"):
            result = Foundation.B("true")
            self.next()
        elif(self.current == "false"):
            result = Foundation.B("false")
            self.next()
        elif(isstr(self.current)):
            result = Foundation.S(self.current[1:-1])
            self.next()
        elif(self.current in ["!","-","~"]):
            return result
        else:
            cAssert(str(self.current),"defined variable","Undefined usage of "+str(self.current)+" Null has been returned")
        return result


    def atomic_variable_grammar(self):
        result = Foundation.Var(self.current)
        self.next()
        if(self.current in ['[','(']):
            if(self.current == '['):
                self.next()
                cNotAssert(self.current,']',"Array cannot be access with a non-index value")
                i = self.union_grammar()
                if(not isinstance(i,Foundation.N) and (not isinstance(i, Foundation.Binary)) and (not isinstance(i, Foundation.Var))):
                    cAssert(str(self.current),"defined variable","Undefined usage of "+str(self.current)+" in array index")
                    cAssert(self.current,']',"Array expected closing ]")
                    self.next()
                else:
                    cAssert(self.current,']',"Array cannot be access with a non-index value")
                cAssert(self.current,']',"Array needs closing ]")
                self.next()
                result = Foundation.Index(result,i)
            elif(self.current == '('):
            #Work here to extent args to list
                self.next()
                arg = self.functionCall_helper_grammar()
                
                result = Foundation.Call(arg,result)
        return result

    #Helper function grammar, vaildation of list arguments
    def functionCall_helper_grammar(self):
        argList = []
        stateIn = False
        cNotAssert(self.current,',',"Invaild syntax for function argument list")
        while(self.current != ')'):
            if(not stateIn):
                cNotAssert(self.current,',',"Invaild syntax for function argument list")
                argList.append(self.union_grammar())
                stateIn = True
            elif(stateIn and self.current == ','):
                stateIn = False
                self.next()
            else:
                print("Invaild syntax for function argument")
                exit()
    
        self.next()
        return argList

    #Cast
    def cast_grammar(self):
        cAssert(self.current,'(',"Improper syntax for cast")
        self.next()
        tau = Foundation.Null()
        if(self.current == "Int"):
            tau = Foundation.TInt()
        elif(self.current == "Float"):
            tau = Foundation.TFloat()
        elif(self.current == "String"):
            tau = Foundation.TS()
        elif(self.current == "Bool"):
            tau = Foundation.TB()
        self.next()
        cAssert(self.current,')',"Cast expected closing )")
        self.next()
        return tau

#t = Tokenizer(['var','f','=','function','(','9',',','10',')','{','return','9',';','}',';'],Memory.Memory())
#print(t.grammar())
