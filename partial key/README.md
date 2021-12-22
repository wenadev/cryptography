<!-- CMAC -->
## CMAC

The program bruteforces to find the last two bytes of the partial AES-128 CMAC key

Given: 
- complete CMAC tag = b's\xaf\x12\n\xdc\xc6\x16~\xd0\xcaI\xf3o\x9au0' 
- complete message = b"message to authenticate" 
- partial key missing last two bytes = b'0123456789abcd'


<!-- MD5 -->
## MD5

The program bruteforces to find the last two bytes of the partial DES key

Given: 
- complete MD5 hash = b'\x1dP\x00q6\x0b5\x96\x1b\x86\x90\xa57\xc2\xcb\x1a'
- partial DES key missing last two bytes = b'dh$g.u'

### Built With

* [Cryptography.io](https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption/)

