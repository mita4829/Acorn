#Acorn v1.0

from sys import exit
import Foundation
import Memory


def case(expr,typep):
    return isinstance(expr,typep)
def isValue(expr):
    return isinstance(expr,Foundation.N) or isinstance(expr,Foundation.B) or isinstance(expr,Foundation.S) or isinstance(expr,Foundation.Null) or isinstance(expr,Foundation.Var) or isinstance(expr,Foundation.Function)

def subsitute(expr,value,x):
    #N
    if(case(expr,Foundation.N)):
        return expr
    #B
    elif(case(expr,Foundation.B)):
        return expr
    #S
    elif(case(expr,Foundation.S)):
        return expr
    #Null
    elif(case(expr,Foundation.Null)):
        return expr
    #Var
    elif(case(expr,Foundation.Var)):
        if(x == expr.X()):
            return value
        else:
            return expr
    #Binary
    elif(case(expr,Foundation.Binary)):
        return Foundation.Binary(expr.bop(),subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))

    #Eq
    elif(case(expr,Foundation.Eq)):
        return Foundation.Eq(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))
    #Ne
    elif(case(expr,Foundation.Ne)):
        return Foundation.Ne(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))
    #Lt
    elif(case(expr,Foundation.Lt)):
        return Foundation.Lt(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))
    #Le
    elif(case(expr,Foundation.Le)):
        return Foundation.Le(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))
    #Ge
    elif(case(expr,Foundation.Ge)):
        return Foundation.Ge(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))
    #Gt
    elif(case(expr,Foundation.Gt)):
        return Foundation.Gt(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))

    #If
    elif(case(expr,Foundation.If)):
        return Foundation.If(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x),subsitute(expr.expr3(),value,x))
    #Seq
    elif(case(expr,Foundation.Seq)):
        e1 = subsitute(expr.expr1(),value,x)
        e2 = subsitute(expr.expr2(),value,x)
        return Foundation.Seq(e1,e2)

    elif(case(expr,Foundation.Call)):
        return Foundation.Call(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))
    #Return
    elif(case(expr,Foundation.Return)):
        return Foundation.Return(subsitute(expr.expr1(),value,x))
    #print
    elif(case(expr,Foundation.Print)):
        return Foundation.Print(subsitute(expr.E(),value,x))
    #Malloc
    elif(case(expr,Foundation.Malloc)):
        return Foundation.Malloc(expr.expr1(),expr.expr2(),subsitute(expr.expr3(),value,x))
    else:
        print(expr)
        print("Uncaught subsitute")

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
            while(not isValue(val) and (type(val) != str) and (type(val) != float) and(type(val) != bool)):
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
        e1 = step(expr.expr1(),stack,heap)
        if(case(e1,Foundation.Return)):
            return e1
        e2 = step(expr.expr2(),stack,heap)
        if(case(e2,Foundation.Return)):
            return e2
        return

    #Return
    elif(case(expr,Foundation.Return)):
        return expr

    #Recursive functions
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

    #Var Const Malloc
    elif(case(expr,Foundation.Malloc)):
        val = step(expr.expr3(),stack,heap)
        while((not isValue(val)) and (type(val) != str) and (type(val) != float) and (type(val) != bool)):
            val = step(val,stack,heap)
        if(expr.expr1() == "Var"):
            heap.heap[expr.expr2().X()] = step(val,stack,heap)
        elif(expr.expr1() == "Const"):
            stack.stack[expr.expr2().X()] = step(val,stack,heap)
        return

    #Call
    elif(case(expr,Foundation.Call)):
        functionName = expr.expr2().X()
        functionObject = heap.heapCall(functionName)
        functionArgName = functionObject.expr1().X()
        argument = expr.expr1()
        while(not isValue(argument)):
            argument = step(argument,stack,heap)
        functionBody = functionObject.expr2()
        sbtBody = subsitute(functionBody,argument,functionArgName)
        rtn = step(sbtBody,stack,heap)
        if(case(rtn,Foundation.Return)):
            if(not case(rtn.expr1(),Foundation.Null)):
                return step(rtn.expr1(),stack,heap)


        return Foundation.Null()

    #gets
    elif(case(expr,Foundation.Input)):
        castToken = input()
        return expr.cast(castToken)
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
