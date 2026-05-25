# COIT13240 Journal - Week 05

# 1. Tutorial Activities

## 1.1 RSA Key Generation

For the prime numbers I chose 
p = 181
q = 191

n = 181 * 191 = 34571
Phi(n) = (p-1)*(q-1)
Phi(n) = 34200

gcd(e,phi(n)) = 1
So e equals 7
(gcd(7,34200) = 1)

For finding d, I used an only python machine for the pow() function.
d =pow(7,-1,phi(34200)) results in 14657.

The public key = {e=7, n= 34571}
the private key = {d=14657, n=34571}
All the values you have to keep secret are p, q and d.
Others may know e and n.

PU{name=AlexHall,e=7,n=34571}

## 1.2 RSA encryption and decryption

## 1.3 RSA Keys in OpenSSL

