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
For this assignment I used an Ubuntu machine with VirtualBox.

For the creation I used a RSA 2048 bit encryption. 1024 is not as safe and 4096 takes longer. It can be seen in the screenshot provided below.
<img width="1283" height="488" alt="image" src="https://github.com/user-attachments/assets/6c686a69-adb7-4fee-ae72-386e781b5435" />

Information stored in the private .pem file is n, e, d and p and q.
Information stored in the public .pem file is n and e. There are no private values in there.

## 1.4 RSA encryption in OpenSSL
The public key taken from teams from Seungeun Lee for an encrypted ciphertext is the following:

-----BEGIN PUBLIC KEY-----
MIIBIDANBgkqhkiG9w0BAQEFAAOCAQ0AMIIBCAKCAQEAw7IAnXwDVrYVmmJz46Xr
BIfN44827PLXH1/B/ZkUgTkANV3iEraI/P9azmmrGvVm0YNxcBC4K59zKsoHEW/i
KktgVgWfTtoR5aBWBc7VviVeywbl9GyqWZYmV0UCOQd4TkN0GCWjF11dy8yIYnF6
oO5srUPQF9pbfMVwr7IMvoSeMdgvXg8nTWV4yBXOK+yL+H/yqX/VUU6Jel6LPOjy
92OYq0lHgjsGJaUpjLq6MrxQwf+lyzj90xx53OyYhrcpE4c9tcFjt11n1+xW3Wep
AVC5f0XcR4FRdIu9HjN0Kq+v7kmmknmqhgiUlgz9h2P+j1L8D8iqdm11gcE5I5L+
IQIBAw==
-----END PUBLIC KEY-----

In the picture below, it can be seen how I used OpenSSL on my virtual machine to encrypt a message for Seungeun Lee 
<img width="1046" height="357" alt="image" src="https://github.com/user-attachments/assets/fdedfbd8-89b9-4304-82a9-dc540ff14d51" />

# 2. Reflection

## 2.1 What did I learn

This week I learnt more about how RSA works and how public and private keys are generated. By manually calculating the RSA values, I got a better understanding of how the prime numbers, phi(n) and the exponents are connected together. I also got more experience using OpenSSL on Linux to generate keypairs and encrypt messages using another person’s public key.

## 2.2 Issues and Solutions

One issue I had was calculating the value for d manually, because it became confusing quite quickly. I solved this by using Python and the pow() function, which made the calculations a lot easier to understand.

I also had some small issues with OpenSSL commands at first, mainly because different commands are needed depending on the key or file being used. After testing a few commands and checking the outputs carefully, I managed to get everything working properly.

## 2.3 How did I improve

I improved my understanding of public key cryptography and became more comfortable using RSA in both manual calculations and OpenSSL. I also improved my Linux terminal skills and got more confident using encryption related commands on my Ubuntu virtual machine.
