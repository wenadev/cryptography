import string
import random
from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms

tag = b's\xaf\x12\n\xdc\xc6\x16~\xd0\xcaI\xf3o\x9au0'
message = b"message to authenticate"
partial_key = b'0123456789abcd'


def randLetter():
     return ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation ) for n in range(2)])
    


bruteforce= True
count = 0
while bruteforce:
    a = randLetter()
    key_attempt = partial_key + a.encode()
    
    c = cmac.CMAC(algorithms.AES(key_attempt))
    c.update(message)
    
    hash_attempt = c.finalize()
    
    if(hash_attempt == tag):    
        #the last two bytes are i/
        #the full key is b'0123456789abcdi/'
        print("The missing bytes are: ",a)
        print("The full key is: ", key_attempt)
        bruteforce = False
    count += 1