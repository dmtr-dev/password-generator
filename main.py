import random
import pyperclip

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = 1
length = 16
for n in range(number):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    print(password)
    pyperclip.copy(password)
