from random import *
from fractions import *
import decimal
import math

class rsa:
    def __init__(self,x=0,bits=1024):    
        self.bits=bits      #set number of bits
        if x==0:
            pass
        else:
            self.generate_keys()
    
    def get_keys(self):     #return original keys
        return self.p,self.q
    
    def set_keys(self,p,q):
        self.p=long(math.fabs(p))
        self.q=long(math.fabs(q))
                       
        self.n=self.p*self.q
        euler=(self.p-1)*(self.q-1)    
        
        self.e=65537
        x=self.eea(self.e,euler)
        self.d=x[0]%euler
    
         
    def rand_prime(self,bits):
        ok=0
        nr=0
        while ok==0:
            p=randrange(pow(2,bits-1),pow(2,bits)-1,2)-1   #random odd number
            ok=self.miller_rabin(p,10)                     #check primality
            nr+=1
        print "\t",nr,"tries"
        return p
        
    def rand(self,bits):
        return randrange(pow(2,bits-1),pow(2,bits)-1)
    
    def generate_keys(self):
        ok=0
        nr=0
        #print "Generating p"
        while ok==0:                    #random odd number
            self.p=randrange(pow(2,self.bits),pow(2,self.bits+1),2)+1   
            ok=self.miller_rabin(self.p,10)            #check primality
            nr+=1                                      #number of tries 
        ok=0
        #print "\t",nr,"tries"
       # print "Generating q"
        nr=0
        if 2*self.p>pow(2,self.bits+1):             # p<q<2p
            limit=pow(2,self.bits+1)
        else:
            limit=2*self.p
        while ok==0:
            self.q=randrange(pow(2,self.bits),limit,2)+1
            ok=self.miller_rabin(self.q,10)
            nr+=1
       # print "\t",nr,"tries"
        self.n=self.p*self.q
        euler=(self.p-1)*(self.q-1) 

       # print "Generating private key"
        
        
        self.e=65537
        x=self.eea(self.e,euler)
        self.d=x[0]%euler
                
        #print "Done"
        
     
    def imod(self,x,n):     #Modular Inverse of x in Zn
        return self.eea(x,n)[0]%n
      
    def request_public_key(self):
        return self.e,self.n

    def encrypt_message(self,m,p_key):
        return pow(m,p_key[0],p_key[1])
    
    def decrypt_message(self,c):
        return pow(c,self.d,self.n)
      
    def eea(self,u, v):     #extended Euclid Algorithm
        u1 = 1
        u2 = 0
        u3 = u
        v1 = 0
        v2 = 1
        v3 = v
        ls=[]
        while v3 != 0:
            q = u3 / v3
            ls.append(q)
            t1 = u1 - q * v1
            t2 = u2 - q * v2
            t3 = u3 - q * v3
            u1 = v1
            u2 = v2
            u3 = v3
            v1 = t1
            v2 = t2
            v3 = t3
        return u1, u2, u3,ls
    
    def miller_rabin(self,n,k): #miller_rabin test for primality
        s=0
        d=n-1
        while 1:
            if d%2==0:
                s+=1
                d=d/2
            else:
                break
        
        for o in range(1,k):
            ok=0
            a=randint(2,n-2)
            x=pow(a,d,n)
            if x==1 or x==n-1:
                continue
            else:
                for p in range(1,s-1):
                    x=pow(x,2,n)            
                    if x==1:
                        return 0
                    if x==n-1:
                        ok=1
                        break
                if (ok==0):
                    return 0
                else:
                    continue
        return 1
        
    
