<!-- GETTING STARTED -->
## RSA Birthday Attack
 
The program:
- Computes the hashes of 16 sets of 3 random prime numbers less than 28 by performing a bitwise XOR operation
- Bruteforces its way with different sets of 3 fraudulent composite numbers less than 28 until it finds a set {c1, c2, c3} with a hash value that matches one of the hashes computed above- the matching set is referred to as {p1, p2, p3}. 
- Demonstrates that in a real-world attack, the legitimate prime set {p1, p2, p3} is replaced with the fraudulent composite set {c1, c2, c3}. The bitwise XOR automatic signing process of the prime set {p1, p2, p3} can be appended to the composite set {c1,  c2,  c3} without  knowing the RSA's  private  key  and  by  
computing just over 16 hashes


<!-- CONTRIBUTING -->
## SHA 256 Birthday Attack
The program: 
- Computes the hashes of 16 sets of 3 random prime numbers less than 28 by performing a SHA-256 operation
- Computes 1000 different sets of 3 fraudulent composite numbers less than 28 by performing a SHA-256 operation and checks all 16 sets to try and find a match until it finds a set {c1, c2, c3} with a hash value that matches one of the hashes computed above
- It does not find a collision because with SHA-256, it is hard. 2128  hash  values would need to be generated to  find  a SHA256 collision which in a regular laptop would take approximately 58.88  septillion  years.

### Built With

* [Cryptography.io](https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/)
* [Sympy](https://www.sympy.org/en/index.html)
