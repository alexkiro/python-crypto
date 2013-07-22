"""
    Class that manages the dealer of a secret sharing scheme with information
dispersal
"""

from random import *

from poly import *
from bituse import *


class ida_secret:
    def __init__(self,x,n,k):
        self.secret=x           #the secret
        self.n=n                #the number of shares
        self.k=k                #the threshold
        if type(self.secret) in (long,int):
            pass
        elif type(self.secret) is str:
            b=bituse(self.secret)
            self.secret=b.long()
        l=len(bin(self.secret))-2         #lenghst of secret
        p=l/(k-1)+(l%(k-1)!=0)            #lenght of the parts of the secret
        b=bituse(self.secret,p*(k-1))     #bit representation
        c=[]                              #vector representation
        self.I=[]
        c.append(p)                       #first coeficient is the size
        for i in range(0,k-1):            #split into blocks 
            blk=b.block(i,p)              #and add to vector
            c.append(blk.long())
                
        self.P=poly(c)                    #create polynomial from vector
    
    def create_shares(self):
        self.I=[(i,self.P(i)) for i in range(1,self.n+1)]
        self.av_shares=self.I             #current available shares
    
    def share_random(self):
        ret=choice(self.av_shares)  #share a random fragment and then remove from list
        self.av_shares.remove(ret)
        return ret
          
        
    def _debug(self):
        print "secret= ",self.secret
        print "k= ",self.k
        print "n= ",self.n
        print "P=\n",self.P
        print self.P.c
       
        print "Shares ----------"
       
        for i in self.I:
            print i
          
        print "-----------------"
       
       
        
        
        
        
            
            
        
            
            
        
        