#Class that manages a string of bits from number of ASCII strings
#It add a leading padd of 0 to reach the desired bitlenght

class bituse:
    def __init__ (self,x,b=0):
        try:                            #only supports integers and strings
            if type(x) in (int,long):
                self._rep=self._add_pad(bin(x),b)
            elif type(x) is str:
                self._rep=self._s2b(x)                
            else:
                raise NameError('Does not suport '+str(type(x)))
        except NameError:
            print 'An exception flew by!'
            raise
            
    def _add_pad (self,s,n):
        s=s[2:len(s)]
        if n is not 0:
            for i in range(0,(n-len(s))%n):
                s="0"+s
            return s          
        else:
            return s
        
    def _c2b (self,c):  #represent an ASCII char on 8 bits with leading 0
        ret=bin(ord(c))
        ret=ret[2:len(ret)]
        for i in range(len(ret),8):
            ret="0"+ret
        return ret

    def _s2b (self,s):  #represents an ASCII string
        if len(s) is not 0:
            ret=""
            for i in range(0,len(s)):
                ret=ret+self._c2b(s[i])
            return ret
        else:
            return bituse(0,8).str()

    def block (self,pos,block,ord=0):   #split the string into blocks
        if (pos+1)*block<=self.len():   #ord changes the order of the bits but
            if ord is 1:                #returns them in the original order
                s=self._rep[::-1]
                return bituse(long(s[pos*block:pos*block+block][::-1],2),block)
            else:
                s=self._rep
                return bituse(long(s[pos*block:pos*block+block],2),block)
        else:
            raise NameError('Out of range')

    def str (self,ord=0):   #get the string representative
        if ord is 0:
            return self._rep
        else:
            return self._rep[::-1]
        
    def long (self,ord=0):  #get the oresponding integer value 
        if ord is 0:
            return long(self._rep,2)
        else:
            return long(self._rep[::-1],2)

    def len(self):          #get the lenght of the bitstring
        return len(self._rep)
    
    def hex (self,ord=0):   #get the hex representation
        if ord is 0:
            ret=hex(long(self._rep,2))
        else:
            ret=hex(long(self._rep[::-1],2))
        return ret[2:len(ret)-1]
    
    
            
        