#Implements Digital Signature Algorithm
from rsa import *
from hash import *
from random import *
import pickle

class dss:
    def __init__ (self):
        pass
    def create_keys(self,f="k.out",gen=1): #get,or generate keys
        if gen is 1:                       #generate keys and save to f
            x=rsa()
            r=x.rand_prime(860)         #get random prime on 860b
            ok=0
            while ok is 0:
                q=x.rand_prime(160)     #get random prime on 160b
                p=2*q*r+1
                ok=x.miller_rabin(p,10) #until p=2qr+1 is prime
            ok=0
            while ok is 0:
                betta=x.rand(1024)%p    #get random betta
                if pow(betta,(p-1)/r,p) is not 1:
                    if pow(betta,(p-1)/q,p) is not 1:
                        if pow(betta,(p-1)/2,p) is not 1:                    
                            ok=1
            
            alfa=pow(betta,(p-1)/q,p)   #calculte alfa
            self.a=randrange(1,q)       #get random signing key
            betta=pow(alfa,self.a,p)    #calculate betta
                        
            file=open(f,"w+")           #save to file
            self.keys=[p,q,alfa,betta]
            pickle.dump(self.keys,file)
            pickle.dump(self.a,file)
        
        else:
            file=open(f,"r")            #load from file
            self.keys=pickle.load(file) #load public keys
            self.a=pickle.load(file)    #load private key
        
    def print_keys(self):
        print "  p   = ",self.keys[0],"\n"
        print "  q   = ",self.keys[1],"\n"
        print " alfa = ",self.keys[2],"\n"
        print "betta = ",self.keys[3],"\n"

    def get_keys(self):    #get public keys
        return self.keys
    
    def sign_message(self,m):   #sign message
        k=self.keys
        a=self.a
        x=rsa()
        h=hash(m)       #digest messasge
        d=h.digest()    

        r=randrange(0,k[1]) #get random r from (0,q)
        ri=x.imod(r,k[1])   #get modular inverse of r 
        
        gamma=pow(k[2],ri,k[0])%k[1]    #sign message
        delta=(r*(d+a*gamma))%k[1]
        ret=[gamma,delta]               #return signed message
        return ret
    
    def verify_message(self,m,s,k): #verify message, s-signature,k-public keys
        x=rsa()
        
        h=hash(m)   #digest message
        d=h.digest()
  
        inv=x.imod(s[1],k[1])   #modular inverse of delta
        e1=(d*inv)%k[1]         
        e2=(s[0]*inv)%k[1]
        o1=pow(k[2],e1,k[0])
        o2=pow(k[3],e2,k[0])
        o=((o1*o2)%k[0])%k[1]
        
        print "? - ",s[0],"==",o    #test validity
        if s[0] == o:
            print "valid"
            return 1
        else:
            print "invalid"
            return 0
        
       
        
        
        