import random

num = 0
password = 'o'
caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
num_caratteri = int(input("Quanti caratteri vuoi nella tua password?(Scrivi un numero da 0 a 71)"))
for i in range(num_caratteri):
    random_password = random.randint(0, 71)
    for i in range(random_password):
        password[num] = random_password[num]
        num += 1
