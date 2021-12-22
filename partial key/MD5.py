
import string
import random
from cryptography.hazmat.primitives import hashes

hashed = b'\x1dP\x00q6\x0b5\x96\x1b\x86\x90\xa57\xc2\xcb\x1a'
partial_y = b'dh$g.u'


def randLetter():
     return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(2)])
    
    
digest = hashes.Hash(hashes.MD5())
bruteforce= True
count = 0
while bruteforce:
    a = randLetter()
    text_attempt = partial_y + a.encode()
    digest = hashes.Hash(hashes.MD5())
    digest.update(text_attempt)
    
    hash_attempt = digest.finalize()
    
    if(hash_attempt == hashed):    
        #the last two bytes are j#
        #the full key is b'dh$g.uj#
        print("The missing bytes are: ",a)
        print("The full DES key is: ", text_attempt)
        bruteforce = False
    count += 1