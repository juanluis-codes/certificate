import random
from random import SystemRandom
import sympy

class RSA:
    def __init__(self):
        self.e = 65537
        self.p = RSA.random_prime_generator(1024)
        self.q = RSA.random_prime_generator(1024)
        self.n = self.p * self.q
        self.fi = (self.p - 1) * (self.q - 1)
        self.private_key_generator()

    def random_prime_generator(length):
        p = random.SystemRandom().randint(pow(2, length), pow(2, length + 1))

        if(p % 2 == 0):
            p = p + 1

        while(not(sympy.isprime(p))):
            p = p + 2
        
        return p

    def private_key_generator(self):
        x = RSA.gcd(self.e, self.fi)
        self.d = x[1] % self.fi

    def gcd(a, b):
        if b == 0:
            return 0,1,0
 
        u0 = 1
        u1 = 0
        v0 = 0
        v1 = 1
 
        while b != 0:
            q = a//b
            r = a - b * q
            u = u0 - q * u1
            v = v0 - q * v1
            # Update a, b
            a = b
            b = r
            # Update for next iteration
            u0 = u1
            u1 = u
            v0 = v1
            v1 = v
 
        return  a, u0, v0

class RSASignature:
    def __init__(self, rsakeyset = RSA()):
        self.rsakeyset = rsakeyset

    def sign(self, to_sign):
        self.signature = pow(to_sign, self.rsakeyset.d, self.rsakeyset.n)
        return self.signature

    def verify(signature, e, n):
        return pow(signature, e, n)
