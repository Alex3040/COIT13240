# COIT13240 Journal - Week 06

# 1. Tutorial Activities

## 1.1 Manual DHKE

For this assignment I will use Joshua Kerley as ServerKeyExchange from Teams.

ServerKeyExchange{name=joshkerley, p = 17, g=11, PU=13}

PUS = Public key Server
PUC = Public key Client.

My private key (PRC) = 6.
PUC = g^PRC mod p
11^6 mod 17 = 9

So ClientKeyExchange{name=AlexHall, PU9}
The shared secret can be calculated with the following formula:
K = PUS^PRC mod p.
13^6 mod 17 = 4.

So the shared key (K) equals 4.
The public values everyone can know are p g PUS and PUC.
Only I know my private key (PRC)
and only the server knows their private key (PRS).

We both obtained the same secret.

## 1.2 DHKE in OpenSSL

For this assignment I do not have a partner, I did however create two dhparams, two private keys and two public keys and compared those.
For this I used "openssl genparam -algorithm DH -pkeyopt dh_param_prime_len:2048 -out dhparams.pem"

I then generated private and public keys with
openssl genpkey -paramfile dhparams.pem -out myprivate.pem
openssl pkey -in myprivate.pem -pubout -out mypublic.pem
I did the same for myprivateB.pem and mypublicB.pem

I then compared the files with openssl pkeyutl -derive -inkey myprivate.pem -peerkey mypublicB.pem -out secret.bin

The secret.bin and secretB.bin can be seen in the screenshot below:
<img width="944" height="868" alt="image" src="https://github.com/user-attachments/assets/c30f0653-bf18-4c60-941d-8a69ff05f36d" />


# 2. Reflection
## 2.1 What did I learn

This week I learnt more about how Diffie-Hellman Key Exchange works and how two systems can create the same shared secret without sending the secret itself. Doing the calculations manually helped me understand how the public and private values work together. I also got more practice using OpenSSL to generate DH parameters, keys and shared secrets on Linux.

## 2.2 Issues and Solutions

At first I was confused with some of the formulas used in the manual DHKE calculations, mainly with the powers and mod calculations. After writing everything down step-by-step it became easier to follow and understand.

I also did not have a partner for the OpenSSL part, so I created two different keypairs myself and tested the shared secret generation that way. Both generated secrets matched correctly.

## 2.3 How did I improve

I improved my understanding of key exchange and became more comfortable using OpenSSL commands in Linux. I also got better at following cryptographic calculations step-by-step and understanding how shared secrets are created securely between two systems.
