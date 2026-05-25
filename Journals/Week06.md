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



