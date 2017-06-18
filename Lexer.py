from re import sub

class LexerClass():
    def __init__(self):
        self.lp = 0
        self.rp = 0
        self.stackFrame = []
    def lexer(self,stream):
        #Remove multiple spaces between tokens
        stream = sub("\s+"," ",stream)
        tokens = []
        inScope = 0
        inString = 0
        l = 0
        r = 0
        while(self.rp < len(stream)):
            #Space
            if(stream[r] == ' ' and not inString):
                if(stream[l:r] != ''):
                    tokens.append(stream[l:r])
                r += 1
                l = r
                self.rp += 1
                self.lp = self.rp
            #;
            elif(stream[r] == ';' and not inString):
                if(stream[l:r] != ''):
                    tokens.append(stream[l:r])
                tokens.append(';')
                r += 1
                l = r
                self.rp += 1
                self.lp = self.rp
                if(not inScope):
                    self.stackFrame = self.stackFrame + [tokens[:]]
                    tokens.clear()
            #"
            elif(stream[r] == '"'):
                if(inString):
                    inString = 0
                    tokens.append(str(stream[l-1:r+1]))
                else:
                    inString = 1

                r += 1
                l = r
                self.rp += 1
                self.lp = self.rp
            #(
            elif(stream[r] == '(' and not inString):
                if(stream[l:r] != ''):
                    tokens.append(stream[l:r])
                tokens.append('(')
                inScope += 1
                r += 1
                l = r
                self.rp += 1
                self.lp = self.rp

            #)
            elif(stream[r] == ')' and not inString):
                if(stream[l:r] != ''):
                    tokens.append(stream[l:r])
                tokens.append(')')
                inScope -= 1
                r += 1
                l = r
                self.rp += 1
                self.lp = self.rp
            #{
            elif(stream[r] == '{' and not inString):
                if(stream[l:r] != ''):
                    tokens.append(stream[l:r])
                tokens.append('{')
                inScope += 1
                r += 1
                l = r
                self.rp += 1
                self.lp = self.rp
            #}
            elif(stream[r] == '}' and not inString):
                if(stream[l:r] != ''):
                    tokens.append(stream[l:r])
                tokens.append('}')
                inScope -= 1
                r += 1
                l = r
                self.rp += 1
                self.lp = self.rp

            #Logical Ops Or,And,Xor,Le,Ge,Eq,Ne
            elif(stream[r:r+2] in ["||","&&","^^","<=",">=","==","!=","~>","<<",">>"] and not inString):
                if(stream[l:r] != ''):
                    tokens.append(stream[l:r])
                tokens.append(stream[r:r+2])
                r += 2
                l = r
                self.rp += 2
                self.lp = self.rp
            #+,>,<,!
            elif(stream[r] in ['+','-','*','/','=','%','>','<','!','[',']',',','&','|','~'] and not inString):
                if(stream[l:r] != ''):
                    tokens.append(stream[l:r])
                tokens.append(stream[r])
                r += 1
                l = r
                self.rp += 1
                self.lp = self.rp

            else:
                r += 1
                self.rp += 1

        #if(tokens != []):
        #    self.stackFrame.append(tokens)



#acorn = LexerClass()
#print(acorn.lexer("print(\"Hello World\");"))
#print(acorn.stackFrame)
#
