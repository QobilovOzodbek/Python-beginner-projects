import random
import string

length = int(input("Enter Length: "))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password = ""

for i in range(length):
    password += random.choice(chars)


password = ''.join([random.choice(chars) for i in range(length)])

print("Your random password is: ", password)
