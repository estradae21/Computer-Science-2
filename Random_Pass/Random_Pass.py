import random

chars = 'abcdefghijklmnopqrstuvwxyz' \
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
        '1234567890' \
        ')(*&^%$#@!'

amount = input("How many passwords? ")
amount = int(amount)

length = input("Password length? ")
length = int(length)

for p in range(amount):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)