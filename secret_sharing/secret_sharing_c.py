"""
    Class that implements the dealer side of Krawczyk's technique for 
computational-secure threshold secret sharing scheme
"""

from Crypto.Cipher import DES

from shamir_secret_c import *
from ida_secret_c import *
from prime import *



class secret_sharing_c:
    def __init__(self):
        self.ida=ida_secret_c()
        self.sha=shamir_secret_c()

    def add_share(self,x):  #add shares to list
        self.ida.add_share(x[0])
        self.sha.add_share(x[1])
        
    def reconstruct(self):  #reconstruct secret
        self.enc=long(self.ida.reconstruct())    #get encrpyted secret
        self.key=long(self.sha.reconstruct())    #get encryption key
        
        self.enc=long(abs(self.enc))        
        self.key=long(abs(self.key))
        
        self.K=bituse(self.key, 8).ascii()       #get ascii equivalent
        self.E=bituse(self.enc, 8).ascii()        
                    
        self.cryp=DES.new(self.K, DES.MODE_ECB)  
            
        return self.cryp.decrypt(self.E)    #decrypt and return
    
    def _debug(self):
        print "--------------------------------Client"
        print "E     : ",self.E
        print "E  b  : ",self.enc
        print "key   : ",self.K
        print "key b : ",self.key
        
        
        
        
        
        
    