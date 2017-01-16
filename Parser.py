#Acorn v1.0

from sys import exit
import Foundation
import Memory


def case(expr,typep):
    return isinstance(expr,typep)
def isValue(expr):
    return isinstance(expr,Foundation.N) or isinstance(expr,Foundation.B) or isinstance(expr,Foundation.S) or isinstance(expr,Foundation.Null)  or isinstance(expr,Foundation.Function) or isinstance(expr,Foundation.Array)
def isfloat(n):
    try:
        float(n)
        return True
    except:
        return False
def isRaw(val):
    if((type(val) == str) or (type(val) == float) or (type(val) == bool) or (type(val) == int)):
        return True
    else:
        return False

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
    #Index
    elif(case(expr, Foundation.Index)):
        return Foundation.Index(expr.expr1(),subsitute(expr.expr2(),value,x))
    elif(case(expr,Foundation.Assign)):
        if(case(expr.expr1(),Foundation.Index)):
            return Foundation.Assign(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))
        return Foundation.Assign(expr.expr1(),subsitute(expr.expr2(),value,x))
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
            #print("isValue")
            val = expr.E()
            if(case(val,Foundation.Var)):
                val = step(val,stack,heap)
            valFinal = step(val,stack,heap)
            if(isfloat(valFinal)):
                if((valFinal % 1) == 0):
                    print(str(int(valFinal)))
                    return
            print(str(valFinal))
        elif(isRaw(expr.E())):
            #print("isRaw")
            valFinal = expr.E()
            if(isfloat(valFinal)):
                if((valFinal % 1) == 0):
                    print(str(int(valFinal)))
                    return
            print(str(valFinal))
        else:
            val = expr.E()
            #print("isExpr")
            while(not isValue(val) and (type(val) != str) and (type(val) != float) and(type(val) != bool)):
                val = step(val,stack,heap)
            valFinal = val
            if(not isRaw(valFinal)):
                valFinal = step(valFinal,stack,heap)
            if(isfloat(valFinal)):
                if((valFinal % 1) == 0):
                    print(str(int(valFinal)))
                    return
            print(str(valFinal))
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

    #ForEach
    elif(case(expr,Foundation.ForEach)):
        indexName = expr.expr1()
        start = int(expr.expr2().N())
        end = int(expr.expr3().N())
        scope = expr.expr4()
        closure = expr.expr5()
        if(closure == "<"):
            for i in range(start,end):
                step(subsitute(scope,Foundation.N(i),indexName),stack,heap)
        elif(closure == "<="):
            for i in range(start,end+1):
                step(subsitute(scope,Foundation.N(i),indexName),stack,heap)
        else:
            print("Acorn: Cannot sequence range of index "+str(closure))
            exit()
        return expr
    #Recursive functions
    #Eq
    elif(case(expr,Foundation.Eq)):
        e1 = expr.expr1()
        e2 = expr.expr2()
        while(not isValue(e1)):
            e1 = step(e1,stack,heap)
        while(not isValue(e2)):
            e2 = step(e1,stack,heap)
        return Foundation.B(step(e1,stack,heap) == step(e2,stack,heap))
    #Ne
    elif(case(expr,Foundation.Ne)):
        e1 = expr.expr1()
        e2 = expr.expr2()
        while(not isValue(e1)):
            e1 = step(e1,stack,heap)
        while(not isValue(e2)):
            e2 = step(e1,stack,heap)
        return Foundation.B(step(e1,stack,heap) != step(e2,stack,heap))
    #Lt
    elif(case(expr,Foundation.Lt)):
        e1 = expr.expr1()
        e2 = expr.expr2()
        while(not isValue(e1)):
            e1 = step(e1,stack,heap)
        while(not isValue(e2)):
            e2 = step(e1,stack,heap)
        return Foundation.B(step(e1,stack,heap) < step(e2,stack,heap))
    #Le
    elif(case(expr,Foundation.Le)):
        e1 = expr.expr1()
        e2 = expr.expr2()
        while(not isValue(e1)):
            e1 = step(e1,stack,heap)
        while(not isValue(e2)):
            e2 = step(e1,stack,heap)
        return Foundation.B(step(e1,stack,heap) <= step(e2,stack,heap))
    #Ge
    elif(case(expr,Foundation.Ge)):
        e1 = expr.expr1()
        e2 = expr.expr2()
        while(not isValue(e1)):
            e1 = step(e1,stack,heap)
        while(not isValue(e2)):
            e2 = step(e1,stack,heap)
        return Foundation.B(step(e1,stack,heap) >= step(e2,stack,heap))
    #Gt
    elif(case(expr,Foundation.Gt)):
        e1 = expr.expr1()
        e2 = expr.expr2()
        while(not isValue(e1)):
            e1 = step(e1,stack,heap)
        while(not isValue(e2)):
            e2 = step(e1,stack,heap)
        return Foundation.B(step(e1,stack,heap) > step(e2,stack,heap))

    #Var Const Malloc
    elif(case(expr,Foundation.Malloc)):
        val = expr.expr3()
        while((not isValue(val)) and (type(val) != str) and (type(val) != float) and (type(val) != bool)):
            val = step(val,stack,heap)
        if(expr.expr1() == "Var"):
            heap.heap[expr.expr2().X()] = val
        elif(expr.expr1() == "Const"):
            stack.stack[expr.expr2().X()] = val
        return

    #Array
    elif(case(expr,Foundation.Array)):
        for i in range(0,len(expr.expr1())):
            step(expr.expr1()[i],stack,heap)
        return expr

    #Assign
    elif(case(expr,Foundation.Assign)):
        if(case(expr.expr1(),Foundation.Index)):
            arrayRaw = heap.heapCall(expr.expr1().expr1().X())
            index = int(step(expr.expr1(),stack,heap).N())
            valToAssign = expr.expr2()
            arrayRaw.expr1()[index] = valToAssign
            return expr
        name = expr.expr1().X()
        val = step(expr.expr2(),stack,heap)
        while((not isValue(val)) and (type(val) != str) and (type(val) != float) and (type(val) != bool)):
            val = step(val,stack,heap)
        heap.heap[name] = val
        return expr

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

    #stdin
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
    #Induct Array Index
    elif(case(expr, Foundation.Index)):
        arrayRaw = step(expr.expr1(),stack,heap).expr1()
        index = step(expr.expr2(),stack,heap)
        while(not isRaw(index)):
            index = step(index,stack,heap)

        if(int(index) >= len(arrayRaw) and int(index) > -1):
            exit("Acorn: Array out-of-bound error. Attempted at accessing index outside of Array's memory")
        return arrayRaw[int(index)]
    #Induct If
    elif(case(expr,Foundation.If)):
        return step(Foundation.If(step(expr.expr1(),stack,heap),expr.expr2(),expr.expr3()),stack,heap)

    else:
        #Code should never hit this
        print("Acorn: Uncaught exception with Parser. Please report this case: "+str(expr))
        if(isRaw(expr)):
            print("Error: 0x000000001")
            #return expr #Uncomment if you're feeling risk-K
        else:
            print("Error: 0xdeadbeef ekk :(")
        exit()
