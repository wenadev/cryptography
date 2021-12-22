import math

#Question (1a)

#where public key is {e = 5, n = 35} and ciphertext (c) = 10 and plaintext = ?
e = 5
n = 35

#to find the plaintext
def plaintext(M):
    c = pow(M, e, n) 
    
    if(c == 10):
        return M

#search for all values where plaintext < n
for i in range(n):
    if(plaintext(i)):
        print("Plaintext is:", plaintext(i))
        M = plaintext(i)
        break


#factors of n = 35
factors = [[1, 35], [5, 7]]

for i in range(2):
    p = (factors[i][0]) - 1
    q = (factors[i][1]) - 1
    phi = p * q
    
    #where gcd(phi(n), e) = 1; 1 < e < phi(n)
    if(math.gcd(phi, e) == 1):
        d = pow(5, -1, phi)
        print("Secret exponent is", d)
        break
    
    
