from rsa import *

print "Alice"
Alice=rsa(1,0,512)
print "Alice is ready"

print "Bob"
Bob=rsa(1,1,512)
print "Bob is ready"

print "Bob requests Alice's public key"
public=Alice.request_public_key()
c=Bob.encrypt_message(55778896654455662555544488779987782554,public)
print "Encrypted: ",c
print "Alice decrypts message with her private key"
print "Decrypted: ",Alice.decrypt_message(c)
print "\n\n"

p,q=Alice.wiener(Bob.request_public_key())
print "------------------------------------------------------------------------"
print "Weiner deduced keys"
print "p=",p
print "q=",q

print "------------------------------------------------------------------------"
print "Bob's original keys"
p,q=Bob.get_keys()
print "p=",p
print "q=",q

##
##
##print "Alice requests Bob's public Key"
##public=Bob.request_public_key()
##print "Bob's public key is:",public[0],hex(public[1])
##
##print "Alice encrypts with Bob's public Key:"
##c=Alice.encrypt_message(123456789123456789123456789123456789123456789123456789123456789,public)
##print "Encrypted message:",hex(c)
##
##print "Bob receives message and decrypts"
##print "Decrypted message:",Bob.decrypt_message(c)
