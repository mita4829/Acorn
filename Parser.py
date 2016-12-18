"""
Grammar for Acorn

expr ::= x | n | b | null | uop expr1 | expr1 bop expr2 | expr1 ? expr2 : expr3 |
function(x){expr} | f(expr1) | print(expr1)
values ::= n | b | null | str | function(x){expr}

"""

from sys import exit
import Foundation
import Memory


def case(expr,typep):
    return isinstance(expr,typep)
def isValue(expr):
    return isinstance(expr,Foundation.N) or isinstance(expr,Foundation.B) or isinstance(expr,Foundation.S) or isinstance(expr,Foundation.Null) or isinstance(expr,Foundation.Var) or isinstance(expr,Foundation.Function)

def step(expr,stack,heap):
    #print(heap.heap)
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
    #Function
    elif(case(expr,Foundation.Function)):
        return expr
    #Var
    elif(case(expr,Foundation.Var)):
        x = expr.X()
        callStack = stack.stackCall(x)
        callHeap = heap.heapCall(x)
        if((callStack == "DNE") and (callHeap == "DNE")):
            exit("Acorn: Use of variable "+str(x)+" before declaration.")
        if(callStack != "DNE"):
            return callStack
        else:
            return callHeap
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
    #Seq
    elif(case(expr,Foundation.Seq)):
        step(expr.expr1(),stack,heap)
        step(expr.expr2(),stack,heap)
    #Eq
    elif(case(expr,Foundation.Eq)):
        return Foundation.B(step(expr.expr1(),stack,heap) == step(expr.expr2(),stack,heap))
    #Ne
    elif(case(expr,Foundation.Ne)):
        return Foundation.B(step(expr.expr1(),stack,heap) != step(expr.expr2(),stack,heap))
    #Lt
    elif(case(expr,Foundation.Lt)):
        return Foundation.B(step(expr.expr1(),stack,heap) < step(expr.expr2(),stack,heap))
    #Le
    elif(case(expr,Foundation.Le)):
        return Foundation.B(step(expr.expr1(),stack,heap) <= step(expr.expr2(),stack,heap))
    #Ge
    elif(case(expr,Foundation.Ge)):
        return Foundation.B(step(expr.expr1(),stack,heap) >= step(expr.expr2(),stack,heap))
    #Gt
    elif(case(expr,Foundation.Gt)):
        return Foundation.B(step(expr.expr1(),stack,heap) > step(expr.expr2(),stack,heap))

    #Var Const
    elif(case(expr,Foundation.Malloc)):
        val = step(expr.expr3(),stack,heap)
        while((not isValue(val)) and (type(val) != str) and (type(val) != float) and(type(val) != bool)):
            val = step(val,stack,heap)
        if(expr.expr1() == "Var"):
            heap.heap[expr.expr2().X()] = step(val,stack,heap)
        elif(expr.expr1() == "Const"):
            stack.stack[expr.expr2().X()] = step(val,stack,heap)
        return

    #Call
    elif(case(expr,Foundation.Call)):
        return step(expr.expr1(),stack,heap)

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
        return step(Foundation.If(step(expr.expr1(),stack,heap),expr.expr2(),expr.expr3()),stack,heap)

    else:
        return expr #
