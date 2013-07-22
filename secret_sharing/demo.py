from secret_sharing import *
from secret_sharing_c import *

S=secret_sharing("The quick brown fox jumps over the lazy dog",100,6)
##S._debug()

s=secret_sharing_c()
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())



print "Reconstructed: ",s.reconstruct()


##s._debug()
