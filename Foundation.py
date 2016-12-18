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
    def __init__(self,arguments,rtn,body):
        self.e1 = arguments
        self.e2 = rtn
        self.e3 = body
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def expr3(self):
        return self.e3

class Call():
    def __init__(self,function,arguments):
        self.e1 = function
        self.e2 = arguments
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2

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


#Side effects
class Print():
    def __init__(self,expr):
        self.expr1 = expr
    def E(self):
        return self.expr1


#Helper functions
def isfloat(n):
    try:
        float(n)
        return True
    except:
        return False
