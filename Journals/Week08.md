COIT13240 Journal - Week 08

# 1. Tutorial Activities

## 1.1 Copy example python code

For this assignment I already downloaded the files in
[Week 08](../wk08tut) (I received these files from my tutor).

## 1.2 Calculate hash in Python

<img width="962" height="590" alt="image" src="https://github.com/user-attachments/assets/d2b3a0d5-7d6b-4044-a0ea-09e5e8ada617" />
As you can see on the screenshot above, I copied hashexample1.py to hashexample2.py and changed it with nano.
The difference in hex and bytes is that hex is human readable and bytes is raw binary data. These two different types can be seen on the screenshot as well.


## 1.3 Calculate MAC in python 

<img width="659" height="616" alt="image" src="https://github.com/user-attachments/assets/dd2b639e-ce44-4743-add8-af58cf8f8ea9" />
As you can see on the screenshot, hmacexample1.py uses a fixed secret key and uses the message Steven, using a SHA256 algorithm.

The other one, hmacexample2.py generates a random 32-byte key and also has the message Steven. However, this script actually tries verifying the message as well.

Below is a screenshot of me running the code.
<img width="860" height="169" alt="image" src="https://github.com/user-attachments/assets/27b7eb96-25fe-46e0-8648-6ac731e0539c" />


## 1.4 Use the MAC helper functions

This assignment was performed in-class during a Brisbane tutorial, so no Teams was necessary.

<img width="941" height="304" alt="image" src="https://github.com/user-attachments/assets/3396869a-5c40-407e-8f75-88ee831c5db1" />


# 2. Reflection
## 2.1 What did I learn

This week I learnt more about hashes and MACs in Python and how they can be used to verify integrity and authenticity. I also got some more practice using Python scripts on Linux and changing the code to test different algorithms and messages. Besides that, I learnt the difference between hex output and raw bytes output and why hex is easier for humans to read.

## 2.2 Issues and Solutions

At first I was a bit confused about what some of the Python examples were actually doing, especially with the HMAC verification part. After looking through the source code step-by-step and comparing the output to the code itself, it became easier to understand.

I also had some small issues when modifying the hash examples because changing the algorithm slightly changed the output formatting. After testing a few different values and messages I understood the differences better.

## 2.3 How did I improve

I improved my understanding of hashes, MACs and HMAC verification. I also became more comfortable reading and editing Python cryptography code and understanding what the scripts are doing internally. This week also gave me more confidence using Linux terminal commands together with Python scripts.


