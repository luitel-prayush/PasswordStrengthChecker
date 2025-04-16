import math
import re

def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"\d", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    print(len(password))
    print(charset)
    print(math.log2(charset))
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

pwd = input("Enter your password: ")
print(calculate_entropy(pwd))
