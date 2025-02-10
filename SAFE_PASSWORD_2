import random

while True:
    password = ''
    caratteri = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    num_caratteri = int(input("Quanti caratteri vuoi nella tua password?(Scrivi un numero da 1 a 16)"))
    if num_caratteri > 0 and num_caratteri < 17:
        for i in range(num_caratteri):
            password += random.choice(caratteri)
        domanda = True
        print(password)
        new_password = input("Ti piace questa password?(scrivi usando solo lettere maiuscole)")
        if new_password == 'NO':
            continue
        elif new_password == 'SI':
            print("La tua password e':", password)
            break
    else:
        print("Questa password non si puo' creare!")
