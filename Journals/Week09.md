# COIT13240 Journal - Week 09

# 1. Tutorial Activities

## 1.1 Web server certificates in tls

After opening the sandilands .pcap files and examining them in wireshark, unfortunately it can not be decoded.

<img width="1919" height="1032" alt="image" src="https://github.com/user-attachments/assets/9412d819-cbee-41b0-84ce-10a92191dcb7" />

We did do it during the tutorial, but for some reason my wireshark will not decode it, even when using the sslkey-log.txt file in preferences.
It can be seen on the screenshot above.

## 1.2 Crypto mechanisms in python.

Unfortunately the Github is still not working for me, so I cannot review and run / inspect the examples.

<img width="933" height="915" alt="image" src="https://github.com/user-attachments/assets/e5844032-6d39-4e19-9144-cc9216f17568" />


# 2. Reflection
## 2.1 What did I learn

This week I learnt more about TLS traffic and how certificates are used during secure web communication. I also got some more experience using Wireshark to inspect TLS packets and look at the TLS handshake process. Besides that, I learnt more about how SSL key log files can be used to try decrypting TLS traffic inside Wireshark.

## 2.2 Issues and Solutions

The main issue I had this week was that my Wireshark would not properly decrypt the provided TLS 1.3 packet capture, even after configuring the sslkey-log.txt file in the TLS preferences. During the tutorial it worked in class, but on my own machine the certificate messages still stayed encrypted. I tried multiple fixes such as checking the TLS settings, reloading the capture and updating the file paths, but it still did not fully work.

I also still had issues accessing some of the GitHub example files, which meant I could not properly run and inspect the Python cryptography examples for this week.

## 2.3 How did I improve

I improved my understanding of how TLS handshakes and certificates work and got more practice using Wireshark for network analysis. Even though the TLS decryption did not fully work on my system, I still learnt more about how encrypted TLS traffic is structured and how decryption keys are normally loaded into Wireshark.
