"""
    Class that manages the client of a secret sharing scheme with information
dispersal
"""

from poly import *
from bituse import *

class ida_secret_c:
    def __init__(self):
        self.list=[]
        
    def add_share(self,x):
        self.list.append(x)
    
    def reconstruct(self):    
        P=lagrange(self.list)
        return self._extract(P)
    
    def _extract(self,X):
        S=""
        l=len(X)
        p=long(X.c[0])         #first coeficient of the polynomial is the parts size
                             
        for i in range(1,l):
            i=long(X.c[i])
            b=bituse(abs(i),p)
            S=S+b.str()
        ret=long(S,2)
        return ret 