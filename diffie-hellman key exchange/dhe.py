# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 21:48:32 2021

@author: Temitayo
"""
#common prime (q) = 11 and primitive root (A) = 2
q = 11
alpha = 2

#Question (2a)- find A's private key while A's public key = 9
a_Y = 9

def private_key(key, pub_key):
    #check if computation equals public key
    comp = pow(alpha, key, q)
    
    if (comp == pub_key):
        return key


for exp in range(q):
    if(private_key(exp, a_Y)):
        
        #A's private key
        a_X =  private_key(exp, a_Y)
        
        print ("A's private key is:", a_X)
        break
        

#Question (2b)- find shared secret key while B's public key = 3
b_Y = 3


#find B's private key first
for exp in range(q):
    if(private_key(exp, b_Y)):
        
        #B's private key
        b_X = private_key(exp, b_Y)
        break
        
        
# find shared secret key with a's public key, b's private key and common prime (q)
K = pow(a_Y, b_X, q)
print("Secret shared key is", K)