from dss import *

d=dss()
d.create_keys("k3.out",0)

sign=d.sign_message("The quick brown fox jumps over the lazy dog")

d.verify_message("The quick brown fox jumps over the lazy dog",sign,d.get_keys())
d.verify_message("The quick crown fox jumps over the lazy dog",sign,d.get_keys())











