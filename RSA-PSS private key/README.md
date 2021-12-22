<!-- GETTING STARTED -->
## Getting Started

Given:
- A hidden 'message' has been signed with RSA-PSS
- Signature = b'\x1e\xde\xabn\x95\xf0\xbbv\xc37\xac=\x9eeM\xf0)\xc7 P\xb2\x8b)X\xac\xe9\x9b&\x83p\x80\x89\xbd%,Q=\xdd\xfd7\xa8j\x90\xa1\xd6\xe7\x1ef\xee\x85CLA\xb2u\xfc3\x1b5c/k\xf3\xf4'

The program:
- Loads 10 pem keys from local directory and finds what private key matches the public key by verfiying the signature


### Built With

* [Cryptography.io](https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/)
