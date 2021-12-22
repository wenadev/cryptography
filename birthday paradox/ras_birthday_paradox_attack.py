import random
from sympy import isprime


#create set of good/fradulent messages
def create_set(x):
    #create a list of numbers
    numbers = list(range(1, 255))  
    
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
    hashed = 0
    #create good/fradulent messages (list of 3 random prime/composite numbers)
    s_num = []
    
    for i in range(3):
        #random value from prime/composite set
        num = numbers[random.randrange(0, len(numbers))]
        s_num.append(num)
        
        #xor operation
        hashed = hashed ^ num
        
    #return the set of 3 numbers and corresponding hashed value 
    return tuple(s_num), hashed


print("16 valid messages: ")
 
valid_dict = {}

print_ = 0
#create 16 good messages
for i in range(16):
    #create
    valid_num, valid_hash = hash_comp(create_set(True))
    valid_dict[valid_num] = valid_hash
    
    print("{ %d, %d, %d } || { %s }" %(valid_num[0], valid_num[1], valid_num[2], valid_hash))


attempt = 1

print("\nllooking for a fraudulent message that matches a valid message's hash...")

loop = True
while loop:
    fraud_set, fraud_hash = hash_comp(create_set(False))
    
    if fraud_hash in valid_dict.values():
        #loop to retrieve the corresponding prime set to collision hash
        for prime_set, prime_hash in valid_dict.items():
            if(fraud_hash == prime_hash):  
                  print("collision found after { %s } attempts: \n{ %d, %d, %d } ||  { %s } \n{ %d, %d, %d } || { %s }" 
                     %(attempt,  fraud_set[0], fraud_set[1], fraud_set[2], fraud_hash, prime_set[0], prime_set[1], prime_set[2], prime_hash))
                  input("Press any key to continue.....\n")
                  loop = False
                  break
        break
                
    attempt += 1

