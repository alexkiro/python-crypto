"""
    Class that implements polynomials and different operation between them
"""

from fractions import *
from copy import *

class poly:
    def __init__(self,coefs):
        if type(coefs) is list:
            self.c=coefs
        else:
            self.c=[coefs]
    def __len__ (self):     #return rank of polynomial
        return len(self.c)
    def __str__ (self):     #for print
        p=0
        S=""
        for i in self.c:
            S+=str(i)+"x ^"+str(p)+"  "
            p+=1
        return S
    def __add__(self,other):        #adding two polynomials
        if len(self)>=len(other):
            c=deepcopy(self.c)
            f=deepcopy(other.c)               
        else:
            c=deepcopy(other.c)
            f=deepcopy(self.c)
        for i in range(0,len(f)):
            c[i]+=f[i]
        return poly(c)
    def __mul__(self,other):    #multiplying two polynomials
        ret=poly(0)
        for i in range(0,len(self)):
            new_poly=deepcopy(other.c)
            for j in range(0,len(other)):
                new_poly[j]*=self.c[i]
            for j in range(0,i):
                new_poly.insert(0,0)
            p=poly(new_poly)
            ret=deepcopy(ret+p)
        return ret
    def __div__(self,other):    #dividing a polynomial with a scalar and saving them in Fraction form
        ret=deepcopy(self)
        for i in range(0,len(ret)):
            ret.c[i]=Fraction(ret.c[i],other)
        return ret
    def __call__(self,x):       #the polynomial acts like a functions and it's called
        p=0
        S=0
        for c in self.c:
            S+=c*pow(x,p)
            p+=1
        return S

def lagrange(list):             #lagrange interpolation
    ret=poly(0)
    for i in list:
        n=poly(i[1])
        d=1
        for j in list:
            if j is not i:
                n=n*poly([-j[0],1])
                d*=i[0]-j[0]
        p=n/d
        ret=ret+p
    return ret
                
                
                
                
                
                
                
                
                
                
            
                
        