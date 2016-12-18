from sys import exit

class Memory():
    def __init__(self):
        self.stack = {}
        self.heap = {}
        self.variableNames = []
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
