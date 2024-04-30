import random
import pyperclip
from ctypes import windll

windll.kernel32.SetConsoleTitleW('Password Generator | by https://t.me/dmtrcrypto')
print("TG Channel - https://t.me/dmtrcrypto\n\n\n")

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = 1
length = 16
for n in range(number):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    print(password)
    pyperclip.copy(password)

input("\nPress Enter to exit...")
