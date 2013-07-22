from random import *
import bigfloat
from fractions import *
import decimal

class rsa:
    def __init__(self,x,weak,bits):
        self.bits=bits      ##set number of bits
        if x==0:
            pass
        else:
            self.generate_keys(weak)
    
    def get_keys(self):     ##return original keys
        return self.p,self.q
    
    def wiener(self,public):
        q=self.eea(public[0],public[1])[3]  ##get continuous fraction
        print "Wiener Attack for:"      
        print "e:",public[0]
        print "n:",public[1]
        conv=[]                             ##start a list with convergent fractions
        for i in range(0,len(q)):
            if i==0:
                alfa=q[0]
                betta=1
            elif i==1:
                alfa=q[0]*q[1]+1            ##generate the fractions
                betta=q[1]
            else:
                alfa= q[i]*conv[i-1][0]+conv[i-2][0]
                betta=q[i]*conv[i-1][1]+conv[i-2][1]
            
            if alfa!=0:                     ##calculate the roots of the ecuation
                with decimal.localcontext() as ctx:
                    ctx.prec = 2048
                    euler=decimal.Decimal((public[0]*betta-1)/alfa)
                    b=public[1]-euler+1
                    disc=decimal.Decimal(b**2-4*public[1])
                    if disc>=0:
                        sqrdt=disc.sqrt()
                        if sqrdt.to_integral()==sqrdt:
                            x=decimal.Decimal((b-sqrdt)/2)
                            y=decimal.Decimal((b+sqrdt)/2)
                            if x.to_integral()==x and y.to_integral()==y:
                                if x*y==public[1]:      ##if the roots are integers and they are factors of "n" return
                                    return long(x),long(y)                
            conv.append((alfa,betta))
        return (0,0)    ##if no solution was found return (0,0)
        
    def generate_keys(self,weak):
        ok=0
        nr=0
        print "Generating p"
        while ok==0:
            self.p=randrange(pow(2,self.bits),pow(2,self.bits+1),2)+1   ##random odd number
            ok=self.miller_rabin(self.p,10)                             ##check primality
            nr+=1                                                       ##number of tries 
        ok=0
        print "\t",nr,"tries"
        print "Generating q"
        nr=0
        if 2*self.p>pow(2,self.bits+1):             ## p<q<2p
            limit=pow(2,self.bits+1)
        else:
            limit=2*self.p
        while ok==0:
            self.q=randrange(pow(2,self.bits),limit,2)+1
            ok=self.miller_rabin(self.q,10)
            nr+=1
        print "\t",nr,"tries"
        self.n=self.p*self.q
        euler=(self.p-1)*(self.q-1) 

        print "Generating private key"
        
        if (weak==0):
            print "\t[Weak mode OFF]"
            self.e=65537
            x=self.eea(self.e,euler)
            self.d=x[0]%euler
        else:
            print "\t[Weak mode ON]"
            ok=0
            nr=0
            t=long(bigfloat.sqrt(bigfloat.sqrt(self.n))/3)
            while ok==0:
                self.d=randrange(2,t,2)-1
                ok=self.miller_rabin(self.d,10)
                nr+=1
            print "\t",nr,"tryes"
            x=self.eea(self.d,euler)
            self.e=x[0]%euler
            
        ##print self.e*self.d%euler
        ##print fractions.gcd(self.e,self.d)
        ##print self.d<long(bigfloat.sqrt(bigfloat.sqrt(self.n))/3)
                
        print "Done"
        
     
      
    def request_public_key(self):
        return self.e,self.n

    def encrypt_message(self,m,p_key):
        return pow(m,p_key[0],p_key[1])
    
    def decrypt_message(self,c):
        return pow(c,self.d,self.n)
      
    def eea(self,u, v):
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
    
    def miller_rabin(self,n,k):
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
        
    
