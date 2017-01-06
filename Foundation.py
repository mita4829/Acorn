#Number meta class
class N():
    def __init__(self,n):
        self.n = float(n)
    def N(self):
        return self.n

#Boolean meta class
class B():
    def __init__(self,b):
        self.boolean = b
    def B(self):
        if(self.boolean == "true"):
            return True
        elif(self.boolean == "false"):
            return False
        elif(isinstance(self.boolean,B)):
            return (self.boolean).B()
        elif(isinstance(self.boolean,N)):
            return bool(self.boolean.N())
        elif(self.boolean == True):
            return True
        else:
            return False

#String meta class
class S():
    def __init__(self,s):
        self.s = str(s)
    def S(self):
        return self.s

#Var meta class
class Var():
    def __init__(self,x):
        self.x = str(x)
    def X(self):
        return self.x

#Null meta class
class Null():
    def __init__(self):
        self.n = "Null"
    def null(self):
        return self.n

#Unary meta operations
class Unary():
    def __init__(self,uop,e1):
        self.op = str(uop)
        self.e1 = e1
    def expr1(self):
        return self.e1
    def uop(self):
        return self.op

#Binary meta operations
class Binary():
    def __init__(self,bop,e1,e2):
        self.op = str(bop)
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def bop(self):
        return self.op

#Trinary meta operator
class If():
    def __init__(self,e1,e2,e3):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def expr3(self):
        return self.e3

class Function():
    def __init__(self,arguments,body):
        self.e1 = arguments
        self.e2 = body
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2

class Call():
    def __init__(self,arguments,body):
        self.e1 = arguments
        self.e2 = body
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2

class Return():
    def __init__(self,returns):
        self.e1 = returns
    def expr1(self):
        return self.e1

class Seq():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2

class Eq():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2

class Ne():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2

class Lt():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2

class Le():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2

class Gt():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2

class Ge():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2

class Malloc():
    def __init__(self,m,x,v):
        self.e1 = m
        self.e2 = x
        self.e3 = v
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def expr3(self):
        return self.e3

class Array():
    def __init__(self,e1):
        self.e1 = e1
    def expr1(self):
        return self.e1

class Index():
    def __init__(self,array,index):
        self.e1 = array
        self.e2 = index
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2

class Assign():
    def __init__(self,var,val):
        self.e1 = var
        self.e2 = val
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2

class ForEach():
    def __init__(self,i,start,end,scope,closure):
        self.e1 = i
        self.e2 = start
        self.e3 = end
        self.e4 = scope
        self.e5 = closure
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def expr3(self):
        return self.e3
    def expr4(self):
        return self.e4
    def expr5(self):
        return self.e5
#Side effects
class Print():
    def __init__(self,expr):
        self.expr1 = expr
    def E(self):
        return self.expr1

class Input():
    def __init__(self):
        self.expr1 = None
    def cast(self,n):
        if(isfloat(n)):
            return N(n)
        if(n=="true" or n=="false"):
            return B(n)
        if(n=="null"):
            return Null()
        return S(n)


#Helper functions
def isfloat(n):
    try:
        float(n)
        return True
    except:
        return False
