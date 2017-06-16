class Memory():
    def __init__(self):
        #Depricate
        self.stack = {}
        self.heap = {}
        #Depricate
        self.variableNames = []
        self.Env = [{}]
    
    def malloc(self,x,v):
        l = len(self.Env)
        (self.Env[l-1])[x] = v
    
    def requestVar(self,x):
        l = len(self.Env)
        i = l-1
        stk = (self.Env[i]).get(x,None)
        while(stk == None and (i)>-1):
            stk = (self.Env[i]).get(x,None)
            i = i-1
        return stk

    def assignVar(self,x,v):
        l = len(self.Env)
        i = l-1
        stk = (self.Env[i]).get(x,None)
        if(stk != None):
            ((self.Env)[i])[x] = v
            return
        while(stk == None and (i)>-1):
            stk = (self.Env[i]).get(x,None)
            i = i-1
        i = i+1
        if(stk != None):
            ((self.Env)[i])[x] = v
            return
        return None
    
    def popLocalStack(self):
        (self.Env).pop()
    
    def pushLocalStack(self):
        (self.Env).append({})
    
    #Depricated
    def alloc(self,m,x,v):
        if(m == "Var"):
            self.heap[x] = v
        else:
            self.stack[x] = v
    def stackCall(self,x):
        callStack = self.stack.get(x,"DNE")
        return callStack
    def heapCall(self,x):
        callHeap = self.heap.get(x,"DNE")
        return callHeap
