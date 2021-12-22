from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def key_loader(file):
    with open(file, 'rb') as pem_in:
        pemlines = pem_in.read()
    key_priv = load_pem_private_key(pemlines, None, default_backend())
    
    return key_priv

message = b'secret message'

signature = b'\x1e\xde\xabn\x95\xf0\xbbv\xc37\xac=\x9eeM\xf0)\xc7 P\xb2\x8b)X\xac\xe9\x9b&\x83p\x80\x89\xbd%,Q=\xdd\xfd7\xa8j\x90\xa1\xd6\xe7\x1ef\xee\x85CLA\xb2u\xfc3\x1b5c/k\xf3\xf4'

for count in range (0,10):
    generated_key = 'private_key_'+str(count+1)+'.pem'    
    public_key = key_loader(generated_key).public_key()     
    
    # catch the exception for invalid signatures in the loop to get to the correct file 
    try:
        public_key.verify(signature,
                          message,
                          padding.PSS(mgf=padding.MGF1(hashes.SHA256()),salt_length=padding.PSS.MAX_LENGTH),
                          hashes.SHA256()
                          )
        #the key is private_key_3.pem
        print(generated_key, "matches the public key", )
        break
    except:
        continue