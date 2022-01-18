<!-- GETTING STARTED -->
## XOR Birthday Attack
 
The program:
- Computes the hashes of 16 sets of 3 random prime numbers less than 28 by performing a bitwise XOR operation
- Bruteforces its way with different sets of 3 fraudulent composite numbers less than 28 until it finds a set {f1, f2, f3} with a hash value that matches one of the prime hashes computed above- the matching set is referred to as {v1, v2, v3}. 
- Demonstrates that the legitimate prime set {v1, v2, v3} can be replaced with the fraudulent composite set {f1, f2, f3}. 
That is, the bitwise XOR hashing of the valid (prime) set {v1, v2, v3} can be appended to the frauduelent (composite) set {f1, f2, f3} by computing just over 16 hashes.


<!-- CONTRIBUTING -->
## SHA 256 Birthday Attack
The program: 
- Computes the hashes of 16 sets of 3 random prime numbers less than 28 by performing a SHA-256 operation
- Computes 1000 different sets of 3 fraudulent composite numbers less than 28 by performing a SHA-256 operation and checks all 16 sets to try and find a match until it finds a set {f1, f2, f3} with a hash value that matches one of the prime hashes computed above
- It does not find a collision because with SHA-256, it is hard. 
That is, 2 (to the power of 128) hash values would need to be generated to find a SHA256 collision which in a regular laptop would take approximately 58.88  septillion  years.

### Built With

* [Cryptography.io](https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/)
* [Sympy](https://www.sympy.org/en/index.html)
