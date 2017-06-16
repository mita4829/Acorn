#Acorn 2.0: Cocoa Butter
#No direct access to stack and heap. Stack data structure with dictionaries for lexical scoping. More efficent usage of dense dictionaries in python3.6+
#String concats
#No direct stepping access to raw values
#Logical operators with short-cir effect

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
'''
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
    #Array
    elif(case(expr,Foundation.Array)):
        subArray = []
        for i in range(0,len(expr.expr1())):
            subArray.append(subsitute(expr.expr1()[i],value,x))
        return Foundation.Array(subArray)
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
    #Or
    elif(case(expr,Foundation.Or)):
        return Foundation.Or(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))
    #And
    elif(case(expr,Foundation.And)):
        return Foundation.And(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))
    #If
    elif(case(expr,Foundation.If)):
        return Foundation.If(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x),subsitute(expr.expr3(),value,x))
    #Seq
    elif(case(expr,Foundation.Seq)):
        e1 = subsitute(expr.expr1(),value,x)
        e2 = subsitute(expr.expr2(),value,x)
        return Foundation.Seq(e1,e2)
    #Call
    elif(case(expr,Foundation.Call)):#Extend list to allow recursion
        sbtBody = subsitute(expr.expr2(),value,x)
        sbtArg = []
        for i in range(0,len(expr.expr1())):
            sbtArg.append(subsitute(expr.expr1()[i],value,x))
        return Foundation.Call(sbtArg,sbtBody)
    #Return
    elif(case(expr,Foundation.Return)):
        return Foundation.Return(subsitute(expr.expr1(),value,x))
    #print
    elif(case(expr,Foundation.Print)):
        return Foundation.Print(subsitute(expr.E(),value,x))
    #Malloc
    elif(case(expr,Foundation.Malloc)):
        return Foundation.Malloc("Var",expr.expr2(),subsitute(expr.expr3(),value,x))
    #Index
    elif(case(expr, Foundation.Index)):
        return Foundation.Index(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))
    elif(case(expr,Foundation.Assign)):
        if(case(expr.expr1(),Foundation.Index)):
            return Foundation.Assign(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x))
        return Foundation.Assign(expr.expr1(),subsitute(expr.expr2(),value,x))
    elif(case(expr,Foundation.For)):
        return Foundation.For(subsitute(expr.expr1(),value,x),subsitute(expr.expr2(),value,x),subsitute(expr.expr3(),value,x),subsitute(expr.expr4(),value,x))
    else:
        print(expr)
        print("Uncaught subsitute")
'''

def step(expr,Env):
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
        varName = expr.X()
        rtn = Env.requestVar(varName)
        if(rtn == None):
            exit("Dynamic run time error. Undefined variable "+str(varName))
        return rtn
    #Null
    elif(case(expr,Foundation.Null)):
        return expr.null()
    #Print
    elif(case(expr,Foundation.Print) or case(expr,Foundation.Println)):
        value = expr.E()
        while(not isValue(value)):
            value = step(value,Env)
        value = step(value,Env)
        newline = ''
        if(case(expr,Foundation.Println)):
            newline = '\n'
        if(isfloat(value)):
            if((value % 1) == 0):
                print(str(int(value)),end=newline)
            else:
                print(str(value),end=newline)
        else:
            print(str(value),end=newline)
    #Input
    elif(case(expr,Foundation.Input)):
        castToken = input()
        return expr.cast(castToken)

    #Unary
    elif(case(expr,Foundation.Unary) and isValue(expr.expr1())):
        if(expr.uop() == "Neg"):
            return Foundation.N(-1*step(expr.expr1(),Env))
        elif(expr.uop() == "Not"):
            return Foundation.B(not step(expr.expr1(),Env))

    #Binary
    elif(case(expr,Foundation.Binary) and isValue(expr.expr1()) and isValue(expr.expr2())):
        if(expr.bop() == "Plus"):
            e1 = expr.expr1()
            e2 = expr.expr2()
            if(case(e1,Foundation.S) and case(e2,Foundation.S)):
                return Foundation.S(step(e1,Env)+step(e2,Env))
            return Foundation.N(step(expr.expr1(),Env)+step(expr.expr2(),Env))
        elif(expr.bop() == "Minus"):
            return Foundation.N(step(expr.expr1(),Env)-step(expr.expr2(),Env))
        elif(expr.bop() == "Times"):
            return Foundation.N(step(expr.expr1(),Env)*step(expr.expr2(),Env))
        elif(expr.bop() == "Div"):
            return Foundation.N(step(expr.expr1(),Env)/step(expr.expr2(),Env))
        elif(expr.bop() == "Mod"):
            return Foundation.N(step(expr.expr1(),Env)%step(expr.expr2(),Env))

    #Malloc
    elif(case(expr,Foundation.Malloc) and isValue(expr.expr3())):
        Env.malloc(expr.expr2().X(),expr.expr3())

    #Assign
    elif(case(expr,Foundation.Assign) and isValue(expr.expr2())):
        #Work on index
        if(case(expr.expr1(),Foundation.Index)):
            array = Env.requestVar(expr.expr1().expr1().X()).expr1()
            index = step(expr.expr1().expr2(),Env)
            while(not isValue(index)):
                index = step(index,Env)
            index = int(step(index,Env))
            array[index] = expr.expr2()
            return
        varName = expr.expr1().X()
        Env.assignVar(varName,expr.expr2())
        return
    
    #Index
    elif(case(expr,Foundation.Index) and isValue(expr.expr2())):
        array = Env.requestVar(expr.expr1().X()).expr1()
        index = step(expr.expr2(),Env)
        if(int(index) >= len(array) or int(index) < 0):
            exit("Dynamic run time error, attempt to access out of bound memory for array")
        return array[int(index)]
    

    #If
    elif(case(expr,Foundation.If) and isValue(expr.expr1())):
        if(step(expr.expr1(),Env)):
            Env.pushLocalStack()
            rtn = step(expr.expr2(),Env)
            Env.popLocalStack()
            return rtn
        else:
           Env.pushLocalStack()
           rtn = step(expr.expr3(),Env)
           Env.popLocalStack()
           return rtn
    #Seq
    elif(case(expr,Foundation.Seq)):
        e1 = step(expr.expr1(),Env)
        if(case(e1,Foundation.Return)):
            return e1
        e2 = step(expr.expr2(),Env)
        if(case(e2,Foundation.Return)):
            return e2
        return

    #Eq
    elif(case(expr,Foundation.Eq) and isValue(expr.expr1()) and isValue(expr.expr2())):
        return Foundation.B(step(expr.expr1(),Env) == step(expr.expr2(),Env))

    #Ne
    elif(case(expr,Foundation.Ne) and isValue(expr.expr1()) and isValue(expr.expr2())):
        return Foundation.B(step(expr.expr1(),Env) != step(expr.expr2(),Env))

    #Lt
    elif(case(expr,Foundation.Lt) and isValue(expr.expr1()) and isValue(expr.expr2())):
        return Foundation.B(step(expr.expr1(),Env) < step(expr.expr2(),Env))

    #Gt
    elif(case(expr,Foundation.Gt) and isValue(expr.expr1()) and isValue(expr.expr2())):
        return Foundation.B(step(expr.expr1(),Env) > step(expr.expr2(),Env))

    #Le
    elif(case(expr,Foundation.Le) and isValue(expr.expr1()) and isValue(expr.expr2())):
        return Foundation.B(step(expr.expr1(),Env) <= step(expr.expr2(),Env))
    
    #Ge
    elif(case(expr,Foundation.Ge) and isValue(expr.expr1()) and isValue(expr.expr2())):
        return Foundation.B(step(expr.expr1(),Env) >= step(expr.expr2(),Env))

    #And
    elif(case(expr,Foundation.And) and isValue(expr.expr1()) and isValue(expr.expr2())):
        a = step(expr.expr1(),Env)
        if(not a):
            return Foundation.B(False)
        return Foundation.B(step(expr.expr2(),Env))
    
    #Or
    elif(case(expr,Foundation.Or) and isValue(expr.expr1()) and isValue(expr.expr2())):
        a = step(expr.expr1(),Env)
        if(a):
            return Foundation.B(True)
        return Foundation.B(step(expr.expr2(),Env))
    


    #Call
    elif(case(expr,Foundation.Call)):
        #For each argument, step until they are values
        argVal = []
        for i in range(0,len(expr.expr1())):
            value = expr.expr1()[i]
            while(not isValue(value)):
                value = step(value,Env)
            argVal.append(value)
        functionName = expr.expr2().X()
        #Function object is an instant of the function
        functionObject = Env.requestVar(functionName)
        #Function arg names is a list of the defined function argument names
        functionArgNames = functionObject.expr1()
        functionBody = functionObject.expr2()
        #Begin subsituting values in the function
#       for i in range(0,len(argVal)):
#functionBody = subsitute(functionBody,argVal[i],functionArgNames[i].X())
        Env.pushLocalStack()
        for i in range(0,len(argVal)):
            step(Foundation.Malloc("Var",functionArgNames[i],argVal[i]),Env)
        rtn = step(functionBody,Env)

        if(case(rtn,Foundation.Return)):
            if(not case(rtn.expr1(),Foundation.Null)):
                rtn = rtn.expr1()
                if(not isValue(rtn)):
                    rtn = step(rtn,Env)
                Env.popLocalStack()
                return rtn
            Env.popLocalStack()
            return rtn.expr1()
        Env.popLocalStack()
        return Foundation.Null()
            
    #Return
    elif(case(expr,Foundation.Return)):
        return expr

    #ForEach
    elif(case(expr,Foundation.ForEach) and isValue(expr.expr2()) and isValue(expr.expr3())):
        index = expr.expr1()
        start = int(step(expr.expr2(),Env))
        end = int(step(expr.expr3(),Env))
        scope = expr.expr4()
        closure = expr.expr5()
        Env.pushLocalStack()
        if(closure == "<"):
            for i in range(start,end):
                step(Foundation.Malloc("Var",Foundation.Var(index),Foundation.N(i)),Env)
                step(scope,Env)
        elif(closure == "<="):
            for i in range(start,end+1):
                step(Foundation.Malloc("Var",Foundation.Var(index),Foundation.N(i)),Env)
                step(scope,Env)
        else:
            exit("Dynamic run time error, cannot sequence range of index "+str(closure))
        Env.popLocalStack()
        return expr

    #For loop
    elif(case(expr,Foundation.For)):
        index = expr.expr1()
        indexVar = index.expr2()
        
        condition = expr.expr2()
        count = expr.expr3()
        scope = expr.expr4()
        Env.pushLocalStack()
        #Initiate starting variable
        step(index,Env)
        while(step(condition,Env).B()):
            #Run body with subsitute of index variable
            #step(subsitute(scope, Foundation.N(step(Env.requestVar(indexVar.X()),Env)), indexVar),Env)
            for i in range(0,len(scope)):
                step(scope[i],Env)
            #Update the counter
            step(count,Env)
        Env.popLocalStack()
        return expr

    #While
    elif(case(expr,Foundation.While)):
        condition = expr.expr1()
        scope = expr.expr2()
        Env.pushLocalStack()
        while(step(condition,Env).B()):
            step(scope,Env)
        Env.popLocalStack()
        return expr

    #BitAnd
    elif(case(expr,Foundation.BitwiseAnd) and isValue(expr.expr1()) and isValue(expr.expr2())):
        p = step(expr.expr1(),Env)
        q = step(expr.expr2(),Env)
        return Foundation.N(int(p) & int(q))

    #BitOr
    elif(case(expr,Foundation.BitwiseOr) and isValue(expr.expr1()) and isValue(expr.expr2())):
        p = step(expr.expr1(),Env)
        q = step(expr.expr2(),Env)
        return Foundation.N(int(p) | int(q))

    #Binary Expr
    elif(case(expr,Foundation.Binary)):
        a  = isValue(expr.expr1())
        b  = isValue(expr.expr2())
        e1 = expr.expr1()
        e2 = expr.expr2()

        if((not a) and (not b)):
            return step(Foundation.Binary(expr.bop(),step(e1,Env),step(e2,Env)),Env)
        if(not a):
            return step(Foundation.Binary(expr.bop(),step(e1,Env),e2),Env)
        return step(Foundation.Binary(expr.bop(),e1,step(e2,Env)),Env)

    #Malloc Expr
    elif(case(expr,Foundation.Malloc)):
        return step(Foundation.Malloc("Var",expr.expr2(),step(expr.expr3(),Env)),Env)

    #If Expr
    elif(case(expr,Foundation.If)):
        value = expr.expr1()
        while(not isValue(value)):
            value = step(value,Env)
        return step(Foundation.If(value,expr.expr2(),expr.expr3()),Env)


    #Eq Expr
    elif(case(expr,Foundation.Eq)):
        e1 = isValue(expr.expr1())
        e2 = isValue(expr.expr2())
        
        if(e1):
            expr2 = step(expr.expr2(),Env)
            return step(Foundation.Eq(expr.expr1(),expr2),Env)
        elif(e2):
            expr1 = step(expr.expr1(),Env)
            return step(Foundation.Eq(expr1,expr.expr2()),Env)
        expr1 = step(expr.expr1(),Env)
        expr2 = step(expr.expr2(),Env)

        return step(Foundation.Eq(expr1,expr2),Env)

    #Ne Expr
    elif(case(expr,Foundation.Ne)):
        e1 = isValue(expr.expr1())
        e2 = isValue(expr.expr2())
        
        if(e1):
            expr2 = step(expr.expr2(),Env)
            return step(Foundation.Ne(expr.expr1(),expr2),Env)
        elif(e2):
            expr1 = step(expr.expr1(),Env)
            return step(Foundation.Ne(expr1,expr.expr2()),Env)
        expr1 = step(expr.expr1(),Env)
        expr2 = step(expr.expr2(),Env)

        return step(Foundation.Ne(expr1,expr2),Env)

    #Gt Expr
    elif(case(expr,Foundation.Gt)):
        e1 = isValue(expr.expr1())
        e2 = isValue(expr.expr2())
        
        if(e1):
            expr2 = step(expr.expr2(),Env)
            return step(Foundation.Gt(expr.expr1(),expr2),Env)
        elif(e2):
            expr1 = step(expr.expr1(),Env)
            return step(Foundation.Gt(expr1,expr.expr2()),Env)
        expr1 = step(expr.expr1(),Env)
        expr2 = step(expr.expr2(),Env)

        return step(Foundation.Gt(expr1,expr2),Env)

    #Lt Expr
    elif(case(expr,Foundation.Lt)):
        e1 = isValue(expr.expr1())
        e2 = isValue(expr.expr2())
        
        if(e1):
            expr2 = step(expr.expr2(),Env)
            return step(Foundation.Lt(expr.expr1(),expr2),Env)
        elif(e2):
            expr1 = step(expr.expr1(),Env)
            return step(Foundation.Lt(expr1,expr.expr2()),Env)
        expr1 = step(expr.expr1(),Env)
        expr2 = step(expr.expr2(),Env)

        return step(Foundation.Lt(expr1,expr2),Env)

    #Gt Expr
    elif(case(expr,Foundation.Ge)):
        e1 = isValue(expr.expr1())
        e2 = isValue(expr.expr2())
        
        if(e1):
            expr2 = step(expr.expr2(),Env)
            return step(Foundation.Ge(expr.expr1(),expr2),Env)
        elif(e2):
            expr1 = step(expr.expr1(),Env)
            return step(Foundation.Ge(expr1,expr.expr2()),Env)
        expr1 = step(expr.expr1(),Env)
        expr2 = step(expr.expr2(),Env)

        return step(Foundation.Ge(expr1,expr2),Env)
    
    #Lt Expr
    elif(case(expr,Foundation.Le)):
        e1 = isValue(expr.expr1())
        e2 = isValue(expr.expr2())
        
        if(e1):
            expr2 = step(expr.expr2(),Env)
            return step(Foundation.Le(expr.expr1(),expr2),Env)
        elif(e2):
            expr1 = step(expr.expr1(),Env)
            return step(Foundation.Le(expr1,expr.expr2()),Env)
        expr1 = step(expr.expr1(),Env)
        expr2 = step(expr.expr2(),Env)

        return step(Foundation.Le(expr1,expr2),Env)

    #And Expr
    elif(case(expr,Foundation.And)):
        e1 = isValue(expr.expr1())
        e2 = isValue(expr.expr2())
        
        if(e1):
            expr2 = step(expr.expr2(),Env)
            return step(Foundation.And(expr.expr1(),expr2),Env)
        elif(e2):
            expr1 = step(expr.expr1(),Env)
            return step(Foundation.And(expr1,expr.expr2()),Env)
        expr1 = step(expr.expr1(),Env)
        expr2 = step(expr.expr2(),Env)

        return step(Foundation.And(expr1,expr2),Env)
            
    #Or Expr
    elif(case(expr,Foundation.Or)):
        e1 = isValue(expr.expr1())
        e2 = isValue(expr.expr2())
        
        if(e1):
            expr2 = step(expr.expr2(),Env)
            return step(Foundation.Or(expr.expr1(),expr2),Env)
        elif(e2):
            expr1 = step(expr.expr1(),Env)
            return step(Foundation.Or(expr1,expr.expr2()),Env)
        expr1 = step(expr.expr1(),Env)
        expr2 = step(expr.expr2(),Env)

        return step(Foundation.Or(expr1,expr2),Env)

    elif(case(expr,Foundation.BitwiseOr)):
        e1 = isValue(expr.expr1())
        e2 = isValue(expr.expr2())
        
        if(e1):
            expr2 = step(expr.expr2(),Env)
            return step(Foundation.BitwiseOr(expr.expr1(),expr2),Env)
        elif(e2):
            expr1 = step(expr.expr1(),Env)
        return step(Foundation.BitwiseOr(expr1,expr.expr2()),Env)
        expr1 = step(expr.expr1(),Env)
        expr2 = step(expr.expr2(),Env)
        
        return step(Foundation.BitwiseOr(expr1,expr2),Env)

    elif(case(expr,Foundation.BitwiseAnd)):
        e1 = isValue(expr.expr1())
        e2 = isValue(expr.expr2())
        
        if(e1):
            expr2 = step(expr.expr2(),Env)
            return step(Foundation.BitwiseAnd(expr.expr1(),expr2),Env)
        elif(e2):
            expr1 = step(expr.expr1(),Env)
        return step(Foundation.BitwiseAnd(expr1,expr.expr2()),Env)
        expr1 = step(expr.expr1(),Env)
        expr2 = step(expr.expr2(),Env)
        
        return step(Foundation.BitwiseAnd(expr1,expr2),Env)


    #Assign Expr
    elif(case(expr,Foundation.Assign)):
        return step(Foundation.Assign(expr.expr1(),step(expr.expr2(),Env)),Env)

    #Index Expr
    elif(case(expr,Foundation.Index)):
        index = step(expr.expr2(),Env)
        return step(Foundation.Index(expr.expr1(),index),Env);
    else:
        print("Uncaught parse step:"+str(expr))
        return Foundation.Null()




