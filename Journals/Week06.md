# COIT13240 Journal - Week 04

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

