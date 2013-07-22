"""
    Class that implements the dealer side of Krawczyk's technique for 
computational-secure threshold secret sharing scheme
"""

from Crypto.Cipher import DES

from shamir_secret import * 
from ida_secret import *
from prime import *
from bituse import *

class secret_sharing:
    def __init__(self,m,n,k):
               
        self.secret=self._pad(m)                    #the secret    
        self.key=rand_ascii(8);                     #generate random key
        
        self.cryp=DES.new(self.key, DES.MODE_ECB)    
        self.S=self.cryp.encrypt(self.secret);      #use key to encrypt message
        
        self.ida_sh=ida_secret(self.S, n, k)        #create new secret sharing object with information dispersal
        self.sha_sh=shamir_secret(self.key, n, k)   #create new secret sharing object with Shamir's Scheme
                
        self.ida_sh.create_shares()                 #create respective shares
        self.sha_sh.create_shares()
    
    def share_random(self): #return a random pair of shares
        return self.ida_sh.share_random(),self.sha_sh.share_random()    
    
    def _pad(self,m):
        if len(m)%8 is not 0:
            for i in range(0,8-len(m)%8):
                m+=chr(0)
        return m
            
        
    
    def _debug(self):
        print "--------------------------------Dealer"
        print "Secret: ",self.secret
        print "S     : ",self.S
        print "S   b : ",bituse(self.S).long()
        print "key   : ",self.key
        print "key b : ",bituse(self.key).long() 
        #self.ida_sh._debug()
        #self.sha_sh._debug()
         
        