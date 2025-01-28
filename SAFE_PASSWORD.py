import random

password = ''
caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
num_caratteri = int(input("Quanti caratteri vuoi nella tua password?(Scrivi un numero da 1 a 16)"))
for i in range(num_caratteri):
    password += random.choice(caratteri)
print(password)
