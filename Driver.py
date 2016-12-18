import sys
import Lexer
import Tokenizer
import Parser
import Foundation
import Memory

WHITE = "\x1B[0m"
RED = "\x1B[31m"
MAGENTA = "\x1B[35m"
YELLOW = "\x1B[33m"
GREEN = "\x1B[32m"
CYAN = "\x1B[36m"

def Driver():
    #Get Acorn script from input
    try:
        argument = sys.argv[1]
    except:
        sys.exit(CYAN+"Acorn: "+RED+"Expected acorn script."+WHITE)

    #test to see if input type is correct
    if(not argument.lower().endswith('.acorn')):
        sys.exit("Acorn: Expected acorn file.")
    dataFile = open(argument,"r")
    #raw is a whole string which is the whole Acorn script
    raw = dataFile.read()

    acorn = Lexer.LexerClass()
    acorn.lexer(raw)

    #Send tokens to tokenizer and get an Abstract syntax tree back: ast is a 2nd array
    acornStackFrame = acorn.stackFrame
    Mem = Memory.Memory()
    for i in range(0,len(acornStackFrame)):
        subStack = acornStackFrame[i]
        #print(subStack)
        ast = Tokenizer.Tokenizer(subStack,Mem)
        #print(Mem.heap)
        astp = ast.grammar()
        #print(astp)
        Parser.step(astp,Mem,Mem)
        #print(str(Mem.heap)+"heap")
        #print(str(Mem.stack)+"stack")
    dataFile.close()
Driver()
