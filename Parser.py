"""
Grammar for Acorn

expr ::= x | n | b | null | uop expr1 | expr1 bop expr2 | expr1 ? expr2 : expr3 |
function(x){expr} | f(expr1) | print(expr1)
values ::= n | b | null | str | function(x){expr}

"""

from sys import exit
import Foundation


def case(expr,typep):
    return isinstance(expr,typep)
def isValue(expr):
    return isinstance(expr,Foundation.N) or isinstance(expr,Foundation.B) or isinstance(expr,Foundation.S) or isinstance(expr,Foundation.Null)

def step(expr,stack,heap):
    #Base cases
    #N
    if(case(expr,Foundation.N)):
        return expr.N()
    #B
    elif(case(expr,Foundation.B)):
        return expr.B()
    #S
    elif(case(expr,Foundation.S)):
        return expr.S()
    #Null
    elif(case(expr,Foundation.Null)):
        return expr.null()
    #Print
    elif(case(expr,Foundation.Print)):
        if(isValue(expr.E())):
            print(step(expr.E(),stack,heap))
        else:
            val = step(expr.E(),stack,heap)
            while(not isValue(val)):
                val = step(val,stack,heap)
            print(str(step(val,stack,heap)))
        return
    #Unary Needs to refactor laters also with Binary
    elif(case(expr,Foundation.Unary) and isValue(expr.expr1())):
        if(expr.uop() == "Neg"):
            return Foundation.N(-1*step(expr.expr1(),stack,heap))
        elif(expr.uop() == "Not"):
            return Foundation.B(not step(expr.expr1(),stack,heap))

    #Binary
    elif(case(expr,Foundation.Binary) and isValue(expr.expr1()) and isValue(expr.expr2())):
        if(expr.bop() == "Plus"):
            return Foundation.N(step(expr.expr1(),stack,heap)+step(expr.expr2(),stack,heap))
        elif(expr.bop() == "Minus"):
            return Foundation.N(step(expr.expr1(),stack,heap)-step(expr.expr2(),stack,heap))
        elif(expr.bop() == "Times"):
            return Foundation.N(step(expr.expr1(),stack,heap)*step(expr.expr2(),stack,heap))
        elif(expr.bop() == "Div"):
            return Foundation.N(step(expr.expr1(),stack,heap)/step(expr.expr2(),stack,heap))

    #If
    elif(case(expr,Foundation.If) and isValue(expr.expr1())):
        if( step(expr.expr1(),stack,heap) ):
            return step(expr.expr2(),stack,heap)
        else:
            return step(expr.expr3(),stack,heap)

    #Inductive cases

    #Induct Unary
    elif(case(expr,Foundation.Unary)):
        if(expr.uop() == "Neg"):
            return Foundation.Unary("Neg",step(expr.expr1(),stack,heap))
        elif(expr.uop() == "Not"):
            return Foundation.Unary("Not",step(expr.expr1(),stack,heap))

    #Induct Binary
    elif(case(expr,Foundation.Binary)):
        if(isValue(expr.expr1())):
            return Foundation.Binary(expr.bop(),expr.expr1(),step(expr.expr2(),stack,heap))
        else:
            return Foundation.Binary(expr.bop(),step(expr.expr1(),stack,heap),expr.expr2())

    #Induct If
    elif(case(expr,Foundation.If)):
        return Foundation.If(step(expr.expr1(),stack,heap),expr.expr2(),expr.expr3())
