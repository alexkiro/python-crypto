"""
    Class that manages the client of a Shamir secret sharing scheme
"""

import decimal
from fractions import *

from poly import *

class shamir_secret_c:
    def __init__(self):
        self.list=[]
        
    def add_share(self,x):
        self.list.append(x)

    def reconstruct(self):
        P=lagrange(self.list)
        return long(P.c[0])