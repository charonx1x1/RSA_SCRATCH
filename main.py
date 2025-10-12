import math
import random
from sympy import randprime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(n):
    p = randprime(1<<n-1,(1<<n)-1)
    q = randprime(1<<n-1,(1<<n)-1)
    return p, q

def mod_inverse(e, phi):
    d = pow(e, -1, phi)
    return d

def calculate_phi(p, q):
    return (p-1)*(q-1)

def generate_e_d(p, q):
    phi = calculate_phi(p, q)
    e = random.randint(3, phi-1)
    while math.gcd(e, phi) != 1:
        e = random.randint(3, phi-1)
    d = mod_inverse(e, phi)
    return e, d

def encrypt(m, e, N):
    return pow(m, e, N)

message = "hi user"
p, q = generate_prime(200)
e, d = generate_e_d(p, q)
message_encoded = message.encode("ascii")
cipher = [pow(c,e,p*q) for c in message_encoded]
message_encoded_decrypted = [pow(c,d,p*q) for c in cipher]
message_decoded = "".join(chr(element) for element in message_encoded_decrypted)
print("Public Key: ",e)
print("Private Key: ",d)
print("N :", p*q)
print("P :", p)
print("Q :", q)
print("Cipher: ", cipher)
print("Message: ", message_decoded)

