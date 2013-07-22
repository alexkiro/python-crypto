#Implements SHA-1
from bituse import *
class hash:
    def __init__(self,x):
        temp=bituse(x)              #get bitstring representation
        if temp.len() % 512 != 0:   #pad if necessary
            self.m=self.pad(temp)
        else:
            self.m=temp
           
        
    def pad (self,t):           #padding message
        l=t.len()   
        x=t.long()
        x=(x<<1) | 1            #add 1 at the end
        k=(448-l-1)%512 
        x=x<<k                  #add k 0
        x=(x<<64) | l           #add lenght of message
        return bituse(x,512)    #return bitstring representation of message
                                #padded to 512 or multiple of 512
                                #if any leading 0 where eliminated
    def digest(self):
        n=self.m.len()/512
        H=[[ 0 for j in range(0,5)] for i in range(0,n+1) ]
        H[0][4]=0xc3d2e1f0      #initial hash values
        H[0][3]=0x10325476
        H[0][2]=0x98badcfe
        H[0][1]=0xefcdab89
        H[0][0]=0x67452301

        W=[0 for i in range(0,80)]  
        
        for i in range(1,n+1):
            #prepare block message list
            for j in range(0,16):
                W[j]=self.m.block(j+(n-1)*16,32).long()
            for j in range(16,80):
                W[j]=self.circ_sh(W[j-3]^W[j-8]^W[j-14]^W[j-16],1)
            a=H[i-1][0]
            b=H[i-1][1]    
            c=H[i-1][2]
            d=H[i-1][3]
            e=H[i-1][4]
            for j in range(0,80):
                T=(self.circ_sh(a,5)+self.f(b,c,d,j)+e+self.K(j)+W[j])%2**32
                e=d
                d=c
                c=self.circ_sh(b,30)
                b=a
                a=T
            H[i][0]=(a+H[i-1][0])%2**32
            H[i][1]=(b+H[i-1][1])%2**32
            H[i][2]=(c+H[i-1][2])%2**32
            H[i][3]=(d+H[i-1][3])%2**32
            H[i][4]=(e+H[i-1][4])%2**32
        hs=[H[n][0],H[n][1],H[n][2],H[n][3],H[n][4]]
        self.dg=hs
        ##self.dig=hs[0]*hs[1]*hs[2]*hs[3]*hs[4]
        self.dig=long(str(hex(hs[0]))[2:10]+str(hex(hs[1]))[2:10]+str(hex(hs[2]))[2:10]+str(hex(hs[3]))[2:10]+str(hex(hs[4])[2:10]),16)        
        return self.dig        
    
    def print_digest (self): #show digested message
        x=hex(self.dg[0])
        print x[2:len(x)-1]," ",
        x=hex(self.dg[1])
        print x[2:len(x)-1]," ",
        x=hex(self.dg[2])
        print x[2:len(x)-1]," ",
        x=hex(self.dg[3])
        print x[2:len(x)-1]," ",
        x=hex(self.dg[4])
        print x[2:len(x)-1]
    
    def circ_sh (self,x,n): #circular left shift ROTL
        return ((x << n) | (x >> 32-n)) & pow(2,32)-1
    
    def f (self,x,y,z,t):   
        if t in range(0,20):
            return (x&y)^(~x&z)
        elif t in range(20,40) or t in range(60,80):
            return x^y^z
        elif t in range(40,60):
            return (x&y)^(x&z)^(y&z)
        
    def K (self,t):
        if t in range(0,20):
            return 0x5a827999
        elif t in range(20,40):
            return 0x6ed9eba1
        elif t in range(40,60):
            return 0x8f1bbcdc
        elif t in range(60,80):
            return 0xca62c1d6

        
        
 

