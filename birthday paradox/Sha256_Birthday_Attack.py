# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:26:42 2021

@author: Temitayo Hayes
Student number: 100794977
"""

import random
from sympy import isprime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


#create set of good/fradulent messages
def create_set(x):
    #create a list of numbers
    numbers = list(range(1, 256))  
    
    prime_numbers = []
    composite_numbers = []
    
    #generate list of prime numbers
    if(x == True):
        for num in numbers:
            #filter out prime numbers
            if(isprime(num)):
                prime_numbers.append(num)
        return prime_numbers   
       
        
    #generate list of composite numbers
    elif(x == False):
        for num in numbers:
            #filter out composite numbers
            if(isprime(num) == False):
                composite_numbers.append(num)
                
        return composite_numbers
    
    
#function to perform hashed computation of composite/prime set
def hash_comp(numbers):
        
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    
    #create good/fradulent messages (list of 3 random prime/composite numbers)
    s_num = []
    
    for i in range(3):
        #random value from prime/composite set
        num = numbers[random.randrange(0, len(numbers))]
        s_num.append(num)
        
        digest.update(str(num).encode())
    
    hashed = digest.finalize()
    
    #return the set of 3 numbers and corresponding hashed value 
    return tuple(s_num), hashed

 
valid_dict = {}
print("16 valid messages: ")

#create 16 good messages
for i in range(16):
    valid_num, valid_hash = hash_comp(create_set(True))
    valid_dict[valid_num] = valid_hash
    
    print("{ %d, %d, %d } || { %s }" %(valid_num[0], valid_num[1], valid_num[2], valid_hash))

    
print("\n10 fraudulent messages: ")

print_ = 0
fraud_dict = {}

#create 1000 fraud messages
for i in range(1000):
    fraud_num, fraud_hash = hash_comp(create_set(False))
    fraud_dict[fraud_num] = fraud_hash



attempt_index = 0

print("looking for a fraudulent message that matches a valid message's hash...")


while attempt_index <= 1000:
    
    for fraud_set, fraud_hash in fraud_dict.items():
        if attempt_index < 10:
            print("Attempt %s with { %d, %d, %d } || { %s }" %(attempt_index+1, fraud_set[0], fraud_set[1], fraud_set[2], fraud_hash))
         
        
        if fraud_hash in valid_dict.values():
            
            print("collision found after { %s } attempts: \n{ %d, %d, %d } || hash-- { %s }\n{ %d, %d, %d } || { %s }" 
                  %(attempt_index, fraud_set[0], fraud_set[1], fraud_set[2], fraud_set, valid_dict[fraud_hash][0], valid_dict[fraud_hash][1], 
                                                                                valid_dict[fraud_hash][2], fraud_hash))
            input("Press any key to continue.....\n")
            break
        attempt_index += 1  
        
    print("\n%s  attempts made, no collision was found " %(attempt_index))
    break

input("Press any key to continue.....\n")



