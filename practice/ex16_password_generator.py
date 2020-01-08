# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list

import random

def create_pass(length):
    chars = "zxcvbnm,./asdfghjkl;'qwertyuiop[]\`1234567890-=ZXCVBNM<>?ASDFGHJKL:\"QWERTYUIOP{}|~!@#$%^&*()_+"

    password = []
    for i in range(8):
        password.append(random.choice(chars))
    return ('').join(password)

print create_pass(10)
