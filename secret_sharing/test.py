from shamir_secret import *
from shamir_secret_c import *
from ida_secret import *
from ida_secret_c import *
from bituse import *

S=shamir_secret("Hello World and Goodbye World", 100, 3)
S.create_shares()

s=shamir_secret_c()
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())

print bituse(s.reconstruct(),8).ascii()

S=ida_secret("Hello World and Goodbye World", 100, 3)
S.create_shares()

s=ida_secret_c()
s.add_share(S.share_random())
s.add_share(S.share_random())
s.add_share(S.share_random())

print bituse(s.reconstruct(),8).ascii()
