from poly import *
from fractions import *

q=poly([1,2,1])
p=poly([2,-1,0,1])
k=poly([1,1])
#print p.c
#print q.c
x=p*q
#print x.c

k=(k/2)/2


print k(0),k(1),k(2),k(3),k(4)

print lagrange([(2,1942),(4,3402),(5,4414)]).c

