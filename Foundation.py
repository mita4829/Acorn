#Number meta class
class N():
    def __init__(self,n):
        self.n = float(n)
    def N(self):
        return self.n

#Boolean meta class
class B():
    def __init__(self,b):
        self.b = bool(b)
    def B(self):
        return self.b

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

#Side effects
class Print():
    def __init__(self,expr):
        self.expr1 = expr
    def E(self):
        return self.expr1
