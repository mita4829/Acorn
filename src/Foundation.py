# Acorn 2.0: Cocoa Butter
# Booleans are treated as integers
# Allow hex 

#Number meta class
class N():
    def __init__(self,n):
        try:
            self.n = float(n)
            if(self.n.is_integer()):
                self.n = int(n)
        except:
            self.n = int(n,16)
    def N(self):
        return self.n
    def __repr__(self):
        return 'N(%s)' % self.n

#Boolean meta class
class B():
    def __init__(self,b):
        self.boolean = b
    def B(self):
        if(self.boolean == "true"):
            return 1
        elif(self.boolean == "false"):
            return 0
        elif(isinstance(self.boolean,B)):
            return int((self.boolean).B())
        elif(isinstance(self.boolean,N)):
            return int(bool(self.boolean.N()))
        elif(self.boolean == True):
            return 1
        else:
            return 0
    def __repr__(self):
        return 'B(\'%s\')' % self.boolean

#String meta class
class S():
    def __init__(self,s):
        self.s = str(s)
    def S(self):
        return self.s
    def __repr__(self):
        return 'S(\'%s\')' % self.s

#Var meta class
class Var():
    def __init__(self,x):
        self.x = str(x)
    def X(self):
        return self.x
    def __repr__(self):
        return 'Var(\'%s\')' % self.x


#Null meta class
class Null():
    def __init__(self):
        self.n = "Null"
    def null(self):
        return self.n
    def __repr__(self):
        return 'Null()'

#Unary meta operations
class Unary():
    def __init__(self,uop,e1):
        self.op = str(uop)
        self.e1 = e1
    def expr1(self):
        return self.e1
    def uop(self):
        return self.op
    def __repr__(self):
        return 'Unary(%s,%s)' % (self.op, self.e1)


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
    def __repr__(self):
        return 'Binary(%s,%s,%s)' % (self.op, self.e1, self.e2)

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
    def __repr__(self):
        return 'If(%s,%s,%s)' % (self.e1, self.e2, self.e3)

class Function():
    def __init__(self,arguments,body):
        self.e1 = arguments
        self.e2 = body
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Function(%s,%s)' % (self.e1, self.e2)

class Call():
    def __init__(self,arguments,body):
        self.e1 = arguments
        self.e2 = body
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Call(%s,%s)' % (self.e1, self.e2)

class Return():
    def __init__(self,returns):
        self.e1 = returns
    def expr1(self):
        return self.e1
    def __repr__(self):
        return 'Return(%s)' % (self.e1)

class Seq():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Seq(%s,%s)' % (self.e1, self.e2)

class Eq():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Eq(%s,%s)' % (self.e1, self.e2)

class Ne():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Ne(%s,%s)' % (self.e1, self.e2)

class Lt():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Lt(%s,%s)' % (self.e1, self.e2)

class Le():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Le(%s,%s)' % (self.e1, self.e2)

class Gt():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Gt(%s,%s)' % (self.e1, self.e2)

class Ge():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Ge(%s,%s)' % (self.e1, self.e2)

class And():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'And(%s,%s)' % (self.e1, self.e2)

class Or():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Or(%s,%s)' % (self.e1, self.e2)

class BitwiseAnd():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Intersect(%s,%s)' % (self.e1, self.e2)

class BitwiseOr():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Union(%s,%s)' % (self.e1, self.e2)

class LeftShift():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'LeftShift(%s,%s)' % (self.e1, self.e2)

class RightShift():
    def __init__(self,e1,e2):
        self.e1 = e1
        self.e2 = e2
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'RightShift(%s,%s)' % (self.e1, self.e2)

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
    def __repr__(self):
        return 'Malloc(%s,%s,%s)' % (self.e1, self.e2, self.e3)

class Array():
    def __init__(self,e1):
        self.e1 = e1
    def expr1(self):
        return self.e1
    def __repr__(self):
        return 'Array(%s)' % self.e1

class Index():
    def __init__(self,array,index):
        self.e1 = array
        self.e2 = index
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Index(%s,%s)' % (self.e1, self.e2)

class Assign():
    def __init__(self,var,val):
        self.e1 = var
        self.e2 = val
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Assign(%s,%s)' % (self.e1, self.e2)

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
    def __repr__(self):
        return 'ForEach(%s,%s,%s,%s,%s)' % (self.e1, self.e2, self.e3, self.e4, self.e5)

class For():
    def __init__(self,index,condition,count,scope):
        self.e1 = index
        self.e2 = condition
        self.e3 = count
        self.e4 = scope
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def expr3(self):
        return self.e3
    def expr4(self):
        return self.e4
    def __repr__(self):
        return 'For(%s,%s,%s,%s)' % (self.e1, self.e2, self.e3, self.e4)

class While():
    def __init__(self,condition,scope):
        self.e1 = condition
        self.e2 = scope
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'While(%s,%s)' % (self.e1, self.e2)

#Side effects
class Print():
    def __init__(self,expr):
        self.expr1 = expr
    def E(self):
        return self.expr1
    def __repr__(self):
        return 'Print(%s)' % self.expr1

#Side effects
class Println():
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
    def __repr__(self):
        return 'Input(%s)' % (self.expr1)

class Cast():
    def __init__(self,value,type):
        self.e1 = value
        self.e2 = type
    def cast(self,value,type):
        if(isinstance(type,TInt)):
            try:
                n = N(int(value))
                return n
            except:
                return False
        elif(isinstance(type,TS)):
            try:
                s = S(str(value))
                return s
            except:
                return False
        elif(isinstance(type,TFloat)):
            try:
                f = N(float(value))
                return f
            except:
                return False
        elif(isinstance(type,TB)):
            try:
                b = B(bool(value))
                return b
            except:
                return False
        return False
    def expr1(self):
        return self.e1
    def expr2(self):
        return self.e2
    def __repr__(self):
        return 'Cast(%s,%s)' % (self.e1, self.e2)

class TInt():
    def __init__(self):
        self.e1 = None
    def __repr__(self):
        return 'Int'


class TFloat():
    def __init__(self):
        self.e1 = None
    def __repr__(self):
        return 'Float'

class TB():
    def __init__(self):
        self.e1 = None
    def __repr__(self):
        return 'Bool' % (self.e1)

class TS():
    def __init__(self):
        self.e1 = None
    def __repr__(self):
        return 'String'

#Helper functions
def isfloat(n):
    try:
        float(n)
        return True
    except:
        return False

