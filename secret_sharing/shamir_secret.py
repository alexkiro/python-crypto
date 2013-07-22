"""
    Class that manages the dealer of a Shamir secret sharing scheme
"""

from random import *

from poly import *
from prime import *
from bituse import *

class shamir_secret:
    def __init__(self,x,n,k,b=256):
        self.field=rand_prime(b)  #the field 
        #self.field=x
        self.secret=x               #the secret we want to share
        self.k=k                    #the threshold
        self.n=n                    #number of shares
        c=[]                        #the polynomial
        
        if type(self.secret) in (long,int):  
            pass
        elif type(self.secret) is str:  #if secret is string transform to long
            b=bituse(self.secret)
            self.secret=b.long()
            #self.field=b.long()
        
        c.append(self.secret)           #append secret as free coeficient
                    
        for i in range(1,k):            #generate random polynomial coeficients
            c.append(randrange(2,self.field))       
        
        self.P=poly(c)                  #create polynomial
        
    def create_shares(self):
        self.I=[(i,self.P(i)) for i in range(1,self.n+1)]
        self.av_shares=self.I           #current available shares
        
    def share_random(self):
        ret=choice(self.av_shares)  #share a random fragment and then remove from list
        self.av_shares.remove(ret)
        return ret
          
    def _debug(self):
        print "field=",self.field
        print "secret= ",self.secret
        print "k= ",self.k
        print "n= ",self.n
        print "P -------------"
        print self.P
        print self.P.c
        print "----------------"
        print "I -------------"
        for i in self.I:  
            print i
        print "----------------"
                    
                    
            
            
                    